from __future__ import annotations

import math
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from app.config import ASPECT_ANGLES, ASPECT_CLASSES, ASPECT_ORBS, ASTEROID_ORDER, PLANET_ORDER
from app.services.astro import (
    _assign_house,
    _calc_body,
    _calc_houses,
    _calc_obliquity,
    _calc_cross_aspects,
    _normalize_deg,
    _normalize_signed_deg,
    _parse_timestamp,
    calc_chart,
)


HOUSE_LABELS_TR = {
    1: "kimlik, beden, yönelim, kişisel duruş",
    2: "gelir, kaynak, mülkiyet, özdeğer",
    3: "öğrenme, yakın çevre, iletişim, kısa hareketlilik",
    4: "ev, aile sistemi, kökler, iç temel",
    5: "yaratıcılık, aşk, sahne, üretken ifade",
    6: "iş rutini, hizmet, sağlık rejimi, teknik bakım",
    7: "ortaklıklar, kontratlar, açık muhataplar",
    8: "paylaşılan kaynaklar, kriz yönetimi, psikolojik derinleşme",
    9: "yüksek eğitim, yayıncılık, hukuk, uzak ufuklar",
    10: "kariyer, statü, otorite, görünür hedefler",
    11: "ağlar, kolektifler, dostluklar, gelecek tasarımı",
    12: "geri çekilme, perde arkası süreçler, çözülme, kapanış",
}

NODE_LABELS_TR = {
    "sun": "irade, amaç, merkez",
    "moon": "duygusal ritim, ihtiyaç, alışkanlık",
    "mercury": "zihin, yazışma, ticaret, analitik süreç",
    "venus": "ilişki kalitesi, değer, estetik, çekim",
    "mars": "dürtü, mücadele, uygulama, ayrışma",
    "jupiter": "genişleme, inanç, fırsat, büyüme",
    "saturn": "yapı, yükümlülük, sınır, kurumsallaşma",
    "uranus": "kopuş, yenilik, hızlanan değişim",
    "neptune": "belirsizlik, ideal, çözünme, geçirgenlik",
    "pluto": "yoğunlaşma, güç, eliminasyon, dönüşüm",
    "ceres": "besleme, bakım, sürdürülebilirlik",
    "pallas": "örüntü zekâsı, strateji, tasarım",
    "juno": "bağlılık, sözleşme, karşılıklılık",
    "vesta": "adanma, odak, kutsal görev",
    "chiron": "kırılganlık, ustalık, onarım",
    "nn": "yön, gelişim vektörü",
    "sn": "geçmiş örüntü, boşalma hattı",
    "asc": "görünüm, başlatma ekseni",
    "dsc": "karşı eksen, ilişki alanı",
    "mc": "kamusal yön, zirve, kariyer",
    "ic": "temel, kök, iç yapı",
    "lilith (black moon)": "ham dürtü, dışlanan içerik",
    "lilith (asteroid)": "temsili lilith varyantı",
}

ASPECT_LABELS_TR = {
    "0": "kavuşum",
    "30": "yarı-sekstil",
    "60": "sekstil",
    "90": "kare",
    "120": "üçgen",
    "150": "quincunx",
    "180": "karşıtlık",
    "210": "180+30 karşıt-uzantı",
    "240": "120 ters faz",
    "270": "kare ters faz",
    "300": "sekstil ters faz",
    "330": "yarı-sekstil ters faz",
    "360": "yeniay kapanışı",
}

PHASE_NAMES_TR = {
    0: "İlerletilmiş Yeniay",
    30: "30° Fazı",
    60: "İlk Altmışlık",
    90: "İlk Kare",
    120: "Büyüyen Üçgen",
    150: "Büyüyen Quincunx",
    180: "İlerletilmiş Dolunay",
    210: "Dağılan 30°",
    240: "Dağılan Üçgen",
    270: "Son Kare",
    300: "Dağılan Sekstil",
    330: "Balsamik Ön Evre",
    360: "Sonraki İlerletilmiş Yeniay",
}


@dataclass(frozen=True)
class Event:
    target_angle: int
    label: str
    event_utc: datetime
    event_local: datetime
    progressed_utc: datetime
    progressed_sun_lon: float
    progressed_moon_lon: float
    separation: float
    exact_delta: float


def to_jd(dt_utc: datetime) -> float:
    import swisseph as swe

    return swe.julday(
        dt_utc.year,
        dt_utc.month,
        dt_utc.day,
        dt_utc.hour + dt_utc.minute / 60 + dt_utc.second / 3600 + dt_utc.microsecond / 3_600_000_000,
    )


def progressed_datetime(natal_dt: datetime, target_dt: datetime) -> datetime:
    delta_years = (target_dt - natal_dt).total_seconds() / (365.25 * 86400.0)
    return natal_dt + timedelta(days=delta_years)


def progressed_moon_sun_state(natal_dt: datetime, target_dt: datetime) -> dict:
    from app.services.astro import _ensure_ephe_path
    import swisseph as swe

    _ensure_ephe_path()
    pdt = progressed_datetime(natal_dt, target_dt)
    jd = to_jd(pdt)
    sun = _calc_body(jd, swe.SUN, "sun")
    moon = _calc_body(jd, swe.MOON, "moon")
    separation = _normalize_deg(moon["lon"] - sun["lon"])
    return {
        "progressed_utc": pdt,
        "sun_lon": sun["lon"],
        "moon_lon": moon["lon"],
        "separation": separation,
    }


def phase_delta(natal_dt: datetime, target_dt: datetime, angle: float) -> float:
    state = progressed_moon_sun_state(natal_dt, target_dt)
    return _normalize_signed_deg(state["separation"] - angle)


def phase_delta_raw(natal_dt: datetime, target_dt: datetime, angle: float) -> float:
    state = progressed_moon_sun_state(natal_dt, target_dt)
    return state["separation"] - angle


def scan_roots(natal_dt: datetime, start_dt: datetime, end_dt: datetime, angle: float, step_days: float = 2.0) -> list[tuple[datetime, datetime]]:
    step = timedelta(days=step_days)
    t = start_dt
    prev = phase_delta(natal_dt, t, angle)
    brackets: list[tuple[datetime, datetime]] = []
    while t < end_dt:
        nxt = min(t + step, end_dt)
        cur = phase_delta(natal_dt, nxt, angle)
        if prev == 0 or prev * cur <= 0:
            brackets.append((t, nxt))
        t = nxt
        prev = cur
    return brackets


def bisect_root(natal_dt: datetime, a: datetime, b: datetime, angle: float, iterations: int = 50) -> datetime:
    fa = phase_delta(natal_dt, a, angle)
    fb = phase_delta(natal_dt, b, angle)
    if fa == 0:
        return a
    if fb == 0:
        return b
    for _ in range(iterations):
        mid = a + (b - a) / 2
        fm = phase_delta(natal_dt, mid, angle)
        if fa * fm <= 0:
            b, fb = mid, fm
        else:
            a, fa = mid, fm
    return a + (b - a) / 2


def find_all_phase_roots(natal_dt: datetime, start_dt: datetime, end_dt: datetime, angle: float) -> list[datetime]:
    brackets = scan_roots(natal_dt, start_dt, end_dt, angle, step_days=5.0)
    roots = [bisect_root(natal_dt, a, b, angle) for a, b in brackets]
    deduped: list[datetime] = []
    for root in sorted(roots):
        if not deduped or abs((root - deduped[-1]).total_seconds()) > 3600:
            deduped.append(root)
    return deduped


def find_single_root(natal_dt: datetime, start_dt: datetime, end_dt: datetime, angle: float) -> datetime:
    roots = find_all_phase_roots_raw(natal_dt, start_dt, end_dt, angle)
    if len(roots) != 1:
        raise RuntimeError(f"expected_single_root angle={angle} roots={len(roots)}")
    return roots[0]


def scan_roots_raw(
    natal_dt: datetime,
    start_dt: datetime,
    end_dt: datetime,
    angle: float,
    step_days: float = 10.0,
) -> list[tuple[datetime, datetime]]:
    step = timedelta(days=step_days)
    t = start_dt
    prev = phase_delta_raw(natal_dt, t, angle)
    brackets: list[tuple[datetime, datetime]] = []
    while t < end_dt:
        nxt = min(t + step, end_dt)
        cur = phase_delta_raw(natal_dt, nxt, angle)
        if prev == 0 or prev * cur <= 0:
            brackets.append((t, nxt))
        t = nxt
        prev = cur
    return brackets


def bisect_root_raw(natal_dt: datetime, a: datetime, b: datetime, angle: float, iterations: int = 50) -> datetime:
    fa = phase_delta_raw(natal_dt, a, angle)
    fb = phase_delta_raw(natal_dt, b, angle)
    if fa == 0:
        return a
    if fb == 0:
        return b
    for _ in range(iterations):
        mid = a + (b - a) / 2
        fm = phase_delta_raw(natal_dt, mid, angle)
        if fa * fm <= 0:
            b, fb = mid, fm
        else:
            a, fa = mid, fm
    return a + (b - a) / 2


def find_all_phase_roots_raw(natal_dt: datetime, start_dt: datetime, end_dt: datetime, angle: float) -> list[datetime]:
    brackets = scan_roots_raw(natal_dt, start_dt, end_dt, angle)
    roots = [bisect_root_raw(natal_dt, a, b, angle) for a, b in brackets]
    deduped: list[datetime] = []
    for root in sorted(roots):
        if not deduped or abs((root - deduped[-1]).total_seconds()) > 3600:
            deduped.append(root)
    return deduped


def find_new_moon_candidates(natal_dt: datetime, start_dt: datetime, end_dt: datetime) -> list[datetime]:
    day = timedelta(days=1)
    samples: list[tuple[datetime, float]] = []
    t = start_dt
    while t <= end_dt:
        samples.append((t, progressed_moon_sun_state(natal_dt, t)["separation"]))
        t += day

    candidates: list[datetime] = []
    for idx in range(1, len(samples) - 1):
        prev_sep = samples[idx - 1][1]
        cur_dt, cur_sep = samples[idx]
        next_sep = samples[idx + 1][1]
        if cur_sep < 5.0 and cur_sep <= prev_sep and cur_sep <= next_sep:
            root = bisect_root(natal_dt, cur_dt - day, cur_dt + day, 0.0)
            if not candidates or abs((root - candidates[-1]).total_seconds()) > 86400 * 300:
                candidates.append(root)
    return candidates


def chart_settings():
    class Settings:
        house_system = "placidus"

    return Settings()


def aspect_targets(chart: dict) -> list[tuple[str, dict]]:
    targets: list[tuple[str, dict]] = []
    for name in PLANET_ORDER:
        if name in chart["bodies"]:
            targets.append((name, chart["bodies"][name]))
    for name in ASTEROID_ORDER:
        if name in chart.get("asteroids", {}):
            targets.append((name, chart["asteroids"][name]))
    for name in ("asc", "dsc", "mc", "ic"):
        if name in chart["angles"]:
            targets.append((name, {"lon": chart["angles"][name]["lon"], "speed": 0.0, "house": None}))
    for name in ("nn", "sn", "lilith (black moon)"):
        if name in chart["points"]:
            targets.append((name, chart["points"][name]))
    return targets


def natal_overlay_house(natal_chart: dict, lon: float, lat: float = 0.0) -> int:
    natal_dt = _parse_timestamp(natal_chart["meta"]["timestamp_utc"])
    jd = to_jd(natal_dt)
    location = natal_chart["meta"]["location"]
    cusps, _asc, _mc, armc, hsys = _calc_houses(jd, location["lat"], location["lon"], natal_chart["houses"]["system"])
    eps = _calc_obliquity(jd)
    return _assign_house(lon, lat, cusps, armc, location["lat"], hsys, eps)


def node_house(chart: dict, node_name: str) -> int | None:
    if node_name in chart["bodies"]:
        return chart["bodies"][node_name]["house"]
    if node_name in chart.get("asteroids", {}):
        return chart["asteroids"][node_name]["house"]
    if node_name in chart["points"]:
        return chart["points"][node_name]["house"]
    return {"asc": 1, "dsc": 7, "mc": 10, "ic": 4}.get(node_name)


def node_lon_lat(chart: dict, node_name: str) -> tuple[float, float]:
    if node_name in chart["bodies"]:
        body = chart["bodies"][node_name]
        return float(body["lon"]), float(body["lat"])
    if node_name in chart.get("asteroids", {}):
        body = chart["asteroids"][node_name]
        return float(body["lon"]), float(body["lat"])
    if node_name in chart["points"]:
        body = chart["points"][node_name]
        return float(body["lon"]), float(body.get("lat", 0.0))
    if node_name in chart["angles"]:
        body = chart["angles"][node_name]
        return float(body["lon"]), 0.0
    raise KeyError(node_name)


def build_contact_graph(aspects: list[dict], moving_chart: dict, natal_chart: dict, moving_prefix: str, natal_prefix: str) -> dict:
    edges: list[dict] = []
    adjacency: dict[str, set[str]] = defaultdict(set)
    weighted_degree: Counter[str] = Counter()
    for aspect in aspects:
        moving_node = str(aspect["a"]).removeprefix(moving_prefix)
        natal_node = str(aspect["b"]).removeprefix(natal_prefix)
        lon, lat = node_lon_lat(moving_chart, moving_node)
        overlay_house = natal_overlay_house(natal_chart, lon, lat)
        contacted_house = node_house(natal_chart, natal_node)
        weight = max(0.01, 1.0 / (float(aspect["orb"]) + 0.01))
        edge = {
            "moving_node": moving_node,
            "natal_node": natal_node,
            "aspect": str(aspect["exact_angle"]),
            "aspect_label_tr": ASPECT_LABELS_TR.get(str(aspect["exact_angle"]), str(aspect["exact_angle"])),
            "class": aspect["type"],
            "orb_deg": round(float(aspect["orb"]), 4),
            "applying": bool(aspect["applying"]),
            "separating": bool(aspect["separating"]),
            "MOVING_NODE_NATAL_OVERLAY_HOUSE": overlay_house,
            "CONTACTED_NATAL_NODE_HOUSE": contacted_house,
            "moving_node_keywords_tr": NODE_LABELS_TR.get(moving_node, moving_node),
            "natal_node_keywords_tr": NODE_LABELS_TR.get(natal_node, natal_node),
        }
        edges.append(edge)
        m_id = f"moving:{moving_node}"
        n_id = f"natal:{natal_node}"
        adjacency[m_id].add(n_id)
        adjacency[n_id].add(m_id)
        weighted_degree[m_id] += weight
        weighted_degree[n_id] += weight

    nodes = []
    for node_id, neighbors in sorted(adjacency.items()):
        side, name = node_id.split(":", 1)
        nodes.append(
            {
                "id": node_id,
                "name": name,
                "side": side,
                "degree": len(neighbors),
                "weighted_degree": round(weighted_degree[node_id], 4),
            }
        )

    centrality = compute_centrality(adjacency)
    for node in nodes:
        cid = node["id"]
        node["degree_centrality"] = round(centrality["degree"].get(cid, 0.0), 4)
        node["betweenness_centrality"] = round(centrality["betweenness"].get(cid, 0.0), 4)

    clusters = connected_components(adjacency)
    pattern_clusters = []
    for idx, component in enumerate(clusters, start=1):
        moving_nodes = sorted(n.split(":", 1)[1] for n in component if n.startswith("moving:"))
        natal_nodes = sorted(n.split(":", 1)[1] for n in component if n.startswith("natal:"))
        pattern_clusters.append(
            {
                "cluster_id": idx,
                "size": len(component),
                "moving_nodes": moving_nodes,
                "natal_nodes": natal_nodes,
            }
        )

    articulation = articulation_points(adjacency)
    bridge_router_nodes = [
        node for node in nodes if node["id"] in articulation or node["betweenness_centrality"] > 0.0
    ]
    bridge_router_nodes.sort(key=lambda item: (-item["betweenness_centrality"], -item["degree"], item["id"]))

    active_pattern_graph = {
        "node_count": len(nodes),
        "edge_count": len(edges),
        "nodes": nodes,
        "edges": edges,
    }
    return {
        "active_pattern_graph": active_pattern_graph,
        "pattern_nodes": nodes,
        "pattern_clusters": pattern_clusters,
        "bridge_router_nodes": bridge_router_nodes,
        "node_centrality": sorted(
            [
                {
                    "id": node["id"],
                    "degree_centrality": node["degree_centrality"],
                    "betweenness_centrality": node["betweenness_centrality"],
                    "weighted_degree": node["weighted_degree"],
                }
                for node in nodes
            ],
            key=lambda item: (-item["betweenness_centrality"], -item["degree_centrality"], -item["weighted_degree"], item["id"]),
        ),
        "contact_graph": edges,
    }


def connected_components(adjacency: dict[str, set[str]]) -> list[list[str]]:
    seen: set[str] = set()
    components: list[list[str]] = []
    for node in adjacency:
        if node in seen:
            continue
        queue = deque([node])
        seen.add(node)
        comp: list[str] = []
        while queue:
            cur = queue.popleft()
            comp.append(cur)
            for nxt in adjacency[cur]:
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        components.append(sorted(comp))
    return components


def compute_centrality(adjacency: dict[str, set[str]]) -> dict[str, dict[str, float]]:
    n = len(adjacency)
    if n <= 1:
        return {"degree": {}, "betweenness": {}}
    degree = {node: len(neighbors) / (n - 1) for node, neighbors in adjacency.items()}
    betweenness = {v: 0.0 for v in adjacency}
    for s in adjacency:
        stack: list[str] = []
        pred: dict[str, list[str]] = {w: [] for w in adjacency}
        sigma = dict.fromkeys(adjacency, 0.0)
        sigma[s] = 1.0
        dist = dict.fromkeys(adjacency, -1)
        dist[s] = 0
        queue = deque([s])
        while queue:
            v = queue.popleft()
            stack.append(v)
            for w in adjacency[v]:
                if dist[w] < 0:
                    queue.append(w)
                    dist[w] = dist[v] + 1
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]
                    pred[w].append(v)
        delta = dict.fromkeys(adjacency, 0.0)
        while stack:
            w = stack.pop()
            for v in pred[w]:
                if sigma[w]:
                    delta_v = (sigma[v] / sigma[w]) * (1.0 + delta[w])
                    delta[v] += delta_v
            if w != s:
                betweenness[w] += delta[w]
    scale = 1.0 / ((n - 1) * (n - 2) / 2) if n > 2 else 1.0
    betweenness = {k: v * scale / 2.0 for k, v in betweenness.items()}
    return {"degree": degree, "betweenness": betweenness}


def articulation_points(adjacency: dict[str, set[str]]) -> set[str]:
    timer = 0
    tin: dict[str, int] = {}
    low: dict[str, int] = {}
    visited: set[str] = set()
    result: set[str] = set()

    def dfs(v: str, parent: str | None) -> None:
        nonlocal timer
        visited.add(v)
        tin[v] = low[v] = timer
        timer += 1
        children = 0
        for to in adjacency[v]:
            if to == parent:
                continue
            if to in visited:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] >= tin[v] and parent is not None:
                    result.add(v)
                children += 1
        if parent is None and children > 1:
            result.add(v)

    for node in adjacency:
        if node not in visited:
            dfs(node, None)
    return result


def analysis_summary(graph: dict) -> dict:
    house_counter = Counter(edge["CONTACTED_NATAL_NODE_HOUSE"] for edge in graph["contact_graph"] if edge["CONTACTED_NATAL_NODE_HOUSE"])
    overlay_counter = Counter(edge["MOVING_NODE_NATAL_OVERLAY_HOUSE"] for edge in graph["contact_graph"] if edge["MOVING_NODE_NATAL_OVERLAY_HOUSE"])
    moving_counter = Counter(edge["moving_node"] for edge in graph["contact_graph"])
    natal_counter = Counter(edge["natal_node"] for edge in graph["contact_graph"])
    aspect_counter = Counter(edge["aspect"] for edge in graph["contact_graph"])
    return {
        "top_contacted_houses": house_counter.most_common(5),
        "top_overlay_houses": overlay_counter.most_common(5),
        "top_moving_nodes": moving_counter.most_common(5),
        "top_natal_nodes": natal_counter.most_common(7),
        "aspect_distribution": aspect_counter.most_common(),
    }


def infer_theme(event: Event, progressed_summary: dict, transit_summary: dict) -> str:
    houses = []
    for house, _count in progressed_summary["top_contacted_houses"][:3]:
        if house not in houses:
            houses.append(house)
    for house, _count in transit_summary["top_contacted_houses"][:3]:
        if house not in houses:
            houses.append(house)
    house_text = "; ".join(HOUSE_LABELS_TR[h] for h in houses[:3]) if houses else "ev teması zayıf yoğunlaşmış durumda değil"

    natal_nodes = []
    for node, _count in progressed_summary["top_natal_nodes"][:3]:
        if node not in natal_nodes:
            natal_nodes.append(node)
    for node, _count in transit_summary["top_natal_nodes"][:3]:
        if node not in natal_nodes:
            natal_nodes.append(node)
    node_text = "; ".join(NODE_LABELS_TR.get(node, node) for node in natal_nodes[:4]) if natal_nodes else "belirgin natal düğüm baskın değil"

    phase_bias = {
        0: "başlatma, tohum atma ve eski yapının kapanışı",
        30: "ilk ayarlama, küçük yön değişikliği ve veri toplama",
        60: "işlevsel açılım, ilk fırsat pencereleri",
        90: "gerilimle biçimlenme, zorunlu karar ve yön ayrışması",
        120: "akış yakalama, kapasiteyi görünür hale getirme",
        150: "uyumsuz parçaları yeniden ayarlama, teknik düzeltme",
        180: "karşılıklılık, görünür sonuç, dış geri bildirim",
        210: "dağıtım, paylaşım ve sonuçları ağlara yayma",
        240: "edinilmiş beceriyi üretken biçimde boşaltma",
        270: "yeniden yapılandırma, eleme ve kapanış baskısı",
        300: "işlevsel çözüm, sadeleştirme ve pratik entegrasyon",
        330: "bırakma, iç değerlendirme ve yeni döngü öncesi çözülme",
        360: "yeni 29 yıllık yapısal döngü eşiği",
    }[event.target_angle]
    return (
        f"Bu fazın teknik matrisi {phase_bias} eksenini öne çıkarıyor. "
        f"En yoğun temas alanları: {house_text}. "
        f"Aktif natal düğüm imzası: {node_text}. "
        "Biyografik doğrulamada tekil olay aramak yerine, rol tanımı, iş-akış mimarisi, ilişki kontratları, kaynak yönetimi "
        "ve iç/dış yönelim dengesinde gözlenen yapısal yeniden dağılımlar izlenmeli."
    )


def build_validation_table(event: Event) -> list[dict]:
    return [
        {
            "target_angle_deg": event.target_angle,
            "event_utc": event.event_utc.isoformat().replace("+00:00", "Z"),
            "event_local": event.event_local.isoformat(),
            "progressed_chart_utc": event.progressed_utc.isoformat().replace("+00:00", "Z"),
            "progressed_sun_lon": round(event.progressed_sun_lon, 6),
            "progressed_moon_lon": round(event.progressed_moon_lon, 6),
            "moon_minus_sun_deg": round(event.separation, 6),
            "exact_delta_deg": round(event.exact_delta, 9),
        }
    ]


def build_shared_nodes(progressed_graph: dict, transit_graph: dict) -> list[dict]:
    p_nodes = {node["name"] for node in progressed_graph["pattern_nodes"] if node["side"] == "natal"}
    t_nodes = {node["name"] for node in transit_graph["pattern_nodes"] if node["side"] == "natal"}
    shared = sorted(p_nodes & t_nodes)
    return [{"natal_node": node, "keywords_tr": NODE_LABELS_TR.get(node, node)} for node in shared]


def make_event(
    natal_dt: datetime,
    event_dt: datetime,
    target_angle: int,
    tz: ZoneInfo,
) -> Event:
    state = progressed_moon_sun_state(natal_dt, event_dt)
    return Event(
        target_angle=target_angle,
        label=PHASE_NAMES_TR[target_angle],
        event_utc=event_dt.astimezone(UTC),
        event_local=event_dt.astimezone(tz),
        progressed_utc=state["progressed_utc"].astimezone(UTC),
        progressed_sun_lon=state["sun_lon"],
        progressed_moon_lon=state["moon_lon"],
        separation=state["separation"],
        exact_delta=_normalize_signed_deg(state["separation"] - (0.0 if target_angle == 360 else float(target_angle))),
    )


def markdown_table(rows: list[dict], columns: list[str]) -> str:
    if not rows:
        return "_Boş_"
    header = "| " + " | ".join(columns) + " |"
    sep = "| " + " | ".join("---" for _ in columns) + " |"
    body = []
    for row in rows:
        body.append("| " + " | ".join(str(row.get(col, "")) for col in columns) + " |")
    return "\n".join([header, sep, *body])


def top_rows(items: list[dict], limit: int) -> list[dict]:
    return items[:limit]


def format_counter_rows(counter_pairs: list[tuple], label: str, mapper=None) -> list[dict]:
    rows = []
    for key, count in counter_pairs:
        mapped = mapper(key) if mapper else key
        rows.append({label: key, "count": count, "label_tr": mapped})
    return rows


def build_report() -> tuple[Path, dict]:
    report_dir = Path("/home/acetkin06/CodeWorks/STYX/SPIN/STYX/Local/Reports")
    report_dir.mkdir(parents=True, exist_ok=True)

    birth_tz = ZoneInfo("Europe/Istanbul")
    birth_local = datetime(1982, 5, 8, 6, 39, tzinfo=birth_tz)
    natal_dt = birth_local.astimezone(UTC)
    location = {"lat": 41.2795516, "lon": 31.4229672, "alt_m": 0.0, "place": "Karadeniz Eregli"}
    settings = chart_settings()
    natal_chart = calc_chart("natal", natal_dt.isoformat(), location, settings, round_output=False)

    nm_search_start = datetime(1990, 1, 1, tzinfo=UTC)
    nm_search_end = datetime(2030, 12, 31, tzinfo=UTC)
    new_moons = find_new_moon_candidates(natal_dt, nm_search_start, nm_search_end)
    if len(new_moons) < 2:
        raise RuntimeError("insufficient_new_moons_found")
    next_nm = min(root for root in new_moons if root > datetime(2026, 1, 1, tzinfo=UTC))
    previous_nm_candidates = [root for root in new_moons if root < next_nm]
    if not previous_nm_candidates:
        raise RuntimeError("previous_new_moon_not_found")
    previous_nm = previous_nm_candidates[-1]

    events: list[Event] = [make_event(natal_dt, previous_nm, 0, birth_tz)]
    interval_start = previous_nm + timedelta(minutes=1)
    interval_end = next_nm - timedelta(minutes=1)
    for angle in (30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330):
        root = find_single_root(natal_dt, interval_start, interval_end, float(angle))
        events.append(make_event(natal_dt, root, angle, birth_tz))
    events.append(make_event(natal_dt, next_nm, 360, birth_tz))
    events.sort(key=lambda item: item.event_utc)

    cycle_summary = []
    cycle_house_counter = Counter()
    cycle_overlay_counter = Counter()
    cycle_natal_counter = Counter()
    phase_sections = []

    for event in events:
        progressed_chart = calc_chart("natal", event.progressed_utc.isoformat(), location, settings, round_output=False)
        transit_chart = calc_chart("moment", event.event_utc.isoformat(), location, settings, round_output=False)
        progressed_aspects = _calc_cross_aspects(
            aspect_targets(progressed_chart),
            aspect_targets(natal_chart),
            ASPECT_ANGLES,
            ASPECT_ORBS,
            ASPECT_CLASSES,
            "sp_",
            "natal_",
        )
        transit_aspects = _calc_cross_aspects(
            aspect_targets(transit_chart),
            aspect_targets(natal_chart),
            ASPECT_ANGLES,
            ASPECT_ORBS,
            ASPECT_CLASSES,
            "tr_",
            "natal_",
        )
        progressed_graph = build_contact_graph(progressed_aspects, progressed_chart, natal_chart, "sp_", "natal_")
        transit_graph = build_contact_graph(transit_aspects, transit_chart, natal_chart, "tr_", "natal_")
        progressed_summary = analysis_summary(progressed_graph)
        transit_summary = analysis_summary(transit_graph)
        shared_nodes = build_shared_nodes(progressed_graph, transit_graph)
        for edge in progressed_graph["contact_graph"] + transit_graph["contact_graph"]:
            if edge["CONTACTED_NATAL_NODE_HOUSE"]:
                cycle_house_counter[edge["CONTACTED_NATAL_NODE_HOUSE"]] += 1
            if edge["MOVING_NODE_NATAL_OVERLAY_HOUSE"]:
                cycle_overlay_counter[edge["MOVING_NODE_NATAL_OVERLAY_HOUSE"]] += 1
            cycle_natal_counter[edge["natal_node"]] += 1

        cycle_summary.append(
            {
                "phase": event.label,
                "target_angle_deg": event.target_angle,
                "event_utc": event.event_utc.isoformat().replace("+00:00", "Z"),
                "event_local": event.event_local.isoformat(),
                "progressed_contacts": len(progressed_graph["contact_graph"]),
                "transit_contacts": len(transit_graph["contact_graph"]),
                "shared_natal_nodes": ", ".join(item["natal_node"] for item in shared_nodes[:8]),
            }
        )

        phase_sections.append(
            {
                "event": event,
                "progressed_graph": progressed_graph,
                "transit_graph": transit_graph,
                "progressed_summary": progressed_summary,
                "transit_summary": transit_summary,
                "shared_nodes": shared_nodes,
                "theme": infer_theme(event, progressed_summary, transit_summary),
            }
        )

    repeated_nodes_text = ", ".join(
        f"{node} ({count})" for node, count in cycle_natal_counter.most_common(10)
    )
    repeated_houses_text = ", ".join(
        f"{house}. ev ({count})" for house, count in cycle_house_counter.most_common(8)
    )
    overlay_text = ", ".join(
        f"{house}. ev ({count})" for house, count in cycle_overlay_counter.most_common(8)
    )

    lines = []
    lines.append("# Çetin İkincil İlerletim Ay Faz Döngüsü Teknik Raporu")
    lines.append("")
    lines.append("## Kapsam ve Kanonik Veri")
    lines.append("")
    lines.append("- Kişi: Çetin")
    lines.append("- Kanonik doğum verisi: 1982-05-08 06:39 Europe/Istanbul, Karadeniz Ereğli, Türkiye")
    lines.append("- Kanonik koordinat: 41.2795516, 31.4229672")
    lines.append("- Ev sistemi: Placidus")
    lines.append("- Zodyak: Tropical")
    lines.append("- Hesap motoru: repo içi STYX Swiss Ephemeris servisleri")
    lines.append("- Kritik house kuralı: `MOVING_NODE_NATAL_OVERLAY_HOUSE` ve `CONTACTED_NATAL_NODE_HOUSE` her tabloda ayrı tutulmuştur.")
    lines.append("")
    lines.append("## Faz Zamanları")
    lines.append("")
    lines.append(
        markdown_table(
            [
                {
                    "phase": event.label,
                    "target_angle_deg": event.target_angle,
                    "event_utc": event.event_utc.isoformat().replace("+00:00", "Z"),
                    "event_local": event.event_local.isoformat(),
                    "progressed_sun_lon": round(event.progressed_sun_lon, 6),
                    "progressed_moon_lon": round(event.progressed_moon_lon, 6),
                    "moon_minus_sun_deg": round(event.separation, 6),
                    "exact_delta_deg": round(event.exact_delta, 9),
                }
                for event in events
            ],
            [
                "phase",
                "target_angle_deg",
                "event_utc",
                "event_local",
                "progressed_sun_lon",
                "progressed_moon_lon",
                "moon_minus_sun_deg",
                "exact_delta_deg",
            ],
        )
    )
    lines.append("")

    for section in phase_sections:
        event = section["event"]
        progressed_graph = section["progressed_graph"]
        transit_graph = section["transit_graph"]
        progressed_summary = section["progressed_summary"]
        transit_summary = section["transit_summary"]
        shared_nodes = section["shared_nodes"]
        lines.append(f"## {event.label} ({event.target_angle}°)")
        lines.append("")
        lines.append("### Faz Doğrulama")
        lines.append("")
        lines.append(
            markdown_table(
                build_validation_table(event),
                [
                    "target_angle_deg",
                    "event_utc",
                    "event_local",
                    "progressed_chart_utc",
                    "progressed_sun_lon",
                    "progressed_moon_lon",
                    "moon_minus_sun_deg",
                    "exact_delta_deg",
                ],
            )
        )
        lines.append("")
        lines.append("### A. Progressed-to-Natal")
        lines.append("")
        lines.append(
            f"Aktif pattern graph: {progressed_graph['active_pattern_graph']['node_count']} düğüm, "
            f"{progressed_graph['active_pattern_graph']['edge_count']} temas."
        )
        lines.append("")
        lines.append(
            markdown_table(
                top_rows(progressed_graph["contact_graph"], 20),
                [
                    "moving_node",
                    "natal_node",
                    "aspect",
                    "aspect_label_tr",
                    "orb_deg",
                    "MOVING_NODE_NATAL_OVERLAY_HOUSE",
                    "CONTACTED_NATAL_NODE_HOUSE",
                    "applying",
                    "separating",
                ],
            )
        )
        lines.append("")
        lines.append(
            markdown_table(
                top_rows(progressed_graph["node_centrality"], 12),
                ["id", "degree_centrality", "betweenness_centrality", "weighted_degree"],
            )
        )
        lines.append("")
        lines.append(
            markdown_table(
                top_rows(progressed_graph["pattern_clusters"], 10),
                ["cluster_id", "size", "moving_nodes", "natal_nodes"],
            )
        )
        lines.append("")
        lines.append(
            markdown_table(
                top_rows(progressed_graph["bridge_router_nodes"], 10),
                ["id", "degree", "degree_centrality", "betweenness_centrality", "weighted_degree"],
            )
        )
        lines.append("")
        lines.append("### B. Transit-to-Natal")
        lines.append("")
        lines.append(
            f"Aktif pattern graph: {transit_graph['active_pattern_graph']['node_count']} düğüm, "
            f"{transit_graph['active_pattern_graph']['edge_count']} temas."
        )
        lines.append("")
        lines.append(
            markdown_table(
                top_rows(transit_graph["contact_graph"], 20),
                [
                    "moving_node",
                    "natal_node",
                    "aspect",
                    "aspect_label_tr",
                    "orb_deg",
                    "MOVING_NODE_NATAL_OVERLAY_HOUSE",
                    "CONTACTED_NATAL_NODE_HOUSE",
                    "applying",
                    "separating",
                ],
            )
        )
        lines.append("")
        lines.append(
            markdown_table(
                top_rows(transit_graph["node_centrality"], 12),
                ["id", "degree_centrality", "betweenness_centrality", "weighted_degree"],
            )
        )
        lines.append("")
        lines.append(
            markdown_table(
                top_rows(transit_graph["pattern_clusters"], 10),
                ["cluster_id", "size", "moving_nodes", "natal_nodes"],
            )
        )
        lines.append("")
        lines.append(
            markdown_table(
                top_rows(transit_graph["bridge_router_nodes"], 10),
                ["id", "degree", "degree_centrality", "betweenness_centrality", "weighted_degree"],
            )
        )
        lines.append("")
        lines.append("### Shared Nodes ve Validation")
        lines.append("")
        lines.append(
            markdown_table(
                shared_nodes[:20],
                ["natal_node", "keywords_tr"],
            )
        )
        lines.append("")
        lines.append("Progressed validation özeti:")
        lines.append("")
        lines.append(
            markdown_table(
                format_counter_rows(
                    progressed_summary["aspect_distribution"], "aspect", lambda key: ASPECT_LABELS_TR.get(str(key), str(key))
                ),
                ["aspect", "count", "label_tr"],
            )
        )
        lines.append("")
        lines.append("Transit validation özeti:")
        lines.append("")
        lines.append(
            markdown_table(
                format_counter_rows(
                    transit_summary["aspect_distribution"], "aspect", lambda key: ASPECT_LABELS_TR.get(str(key), str(key))
                ),
                ["aspect", "count", "label_tr"],
            )
        )
        lines.append("")
        lines.append("### Teknik Tematik Özet")
        lines.append("")
        lines.append(section["theme"])
        lines.append("")

    lines.append("## Döngü Sentezi")
    lines.append("")
    lines.append(
        "Bu yaklaşık 29 yıllık döngü boyunca tekrar eden natal düğümler ve ev kümeleri, gelişimin tek bir olay çizgisi yerine "
        "tekrarlanan yapısal stres noktaları ve entegrasyon eşikleri üzerinden çalıştığını gösteriyor."
    )
    lines.append("")
    lines.append(f"- Tekrarlayan natal düğümler: {repeated_nodes_text}")
    lines.append(f"- En çok aktive olan natal evler: {repeated_houses_text}")
    lines.append(f"- Hareketli düğümlerin natal overlay yoğunluğu: {overlay_text}")
    lines.append(
        "- Yapısal geçiş mantığı: yeniay eksenlerinde kapanış/başlatma, karelerde zorunlu yeniden yapılandırma, dolunayda karşılıklılık ve dış görünürlük, balsamik alanda ise çözülme ve sadeleşme baskın."
    )
    lines.append(
        "- Biyografik validasyon odağı: kariyer/otorite mimarisi, ortaklık ve kontrat örüntüleri, kök-aile ile kamusal yön arasındaki eksen, gelir-paylaşılan kaynaklar ve çalışma rejimi yeniden dağılımları."
    )
    lines.append(
        "- En tutarlı teknik imza, aynı natal düğümlerin hem progressed hem transit katmanda tekrarlı eşzamanlı temas almasıdır; bu düğümler sonraki döngü başında da ana yönlendirici olarak izlenmelidir."
    )
    lines.append("")
    lines.append("## Fazlar Arası Hızlı Özet")
    lines.append("")
    lines.append(
        markdown_table(
            cycle_summary,
            [
                "phase",
                "target_angle_deg",
                "event_utc",
                "event_local",
                "progressed_contacts",
                "transit_contacts",
                "shared_natal_nodes",
            ],
        )
    )
    lines.append("")

    report_path = report_dir / "cetin_progressed_lunar_phase_cycle_1997_2026_tr.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path, {
        "previous_new_moon_utc": previous_nm.isoformat().replace("+00:00", "Z"),
        "next_new_moon_utc": next_nm.isoformat().replace("+00:00", "Z"),
        "event_count": len(events),
    }


if __name__ == "__main__":
    path, meta = build_report()
    print(path)
    print(meta)
