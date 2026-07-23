# Çetin İkincil İlerletim Ay Faz Döngüsü Teknik Raporu

## Kapsam ve Kanonik Veri

- Kişi: Çetin
- Kanonik doğum verisi: 1982-05-08 06:39 Europe/Istanbul, Karadeniz Ereğli, Türkiye
- Kanonik koordinat: 41.2795516, 31.4229672
- Ev sistemi: Placidus
- Zodyak: Tropical
- Hesap motoru: repo içi STYX Swiss Ephemeris servisleri
- Kritik house kuralı: `MOVING_NODE_NATAL_OVERLAY_HOUSE` ve `CONTACTED_NATAL_NODE_HOUSE` her tabloda ayrı tutulmuştur.

## Faz Zamanları

| phase | target_angle_deg | event_utc | event_local | progressed_sun_lon | progressed_moon_lon | moon_minus_sun_deg | exact_delta_deg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| İlerletilmiş Yeniay | 0 | 1997-05-23T10:51:31.193435Z | 1997-05-23T13:51:31.193435+03:00 | 61.735303 | 61.735303 | 360.0 | -3e-09 |
| 30° Fazı | 30 | 1999-07-08T21:33:27.119183Z | 1999-07-09T00:33:27.119183+03:00 | 63.778981 | 93.778981 | 30.0 | -5e-09 |
| İlk Altmışlık | 60 | 2001-09-16T04:04:12.032884Z | 2001-09-16T07:04:12.032884+03:00 | 65.883536 | 125.883536 | 60.0 | -4e-09 |
| İlk Kare | 90 | 2004-01-13T21:29:25.730005Z | 2004-01-13T23:29:25.730005+02:00 | 68.115962 | 158.115962 | 90.0 | -5e-09 |
| Büyüyen Üçgen | 120 | 2006-07-09T11:54:58.090679Z | 2006-07-09T14:54:58.090679+03:00 | 70.498049 | 190.498049 | 120.0 | -2e-09 |
| Büyüyen Quincunx | 150 | 2009-02-21T14:02:48.922205Z | 2009-02-21T16:02:48.922205+02:00 | 73.010287 | 223.010287 | 150.0 | -2e-09 |
| İlerletilmiş Dolunay | 180 | 2011-11-12T04:35:13.137426Z | 2011-11-12T06:35:13.137426+02:00 | 75.613512 | 255.613512 | 180.0 | -2e-09 |
| Dağılan 30° | 210 | 2014-08-17T22:43:08.150422Z | 2014-08-18T01:43:08.150422+03:00 | 78.257223 | 288.257223 | 210.0 | -0.0 |
| Dağılan Üçgen | 240 | 2017-05-10T16:05:30.413728Z | 2017-05-10T19:05:30.413728+03:00 | 80.865373 | 320.865373 | 240.0 | -3e-09 |
| Son Kare | 270 | 2019-12-14T06:58:19.184864Z | 2019-12-14T09:58:19.184864+03:00 | 83.34401 | 353.34401 | 270.0 | -4e-09 |
| Dağılan Sekstil | 300 | 2022-05-08T09:09:32.078780Z | 2022-05-08T12:09:32.078780+03:00 | 85.634916 | 25.634916 | 300.0 | -3e-09 |
| Balsamik Ön Evre | 330 | 2024-07-27T08:29:22.564831Z | 2024-07-27T11:29:22.564831+03:00 | 87.755149 | 57.755149 | 330.0 | -5e-09 |
| Sonraki İlerletilmiş Yeniay | 360 | 2026-09-10T03:19:14.623301Z | 2026-09-10T06:19:14.623301+03:00 | 89.780416 | 89.780416 | 360.0 | -2e-09 |

## İlerletilmiş Yeniay (0°)

### Faz Doğrulama

| target_angle_deg | event_utc | event_local | progressed_chart_utc | progressed_sun_lon | progressed_moon_lon | moon_minus_sun_deg | exact_delta_deg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1997-05-23T10:51:31.193435Z | 1997-05-23T13:51:31.193435+03:00 | 1982-05-23T04:40:18.442692Z | 61.735303 | 61.735303 | 360.0 | -3e-09 |

### A. Progressed-to-Natal

Aktif pattern graph: 46 düğüm, 342 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | mercury | 0 | kavuşum | 6.6764 | 12 | 1 | False | True |
| sun | venus | 60 | sekstil | 2.3267 | 12 | 11 | False | True |
| sun | mars | 120 | üçgen | 1.272 | 12 | 5 | False | True |
| sun | jupiter | 150 | quincunx | 2.1979 | 12 | 6 | True | False |
| sun | saturn | 135 | 135 | 0.1013 | 12 | 5 | True | False |
| sun | uranus | 180 | karşıtlık | 1.5389 | 12 | 6 | True | False |
| sun | neptune | 150 | quincunx | 5.093 | 12 | 7 | False | True |
| sun | pallas | 120 | üçgen | 1.4562 | 12 | 5 | True | False |
| sun | lilith (asteroid) | 60 | sekstil | 0.4228 | 12 | 11 | True | False |
| sun | asc | 0 | kavuşum | 1.62 | 12 | 1 | True | False |
| sun | dsc | 180 | karşıtlık | 1.62 | 12 | 7 | True | False |
| sun | ic | 72 | 72 | 4.3555 | 12 | 4 | False | True |
| sun | nn | 45 | 45 | 1.8691 | 12 | 2 | False | True |
| sun | sn | 135 | 135 | 1.8691 | 12 | 8 | False | True |
| moon | mercury | 0 | kavuşum | 6.6764 | 12 | 1 | True | False |
| moon | venus | 60 | sekstil | 2.3267 | 12 | 11 | True | False |
| moon | mars | 120 | üçgen | 1.272 | 12 | 5 | False | True |
| moon | jupiter | 150 | quincunx | 2.1979 | 12 | 6 | True | False |
| moon | saturn | 135 | 135 | 0.1013 | 12 | 5 | True | False |
| moon | uranus | 180 | karşıtlık | 1.5389 | 12 | 6 | True | False |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| moving:dsc | 0.4444 | 0.0419 | 80.8494 |
| moving:asc | 0.4 | 0.0326 | 80.3226 |
| moving:vesta | 0.3778 | 0.0325 | 9.0491 |
| natal:ic | 0.3556 | 0.0302 | 8.5279 |
| moving:lilith (asteroid) | 0.3778 | 0.0284 | 9.981 |
| natal:vesta | 0.3556 | 0.028 | 34.203 |
| natal:neptune | 0.3333 | 0.0267 | 16.386 |
| natal:moon | 0.3556 | 0.0264 | 10.6246 |
| moving:juno | 0.3556 | 0.0263 | 13.9079 |
| natal:saturn | 0.3333 | 0.0246 | 36.4518 |
| moving:mars | 0.3333 | 0.0241 | 28.0997 |
| natal:sun | 0.3333 | 0.0239 | 13.7324 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| moving:dsc | 20 | 0.4444 | 0.0419 | 80.8494 |
| moving:asc | 18 | 0.4 | 0.0326 | 80.3226 |
| moving:vesta | 17 | 0.3778 | 0.0325 | 9.0491 |
| natal:ic | 16 | 0.3556 | 0.0302 | 8.5279 |
| moving:lilith (asteroid) | 17 | 0.3778 | 0.0284 | 9.981 |
| natal:vesta | 16 | 0.3556 | 0.028 | 34.203 |
| natal:neptune | 15 | 0.3333 | 0.0267 | 16.386 |
| natal:moon | 16 | 0.3556 | 0.0264 | 10.6246 |
| moving:juno | 16 | 0.3556 | 0.0263 | 13.9079 |
| natal:saturn | 15 | 0.3333 | 0.0246 | 36.4518 |

### B. Transit-to-Natal

Aktif pattern graph: 46 düğüm, 348 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | mercury | 0 | kavuşum | 6.0664 | 12 | 1 | False | True |
| sun | venus | 60 | sekstil | 1.7167 | 12 | 11 | False | True |
| sun | mars | 120 | üçgen | 1.882 | 12 | 5 | False | True |
| sun | jupiter | 150 | quincunx | 1.5879 | 12 | 6 | True | False |
| sun | saturn | 135 | 135 | 0.5087 | 12 | 5 | False | True |
| sun | uranus | 180 | karşıtlık | 0.9289 | 12 | 6 | True | False |
| sun | neptune | 150 | quincunx | 5.703 | 12 | 7 | False | True |
| sun | pallas | 120 | üçgen | 0.8462 | 12 | 5 | True | False |
| sun | lilith (asteroid) | 60 | sekstil | 0.1872 | 12 | 11 | False | True |
| sun | asc | 0 | kavuşum | 1.01 | 12 | 1 | True | False |
| sun | dsc | 180 | karşıtlık | 1.01 | 12 | 7 | True | False |
| sun | ic | 72 | 72 | 4.9655 | 12 | 4 | False | True |
| sun | nn | 45 | 45 | 2.4791 | 12 | 2 | False | True |
| sun | sn | 135 | 135 | 2.4791 | 12 | 8 | False | True |
| moon | sun | 150 | quincunx | 1.5239 | 7 | 12 | True | False |
| moon | moon | 30 | yarı-sekstil | 2.8824 | 7 | 6 | True | False |
| moon | mercury | 180 | karşıtlık | 7.2946 | 7 | 1 | False | True |
| moon | mars | 72 | 72 | 3.243 | 7 | 5 | False | True |
| moon | jupiter | 45 | 45 | 3.2269 | 7 | 6 | True | False |
| moon | saturn | 60 | sekstil | 1.1303 | 7 | 5 | True | False |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| natal:jupiter | 0.4222 | 0.0423 | 15.1311 |
| moving:pluto | 0.3778 | 0.0313 | 25.0302 |
| moving:vesta | 0.3778 | 0.0295 | 6.9951 |
| moving:juno | 0.3778 | 0.0294 | 4.8694 |
| moving:sn | 0.3556 | 0.0291 | 32.7421 |
| natal:vesta | 0.3556 | 0.0271 | 26.5926 |
| natal:ic | 0.3556 | 0.0255 | 7.0853 |
| natal:moon | 0.3333 | 0.0237 | 25.9614 |
| moving:nn | 0.3333 | 0.0237 | 12.1827 |
| natal:sun | 0.3333 | 0.0233 | 9.3006 |
| natal:chiron | 0.3111 | 0.0227 | 6.2315 |
| moving:jupiter | 0.3111 | 0.0227 | 5.3012 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| natal:jupiter | 19 | 0.4222 | 0.0423 | 15.1311 |
| moving:pluto | 17 | 0.3778 | 0.0313 | 25.0302 |
| moving:vesta | 17 | 0.3778 | 0.0295 | 6.9951 |
| moving:juno | 17 | 0.3778 | 0.0294 | 4.8694 |
| moving:sn | 16 | 0.3556 | 0.0291 | 32.7421 |
| natal:vesta | 16 | 0.3556 | 0.0271 | 26.5926 |
| natal:ic | 16 | 0.3556 | 0.0255 | 7.0853 |
| moving:nn | 15 | 0.3333 | 0.0237 | 12.1827 |
| natal:moon | 15 | 0.3333 | 0.0237 | 25.9614 |
| natal:sun | 15 | 0.3333 | 0.0233 | 9.3006 |

### Shared Nodes ve Validation

| natal_node | keywords_tr |
| --- | --- |
| asc | görünüm, başlatma ekseni |
| ceres | besleme, bakım, sürdürülebilirlik |
| chiron | kırılganlık, ustalık, onarım |
| dsc | karşı eksen, ilişki alanı |
| ic | temel, kök, iç yapı |
| juno | bağlılık, sözleşme, karşılıklılık |
| jupiter | genişleme, inanç, fırsat, büyüme |
| lilith (asteroid) | temsili lilith varyantı |
| lilith (black moon) | ham dürtü, dışlanan içerik |
| mars | dürtü, mücadele, uygulama, ayrışma |
| mc | kamusal yön, zirve, kariyer |
| mercury | zihin, yazışma, ticaret, analitik süreç |
| moon | duygusal ritim, ihtiyaç, alışkanlık |
| neptune | belirsizlik, ideal, çözünme, geçirgenlik |
| nn | yön, gelişim vektörü |
| pallas | örüntü zekâsı, strateji, tasarım |
| pluto | yoğunlaşma, güç, eliminasyon, dönüşüm |
| saturn | yapı, yükümlülük, sınır, kurumsallaşma |
| sn | geçmiş örüntü, boşalma hattı |
| sun | irade, amaç, merkez |

Progressed validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 150 | 40 | quincunx |
| 135 | 40 | 135 |
| 0 | 39 | kavuşum |
| 45 | 37 | 45 |
| 72 | 35 | 72 |
| 30 | 34 | yarı-sekstil |
| 90 | 34 | kare |
| 60 | 32 | sekstil |
| 120 | 27 | üçgen |
| 180 | 24 | karşıtlık |

Transit validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 60 | 46 | sekstil |
| 120 | 42 | üçgen |
| 72 | 42 | 72 |
| 30 | 41 | yarı-sekstil |
| 90 | 39 | kare |
| 150 | 37 | quincunx |
| 45 | 37 | 45 |
| 135 | 29 | 135 |
| 180 | 18 | karşıtlık |
| 0 | 17 | kavuşum |

### Teknik Tematik Özet

Bu fazın teknik matrisi başlatma, tohum atma ve eski yapının kapanışı eksenini öne çıkarıyor. En yoğun temas alanları: iş rutini, hizmet, sağlık rejimi, teknik bakım; ortaklıklar, kontratlar, açık muhataplar; yaratıcılık, aşk, sahne, üretken ifade. Aktif natal düğüm imzası: ham dürtü, dışlanan içerik; temel, kök, iç yapı; adanma, odak, kutsal görev; genişleme, inanç, fırsat, büyüme. Biyografik doğrulamada tekil olay aramak yerine, rol tanımı, iş-akış mimarisi, ilişki kontratları, kaynak yönetimi ve iç/dış yönelim dengesinde gözlenen yapısal yeniden dağılımlar izlenmeli.

## 30° Fazı (30°)

### Faz Doğrulama

| target_angle_deg | event_utc | event_local | progressed_chart_utc | progressed_sun_lon | progressed_moon_lon | moon_minus_sun_deg | exact_delta_deg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 30 | 1999-07-08T21:33:27.119183Z | 1999-07-09T00:33:27.119183+03:00 | 1982-05-25T07:41:26.932564Z | 63.778981 | 93.778981 | 30.0 | -5e-09 |

### A. Progressed-to-Natal

Aktif pattern graph: 46 düğüm, 340 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | mercury | 0 | kavuşum | 4.6327 | 1 | 1 | False | True |
| sun | venus | 60 | sekstil | 0.283 | 1 | 11 | False | True |
| sun | mars | 120 | üçgen | 3.3157 | 1 | 5 | False | True |
| sun | jupiter | 150 | quincunx | 0.1543 | 1 | 6 | True | False |
| sun | saturn | 135 | 135 | 1.9424 | 1 | 5 | False | True |
| sun | uranus | 180 | karşıtlık | 0.5048 | 1 | 6 | False | True |
| sun | pallas | 120 | üçgen | 0.5874 | 1 | 5 | False | True |
| sun | lilith (asteroid) | 60 | sekstil | 1.6208 | 1 | 11 | False | True |
| sun | asc | 0 | kavuşum | 0.4236 | 1 | 1 | False | True |
| sun | dsc | 180 | karşıtlık | 0.4236 | 1 | 7 | False | True |
| sun | mc | 120 | üçgen | 5.6008 | 1 | 10 | True | False |
| sun | ic | 60 | sekstil | 5.6008 | 1 | 4 | True | False |
| sun | nn | 45 | 45 | 3.9128 | 1 | 2 | False | True |
| sun | sn | 135 | 135 | 3.9128 | 1 | 8 | False | True |
| moon | sun | 45 | 45 | 1.5488 | 2 | 12 | False | True |
| moon | moon | 135 | 135 | 0.1902 | 2 | 6 | False | True |
| moon | mercury | 30 | yarı-sekstil | 4.6327 | 2 | 1 | True | False |
| moon | venus | 90 | kare | 0.283 | 2 | 11 | True | False |
| moon | mars | 90 | kare | 3.3157 | 2 | 5 | False | True |
| moon | jupiter | 120 | üçgen | 0.1543 | 2 | 6 | True | False |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| moving:vesta | 0.4 | 0.0367 | 6.4209 |
| moving:moon | 0.4 | 0.0346 | 26.608 |
| natal:neptune | 0.3778 | 0.0339 | 12.9341 |
| moving:juno | 0.3556 | 0.0285 | 12.4633 |
| natal:mars | 0.3556 | 0.0283 | 8.2753 |
| moving:asc | 0.3556 | 0.0281 | 8.1397 |
| natal:lilith (asteroid) | 0.3556 | 0.027 | 26.6618 |
| moving:dsc | 0.3556 | 0.0268 | 6.2337 |
| natal:vesta | 0.3556 | 0.0263 | 19.6407 |
| moving:pallas | 0.3556 | 0.0255 | 18.0555 |
| natal:saturn | 0.3333 | 0.0249 | 8.7387 |
| moving:mercury | 0.3333 | 0.0246 | 11.8906 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| moving:vesta | 18 | 0.4 | 0.0367 | 6.4209 |
| moving:moon | 18 | 0.4 | 0.0346 | 26.608 |
| natal:neptune | 17 | 0.3778 | 0.0339 | 12.9341 |
| moving:juno | 16 | 0.3556 | 0.0285 | 12.4633 |
| natal:mars | 16 | 0.3556 | 0.0283 | 8.2753 |
| moving:asc | 16 | 0.3556 | 0.0281 | 8.1397 |
| natal:lilith (asteroid) | 16 | 0.3556 | 0.027 | 26.6618 |
| moving:dsc | 16 | 0.3556 | 0.0268 | 6.2337 |
| natal:vesta | 16 | 0.3556 | 0.0263 | 19.6407 |
| moving:pallas | 16 | 0.3556 | 0.0255 | 18.0555 |

### B. Transit-to-Natal

Aktif pattern graph: 46 düğüm, 354 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | sun | 60 | sekstil | 0.9532 | 2 | 12 | False | True |
| sun | moon | 120 | üçgen | 2.3117 | 2 | 6 | False | True |
| sun | mars | 72 | 72 | 2.1863 | 2 | 5 | True | False |
| sun | saturn | 90 | kare | 0.5596 | 2 | 5 | True | False |
| sun | uranus | 135 | 135 | 1.9972 | 2 | 6 | True | False |
| sun | ceres | 120 | üçgen | 3.7731 | 2 | 6 | True | False |
| sun | pallas | 72 | 72 | 4.9145 | 2 | 5 | True | False |
| sun | juno | 180 | karşıtlık | 6.4867 | 2 | 8 | False | True |
| sun | vesta | 150 | quincunx | 0.0702 | 2 | 10 | False | True |
| sun | asc | 45 | 45 | 2.0783 | 2 | 1 | True | False |
| sun | dsc | 135 | 135 | 2.0783 | 2 | 7 | True | False |
| sun | nn | 0 | kavuşum | 1.4108 | 2 | 2 | False | True |
| sun | sn | 180 | karşıtlık | 1.4108 | 2 | 8 | False | True |
| moon | sun | 0 | kavuşum | 0.8857 | 12 | 12 | False | True |
| moon | moon | 180 | karşıtlık | 0.4729 | 12 | 6 | True | False |
| moon | venus | 45 | 45 | 0.9461 | 12 | 11 | True | False |
| moon | mars | 135 | 135 | 2.6526 | 12 | 5 | False | True |
| moon | saturn | 150 | quincunx | 1.2793 | 12 | 5 | False | True |
| moon | ceres | 180 | karşıtlık | 1.9342 | 12 | 6 | True | False |
| moon | pallas | 135 | 135 | 0.0756 | 12 | 5 | True | False |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| moving:nn | 0.4 | 0.0324 | 9.5327 |
| moving:sn | 0.4 | 0.0316 | 6.5722 |
| moving:saturn | 0.3778 | 0.0294 | 45.2174 |
| natal:pallas | 0.3778 | 0.0283 | 23.1215 |
| moving:uranus | 0.3778 | 0.028 | 15.6082 |
| natal:dsc | 0.3778 | 0.0277 | 22.5865 |
| natal:uranus | 0.3778 | 0.0277 | 16.6899 |
| moving:mercury | 0.3556 | 0.0263 | 10.7771 |
| natal:sn | 0.3556 | 0.026 | 26.3949 |
| natal:mc | 0.3556 | 0.0259 | 11.7649 |
| natal:nn | 0.3556 | 0.0258 | 26.5217 |
| moving:dsc | 0.3556 | 0.0256 | 8.9724 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| moving:nn | 18 | 0.4 | 0.0324 | 9.5327 |
| moving:sn | 18 | 0.4 | 0.0316 | 6.5722 |
| moving:saturn | 17 | 0.3778 | 0.0294 | 45.2174 |
| natal:pallas | 17 | 0.3778 | 0.0283 | 23.1215 |
| moving:uranus | 17 | 0.3778 | 0.028 | 15.6082 |
| natal:dsc | 17 | 0.3778 | 0.0277 | 22.5865 |
| natal:uranus | 17 | 0.3778 | 0.0277 | 16.6899 |
| moving:mercury | 16 | 0.3556 | 0.0263 | 10.7771 |
| natal:sn | 16 | 0.3556 | 0.026 | 26.3949 |
| natal:mc | 16 | 0.3556 | 0.0259 | 11.7649 |

### Shared Nodes ve Validation

| natal_node | keywords_tr |
| --- | --- |
| asc | görünüm, başlatma ekseni |
| ceres | besleme, bakım, sürdürülebilirlik |
| chiron | kırılganlık, ustalık, onarım |
| dsc | karşı eksen, ilişki alanı |
| ic | temel, kök, iç yapı |
| juno | bağlılık, sözleşme, karşılıklılık |
| jupiter | genişleme, inanç, fırsat, büyüme |
| lilith (asteroid) | temsili lilith varyantı |
| lilith (black moon) | ham dürtü, dışlanan içerik |
| mars | dürtü, mücadele, uygulama, ayrışma |
| mc | kamusal yön, zirve, kariyer |
| mercury | zihin, yazışma, ticaret, analitik süreç |
| moon | duygusal ritim, ihtiyaç, alışkanlık |
| neptune | belirsizlik, ideal, çözünme, geçirgenlik |
| nn | yön, gelişim vektörü |
| pallas | örüntü zekâsı, strateji, tasarım |
| pluto | yoğunlaşma, güç, eliminasyon, dönüşüm |
| saturn | yapı, yükümlülük, sınır, kurumsallaşma |
| sn | geçmiş örüntü, boşalma hattı |
| sun | irade, amaç, merkez |

Progressed validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 150 | 41 | quincunx |
| 135 | 41 | 135 |
| 0 | 40 | kavuşum |
| 45 | 38 | 45 |
| 30 | 38 | yarı-sekstil |
| 72 | 33 | 72 |
| 60 | 29 | sekstil |
| 90 | 28 | kare |
| 180 | 27 | karşıtlık |
| 120 | 25 | üçgen |

Transit validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 45 | 40 | 45 |
| 120 | 39 | üçgen |
| 72 | 39 | 72 |
| 135 | 37 | 135 |
| 30 | 37 | yarı-sekstil |
| 60 | 35 | sekstil |
| 150 | 34 | quincunx |
| 0 | 33 | kavuşum |
| 180 | 32 | karşıtlık |
| 90 | 28 | kare |

### Teknik Tematik Özet

Bu fazın teknik matrisi ilk ayarlama, küçük yön değişikliği ve veri toplama eksenini öne çıkarıyor. En yoğun temas alanları: iş rutini, hizmet, sağlık rejimi, teknik bakım; ortaklıklar, kontratlar, açık muhataplar; yaratıcılık, aşk, sahne, üretken ifade. Aktif natal düğüm imzası: ham dürtü, dışlanan içerik; belirsizlik, ideal, çözünme, geçirgenlik; dürtü, mücadele, uygulama, ayrışma; kopuş, yenilik, hızlanan değişim. Biyografik doğrulamada tekil olay aramak yerine, rol tanımı, iş-akış mimarisi, ilişki kontratları, kaynak yönetimi ve iç/dış yönelim dengesinde gözlenen yapısal yeniden dağılımlar izlenmeli.

## İlk Altmışlık (60°)

### Faz Doğrulama

| target_angle_deg | event_utc | event_local | progressed_chart_utc | progressed_sun_lon | progressed_moon_lon | moon_minus_sun_deg | exact_delta_deg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 60 | 2001-09-16T04:04:12.032884Z | 2001-09-16T07:04:12.032884+03:00 | 1982-05-27T12:16:31.367646Z | 65.883536 | 125.883536 | 60.0 | -4e-09 |

### A. Progressed-to-Natal

Aktif pattern graph: 46 düğüm, 337 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | mercury | 0 | kavuşum | 2.5282 | 1 | 1 | False | True |
| sun | venus | 60 | sekstil | 1.8215 | 1 | 11 | True | False |
| sun | mars | 120 | üçgen | 5.4202 | 1 | 5 | False | True |
| sun | jupiter | 150 | quincunx | 1.9503 | 1 | 6 | False | True |
| sun | saturn | 135 | 135 | 4.0469 | 1 | 5 | False | True |
| sun | uranus | 180 | karşıtlık | 2.6093 | 1 | 6 | False | True |
| sun | pluto | 135 | 135 | 4.0565 | 1 | 6 | True | False |
| sun | pallas | 120 | üçgen | 2.692 | 1 | 5 | False | True |
| sun | juno | 150 | quincunx | 3.9068 | 1 | 8 | True | False |
| sun | lilith (asteroid) | 60 | sekstil | 3.7254 | 1 | 11 | False | True |
| sun | asc | 0 | kavuşum | 2.5282 | 1 | 1 | False | True |
| sun | dsc | 180 | karşıtlık | 2.5282 | 1 | 7 | False | True |
| sun | mc | 120 | üçgen | 3.4963 | 1 | 10 | True | False |
| sun | ic | 60 | sekstil | 3.4963 | 1 | 4 | True | False |
| moon | mercury | 60 | sekstil | 2.5282 | 3 | 1 | True | False |
| moon | venus | 120 | üçgen | 1.8215 | 3 | 11 | False | True |
| moon | mars | 60 | sekstil | 5.4202 | 3 | 5 | False | True |
| moon | jupiter | 90 | kare | 1.9503 | 3 | 6 | False | True |
| moon | saturn | 72 | 72 | 1.0469 | 3 | 5 | False | True |
| moon | uranus | 120 | üçgen | 2.6093 | 3 | 6 | False | True |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| moving:juno | 0.4 | 0.0355 | 9.1078 |
| natal:chiron | 0.3556 | 0.0312 | 9.399 |
| natal:ic | 0.3556 | 0.0309 | 31.9292 |
| moving:asc | 0.3778 | 0.0305 | 9.327 |
| moving:vesta | 0.3556 | 0.0292 | 5.5936 |
| moving:moon | 0.3556 | 0.0279 | 6.4796 |
| natal:venus | 0.3556 | 0.0273 | 5.9287 |
| moving:pallas | 0.3556 | 0.0266 | 16.4019 |
| natal:mc | 0.3333 | 0.0266 | 31.5679 |
| natal:mars | 0.3333 | 0.0258 | 6.8058 |
| natal:mercury | 0.3333 | 0.025 | 13.8601 |
| natal:juno | 0.3333 | 0.025 | 11.3159 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| moving:juno | 18 | 0.4 | 0.0355 | 9.1078 |
| natal:chiron | 16 | 0.3556 | 0.0312 | 9.399 |
| natal:ic | 16 | 0.3556 | 0.0309 | 31.9292 |
| moving:asc | 17 | 0.3778 | 0.0305 | 9.327 |
| moving:vesta | 16 | 0.3556 | 0.0292 | 5.5936 |
| moving:moon | 16 | 0.3556 | 0.0279 | 6.4796 |
| natal:venus | 16 | 0.3556 | 0.0273 | 5.9287 |
| moving:pallas | 16 | 0.3556 | 0.0266 | 16.4019 |
| natal:mc | 15 | 0.3333 | 0.0266 | 31.5679 |
| natal:mars | 15 | 0.3333 | 0.0258 | 6.8058 |

### B. Transit-to-Natal

Aktif pattern graph: 46 düğüm, 375 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | moon | 60 | sekstil | 4.7746 | 5 | 6 | True | False |
| sun | mars | 0 | kavuşum | 7.1 | 5 | 5 | True | False |
| sun | jupiter | 45 | 45 | 4.4301 | 5 | 6 | False | True |
| sun | uranus | 72 | 72 | 2.0891 | 5 | 6 | False | True |
| sun | neptune | 90 | kare | 3.279 | 5 | 7 | True | False |
| sun | pluto | 30 | yarı-sekstil | 1.5767 | 5 | 6 | True | False |
| sun | ceres | 60 | sekstil | 3.3132 | 5 | 6 | False | True |
| sun | chiron | 120 | üçgen | 1.0647 | 5 | 12 | False | True |
| sun | lilith (black moon) | 90 | kare | 1.8058 | 5 | 7 | True | False |
| sun | dsc | 72 | 72 | 2.008 | 5 | 7 | False | True |
| sun | mc | 135 | 135 | 1.0165 | 5 | 10 | True | False |
| sun | ic | 45 | 45 | 1.0165 | 5 | 4 | True | False |
| sun | nn | 72 | 72 | 3.5029 | 5 | 2 | True | False |
| sun | lilith (black moon) | 90 | kare | 1.8058 | 5 | 7 | True | False |
| moon | moon | 72 | 72 | 1.2685 | 4 | 6 | True | False |
| moon | mercury | 90 | kare | 3.0915 | 4 | 1 | True | False |
| moon | venus | 150 | quincunx | 1.2583 | 4 | 11 | False | True |
| moon | mars | 30 | yarı-sekstil | 4.857 | 4 | 5 | False | True |
| moon | jupiter | 60 | sekstil | 1.387 | 4 | 6 | False | True |
| moon | saturn | 45 | 45 | 3.4837 | 4 | 5 | False | True |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| moving:mars | 0.4444 | 0.0324 | 101.1414 |
| moving:moon | 0.4 | 0.0303 | 7.0441 |
| moving:dsc | 0.4222 | 0.03 | 6.2422 |
| natal:pluto | 0.4 | 0.0297 | 6.9391 |
| moving:sn | 0.4222 | 0.0287 | 17.2492 |
| natal:mercury | 0.3778 | 0.0268 | 5.6121 |
| natal:sun | 0.3778 | 0.0265 | 13.2948 |
| moving:asc | 0.4 | 0.0263 | 5.668 |
| natal:ic | 0.3556 | 0.0245 | 8.2842 |
| moving:mercury | 0.3556 | 0.0243 | 9.0354 |
| natal:chiron | 0.3556 | 0.0238 | 7.0917 |
| natal:moon | 0.3778 | 0.0237 | 12.0027 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| moving:mars | 20 | 0.4444 | 0.0324 | 101.1414 |
| moving:moon | 18 | 0.4 | 0.0303 | 7.0441 |
| moving:dsc | 19 | 0.4222 | 0.03 | 6.2422 |
| natal:pluto | 18 | 0.4 | 0.0297 | 6.9391 |
| moving:sn | 19 | 0.4222 | 0.0287 | 17.2492 |
| natal:mercury | 17 | 0.3778 | 0.0268 | 5.6121 |
| natal:sun | 17 | 0.3778 | 0.0265 | 13.2948 |
| moving:asc | 18 | 0.4 | 0.0263 | 5.668 |
| natal:ic | 16 | 0.3556 | 0.0245 | 8.2842 |
| moving:mercury | 16 | 0.3556 | 0.0243 | 9.0354 |

### Shared Nodes ve Validation

| natal_node | keywords_tr |
| --- | --- |
| asc | görünüm, başlatma ekseni |
| ceres | besleme, bakım, sürdürülebilirlik |
| chiron | kırılganlık, ustalık, onarım |
| dsc | karşı eksen, ilişki alanı |
| ic | temel, kök, iç yapı |
| juno | bağlılık, sözleşme, karşılıklılık |
| jupiter | genişleme, inanç, fırsat, büyüme |
| lilith (asteroid) | temsili lilith varyantı |
| lilith (black moon) | ham dürtü, dışlanan içerik |
| mars | dürtü, mücadele, uygulama, ayrışma |
| mc | kamusal yön, zirve, kariyer |
| mercury | zihin, yazışma, ticaret, analitik süreç |
| moon | duygusal ritim, ihtiyaç, alışkanlık |
| neptune | belirsizlik, ideal, çözünme, geçirgenlik |
| nn | yön, gelişim vektörü |
| pallas | örüntü zekâsı, strateji, tasarım |
| pluto | yoğunlaşma, güç, eliminasyon, dönüşüm |
| saturn | yapı, yükümlülük, sınır, kurumsallaşma |
| sn | geçmiş örüntü, boşalma hattı |
| sun | irade, amaç, merkez |

Progressed validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 0 | 42 | kavuşum |
| 135 | 40 | 135 |
| 60 | 38 | sekstil |
| 45 | 37 | 45 |
| 120 | 32 | üçgen |
| 150 | 30 | quincunx |
| 90 | 30 | kare |
| 72 | 30 | 72 |
| 30 | 30 | yarı-sekstil |
| 180 | 28 | karşıtlık |

Transit validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 90 | 53 | kare |
| 45 | 45 | 45 |
| 72 | 40 | 72 |
| 30 | 39 | yarı-sekstil |
| 150 | 39 | quincunx |
| 135 | 37 | 135 |
| 120 | 36 | üçgen |
| 60 | 35 | sekstil |
| 0 | 30 | kavuşum |
| 180 | 21 | karşıtlık |

### Teknik Tematik Özet

Bu fazın teknik matrisi işlevsel açılım, ilk fırsat pencereleri eksenini öne çıkarıyor. En yoğun temas alanları: iş rutini, hizmet, sağlık rejimi, teknik bakım; ortaklıklar, kontratlar, açık muhataplar; yaratıcılık, aşk, sahne, üretken ifade. Aktif natal düğüm imzası: ham dürtü, dışlanan içerik; temel, kök, iç yapı; kırılganlık, ustalık, onarım; yoğunlaşma, güç, eliminasyon, dönüşüm. Biyografik doğrulamada tekil olay aramak yerine, rol tanımı, iş-akış mimarisi, ilişki kontratları, kaynak yönetimi ve iç/dış yönelim dengesinde gözlenen yapısal yeniden dağılımlar izlenmeli.

## İlk Kare (90°)

### Faz Doğrulama

| target_angle_deg | event_utc | event_local | progressed_chart_utc | progressed_sun_lon | progressed_moon_lon | moon_minus_sun_deg | exact_delta_deg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 90 | 2004-01-13T21:29:25.730005Z | 2004-01-13T23:29:25.730005+02:00 | 1982-05-29T20:06:34.279890Z | 68.115962 | 158.115962 | 90.0 | -5e-09 |

### A. Progressed-to-Natal

Aktif pattern graph: 46 düğüm, 343 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | mercury | 0 | kavuşum | 0.2958 | 1 | 1 | False | True |
| sun | venus | 60 | sekstil | 4.0539 | 1 | 11 | True | False |
| sun | jupiter | 150 | quincunx | 4.1827 | 1 | 6 | False | True |
| sun | uranus | 180 | karşıtlık | 4.8418 | 1 | 6 | False | True |
| sun | pluto | 135 | 135 | 1.824 | 1 | 6 | True | False |
| sun | pallas | 120 | üçgen | 4.9244 | 1 | 5 | False | True |
| sun | juno | 150 | quincunx | 1.6744 | 1 | 8 | True | False |
| sun | lilith (asteroid) | 60 | sekstil | 5.9578 | 1 | 11 | False | True |
| sun | asc | 0 | kavuşum | 4.7606 | 1 | 1 | False | True |
| sun | dsc | 180 | karşıtlık | 4.7606 | 1 | 7 | False | True |
| sun | mc | 120 | üçgen | 1.2639 | 1 | 10 | True | False |
| sun | ic | 60 | sekstil | 1.2639 | 1 | 4 | True | False |
| moon | moon | 72 | 72 | 1.5272 | 5 | 6 | False | True |
| moon | mercury | 90 | kare | 0.2958 | 5 | 1 | True | False |
| moon | venus | 150 | quincunx | 4.0539 | 5 | 11 | False | True |
| moon | jupiter | 60 | sekstil | 4.1827 | 5 | 6 | False | True |
| moon | uranus | 90 | kare | 4.8418 | 5 | 6 | False | True |
| moon | pluto | 45 | 45 | 1.824 | 5 | 6 | True | False |
| moon | ceres | 72 | 72 | 0.0659 | 5 | 6 | False | True |
| moon | pallas | 30 | yarı-sekstil | 4.9244 | 5 | 5 | False | True |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| moving:juno | 0.4 | 0.0363 | 10.3628 |
| natal:vesta | 0.3778 | 0.0313 | 12.0827 |
| natal:juno | 0.3556 | 0.0295 | 6.0056 |
| moving:lilith (black moon) | 0.3333 | 0.0269 | 11.2342 |
| moving:ic | 0.3556 | 0.0268 | 5.7915 |
| moving:mc | 0.3556 | 0.0268 | 5.7915 |
| natal:moon | 0.3556 | 0.0266 | 6.7977 |
| moving:pallas | 0.3556 | 0.0259 | 15.3665 |
| moving:asc | 0.3556 | 0.0258 | 12.992 |
| natal:sun | 0.3556 | 0.0255 | 25.5567 |
| natal:saturn | 0.3333 | 0.0251 | 10.2441 |
| natal:ic | 0.3111 | 0.0241 | 5.8801 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| moving:juno | 18 | 0.4 | 0.0363 | 10.3628 |
| natal:vesta | 17 | 0.3778 | 0.0313 | 12.0827 |
| natal:juno | 16 | 0.3556 | 0.0295 | 6.0056 |
| moving:lilith (black moon) | 15 | 0.3333 | 0.0269 | 11.2342 |
| moving:ic | 16 | 0.3556 | 0.0268 | 5.7915 |
| moving:mc | 16 | 0.3556 | 0.0268 | 5.7915 |
| natal:moon | 16 | 0.3556 | 0.0266 | 6.7977 |
| moving:pallas | 16 | 0.3556 | 0.0259 | 15.3665 |
| moving:asc | 16 | 0.3556 | 0.0258 | 12.992 |
| natal:sun | 16 | 0.3556 | 0.0255 | 25.5567 |

### B. Transit-to-Natal

Aktif pattern graph: 46 düğüm, 348 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | sun | 120 | üçgen | 5.8005 | 9 | 12 | False | True |
| sun | moon | 60 | sekstil | 4.442 | 9 | 6 | True | False |
| sun | mercury | 135 | 135 | 0.381 | 9 | 1 | False | True |
| sun | venus | 72 | 72 | 0.9687 | 9 | 11 | True | False |
| sun | uranus | 45 | 45 | 4.7565 | 9 | 6 | False | True |
| sun | neptune | 30 | yarı-sekstil | 3.6116 | 9 | 7 | True | False |
| sun | pluto | 90 | kare | 1.9093 | 9 | 6 | True | False |
| sun | ceres | 60 | sekstil | 2.9806 | 9 | 6 | False | True |
| sun | chiron | 120 | üçgen | 0.7322 | 9 | 12 | False | True |
| sun | lilith (black moon) | 30 | yarı-sekstil | 2.1384 | 9 | 7 | True | False |
| sun | lilith (asteroid) | 72 | 72 | 2.8726 | 9 | 11 | False | True |
| sun | asc | 135 | 135 | 4.6754 | 9 | 1 | False | True |
| sun | dsc | 45 | 45 | 4.6754 | 9 | 7 | False | True |
| sun | lilith (black moon) | 30 | yarı-sekstil | 2.1384 | 9 | 7 | True | False |
| moon | sun | 135 | 135 | 4.387 | 5 | 12 | False | True |
| moon | moon | 45 | 45 | 3.0284 | 5 | 6 | False | True |
| moon | mercury | 120 | üçgen | 1.7946 | 5 | 1 | True | False |
| moon | venus | 180 | karşıtlık | 2.5552 | 5 | 11 | False | True |
| moon | mars | 0 | kavuşum | 6.1539 | 5 | 5 | False | True |
| moon | jupiter | 30 | yarı-sekstil | 2.6839 | 5 | 6 | False | True |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| natal:saturn | 0.4444 | 0.0423 | 14.2805 |
| moving:mercury | 0.4 | 0.0382 | 7.163 |
| natal:sun | 0.4222 | 0.0349 | 16.6716 |
| moving:moon | 0.3778 | 0.0309 | 6.7587 |
| moving:chiron | 0.3778 | 0.0305 | 11.2249 |
| moving:uranus | 0.3556 | 0.0297 | 12.4502 |
| natal:uranus | 0.4 | 0.0287 | 7.2913 |
| natal:dsc | 0.4 | 0.0287 | 7.0716 |
| natal:nn | 0.3778 | 0.0277 | 24.8988 |
| natal:sn | 0.3778 | 0.0277 | 24.8988 |
| natal:vesta | 0.3778 | 0.0265 | 8.7044 |
| moving:venus | 0.3333 | 0.0265 | 6.3727 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| natal:saturn | 20 | 0.4444 | 0.0423 | 14.2805 |
| moving:mercury | 18 | 0.4 | 0.0382 | 7.163 |
| natal:sun | 19 | 0.4222 | 0.0349 | 16.6716 |
| moving:moon | 17 | 0.3778 | 0.0309 | 6.7587 |
| moving:chiron | 17 | 0.3778 | 0.0305 | 11.2249 |
| moving:uranus | 16 | 0.3556 | 0.0297 | 12.4502 |
| natal:dsc | 18 | 0.4 | 0.0287 | 7.0716 |
| natal:uranus | 18 | 0.4 | 0.0287 | 7.2913 |
| natal:nn | 17 | 0.3778 | 0.0277 | 24.8988 |
| natal:sn | 17 | 0.3778 | 0.0277 | 24.8988 |

### Shared Nodes ve Validation

| natal_node | keywords_tr |
| --- | --- |
| asc | görünüm, başlatma ekseni |
| ceres | besleme, bakım, sürdürülebilirlik |
| chiron | kırılganlık, ustalık, onarım |
| dsc | karşı eksen, ilişki alanı |
| ic | temel, kök, iç yapı |
| juno | bağlılık, sözleşme, karşılıklılık |
| jupiter | genişleme, inanç, fırsat, büyüme |
| lilith (asteroid) | temsili lilith varyantı |
| lilith (black moon) | ham dürtü, dışlanan içerik |
| mars | dürtü, mücadele, uygulama, ayrışma |
| mc | kamusal yön, zirve, kariyer |
| mercury | zihin, yazışma, ticaret, analitik süreç |
| moon | duygusal ritim, ihtiyaç, alışkanlık |
| neptune | belirsizlik, ideal, çözünme, geçirgenlik |
| nn | yön, gelişim vektörü |
| pallas | örüntü zekâsı, strateji, tasarım |
| pluto | yoğunlaşma, güç, eliminasyon, dönüşüm |
| saturn | yapı, yükümlülük, sınır, kurumsallaşma |
| sn | geçmiş örüntü, boşalma hattı |
| sun | irade, amaç, merkez |

Progressed validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 45 | 41 | 45 |
| 0 | 40 | kavuşum |
| 60 | 36 | sekstil |
| 150 | 36 | quincunx |
| 135 | 36 | 135 |
| 90 | 36 | kare |
| 30 | 35 | yarı-sekstil |
| 72 | 30 | 72 |
| 120 | 28 | üçgen |
| 180 | 25 | karşıtlık |

Transit validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 60 | 46 | sekstil |
| 135 | 45 | 135 |
| 45 | 44 | 45 |
| 90 | 37 | kare |
| 120 | 35 | üçgen |
| 30 | 33 | yarı-sekstil |
| 150 | 31 | quincunx |
| 0 | 30 | kavuşum |
| 180 | 24 | karşıtlık |
| 72 | 23 | 72 |

### Teknik Tematik Özet

Bu fazın teknik matrisi gerilimle biçimlenme, zorunlu karar ve yön ayrışması eksenini öne çıkarıyor. En yoğun temas alanları: iş rutini, hizmet, sağlık rejimi, teknik bakım; ortaklıklar, kontratlar, açık muhataplar; yaratıcılık, aşk, sahne, üretken ifade. Aktif natal düğüm imzası: ham dürtü, dışlanan içerik; adanma, odak, kutsal görev; irade, amaç, merkez; yapı, yükümlülük, sınır, kurumsallaşma. Biyografik doğrulamada tekil olay aramak yerine, rol tanımı, iş-akış mimarisi, ilişki kontratları, kaynak yönetimi ve iç/dış yönelim dengesinde gözlenen yapısal yeniden dağılımlar izlenmeli.

## Büyüyen Üçgen (120°)

### Faz Doğrulama

| target_angle_deg | event_utc | event_local | progressed_chart_utc | progressed_sun_lon | progressed_moon_lon | moon_minus_sun_deg | exact_delta_deg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 120 | 2006-07-09T11:54:58.090679Z | 2006-07-09T14:54:58.090679+03:00 | 1982-06-01T07:44:47.592308Z | 70.498049 | 190.498049 | 120.0 | -2e-09 |

### A. Progressed-to-Natal

Aktif pattern graph: 46 düğüm, 345 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | mercury | 0 | kavuşum | 2.0863 | 1 | 1 | True | False |
| sun | venus | 72 | 72 | 5.564 | 1 | 11 | False | True |
| sun | uranus | 180 | karşıtlık | 7.2239 | 1 | 6 | False | True |
| sun | pluto | 135 | 135 | 0.5581 | 1 | 6 | False | True |
| sun | juno | 150 | quincunx | 0.7077 | 1 | 8 | False | True |
| sun | vesta | 120 | üçgen | 5.7088 | 1 | 10 | True | False |
| sun | lilith (asteroid) | 72 | 72 | 3.6601 | 1 | 11 | True | False |
| sun | asc | 0 | kavuşum | 7.1427 | 1 | 1 | False | True |
| sun | dsc | 180 | karşıtlık | 7.1427 | 1 | 7 | False | True |
| sun | mc | 120 | üçgen | 1.1182 | 1 | 10 | False | True |
| sun | ic | 60 | sekstil | 1.1182 | 1 | 4 | False | True |
| sun | nn | 30 | yarı-sekstil | 4.3682 | 1 | 2 | True | False |
| sun | sn | 150 | quincunx | 4.3682 | 1 | 8 | True | False |
| moon | mercury | 120 | üçgen | 2.0863 | 5 | 1 | False | True |
| moon | venus | 180 | karşıtlık | 6.436 | 5 | 11 | False | True |
| moon | saturn | 0 | kavuşum | 6.3386 | 5 | 5 | True | False |
| moon | neptune | 72 | 72 | 4.1443 | 5 | 7 | True | False |
| moon | ceres | 45 | 45 | 5.4479 | 5 | 6 | False | True |
| moon | pallas | 0 | kavuşum | 7.3065 | 5 | 5 | False | True |
| moon | juno | 90 | kare | 0.7077 | 5 | 8 | False | True |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| moving:juno | 0.4222 | 0.0394 | 17.1139 |
| natal:vesta | 0.4 | 0.0344 | 8.7238 |
| natal:nn | 0.4 | 0.033 | 11.4771 |
| moving:ceres | 0.3778 | 0.0316 | 16.1004 |
| moving:lilith (black moon) | 0.3556 | 0.0308 | 11.4195 |
| moving:asc | 0.3556 | 0.0276 | 24.5032 |
| natal:venus | 0.3556 | 0.0274 | 8.5982 |
| natal:sn | 0.3556 | 0.0259 | 11.0183 |
| natal:sun | 0.3556 | 0.0257 | 8.4629 |
| natal:juno | 0.3333 | 0.025 | 13.5902 |
| natal:ic | 0.3333 | 0.0249 | 22.3726 |
| moving:uranus | 0.3333 | 0.0231 | 17.1713 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| moving:juno | 19 | 0.4222 | 0.0394 | 17.1139 |
| natal:vesta | 18 | 0.4 | 0.0344 | 8.7238 |
| natal:nn | 18 | 0.4 | 0.033 | 11.4771 |
| moving:ceres | 17 | 0.3778 | 0.0316 | 16.1004 |
| moving:lilith (black moon) | 16 | 0.3556 | 0.0308 | 11.4195 |
| moving:asc | 16 | 0.3556 | 0.0276 | 24.5032 |
| natal:venus | 16 | 0.3556 | 0.0274 | 8.5982 |
| natal:sn | 16 | 0.3556 | 0.0259 | 11.0183 |
| natal:sun | 16 | 0.3556 | 0.0257 | 8.4629 |
| natal:juno | 15 | 0.3333 | 0.025 | 13.5902 |

### B. Transit-to-Natal

Aktif pattern graph: 46 düğüm, 371 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | sun | 60 | sekstil | 0.0833 | 2 | 12 | False | True |
| sun | moon | 120 | üçgen | 1.4418 | 2 | 6 | False | True |
| sun | mars | 72 | 72 | 1.3164 | 2 | 5 | True | False |
| sun | saturn | 90 | kare | 0.3103 | 2 | 5 | False | True |
| sun | uranus | 135 | 135 | 1.1273 | 2 | 6 | True | False |
| sun | ceres | 120 | üçgen | 2.9032 | 2 | 6 | True | False |
| sun | pallas | 72 | 72 | 4.0446 | 2 | 5 | True | False |
| sun | juno | 180 | karşıtlık | 7.3566 | 2 | 8 | False | True |
| sun | vesta | 150 | quincunx | 0.9401 | 2 | 10 | False | True |
| sun | chiron | 60 | sekstil | 5.1516 | 2 | 12 | True | False |
| sun | asc | 45 | 45 | 1.2084 | 2 | 1 | True | False |
| sun | dsc | 135 | 135 | 1.2084 | 2 | 7 | True | False |
| sun | nn | 0 | kavuşum | 2.2807 | 2 | 2 | False | True |
| sun | sn | 180 | karşıtlık | 2.2807 | 2 | 8 | False | True |
| moon | mars | 90 | kare | 4.8116 | 7 | 5 | True | False |
| moon | saturn | 72 | 72 | 3.1849 | 7 | 5 | True | False |
| moon | neptune | 0 | kavuşum | 0.9906 | 7 | 7 | True | False |
| moon | pluto | 60 | sekstil | 0.7117 | 7 | 6 | False | True |
| moon | ceres | 30 | yarı-sekstil | 5.6016 | 7 | 6 | False | True |
| moon | vesta | 45 | 45 | 5.5551 | 7 | 10 | True | False |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| moving:nn | 0.4222 | 0.0329 | 6.2491 |
| natal:lilith (black moon) | 0.4 | 0.0322 | 23.3029 |
| moving:juno | 0.4222 | 0.0314 | 108.367 |
| moving:mc | 0.4222 | 0.0314 | 25.5009 |
| moving:pallas | 0.4 | 0.0297 | 9.6012 |
| natal:neptune | 0.3778 | 0.029 | 9.649 |
| moving:sn | 0.4 | 0.0286 | 5.6729 |
| moving:ic | 0.4 | 0.0279 | 28.1641 |
| natal:ic | 0.3778 | 0.0275 | 10.2537 |
| moving:neptune | 0.3778 | 0.0253 | 12.7132 |
| natal:mc | 0.3556 | 0.0243 | 10.0489 |
| natal:saturn | 0.3556 | 0.0241 | 12.5205 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| moving:nn | 19 | 0.4222 | 0.0329 | 6.2491 |
| natal:lilith (black moon) | 18 | 0.4 | 0.0322 | 23.3029 |
| moving:juno | 19 | 0.4222 | 0.0314 | 108.367 |
| moving:mc | 19 | 0.4222 | 0.0314 | 25.5009 |
| moving:pallas | 18 | 0.4 | 0.0297 | 9.6012 |
| natal:neptune | 17 | 0.3778 | 0.029 | 9.649 |
| moving:sn | 18 | 0.4 | 0.0286 | 5.6729 |
| moving:ic | 18 | 0.4 | 0.0279 | 28.1641 |
| natal:ic | 17 | 0.3778 | 0.0275 | 10.2537 |
| moving:neptune | 17 | 0.3778 | 0.0253 | 12.7132 |

### Shared Nodes ve Validation

| natal_node | keywords_tr |
| --- | --- |
| asc | görünüm, başlatma ekseni |
| ceres | besleme, bakım, sürdürülebilirlik |
| chiron | kırılganlık, ustalık, onarım |
| dsc | karşı eksen, ilişki alanı |
| ic | temel, kök, iç yapı |
| juno | bağlılık, sözleşme, karşılıklılık |
| jupiter | genişleme, inanç, fırsat, büyüme |
| lilith (asteroid) | temsili lilith varyantı |
| lilith (black moon) | ham dürtü, dışlanan içerik |
| mars | dürtü, mücadele, uygulama, ayrışma |
| mc | kamusal yön, zirve, kariyer |
| mercury | zihin, yazışma, ticaret, analitik süreç |
| moon | duygusal ritim, ihtiyaç, alışkanlık |
| neptune | belirsizlik, ideal, çözünme, geçirgenlik |
| nn | yön, gelişim vektörü |
| pallas | örüntü zekâsı, strateji, tasarım |
| pluto | yoğunlaşma, güç, eliminasyon, dönüşüm |
| saturn | yapı, yükümlülük, sınır, kurumsallaşma |
| sn | geçmiş örüntü, boşalma hattı |
| sun | irade, amaç, merkez |

Progressed validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 45 | 43 | 45 |
| 90 | 40 | kare |
| 0 | 39 | kavuşum |
| 135 | 38 | 135 |
| 30 | 35 | yarı-sekstil |
| 72 | 34 | 72 |
| 150 | 34 | quincunx |
| 60 | 31 | sekstil |
| 120 | 26 | üçgen |
| 180 | 25 | karşıtlık |

Transit validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 90 | 46 | kare |
| 135 | 46 | 135 |
| 45 | 46 | 45 |
| 72 | 43 | 72 |
| 150 | 40 | quincunx |
| 60 | 39 | sekstil |
| 120 | 34 | üçgen |
| 30 | 34 | yarı-sekstil |
| 0 | 23 | kavuşum |
| 180 | 20 | karşıtlık |

### Teknik Tematik Özet

Bu fazın teknik matrisi akış yakalama, kapasiteyi görünür hale getirme eksenini öne çıkarıyor. En yoğun temas alanları: iş rutini, hizmet, sağlık rejimi, teknik bakım; ortaklıklar, kontratlar, açık muhataplar; yaratıcılık, aşk, sahne, üretken ifade. Aktif natal düğüm imzası: ham dürtü, dışlanan içerik; adanma, odak, kutsal görev; yön, gelişim vektörü; temel, kök, iç yapı. Biyografik doğrulamada tekil olay aramak yerine, rol tanımı, iş-akış mimarisi, ilişki kontratları, kaynak yönetimi ve iç/dış yönelim dengesinde gözlenen yapısal yeniden dağılımlar izlenmeli.

## Büyüyen Quincunx (150°)

### Faz Doğrulama

| target_angle_deg | event_utc | event_local | progressed_chart_utc | progressed_sun_lon | progressed_moon_lon | moon_minus_sun_deg | exact_delta_deg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 150 | 2009-02-21T14:02:48.922205Z | 2009-02-21T16:02:48.922205+02:00 | 1982-06-03T22:42:03.788972Z | 73.010287 | 223.010287 | 150.0 | -2e-09 |

### A. Progressed-to-Natal

Aktif pattern graph: 46 düğüm, 350 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | sun | 30 | yarı-sekstil | 4.2199 | 1 | 12 | False | True |
| sun | moon | 150 | quincunx | 5.5785 | 1 | 6 | False | True |
| sun | mercury | 0 | kavuşum | 4.5986 | 1 | 1 | True | False |
| sun | venus | 72 | 72 | 3.0517 | 1 | 11 | False | True |
| sun | jupiter | 135 | 135 | 5.923 | 1 | 6 | True | False |
| sun | saturn | 120 | üçgen | 3.8263 | 1 | 5 | True | False |
| sun | pluto | 135 | 135 | 3.0703 | 1 | 6 | False | True |
| sun | juno | 150 | quincunx | 3.22 | 1 | 8 | False | True |
| sun | vesta | 120 | üçgen | 3.1965 | 1 | 10 | True | False |
| sun | lilith (asteroid) | 72 | 72 | 1.1478 | 1 | 11 | True | False |
| sun | mc | 120 | üçgen | 3.6305 | 1 | 10 | False | True |
| sun | ic | 60 | sekstil | 3.6305 | 1 | 4 | False | True |
| sun | nn | 30 | yarı-sekstil | 1.8559 | 1 | 2 | True | False |
| sun | sn | 150 | quincunx | 1.8559 | 1 | 8 | True | False |
| moon | sun | 180 | karşıtlık | 4.2199 | 6 | 12 | True | False |
| moon | moon | 0 | kavuşum | 5.5785 | 6 | 6 | False | True |
| moon | mercury | 150 | quincunx | 4.5986 | 6 | 1 | False | True |
| moon | mars | 45 | 45 | 2.453 | 6 | 5 | True | False |
| moon | saturn | 30 | yarı-sekstil | 3.8263 | 6 | 5 | True | False |
| moon | neptune | 45 | 45 | 1.3679 | 6 | 7 | False | True |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| natal:ic | 0.4222 | 0.0411 | 24.2056 |
| moving:lilith (black moon) | 0.4 | 0.0369 | 12.6145 |
| natal:moon | 0.4 | 0.0352 | 14.4527 |
| natal:mc | 0.3778 | 0.0317 | 23.5977 |
| moving:ceres | 0.3778 | 0.0317 | 15.5836 |
| moving:juno | 0.3778 | 0.031 | 11.0875 |
| moving:moon | 0.3556 | 0.028 | 5.5439 |
| moving:mars | 0.3556 | 0.027 | 40.1885 |
| natal:vesta | 0.3556 | 0.0254 | 7.6362 |
| moving:uranus | 0.3333 | 0.0253 | 46.8747 |
| natal:juno | 0.3333 | 0.0247 | 68.9995 |
| natal:saturn | 0.3333 | 0.0242 | 10.1577 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| natal:ic | 19 | 0.4222 | 0.0411 | 24.2056 |
| moving:lilith (black moon) | 18 | 0.4 | 0.0369 | 12.6145 |
| natal:moon | 18 | 0.4 | 0.0352 | 14.4527 |
| moving:ceres | 17 | 0.3778 | 0.0317 | 15.5836 |
| natal:mc | 17 | 0.3778 | 0.0317 | 23.5977 |
| moving:juno | 17 | 0.3778 | 0.031 | 11.0875 |
| moving:moon | 16 | 0.3556 | 0.028 | 5.5439 |
| moving:mars | 16 | 0.3556 | 0.027 | 40.1885 |
| natal:vesta | 16 | 0.3556 | 0.0254 | 7.6362 |
| moving:uranus | 15 | 0.3333 | 0.0253 | 46.8747 |

### B. Transit-to-Natal

Aktif pattern graph: 46 düğüm, 379 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | sun | 72 | 72 | 2.1517 | 10 | 12 | True | False |
| sun | mercury | 90 | kare | 5.3332 | 10 | 1 | False | True |
| sun | venus | 30 | yarı-sekstil | 0.9835 | 10 | 11 | False | True |
| sun | mars | 150 | quincunx | 2.6152 | 10 | 5 | False | True |
| sun | jupiter | 120 | üçgen | 0.8547 | 10 | 6 | True | False |
| sun | saturn | 135 | 135 | 1.2419 | 10 | 5 | False | True |
| sun | uranus | 90 | kare | 0.1957 | 10 | 6 | True | False |
| sun | neptune | 72 | 72 | 5.5638 | 10 | 7 | True | False |
| sun | pallas | 150 | quincunx | 0.113 | 10 | 5 | True | False |
| sun | lilith (black moon) | 72 | 72 | 4.0906 | 10 | 7 | True | False |
| sun | lilith (asteroid) | 30 | yarı-sekstil | 0.9204 | 10 | 11 | False | True |
| sun | asc | 90 | kare | 0.2768 | 10 | 1 | True | False |
| sun | dsc | 90 | kare | 0.2768 | 10 | 7 | True | False |
| sun | nn | 135 | 135 | 3.2123 | 10 | 2 | False | True |
| sun | sn | 45 | 45 | 3.2123 | 10 | 8 | False | True |
| sun | lilith (black moon) | 72 | 72 | 4.0906 | 10 | 7 | True | False |
| moon | moon | 60 | sekstil | 5.4022 | 9 | 6 | True | False |
| moon | mercury | 135 | 135 | 0.5792 | 9 | 1 | False | True |
| moon | venus | 72 | 72 | 1.9289 | 9 | 11 | False | True |
| moon | uranus | 45 | 45 | 5.7168 | 9 | 6 | False | True |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| moving:pluto | 0.4222 | 0.0361 | 17.7218 |
| natal:lilith (black moon) | 0.4222 | 0.0326 | 21.4127 |
| moving:lilith (black moon) | 0.4 | 0.0326 | 19.0595 |
| natal:mercury | 0.4222 | 0.0318 | 14.0254 |
| natal:juno | 0.4 | 0.0306 | 15.4685 |
| moving:asc | 0.4 | 0.0293 | 14.6479 |
| natal:neptune | 0.4 | 0.0289 | 8.8138 |
| natal:ic | 0.4 | 0.0271 | 18.9585 |
| natal:mc | 0.4 | 0.0271 | 18.9585 |
| moving:sn | 0.3778 | 0.026 | 19.9138 |
| moving:mars | 0.4 | 0.025 | 6.511 |
| moving:uranus | 0.3556 | 0.0246 | 15.0277 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| moving:pluto | 19 | 0.4222 | 0.0361 | 17.7218 |
| natal:lilith (black moon) | 19 | 0.4222 | 0.0326 | 21.4127 |
| moving:lilith (black moon) | 18 | 0.4 | 0.0326 | 19.0595 |
| natal:mercury | 19 | 0.4222 | 0.0318 | 14.0254 |
| natal:juno | 18 | 0.4 | 0.0306 | 15.4685 |
| moving:asc | 18 | 0.4 | 0.0293 | 14.6479 |
| natal:neptune | 18 | 0.4 | 0.0289 | 8.8138 |
| natal:ic | 18 | 0.4 | 0.0271 | 18.9585 |
| natal:mc | 18 | 0.4 | 0.0271 | 18.9585 |
| moving:sn | 17 | 0.3778 | 0.026 | 19.9138 |

### Shared Nodes ve Validation

| natal_node | keywords_tr |
| --- | --- |
| asc | görünüm, başlatma ekseni |
| ceres | besleme, bakım, sürdürülebilirlik |
| chiron | kırılganlık, ustalık, onarım |
| dsc | karşı eksen, ilişki alanı |
| ic | temel, kök, iç yapı |
| juno | bağlılık, sözleşme, karşılıklılık |
| jupiter | genişleme, inanç, fırsat, büyüme |
| lilith (asteroid) | temsili lilith varyantı |
| lilith (black moon) | ham dürtü, dışlanan içerik |
| mars | dürtü, mücadele, uygulama, ayrışma |
| mc | kamusal yön, zirve, kariyer |
| mercury | zihin, yazışma, ticaret, analitik süreç |
| moon | duygusal ritim, ihtiyaç, alışkanlık |
| neptune | belirsizlik, ideal, çözünme, geçirgenlik |
| nn | yön, gelişim vektörü |
| pallas | örüntü zekâsı, strateji, tasarım |
| pluto | yoğunlaşma, güç, eliminasyon, dönüşüm |
| saturn | yapı, yükümlülük, sınır, kurumsallaşma |
| sn | geçmiş örüntü, boşalma hattı |
| sun | irade, amaç, merkez |

Progressed validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 45 | 44 | 45 |
| 30 | 40 | yarı-sekstil |
| 150 | 39 | quincunx |
| 135 | 39 | 135 |
| 60 | 39 | sekstil |
| 90 | 38 | kare |
| 0 | 37 | kavuşum |
| 120 | 27 | üçgen |
| 72 | 26 | 72 |
| 180 | 21 | karşıtlık |

Transit validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 90 | 59 | kare |
| 45 | 52 | 45 |
| 135 | 43 | 135 |
| 30 | 42 | yarı-sekstil |
| 72 | 36 | 72 |
| 150 | 35 | quincunx |
| 120 | 35 | üçgen |
| 60 | 34 | sekstil |
| 0 | 25 | kavuşum |
| 180 | 18 | karşıtlık |

### Teknik Tematik Özet

Bu fazın teknik matrisi uyumsuz parçaları yeniden ayarlama, teknik düzeltme eksenini öne çıkarıyor. En yoğun temas alanları: iş rutini, hizmet, sağlık rejimi, teknik bakım; ortaklıklar, kontratlar, açık muhataplar; yaratıcılık, aşk, sahne, üretken ifade. Aktif natal düğüm imzası: ham dürtü, dışlanan içerik; temel, kök, iç yapı; duygusal ritim, ihtiyaç, alışkanlık; zihin, yazışma, ticaret, analitik süreç. Biyografik doğrulamada tekil olay aramak yerine, rol tanımı, iş-akış mimarisi, ilişki kontratları, kaynak yönetimi ve iç/dış yönelim dengesinde gözlenen yapısal yeniden dağılımlar izlenmeli.

## İlerletilmiş Dolunay (180°)

### Faz Doğrulama

| target_angle_deg | event_utc | event_local | progressed_chart_utc | progressed_sun_lon | progressed_moon_lon | moon_minus_sun_deg | exact_delta_deg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 180 | 2011-11-12T04:35:13.137426Z | 2011-11-12T06:35:13.137426+02:00 | 1982-06-06T15:59:21.555475Z | 75.613512 | 255.613512 | 180.0 | -2e-09 |

### A. Progressed-to-Natal

Aktif pattern graph: 46 düğüm, 353 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | sun | 30 | yarı-sekstil | 1.6167 | 1 | 12 | False | True |
| sun | moon | 150 | quincunx | 2.9752 | 1 | 6 | False | True |
| sun | mercury | 0 | kavuşum | 7.2018 | 1 | 1 | True | False |
| sun | venus | 72 | 72 | 0.4485 | 1 | 11 | False | True |
| sun | jupiter | 135 | 135 | 3.3197 | 1 | 6 | True | False |
| sun | saturn | 120 | üçgen | 1.2231 | 1 | 5 | True | False |
| sun | pluto | 135 | 135 | 5.6735 | 1 | 6 | False | True |
| sun | ceres | 150 | quincunx | 4.4366 | 1 | 6 | True | False |
| sun | juno | 150 | quincunx | 5.8232 | 1 | 8 | False | True |
| sun | vesta | 120 | üçgen | 0.5933 | 1 | 10 | True | False |
| sun | lilith (asteroid) | 72 | 72 | 1.4554 | 1 | 11 | False | True |
| sun | nn | 30 | yarı-sekstil | 0.7473 | 1 | 2 | False | True |
| sun | sn | 150 | quincunx | 0.7473 | 1 | 8 | False | True |
| moon | sun | 150 | quincunx | 1.6167 | 7 | 12 | True | False |
| moon | moon | 30 | yarı-sekstil | 2.9752 | 7 | 6 | False | True |
| moon | mercury | 180 | karşıtlık | 7.2018 | 7 | 1 | False | True |
| moon | mars | 72 | 72 | 3.1502 | 7 | 5 | False | True |
| moon | jupiter | 45 | 45 | 3.3197 | 7 | 6 | True | False |
| moon | saturn | 60 | sekstil | 1.2231 | 7 | 5 | True | False |
| moon | pluto | 45 | 45 | 5.6735 | 7 | 6 | False | True |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| natal:juno | 0.4222 | 0.0389 | 7.2534 |
| moving:asc | 0.4 | 0.0347 | 10.9319 |
| moving:juno | 0.4 | 0.033 | 7.9914 |
| moving:ceres | 0.3778 | 0.0311 | 8.3793 |
| moving:dsc | 0.3778 | 0.0309 | 10.7192 |
| moving:lilith (black moon) | 0.3778 | 0.0296 | 14.3371 |
| natal:vesta | 0.3778 | 0.0296 | 11.381 |
| moving:mars | 0.3778 | 0.0289 | 21.7196 |
| natal:ic | 0.3556 | 0.0273 | 5.8664 |
| natal:moon | 0.3556 | 0.0256 | 8.036 |
| natal:saturn | 0.3333 | 0.0229 | 15.4602 |
| natal:pluto | 0.3111 | 0.0224 | 8.6489 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| natal:juno | 19 | 0.4222 | 0.0389 | 7.2534 |
| moving:asc | 18 | 0.4 | 0.0347 | 10.9319 |
| moving:juno | 18 | 0.4 | 0.033 | 7.9914 |
| moving:ceres | 17 | 0.3778 | 0.0311 | 8.3793 |
| moving:dsc | 17 | 0.3778 | 0.0309 | 10.7192 |
| moving:lilith (black moon) | 17 | 0.3778 | 0.0296 | 14.3371 |
| natal:vesta | 17 | 0.3778 | 0.0296 | 11.381 |
| moving:mars | 17 | 0.3778 | 0.0289 | 21.7196 |
| natal:ic | 16 | 0.3556 | 0.0273 | 5.8664 |
| natal:moon | 16 | 0.3556 | 0.0256 | 8.036 |

### B. Transit-to-Natal

Aktif pattern graph: 46 düğüm, 344 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | sun | 180 | karşıtlık | 2.2054 | 6 | 12 | False | True |
| sun | moon | 0 | kavuşum | 0.8469 | 6 | 6 | True | False |
| sun | venus | 135 | 135 | 0.3736 | 6 | 11 | True | False |
| sun | mars | 45 | 45 | 3.9723 | 6 | 5 | False | True |
| sun | saturn | 30 | yarı-sekstil | 2.599 | 6 | 5 | False | True |
| sun | pluto | 30 | yarı-sekstil | 5.5044 | 6 | 6 | True | False |
| sun | ceres | 0 | kavuşum | 0.6145 | 6 | 6 | True | False |
| sun | pallas | 45 | 45 | 1.2441 | 6 | 5 | False | True |
| sun | juno | 45 | 45 | 5.3547 | 6 | 8 | True | False |
| sun | vesta | 90 | kare | 3.2288 | 6 | 10 | False | True |
| sun | chiron | 180 | karşıtlık | 2.863 | 6 | 12 | True | False |
| sun | lilith (black moon) | 30 | yarı-sekstil | 5.7335 | 6 | 7 | True | False |
| sun | lilith (asteroid) | 135 | 135 | 2.2775 | 6 | 11 | False | True |
| sun | nn | 120 | üçgen | 4.5694 | 6 | 2 | False | True |
| sun | sn | 60 | sekstil | 4.5694 | 6 | 8 | False | True |
| sun | lilith (black moon) | 30 | yarı-sekstil | 5.7335 | 6 | 7 | True | False |
| moon | mercury | 0 | kavuşum | 4.1893 | 1 | 1 | True | False |
| moon | venus | 60 | sekstil | 0.1604 | 1 | 11 | False | True |
| moon | mars | 120 | üçgen | 3.7591 | 1 | 5 | False | True |
| moon | jupiter | 150 | quincunx | 0.2892 | 1 | 6 | False | True |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| moving:pluto | 0.4 | 0.0383 | 8.4101 |
| natal:mars | 0.4222 | 0.0381 | 37.5758 |
| moving:vesta | 0.3778 | 0.0321 | 16.0487 |
| natal:pallas | 0.4 | 0.0312 | 23.0011 |
| natal:saturn | 0.3778 | 0.031 | 10.7857 |
| natal:sn | 0.3778 | 0.0283 | 13.193 |
| moving:uranus | 0.3556 | 0.0282 | 11.6228 |
| natal:jupiter | 0.3556 | 0.0281 | 10.1739 |
| natal:nn | 0.3556 | 0.0251 | 14.4325 |
| moving:neptune | 0.3556 | 0.0249 | 5.3281 |
| natal:pluto | 0.3333 | 0.0244 | 6.6077 |
| moving:moon | 0.3556 | 0.0233 | 16.0954 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| moving:pluto | 18 | 0.4 | 0.0383 | 8.4101 |
| natal:mars | 19 | 0.4222 | 0.0381 | 37.5758 |
| moving:vesta | 17 | 0.3778 | 0.0321 | 16.0487 |
| natal:pallas | 18 | 0.4 | 0.0312 | 23.0011 |
| natal:saturn | 17 | 0.3778 | 0.031 | 10.7857 |
| natal:sn | 17 | 0.3778 | 0.0283 | 13.193 |
| moving:uranus | 16 | 0.3556 | 0.0282 | 11.6228 |
| natal:jupiter | 16 | 0.3556 | 0.0281 | 10.1739 |
| natal:nn | 16 | 0.3556 | 0.0251 | 14.4325 |
| moving:neptune | 16 | 0.3556 | 0.0249 | 5.3281 |

### Shared Nodes ve Validation

| natal_node | keywords_tr |
| --- | --- |
| asc | görünüm, başlatma ekseni |
| ceres | besleme, bakım, sürdürülebilirlik |
| chiron | kırılganlık, ustalık, onarım |
| dsc | karşı eksen, ilişki alanı |
| ic | temel, kök, iç yapı |
| juno | bağlılık, sözleşme, karşılıklılık |
| jupiter | genişleme, inanç, fırsat, büyüme |
| lilith (asteroid) | temsili lilith varyantı |
| lilith (black moon) | ham dürtü, dışlanan içerik |
| mars | dürtü, mücadele, uygulama, ayrışma |
| mc | kamusal yön, zirve, kariyer |
| mercury | zihin, yazışma, ticaret, analitik süreç |
| moon | duygusal ritim, ihtiyaç, alışkanlık |
| neptune | belirsizlik, ideal, çözünme, geçirgenlik |
| nn | yön, gelişim vektörü |
| pallas | örüntü zekâsı, strateji, tasarım |
| pluto | yoğunlaşma, güç, eliminasyon, dönüşüm |
| saturn | yapı, yükümlülük, sınır, kurumsallaşma |
| sn | geçmiş örüntü, boşalma hattı |
| sun | irade, amaç, merkez |

Progressed validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 30 | 45 | yarı-sekstil |
| 150 | 42 | quincunx |
| 45 | 42 | 45 |
| 60 | 42 | sekstil |
| 135 | 39 | 135 |
| 0 | 36 | kavuşum |
| 90 | 31 | kare |
| 120 | 28 | üçgen |
| 72 | 27 | 72 |
| 180 | 21 | karşıtlık |

Transit validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 30 | 44 | yarı-sekstil |
| 60 | 43 | sekstil |
| 150 | 42 | quincunx |
| 45 | 41 | 45 |
| 120 | 40 | üçgen |
| 90 | 34 | kare |
| 135 | 31 | 135 |
| 72 | 28 | 72 |
| 0 | 21 | kavuşum |
| 180 | 20 | karşıtlık |

### Teknik Tematik Özet

Bu fazın teknik matrisi karşılıklılık, görünür sonuç, dış geri bildirim eksenini öne çıkarıyor. En yoğun temas alanları: iş rutini, hizmet, sağlık rejimi, teknik bakım; ortaklıklar, kontratlar, açık muhataplar; yaratıcılık, aşk, sahne, üretken ifade. Aktif natal düğüm imzası: ham dürtü, dışlanan içerik; bağlılık, sözleşme, karşılıklılık; adanma, odak, kutsal görev; dürtü, mücadele, uygulama, ayrışma. Biyografik doğrulamada tekil olay aramak yerine, rol tanımı, iş-akış mimarisi, ilişki kontratları, kaynak yönetimi ve iç/dış yönelim dengesinde gözlenen yapısal yeniden dağılımlar izlenmeli.

## Dağılan 30° (210°)

### Faz Doğrulama

| target_angle_deg | event_utc | event_local | progressed_chart_utc | progressed_sun_lon | progressed_moon_lon | moon_minus_sun_deg | exact_delta_deg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 210 | 2014-08-17T22:43:08.150422Z | 2014-08-18T01:43:08.150422+03:00 | 1982-06-09T10:20:19.529501Z | 78.257223 | 288.257223 | 210.0 | -0.0 |

### A. Progressed-to-Natal

Aktif pattern graph: 46 düğüm, 346 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | sun | 30 | yarı-sekstil | 1.027 | 1 | 12 | True | False |
| sun | moon | 150 | quincunx | 0.3315 | 1 | 6 | False | True |
| sun | venus | 72 | 72 | 2.1952 | 1 | 11 | True | False |
| sun | jupiter | 135 | 135 | 0.676 | 1 | 6 | True | False |
| sun | saturn | 120 | üçgen | 1.4206 | 1 | 5 | False | True |
| sun | ceres | 150 | quincunx | 1.7929 | 1 | 6 | True | False |
| sun | vesta | 120 | üçgen | 2.0504 | 1 | 10 | False | True |
| sun | chiron | 30 | yarı-sekstil | 4.0414 | 1 | 12 | True | False |
| sun | lilith (black moon) | 180 | karşıtlık | 6.9119 | 1 | 7 | True | False |
| sun | lilith (asteroid) | 72 | 72 | 4.0991 | 1 | 11 | False | True |
| sun | nn | 30 | yarı-sekstil | 3.391 | 1 | 2 | False | True |
| sun | sn | 150 | quincunx | 3.391 | 1 | 8 | False | True |
| sun | lilith (black moon) | 180 | karşıtlık | 6.9119 | 1 | 7 | True | False |
| moon | sun | 120 | üçgen | 1.027 | 9 | 12 | False | True |
| moon | moon | 60 | sekstil | 0.3315 | 9 | 6 | False | True |
| moon | mercury | 135 | 135 | 5.1545 | 9 | 1 | True | False |
| moon | venus | 72 | 72 | 3.8048 | 9 | 11 | True | False |
| moon | jupiter | 72 | 72 | 2.324 | 9 | 6 | False | True |
| moon | saturn | 90 | kare | 1.4206 | 9 | 5 | False | True |
| moon | uranus | 45 | 45 | 0.017 | 9 | 6 | True | False |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| moving:juno | 0.4 | 0.035 | 8.4887 |
| natal:moon | 0.3778 | 0.034 | 24.0081 |
| natal:ic | 0.3778 | 0.033 | 29.0624 |
| moving:ceres | 0.3778 | 0.0328 | 6.8121 |
| moving:lilith (black moon) | 0.3778 | 0.0323 | 29.9034 |
| natal:vesta | 0.3778 | 0.0316 | 11.6192 |
| natal:ceres | 0.3556 | 0.0305 | 16.788 |
| moving:mars | 0.3778 | 0.0297 | 18.7188 |
| natal:mc | 0.3556 | 0.0294 | 28.6202 |
| moving:pallas | 0.3556 | 0.0259 | 39.7136 |
| moving:dsc | 0.3333 | 0.0255 | 35.4764 |
| moving:uranus | 0.3333 | 0.0249 | 19.0123 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| moving:juno | 18 | 0.4 | 0.035 | 8.4887 |
| natal:moon | 17 | 0.3778 | 0.034 | 24.0081 |
| natal:ic | 17 | 0.3778 | 0.033 | 29.0624 |
| moving:ceres | 17 | 0.3778 | 0.0328 | 6.8121 |
| moving:lilith (black moon) | 17 | 0.3778 | 0.0323 | 29.9034 |
| natal:vesta | 17 | 0.3778 | 0.0316 | 11.6192 |
| natal:ceres | 16 | 0.3556 | 0.0305 | 16.788 |
| moving:mars | 17 | 0.3778 | 0.0297 | 18.7188 |
| natal:mc | 16 | 0.3556 | 0.0294 | 28.6202 |
| moving:pallas | 16 | 0.3556 | 0.0259 | 39.7136 |

### B. Transit-to-Natal

Aktif pattern graph: 46 düğüm, 366 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | mercury | 72 | 72 | 4.5315 | 4 | 1 | True | False |
| sun | venus | 135 | 135 | 5.8812 | 4 | 11 | True | False |
| sun | mars | 30 | yarı-sekstil | 5.5201 | 4 | 5 | True | False |
| sun | jupiter | 72 | 72 | 3.01 | 4 | 6 | False | True |
| sun | neptune | 120 | üçgen | 1.6991 | 4 | 7 | True | False |
| sun | pluto | 60 | sekstil | 0.0032 | 4 | 6 | False | True |
| sun | ceres | 90 | kare | 4.8931 | 4 | 6 | False | True |
| sun | juno | 135 | 135 | 0.1529 | 4 | 8 | False | True |
| sun | chiron | 90 | kare | 2.6446 | 4 | 12 | False | True |
| sun | lilith (black moon) | 120 | üçgen | 0.2259 | 4 | 7 | True | False |
| sun | nn | 45 | 45 | 4.923 | 4 | 2 | True | False |
| sun | sn | 135 | 135 | 4.923 | 4 | 8 | True | False |
| sun | lilith (black moon) | 120 | üçgen | 0.2259 | 4 | 7 | True | False |
| moon | venus | 60 | sekstil | 4.0434 | 12 | 11 | True | False |
| moon | mars | 120 | üçgen | 0.4447 | 12 | 5 | True | False |
| moon | jupiter | 150 | quincunx | 3.9146 | 12 | 6 | True | False |
| moon | saturn | 135 | 135 | 1.818 | 12 | 5 | True | False |
| moon | uranus | 180 | karşıtlık | 3.2556 | 12 | 6 | True | False |
| moon | neptune | 150 | quincunx | 3.3762 | 12 | 7 | False | True |
| moon | pluto | 150 | quincunx | 5.0786 | 12 | 6 | False | True |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| moving:mercury | 0.4 | 0.031 | 15.8168 |
| natal:jupiter | 0.4 | 0.0302 | 13.0034 |
| natal:asc | 0.4 | 0.0297 | 62.9398 |
| moving:mars | 0.3556 | 0.0278 | 5.5588 |
| moving:moon | 0.3778 | 0.0276 | 18.8489 |
| natal:saturn | 0.3778 | 0.0275 | 11.2716 |
| moving:juno | 0.3778 | 0.0263 | 13.1094 |
| natal:dsc | 0.3778 | 0.025 | 62.6675 |
| natal:uranus | 0.3778 | 0.025 | 18.4305 |
| moving:lilith (black moon) | 0.3556 | 0.0242 | 75.5221 |
| natal:mercury | 0.3556 | 0.0234 | 7.4962 |
| moving:mc | 0.3778 | 0.0232 | 9.9195 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| moving:mercury | 18 | 0.4 | 0.031 | 15.8168 |
| natal:jupiter | 18 | 0.4 | 0.0302 | 13.0034 |
| natal:asc | 18 | 0.4 | 0.0297 | 62.9398 |
| moving:mars | 16 | 0.3556 | 0.0278 | 5.5588 |
| moving:moon | 17 | 0.3778 | 0.0276 | 18.8489 |
| natal:saturn | 17 | 0.3778 | 0.0275 | 11.2716 |
| moving:juno | 17 | 0.3778 | 0.0263 | 13.1094 |
| natal:dsc | 17 | 0.3778 | 0.025 | 62.6675 |
| natal:uranus | 17 | 0.3778 | 0.025 | 18.4305 |
| moving:lilith (black moon) | 16 | 0.3556 | 0.0242 | 75.5221 |

### Shared Nodes ve Validation

| natal_node | keywords_tr |
| --- | --- |
| asc | görünüm, başlatma ekseni |
| ceres | besleme, bakım, sürdürülebilirlik |
| chiron | kırılganlık, ustalık, onarım |
| dsc | karşı eksen, ilişki alanı |
| ic | temel, kök, iç yapı |
| juno | bağlılık, sözleşme, karşılıklılık |
| jupiter | genişleme, inanç, fırsat, büyüme |
| lilith (asteroid) | temsili lilith varyantı |
| lilith (black moon) | ham dürtü, dışlanan içerik |
| mars | dürtü, mücadele, uygulama, ayrışma |
| mc | kamusal yön, zirve, kariyer |
| mercury | zihin, yazışma, ticaret, analitik süreç |
| moon | duygusal ritim, ihtiyaç, alışkanlık |
| neptune | belirsizlik, ideal, çözünme, geçirgenlik |
| nn | yön, gelişim vektörü |
| pallas | örüntü zekâsı, strateji, tasarım |
| pluto | yoğunlaşma, güç, eliminasyon, dönüşüm |
| saturn | yapı, yükümlülük, sınır, kurumsallaşma |
| sn | geçmiş örüntü, boşalma hattı |
| sun | irade, amaç, merkez |

Progressed validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 135 | 42 | 135 |
| 45 | 41 | 45 |
| 0 | 39 | kavuşum |
| 60 | 37 | sekstil |
| 90 | 37 | kare |
| 30 | 36 | yarı-sekstil |
| 150 | 32 | quincunx |
| 72 | 31 | 72 |
| 180 | 26 | karşıtlık |
| 120 | 25 | üçgen |

Transit validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 90 | 51 | kare |
| 72 | 44 | 72 |
| 150 | 44 | quincunx |
| 135 | 43 | 135 |
| 30 | 40 | yarı-sekstil |
| 45 | 37 | 45 |
| 120 | 35 | üçgen |
| 60 | 34 | sekstil |
| 180 | 19 | karşıtlık |
| 0 | 19 | kavuşum |

### Teknik Tematik Özet

Bu fazın teknik matrisi dağıtım, paylaşım ve sonuçları ağlara yayma eksenini öne çıkarıyor. En yoğun temas alanları: iş rutini, hizmet, sağlık rejimi, teknik bakım; ortaklıklar, kontratlar, açık muhataplar; yaratıcılık, aşk, sahne, üretken ifade. Aktif natal düğüm imzası: ham dürtü, dışlanan içerik; duygusal ritim, ihtiyaç, alışkanlık; adanma, odak, kutsal görev; genişleme, inanç, fırsat, büyüme. Biyografik doğrulamada tekil olay aramak yerine, rol tanımı, iş-akış mimarisi, ilişki kontratları, kaynak yönetimi ve iç/dış yönelim dengesinde gözlenen yapısal yeniden dağılımlar izlenmeli.

## Dağılan Üçgen (240°)

### Faz Doğrulama

| target_angle_deg | event_utc | event_local | progressed_chart_utc | progressed_sun_lon | progressed_moon_lon | moon_minus_sun_deg | exact_delta_deg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 240 | 2017-05-10T16:05:30.413728Z | 2017-05-10T19:05:30.413728+03:00 | 1982-06-12T03:49:54.867662Z | 80.865373 | 320.865373 | 240.0 | -3e-09 |

### A. Progressed-to-Natal

Aktif pattern graph: 46 düğüm, 350 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | sun | 30 | yarı-sekstil | 3.6352 | 1 | 12 | True | False |
| sun | moon | 150 | quincunx | 2.2766 | 1 | 6 | True | False |
| sun | venus | 72 | 72 | 4.8034 | 1 | 11 | True | False |
| sun | jupiter | 135 | 135 | 1.9321 | 1 | 6 | False | True |
| sun | saturn | 120 | üçgen | 4.0288 | 1 | 5 | False | True |
| sun | neptune | 180 | karşıtlık | 5.777 | 1 | 7 | True | False |
| sun | pluto | 120 | üçgen | 4.0746 | 1 | 6 | True | False |
| sun | ceres | 150 | quincunx | 0.8153 | 1 | 6 | False | True |
| sun | vesta | 120 | üçgen | 4.6586 | 1 | 10 | False | True |
| sun | chiron | 30 | yarı-sekstil | 1.4332 | 1 | 12 | True | False |
| sun | lilith (black moon) | 180 | karşıtlık | 4.3037 | 1 | 7 | True | False |
| sun | mc | 135 | 135 | 3.5144 | 1 | 10 | True | False |
| sun | ic | 45 | 45 | 3.5144 | 1 | 4 | True | False |
| sun | nn | 30 | yarı-sekstil | 5.9992 | 1 | 2 | False | True |
| sun | sn | 150 | quincunx | 5.9992 | 1 | 8 | False | True |
| sun | lilith (black moon) | 180 | karşıtlık | 4.3037 | 1 | 7 | True | False |
| moon | sun | 90 | kare | 3.6352 | 10 | 12 | False | True |
| moon | moon | 90 | kare | 2.2766 | 10 | 6 | True | False |
| moon | venus | 45 | 45 | 1.8034 | 10 | 11 | False | True |
| moon | mars | 135 | 135 | 5.4021 | 10 | 5 | False | True |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| natal:ceres | 0.4 | 0.0369 | 26.3476 |
| moving:moon | 0.4 | 0.0351 | 6.2839 |
| moving:lilith (black moon) | 0.4 | 0.0345 | 19.1729 |
| natal:juno | 0.3778 | 0.0339 | 18.7334 |
| moving:juno | 0.4 | 0.0333 | 25.9938 |
| moving:venus | 0.3778 | 0.0301 | 8.4188 |
| moving:ceres | 0.3778 | 0.0301 | 6.1737 |
| natal:vesta | 0.3778 | 0.0295 | 7.8132 |
| moving:pallas | 0.3778 | 0.0286 | 35.9925 |
| moving:mars | 0.3778 | 0.0286 | 7.2537 |
| natal:moon | 0.3778 | 0.0282 | 12.3002 |
| natal:ic | 0.3556 | 0.0281 | 7.0128 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| natal:ceres | 18 | 0.4 | 0.0369 | 26.3476 |
| moving:moon | 18 | 0.4 | 0.0351 | 6.2839 |
| moving:lilith (black moon) | 18 | 0.4 | 0.0345 | 19.1729 |
| natal:juno | 17 | 0.3778 | 0.0339 | 18.7334 |
| moving:juno | 18 | 0.4 | 0.0333 | 25.9938 |
| moving:ceres | 17 | 0.3778 | 0.0301 | 6.1737 |
| moving:venus | 17 | 0.3778 | 0.0301 | 8.4188 |
| natal:vesta | 17 | 0.3778 | 0.0295 | 7.8132 |
| moving:mars | 17 | 0.3778 | 0.0286 | 7.2537 |
| moving:pallas | 17 | 0.3778 | 0.0286 | 35.9925 |

### B. Transit-to-Natal

Aktif pattern graph: 46 düğüm, 359 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | sun | 0 | kavuşum | 2.9516 | 12 | 12 | True | False |
| sun | moon | 180 | karşıtlık | 1.593 | 12 | 6 | True | False |
| sun | venus | 45 | 45 | 1.1198 | 12 | 11 | True | False |
| sun | mars | 135 | 135 | 4.7185 | 12 | 5 | False | True |
| sun | saturn | 150 | quincunx | 3.3452 | 12 | 5 | False | True |
| sun | pluto | 150 | quincunx | 4.7582 | 12 | 6 | True | False |
| sun | ceres | 180 | karşıtlık | 0.1317 | 12 | 6 | False | True |
| sun | pallas | 135 | 135 | 1.9902 | 12 | 5 | False | True |
| sun | juno | 135 | 135 | 4.6085 | 12 | 8 | True | False |
| sun | vesta | 90 | kare | 3.975 | 12 | 10 | False | True |
| sun | chiron | 0 | kavuşum | 2.1168 | 12 | 12 | True | False |
| sun | lilith (black moon) | 150 | quincunx | 4.9873 | 12 | 7 | True | False |
| sun | lilith (asteroid) | 45 | 45 | 3.0236 | 12 | 11 | False | True |
| sun | nn | 60 | sekstil | 5.3156 | 12 | 2 | False | True |
| sun | sn | 120 | üçgen | 5.3156 | 12 | 8 | False | True |
| sun | lilith (black moon) | 150 | quincunx | 4.9873 | 12 | 7 | True | False |
| moon | sun | 180 | karşıtlık | 0.3757 | 6 | 12 | False | True |
| moon | moon | 0 | kavuşum | 0.9829 | 6 | 6 | False | True |
| moon | venus | 135 | 135 | 1.4561 | 6 | 11 | True | False |
| moon | mars | 45 | 45 | 2.1426 | 6 | 5 | False | True |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| natal:vesta | 0.4222 | 0.0381 | 6.9544 |
| moving:chiron | 0.4222 | 0.0366 | 6.9973 |
| natal:sun | 0.4 | 0.0302 | 8.3905 |
| natal:sn | 0.4 | 0.029 | 39.1153 |
| moving:venus | 0.3778 | 0.029 | 8.8275 |
| natal:mars | 0.3556 | 0.0271 | 7.3035 |
| moving:pluto | 0.3778 | 0.0268 | 10.3213 |
| natal:nn | 0.3778 | 0.0262 | 37.9878 |
| moving:mc | 0.3778 | 0.026 | 28.257 |
| moving:lilith (asteroid) | 0.3556 | 0.0247 | 7.6683 |
| natal:mc | 0.3333 | 0.0239 | 15.0536 |
| moving:sn | 0.3556 | 0.0237 | 33.1231 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| natal:vesta | 19 | 0.4222 | 0.0381 | 6.9544 |
| moving:chiron | 19 | 0.4222 | 0.0366 | 6.9973 |
| natal:sun | 18 | 0.4 | 0.0302 | 8.3905 |
| natal:sn | 18 | 0.4 | 0.029 | 39.1153 |
| moving:venus | 17 | 0.3778 | 0.029 | 8.8275 |
| natal:mars | 16 | 0.3556 | 0.0271 | 7.3035 |
| moving:pluto | 17 | 0.3778 | 0.0268 | 10.3213 |
| natal:nn | 17 | 0.3778 | 0.0262 | 37.9878 |
| moving:mc | 17 | 0.3778 | 0.026 | 28.257 |
| moving:lilith (asteroid) | 16 | 0.3556 | 0.0247 | 7.6683 |

### Shared Nodes ve Validation

| natal_node | keywords_tr |
| --- | --- |
| asc | görünüm, başlatma ekseni |
| ceres | besleme, bakım, sürdürülebilirlik |
| chiron | kırılganlık, ustalık, onarım |
| dsc | karşı eksen, ilişki alanı |
| ic | temel, kök, iç yapı |
| juno | bağlılık, sözleşme, karşılıklılık |
| jupiter | genişleme, inanç, fırsat, büyüme |
| lilith (asteroid) | temsili lilith varyantı |
| lilith (black moon) | ham dürtü, dışlanan içerik |
| mars | dürtü, mücadele, uygulama, ayrışma |
| mc | kamusal yön, zirve, kariyer |
| mercury | zihin, yazışma, ticaret, analitik süreç |
| moon | duygusal ritim, ihtiyaç, alışkanlık |
| neptune | belirsizlik, ideal, çözünme, geçirgenlik |
| nn | yön, gelişim vektörü |
| pallas | örüntü zekâsı, strateji, tasarım |
| pluto | yoğunlaşma, güç, eliminasyon, dönüşüm |
| saturn | yapı, yükümlülük, sınır, kurumsallaşma |
| sn | geçmiş örüntü, boşalma hattı |
| sun | irade, amaç, merkez |

Progressed validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 45 | 46 | 45 |
| 135 | 41 | 135 |
| 60 | 41 | sekstil |
| 30 | 37 | yarı-sekstil |
| 0 | 36 | kavuşum |
| 90 | 35 | kare |
| 150 | 34 | quincunx |
| 120 | 29 | üçgen |
| 72 | 27 | 72 |
| 180 | 24 | karşıtlık |

Transit validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 120 | 49 | üçgen |
| 90 | 41 | kare |
| 45 | 40 | 45 |
| 135 | 40 | 135 |
| 60 | 39 | sekstil |
| 72 | 37 | 72 |
| 150 | 32 | quincunx |
| 30 | 29 | yarı-sekstil |
| 180 | 27 | karşıtlık |
| 0 | 25 | kavuşum |

### Teknik Tematik Özet

Bu fazın teknik matrisi edinilmiş beceriyi üretken biçimde boşaltma eksenini öne çıkarıyor. En yoğun temas alanları: iş rutini, hizmet, sağlık rejimi, teknik bakım; ortaklıklar, kontratlar, açık muhataplar; yaratıcılık, aşk, sahne, üretken ifade. Aktif natal düğüm imzası: ham dürtü, dışlanan içerik; besleme, bakım, sürdürülebilirlik; duygusal ritim, ihtiyaç, alışkanlık; adanma, odak, kutsal görev. Biyografik doğrulamada tekil olay aramak yerine, rol tanımı, iş-akış mimarisi, ilişki kontratları, kaynak yönetimi ve iç/dış yönelim dengesinde gözlenen yapısal yeniden dağılımlar izlenmeli.

## Son Kare (270°)

### Faz Doğrulama

| target_angle_deg | event_utc | event_local | progressed_chart_utc | progressed_sun_lon | progressed_moon_lon | moon_minus_sun_deg | exact_delta_deg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 270 | 2019-12-14T06:58:19.184864Z | 2019-12-14T09:58:19.184864+03:00 | 1982-06-14T18:05:54.672648Z | 83.34401 | 353.34401 | 270.0 | -4e-09 |

### A. Progressed-to-Natal

Aktif pattern graph: 46 düğüm, 367 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | moon | 150 | quincunx | 4.7552 | 1 | 6 | True | False |
| sun | jupiter | 135 | 135 | 4.4108 | 1 | 6 | False | True |
| sun | neptune | 180 | karşıtlık | 3.2983 | 1 | 7 | True | False |
| sun | pluto | 120 | üçgen | 1.596 | 1 | 6 | True | False |
| sun | ceres | 150 | quincunx | 3.2939 | 1 | 6 | False | True |
| sun | chiron | 30 | yarı-sekstil | 1.0454 | 1 | 12 | False | True |
| sun | lilith (black moon) | 180 | karşıtlık | 1.8251 | 1 | 7 | True | False |
| sun | mc | 135 | 135 | 1.0358 | 1 | 10 | True | False |
| sun | ic | 45 | 45 | 1.0358 | 1 | 4 | True | False |
| sun | lilith (black moon) | 180 | karşıtlık | 1.8251 | 1 | 7 | True | False |
| moon | moon | 120 | üçgen | 4.7552 | 11 | 6 | False | True |
| moon | mercury | 72 | 72 | 3.0677 | 11 | 1 | True | False |
| moon | mars | 180 | karşıtlık | 7.1193 | 11 | 5 | True | False |
| moon | jupiter | 135 | 135 | 4.4108 | 11 | 6 | False | True |
| moon | neptune | 90 | kare | 3.2983 | 11 | 7 | True | False |
| moon | pluto | 150 | quincunx | 1.596 | 11 | 6 | True | False |
| moon | ceres | 120 | üçgen | 3.2939 | 11 | 6 | False | True |
| moon | juno | 72 | 72 | 1.5537 | 11 | 8 | False | True |
| moon | chiron | 60 | sekstil | 1.0454 | 11 | 12 | False | True |
| moon | lilith (black moon) | 90 | kare | 1.8251 | 11 | 7 | True | False |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| moving:juno | 0.4444 | 0.0358 | 13.1737 |
| moving:asc | 0.4222 | 0.0317 | 23.1652 |
| moving:lilith (black moon) | 0.4 | 0.0297 | 14.7795 |
| natal:neptune | 0.3778 | 0.0297 | 8.6526 |
| moving:ceres | 0.3778 | 0.029 | 5.8849 |
| natal:moon | 0.3778 | 0.0276 | 22.5597 |
| natal:asc | 0.3778 | 0.0248 | 14.5674 |
| natal:ceres | 0.3556 | 0.0247 | 8.0346 |
| moving:pallas | 0.3778 | 0.0244 | 17.2323 |
| moving:mars | 0.3778 | 0.0244 | 6.8175 |
| moving:dsc | 0.3778 | 0.024 | 22.6724 |
| natal:juno | 0.3556 | 0.0236 | 24.9123 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| moving:juno | 20 | 0.4444 | 0.0358 | 13.1737 |
| moving:asc | 19 | 0.4222 | 0.0317 | 23.1652 |
| moving:lilith (black moon) | 18 | 0.4 | 0.0297 | 14.7795 |
| natal:neptune | 17 | 0.3778 | 0.0297 | 8.6526 |
| moving:ceres | 17 | 0.3778 | 0.029 | 5.8849 |
| natal:moon | 17 | 0.3778 | 0.0276 | 22.5597 |
| natal:asc | 17 | 0.3778 | 0.0248 | 14.5674 |
| natal:ceres | 16 | 0.3556 | 0.0247 | 8.0346 |
| moving:mars | 17 | 0.3778 | 0.0244 | 6.8175 |
| moving:pallas | 17 | 0.3778 | 0.0244 | 17.2323 |

### B. Transit-to-Natal

Aktif pattern graph: 46 düğüm, 356 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | sun | 150 | quincunx | 4.7401 | 7 | 12 | False | True |
| sun | moon | 30 | yarı-sekstil | 3.3815 | 7 | 6 | True | False |
| sun | jupiter | 45 | 45 | 3.0371 | 7 | 6 | False | True |
| sun | saturn | 60 | sekstil | 5.1337 | 7 | 5 | False | True |
| sun | neptune | 0 | kavuşum | 4.6721 | 7 | 7 | True | False |
| sun | pluto | 60 | sekstil | 2.9697 | 7 | 6 | True | False |
| sun | ceres | 30 | yarı-sekstil | 1.9202 | 7 | 6 | False | True |
| sun | vesta | 60 | sekstil | 5.7635 | 7 | 10 | False | True |
| sun | chiron | 150 | quincunx | 0.3283 | 7 | 12 | True | False |
| sun | lilith (black moon) | 0 | kavuşum | 3.1988 | 7 | 7 | True | False |
| sun | mc | 45 | 45 | 2.4095 | 7 | 10 | True | False |
| sun | ic | 135 | 135 | 2.4095 | 7 | 4 | True | False |
| sun | lilith (black moon) | 0 | kavuşum | 3.1988 | 7 | 7 | True | False |
| moon | sun | 60 | sekstil | 0.6926 | 3 | 12 | False | True |
| moon | moon | 120 | üçgen | 0.6659 | 3 | 6 | True | False |
| moon | mercury | 45 | 45 | 5.4889 | 3 | 1 | True | False |
| moon | mars | 72 | 72 | 0.5405 | 3 | 5 | True | False |
| moon | saturn | 90 | kare | 1.0862 | 3 | 5 | False | True |
| moon | uranus | 135 | 135 | 0.3514 | 3 | 6 | True | False |
| moon | ceres | 120 | üçgen | 2.1273 | 3 | 6 | True | False |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| moving:jupiter | 0.4222 | 0.0373 | 16.0475 |
| natal:vesta | 0.4222 | 0.0355 | 28.3687 |
| natal:sn | 0.4222 | 0.0337 | 9.6623 |
| natal:nn | 0.4 | 0.0306 | 16.6771 |
| natal:mercury | 0.4 | 0.0303 | 67.7043 |
| natal:saturn | 0.4 | 0.0303 | 11.3349 |
| moving:pluto | 0.4 | 0.0303 | 11.2425 |
| natal:moon | 0.4 | 0.0289 | 8.0379 |
| natal:ceres | 0.3778 | 0.0271 | 6.6337 |
| moving:saturn | 0.3778 | 0.026 | 10.2015 |
| moving:vesta | 0.3556 | 0.0258 | 5.5438 |
| moving:sn | 0.3556 | 0.0256 | 36.6757 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| moving:jupiter | 19 | 0.4222 | 0.0373 | 16.0475 |
| natal:vesta | 19 | 0.4222 | 0.0355 | 28.3687 |
| natal:sn | 19 | 0.4222 | 0.0337 | 9.6623 |
| natal:nn | 18 | 0.4 | 0.0306 | 16.6771 |
| moving:pluto | 18 | 0.4 | 0.0303 | 11.2425 |
| natal:mercury | 18 | 0.4 | 0.0303 | 67.7043 |
| natal:saturn | 18 | 0.4 | 0.0303 | 11.3349 |
| natal:moon | 18 | 0.4 | 0.0289 | 8.0379 |
| natal:ceres | 17 | 0.3778 | 0.0271 | 6.6337 |
| moving:saturn | 17 | 0.3778 | 0.026 | 10.2015 |

### Shared Nodes ve Validation

| natal_node | keywords_tr |
| --- | --- |
| asc | görünüm, başlatma ekseni |
| ceres | besleme, bakım, sürdürülebilirlik |
| chiron | kırılganlık, ustalık, onarım |
| dsc | karşı eksen, ilişki alanı |
| ic | temel, kök, iç yapı |
| juno | bağlılık, sözleşme, karşılıklılık |
| jupiter | genişleme, inanç, fırsat, büyüme |
| lilith (asteroid) | temsili lilith varyantı |
| lilith (black moon) | ham dürtü, dışlanan içerik |
| mars | dürtü, mücadele, uygulama, ayrışma |
| mc | kamusal yön, zirve, kariyer |
| mercury | zihin, yazışma, ticaret, analitik süreç |
| moon | duygusal ritim, ihtiyaç, alışkanlık |
| neptune | belirsizlik, ideal, çözünme, geçirgenlik |
| nn | yön, gelişim vektörü |
| pallas | örüntü zekâsı, strateji, tasarım |
| pluto | yoğunlaşma, güç, eliminasyon, dönüşüm |
| saturn | yapı, yükümlülük, sınır, kurumsallaşma |
| sn | geçmiş örüntü, boşalma hattı |
| sun | irade, amaç, merkez |

Progressed validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 45 | 48 | 45 |
| 135 | 43 | 135 |
| 90 | 40 | kare |
| 0 | 40 | kavuşum |
| 150 | 39 | quincunx |
| 30 | 39 | yarı-sekstil |
| 60 | 37 | sekstil |
| 72 | 29 | 72 |
| 180 | 28 | karşıtlık |
| 120 | 24 | üçgen |

Transit validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 72 | 42 | 72 |
| 45 | 41 | 45 |
| 30 | 40 | yarı-sekstil |
| 90 | 38 | kare |
| 135 | 37 | 135 |
| 60 | 34 | sekstil |
| 0 | 34 | kavuşum |
| 120 | 34 | üçgen |
| 150 | 28 | quincunx |
| 180 | 28 | karşıtlık |

### Teknik Tematik Özet

Bu fazın teknik matrisi yeniden yapılandırma, eleme ve kapanış baskısı eksenini öne çıkarıyor. En yoğun temas alanları: iş rutini, hizmet, sağlık rejimi, teknik bakım; ortaklıklar, kontratlar, açık muhataplar; yaratıcılık, aşk, sahne, üretken ifade. Aktif natal düğüm imzası: ham dürtü, dışlanan içerik; duygusal ritim, ihtiyaç, alışkanlık; belirsizlik, ideal, çözünme, geçirgenlik; geçmiş örüntü, boşalma hattı. Biyografik doğrulamada tekil olay aramak yerine, rol tanımı, iş-akış mimarisi, ilişki kontratları, kaynak yönetimi ve iç/dış yönelim dengesinde gözlenen yapısal yeniden dağılımlar izlenmeli.

## Dağılan Sekstil (300°)

### Faz Doğrulama

| target_angle_deg | event_utc | event_local | progressed_chart_utc | progressed_sun_lon | progressed_moon_lon | moon_minus_sun_deg | exact_delta_deg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 300 | 2022-05-08T09:09:32.078780Z | 2022-05-08T12:09:32.078780+03:00 | 1982-06-17T03:39:54.297272Z | 85.634916 | 25.634916 | 300.0 | -3e-09 |

### A. Progressed-to-Natal

Aktif pattern graph: 46 düğüm, 355 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | mars | 90 | kare | 4.8284 | 1 | 5 | True | False |
| sun | neptune | 180 | karşıtlık | 1.0074 | 1 | 7 | True | False |
| sun | pluto | 120 | üçgen | 0.6949 | 1 | 6 | False | True |
| sun | ceres | 150 | quincunx | 5.5848 | 1 | 6 | False | True |
| sun | vesta | 135 | 135 | 5.5719 | 1 | 10 | True | False |
| sun | chiron | 30 | yarı-sekstil | 3.3363 | 1 | 12 | False | True |
| sun | lilith (black moon) | 180 | karşıtlık | 0.4658 | 1 | 7 | False | True |
| sun | mc | 135 | 135 | 1.2551 | 1 | 10 | False | True |
| sun | ic | 45 | 45 | 1.2551 | 1 | 4 | False | True |
| sun | lilith (black moon) | 180 | karşıtlık | 0.4658 | 1 | 7 | False | True |
| moon | mercury | 45 | 45 | 2.2232 | 12 | 1 | False | True |
| moon | mars | 150 | quincunx | 4.8284 | 12 | 5 | True | False |
| moon | neptune | 120 | üçgen | 1.0074 | 12 | 7 | True | False |
| moon | pluto | 180 | karşıtlık | 0.6949 | 12 | 6 | False | True |
| moon | ceres | 150 | quincunx | 5.5848 | 12 | 6 | False | True |
| moon | vesta | 72 | 72 | 2.5719 | 12 | 10 | True | False |
| moon | chiron | 30 | yarı-sekstil | 3.3363 | 12 | 12 | False | True |
| moon | lilith (black moon) | 120 | üçgen | 0.4658 | 12 | 7 | False | True |
| moon | mc | 72 | 72 | 4.2551 | 12 | 10 | False | True |
| moon | lilith (black moon) | 120 | üçgen | 0.4658 | 12 | 7 | False | True |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| moving:juno | 0.4444 | 0.043 | 39.7513 |
| moving:lilith (black moon) | 0.4 | 0.0347 | 14.3559 |
| natal:mc | 0.3778 | 0.032 | 6.3368 |
| moving:ceres | 0.3778 | 0.0314 | 5.7601 |
| natal:vesta | 0.3778 | 0.0312 | 6.9503 |
| moving:mars | 0.3778 | 0.031 | 10.817 |
| natal:ic | 0.3778 | 0.0307 | 6.2324 |
| moving:pallas | 0.3778 | 0.0304 | 11.9643 |
| natal:juno | 0.3556 | 0.0278 | 11.2009 |
| moving:mc | 0.3778 | 0.0275 | 8.2736 |
| natal:ceres | 0.3556 | 0.0264 | 20.2063 |
| natal:pluto | 0.3333 | 0.0263 | 24.5055 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| moving:juno | 20 | 0.4444 | 0.043 | 39.7513 |
| moving:lilith (black moon) | 18 | 0.4 | 0.0347 | 14.3559 |
| natal:mc | 17 | 0.3778 | 0.032 | 6.3368 |
| moving:ceres | 17 | 0.3778 | 0.0314 | 5.7601 |
| natal:vesta | 17 | 0.3778 | 0.0312 | 6.9503 |
| moving:mars | 17 | 0.3778 | 0.031 | 10.817 |
| natal:ic | 17 | 0.3778 | 0.0307 | 6.2324 |
| moving:pallas | 17 | 0.3778 | 0.0304 | 11.9643 |
| natal:juno | 16 | 0.3556 | 0.0278 | 11.2009 |
| moving:mc | 17 | 0.3778 | 0.0275 | 8.2736 |

### B. Transit-to-Natal

Aktif pattern graph: 46 düğüm, 363 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | sun | 0 | kavuşum | 0.5429 | 12 | 12 | False | True |
| sun | moon | 180 | karşıtlık | 0.8157 | 12 | 6 | False | True |
| sun | venus | 45 | 45 | 1.2889 | 12 | 11 | False | True |
| sun | mars | 135 | 135 | 2.3098 | 12 | 5 | False | True |
| sun | saturn | 150 | quincunx | 0.9365 | 12 | 5 | False | True |
| sun | ceres | 180 | karşıtlık | 2.277 | 12 | 6 | True | False |
| sun | pallas | 135 | 135 | 0.4185 | 12 | 5 | True | False |
| sun | vesta | 90 | kare | 1.5663 | 12 | 10 | False | True |
| sun | chiron | 0 | kavuşum | 4.5255 | 12 | 12 | True | False |
| sun | lilith (asteroid) | 45 | 45 | 0.6149 | 12 | 11 | False | True |
| sun | nn | 60 | sekstil | 2.9069 | 12 | 2 | False | True |
| sun | sn | 120 | üçgen | 2.9069 | 12 | 8 | False | True |
| moon | mercury | 60 | sekstil | 2.269 | 4 | 1 | False | True |
| moon | mars | 45 | 45 | 4.7826 | 4 | 5 | True | False |
| moon | saturn | 72 | 72 | 5.8441 | 4 | 5 | False | True |
| moon | neptune | 135 | 135 | 0.9617 | 4 | 7 | True | False |
| moon | pluto | 72 | 72 | 2.2593 | 4 | 6 | True | False |
| moon | juno | 150 | quincunx | 0.8904 | 4 | 8 | False | True |
| moon | vesta | 180 | karşıtlık | 5.5261 | 4 | 10 | True | False |
| moon | lilith (black moon) | 135 | 135 | 0.5116 | 4 | 7 | False | True |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| moving:jupiter | 0.4222 | 0.0348 | 6.3733 |
| moving:asc | 0.4222 | 0.0345 | 29.1104 |
| natal:venus | 0.4 | 0.0322 | 10.1036 |
| moving:juno | 0.4 | 0.0313 | 8.224 |
| natal:lilith (asteroid) | 0.4 | 0.0296 | 23.6591 |
| moving:dsc | 0.3778 | 0.0282 | 28.9911 |
| moving:lilith (black moon) | 0.3778 | 0.0279 | 31.0766 |
| natal:juno | 0.3556 | 0.0273 | 18.3261 |
| moving:venus | 0.3778 | 0.0266 | 6.6583 |
| moving:uranus | 0.3778 | 0.0263 | 23.8162 |
| natal:ceres | 0.3556 | 0.0258 | 5.4083 |
| natal:mars | 0.3556 | 0.0257 | 8.2407 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| moving:jupiter | 19 | 0.4222 | 0.0348 | 6.3733 |
| moving:asc | 19 | 0.4222 | 0.0345 | 29.1104 |
| natal:venus | 18 | 0.4 | 0.0322 | 10.1036 |
| moving:juno | 18 | 0.4 | 0.0313 | 8.224 |
| natal:lilith (asteroid) | 18 | 0.4 | 0.0296 | 23.6591 |
| moving:dsc | 17 | 0.3778 | 0.0282 | 28.9911 |
| moving:lilith (black moon) | 17 | 0.3778 | 0.0279 | 31.0766 |
| natal:juno | 16 | 0.3556 | 0.0273 | 18.3261 |
| moving:venus | 17 | 0.3778 | 0.0266 | 6.6583 |
| moving:uranus | 17 | 0.3778 | 0.0263 | 23.8162 |

### Shared Nodes ve Validation

| natal_node | keywords_tr |
| --- | --- |
| asc | görünüm, başlatma ekseni |
| ceres | besleme, bakım, sürdürülebilirlik |
| chiron | kırılganlık, ustalık, onarım |
| dsc | karşı eksen, ilişki alanı |
| ic | temel, kök, iç yapı |
| juno | bağlılık, sözleşme, karşılıklılık |
| jupiter | genişleme, inanç, fırsat, büyüme |
| lilith (asteroid) | temsili lilith varyantı |
| lilith (black moon) | ham dürtü, dışlanan içerik |
| mars | dürtü, mücadele, uygulama, ayrışma |
| mc | kamusal yön, zirve, kariyer |
| mercury | zihin, yazışma, ticaret, analitik süreç |
| moon | duygusal ritim, ihtiyaç, alışkanlık |
| neptune | belirsizlik, ideal, çözünme, geçirgenlik |
| nn | yön, gelişim vektörü |
| pallas | örüntü zekâsı, strateji, tasarım |
| pluto | yoğunlaşma, güç, eliminasyon, dönüşüm |
| saturn | yapı, yükümlülük, sınır, kurumsallaşma |
| sn | geçmiş örüntü, boşalma hattı |
| sun | irade, amaç, merkez |

Progressed validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 45 | 46 | 45 |
| 60 | 39 | sekstil |
| 90 | 38 | kare |
| 150 | 38 | quincunx |
| 135 | 37 | 135 |
| 30 | 36 | yarı-sekstil |
| 0 | 36 | kavuşum |
| 120 | 30 | üçgen |
| 72 | 30 | 72 |
| 180 | 25 | karşıtlık |

Transit validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 135 | 50 | 135 |
| 90 | 49 | kare |
| 150 | 44 | quincunx |
| 45 | 38 | 45 |
| 180 | 34 | karşıtlık |
| 30 | 34 | yarı-sekstil |
| 72 | 32 | 72 |
| 60 | 31 | sekstil |
| 120 | 30 | üçgen |
| 0 | 21 | kavuşum |

### Teknik Tematik Özet

Bu fazın teknik matrisi işlevsel çözüm, sadeleştirme ve pratik entegrasyon eksenini öne çıkarıyor. En yoğun temas alanları: iş rutini, hizmet, sağlık rejimi, teknik bakım; ortaklıklar, kontratlar, açık muhataplar; yaratıcılık, aşk, sahne, üretken ifade. Aktif natal düğüm imzası: ham dürtü, dışlanan içerik; adanma, odak, kutsal görev; kamusal yön, zirve, kariyer; ilişki kalitesi, değer, estetik, çekim. Biyografik doğrulamada tekil olay aramak yerine, rol tanımı, iş-akış mimarisi, ilişki kontratları, kaynak yönetimi ve iç/dış yönelim dengesinde gözlenen yapısal yeniden dağılımlar izlenmeli.

## Balsamik Ön Evre (330°)

### Faz Doğrulama

| target_angle_deg | event_utc | event_local | progressed_chart_utc | progressed_sun_lon | progressed_moon_lon | moon_minus_sun_deg | exact_delta_deg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 330 | 2024-07-27T08:29:22.564831Z | 2024-07-27T11:29:22.564831+03:00 | 1982-06-19T08:57:10.000177Z | 87.755149 | 57.755149 | 330.0 | -5e-09 |

### A. Progressed-to-Natal

Aktif pattern graph: 46 düğüm, 358 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | sun | 45 | 45 | 4.4751 | 2 | 12 | False | True |
| sun | moon | 135 | 135 | 5.8336 | 2 | 6 | False | True |
| sun | mars | 90 | kare | 2.7082 | 2 | 5 | True | False |
| sun | uranus | 150 | quincunx | 5.519 | 2 | 6 | True | False |
| sun | neptune | 180 | karşıtlık | 1.1128 | 2 | 7 | False | True |
| sun | pluto | 120 | üçgen | 2.8152 | 2 | 6 | False | True |
| sun | pallas | 90 | kare | 5.4364 | 2 | 5 | True | False |
| sun | vesta | 135 | 135 | 3.4517 | 2 | 10 | True | False |
| sun | chiron | 30 | yarı-sekstil | 5.4566 | 2 | 12 | False | True |
| sun | lilith (black moon) | 180 | karşıtlık | 2.586 | 2 | 7 | False | True |
| sun | lilith (asteroid) | 90 | kare | 4.403 | 2 | 11 | True | False |
| sun | asc | 30 | yarı-sekstil | 5.6002 | 2 | 1 | True | False |
| sun | dsc | 150 | quincunx | 5.6002 | 2 | 7 | True | False |
| sun | mc | 135 | 135 | 3.3753 | 2 | 10 | False | True |
| sun | ic | 45 | 45 | 3.3753 | 2 | 4 | False | True |
| sun | lilith (black moon) | 180 | karşıtlık | 2.586 | 2 | 7 | False | True |
| moon | mars | 120 | üçgen | 2.7082 | 12 | 5 | True | False |
| moon | saturn | 135 | 135 | 4.0815 | 12 | 5 | True | False |
| moon | uranus | 180 | karşıtlık | 5.519 | 12 | 6 | True | False |
| moon | neptune | 150 | quincunx | 1.1128 | 12 | 7 | False | True |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| moving:juno | 0.4444 | 0.0404 | 39.0752 |
| natal:moon | 0.4 | 0.0328 | 16.1824 |
| moving:lilith (black moon) | 0.4 | 0.0326 | 15.1345 |
| natal:juno | 0.3778 | 0.0307 | 9.8519 |
| natal:ceres | 0.3778 | 0.0301 | 34.3322 |
| natal:saturn | 0.3778 | 0.0298 | 16.9132 |
| moving:pallas | 0.3778 | 0.0283 | 36.0324 |
| natal:ic | 0.3778 | 0.0281 | 8.3232 |
| moving:mars | 0.3556 | 0.0259 | 13.0223 |
| moving:moon | 0.3556 | 0.0259 | 7.7617 |
| moving:ceres | 0.3556 | 0.0256 | 5.5486 |
| moving:uranus | 0.3333 | 0.0241 | 11.6346 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| moving:juno | 20 | 0.4444 | 0.0404 | 39.0752 |
| natal:moon | 18 | 0.4 | 0.0328 | 16.1824 |
| moving:lilith (black moon) | 18 | 0.4 | 0.0326 | 15.1345 |
| natal:juno | 17 | 0.3778 | 0.0307 | 9.8519 |
| natal:ceres | 17 | 0.3778 | 0.0301 | 34.3322 |
| natal:saturn | 17 | 0.3778 | 0.0298 | 16.9132 |
| moving:pallas | 17 | 0.3778 | 0.0283 | 36.0324 |
| natal:ic | 17 | 0.3778 | 0.0281 | 8.3232 |
| moving:mars | 16 | 0.3556 | 0.0259 | 13.0223 |
| moving:moon | 16 | 0.3556 | 0.0259 | 7.7617 |

### B. Transit-to-Natal

Aktif pattern graph: 46 düğüm, 360 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | sun | 72 | 72 | 5.5741 | 3 | 12 | True | False |
| sun | mercury | 60 | sekstil | 3.6074 | 3 | 1 | False | True |
| sun | venus | 120 | üçgen | 0.7423 | 3 | 11 | True | False |
| sun | mars | 60 | sekstil | 4.341 | 3 | 5 | False | True |
| sun | jupiter | 90 | kare | 0.8711 | 3 | 6 | False | True |
| sun | saturn | 72 | 72 | 0.0323 | 3 | 5 | True | False |
| sun | uranus | 120 | üçgen | 1.5301 | 3 | 6 | False | True |
| sun | pallas | 60 | sekstil | 1.6128 | 3 | 5 | False | True |
| sun | juno | 150 | quincunx | 4.986 | 3 | 8 | True | False |
| sun | chiron | 72 | 72 | 0.5057 | 3 | 12 | False | True |
| sun | lilith (black moon) | 135 | 135 | 5.3648 | 3 | 7 | True | False |
| sun | lilith (asteroid) | 120 | üçgen | 2.6462 | 3 | 11 | False | True |
| sun | asc | 60 | sekstil | 1.449 | 3 | 1 | False | True |
| sun | dsc | 120 | üçgen | 1.449 | 3 | 7 | False | True |
| sun | mc | 180 | karşıtlık | 4.5755 | 3 | 10 | True | False |
| sun | ic | 0 | kavuşum | 4.5755 | 3 | 4 | True | False |
| sun | lilith (black moon) | 135 | 135 | 5.3648 | 3 | 7 | True | False |
| moon | mercury | 45 | 45 | 1.3722 | 12 | 1 | False | True |
| moon | mars | 150 | quincunx | 5.6793 | 12 | 5 | True | False |
| moon | saturn | 180 | karşıtlık | 7.9474 | 12 | 5 | False | True |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| moving:neptune | 0.4222 | 0.036 | 6.9518 |
| moving:vesta | 0.4222 | 0.0349 | 18.5843 |
| natal:chiron | 0.4 | 0.0331 | 8.3884 |
| moving:venus | 0.4 | 0.0311 | 13.4562 |
| natal:mc | 0.3778 | 0.0292 | 9.6908 |
| natal:mercury | 0.3556 | 0.0254 | 17.482 |
| moving:pallas | 0.3556 | 0.0253 | 6.0627 |
| natal:saturn | 0.3556 | 0.0247 | 34.9125 |
| moving:sun | 0.3556 | 0.0239 | 32.7535 |
| moving:mars | 0.3556 | 0.0237 | 10.177 |
| moving:sn | 0.3556 | 0.0237 | 9.939 |
| natal:ceres | 0.3333 | 0.0225 | 7.3835 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| moving:neptune | 19 | 0.4222 | 0.036 | 6.9518 |
| moving:vesta | 19 | 0.4222 | 0.0349 | 18.5843 |
| natal:chiron | 18 | 0.4 | 0.0331 | 8.3884 |
| moving:venus | 18 | 0.4 | 0.0311 | 13.4562 |
| natal:mc | 17 | 0.3778 | 0.0292 | 9.6908 |
| natal:mercury | 16 | 0.3556 | 0.0254 | 17.482 |
| moving:pallas | 16 | 0.3556 | 0.0253 | 6.0627 |
| natal:saturn | 16 | 0.3556 | 0.0247 | 34.9125 |
| moving:sun | 16 | 0.3556 | 0.0239 | 32.7535 |
| moving:mars | 16 | 0.3556 | 0.0237 | 10.177 |

### Shared Nodes ve Validation

| natal_node | keywords_tr |
| --- | --- |
| asc | görünüm, başlatma ekseni |
| ceres | besleme, bakım, sürdürülebilirlik |
| chiron | kırılganlık, ustalık, onarım |
| dsc | karşı eksen, ilişki alanı |
| ic | temel, kök, iç yapı |
| juno | bağlılık, sözleşme, karşılıklılık |
| jupiter | genişleme, inanç, fırsat, büyüme |
| lilith (asteroid) | temsili lilith varyantı |
| lilith (black moon) | ham dürtü, dışlanan içerik |
| mars | dürtü, mücadele, uygulama, ayrışma |
| mc | kamusal yön, zirve, kariyer |
| mercury | zihin, yazışma, ticaret, analitik süreç |
| moon | duygusal ritim, ihtiyaç, alışkanlık |
| neptune | belirsizlik, ideal, çözünme, geçirgenlik |
| nn | yön, gelişim vektörü |
| pallas | örüntü zekâsı, strateji, tasarım |
| pluto | yoğunlaşma, güç, eliminasyon, dönüşüm |
| saturn | yapı, yükümlülük, sınır, kurumsallaşma |
| sn | geçmiş örüntü, boşalma hattı |
| sun | irade, amaç, merkez |

Progressed validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 45 | 45 | 45 |
| 150 | 43 | quincunx |
| 60 | 42 | sekstil |
| 135 | 37 | 135 |
| 30 | 37 | yarı-sekstil |
| 0 | 36 | kavuşum |
| 90 | 31 | kare |
| 120 | 31 | üçgen |
| 72 | 31 | 72 |
| 180 | 25 | karşıtlık |

Transit validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 120 | 48 | üçgen |
| 135 | 44 | 135 |
| 60 | 40 | sekstil |
| 72 | 38 | 72 |
| 45 | 35 | 45 |
| 180 | 33 | karşıtlık |
| 90 | 31 | kare |
| 0 | 31 | kavuşum |
| 30 | 31 | yarı-sekstil |
| 150 | 29 | quincunx |

### Teknik Tematik Özet

Bu fazın teknik matrisi bırakma, iç değerlendirme ve yeni döngü öncesi çözülme eksenini öne çıkarıyor. En yoğun temas alanları: iş rutini, hizmet, sağlık rejimi, teknik bakım; ortaklıklar, kontratlar, açık muhataplar; yaratıcılık, aşk, sahne, üretken ifade. Aktif natal düğüm imzası: ham dürtü, dışlanan içerik; duygusal ritim, ihtiyaç, alışkanlık; temel, kök, iç yapı; kırılganlık, ustalık, onarım. Biyografik doğrulamada tekil olay aramak yerine, rol tanımı, iş-akış mimarisi, ilişki kontratları, kaynak yönetimi ve iç/dış yönelim dengesinde gözlenen yapısal yeniden dağılımlar izlenmeli.

## Sonraki İlerletilmiş Yeniay (360°)

### Faz Doğrulama

| target_angle_deg | event_utc | event_local | progressed_chart_utc | progressed_sun_lon | progressed_moon_lon | moon_minus_sun_deg | exact_delta_deg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 360 | 2026-09-10T03:19:14.623301Z | 2026-09-10T06:19:14.623301+03:00 | 1982-06-21T11:51:45.543116Z | 89.780416 | 89.780416 | 360.0 | -2e-09 |

### A. Progressed-to-Natal

Aktif pattern graph: 46 düğüm, 359 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | sun | 45 | 45 | 2.4498 | 2 | 12 | False | True |
| sun | moon | 135 | 135 | 3.8083 | 2 | 6 | False | True |
| sun | venus | 90 | kare | 4.2816 | 2 | 11 | False | True |
| sun | mars | 90 | kare | 0.6829 | 2 | 5 | True | False |
| sun | jupiter | 120 | üçgen | 4.1528 | 2 | 6 | True | False |
| sun | uranus | 150 | quincunx | 3.4938 | 2 | 6 | True | False |
| sun | neptune | 180 | karşıtlık | 3.1381 | 2 | 7 | False | True |
| sun | pluto | 120 | üçgen | 4.8404 | 2 | 6 | False | True |
| sun | ceres | 135 | 135 | 5.2697 | 2 | 6 | True | False |
| sun | pallas | 90 | kare | 3.4111 | 2 | 5 | True | False |
| sun | vesta | 135 | 135 | 1.4264 | 2 | 10 | True | False |
| sun | lilith (black moon) | 180 | karşıtlık | 4.6113 | 2 | 7 | False | True |
| sun | lilith (asteroid) | 90 | kare | 2.3777 | 2 | 11 | True | False |
| sun | asc | 30 | yarı-sekstil | 3.5749 | 2 | 1 | True | False |
| sun | dsc | 150 | quincunx | 3.5749 | 2 | 7 | True | False |
| sun | mc | 135 | 135 | 5.4006 | 2 | 10 | False | True |
| sun | ic | 45 | 45 | 5.4006 | 2 | 4 | False | True |
| sun | lilith (black moon) | 180 | karşıtlık | 4.6113 | 2 | 7 | False | True |
| moon | sun | 45 | 45 | 2.4498 | 2 | 12 | True | False |
| moon | moon | 135 | 135 | 3.8083 | 2 | 6 | True | False |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| moving:mars | 0.4222 | 0.0416 | 12.5692 |
| natal:neptune | 0.4222 | 0.0398 | 47.1706 |
| moving:juno | 0.4222 | 0.037 | 24.3536 |
| natal:lilith (black moon) | 0.4 | 0.0348 | 58.0589 |
| natal:moon | 0.4 | 0.0328 | 6.1858 |
| moving:lilith (black moon) | 0.4 | 0.0313 | 17.358 |
| moving:pallas | 0.3778 | 0.0297 | 9.1665 |
| natal:pluto | 0.3556 | 0.0291 | 15.3876 |
| natal:ceres | 0.3778 | 0.0287 | 7.2686 |
| moving:ceres | 0.3556 | 0.0287 | 5.5448 |
| moving:moon | 0.3778 | 0.0274 | 6.3511 |
| moving:sun | 0.3778 | 0.0274 | 6.3511 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| moving:mars | 19 | 0.4222 | 0.0416 | 12.5692 |
| natal:neptune | 19 | 0.4222 | 0.0398 | 47.1706 |
| moving:juno | 19 | 0.4222 | 0.037 | 24.3536 |
| natal:lilith (black moon) | 18 | 0.4 | 0.0348 | 58.0589 |
| natal:moon | 18 | 0.4 | 0.0328 | 6.1858 |
| moving:lilith (black moon) | 18 | 0.4 | 0.0313 | 17.358 |
| moving:pallas | 17 | 0.3778 | 0.0297 | 9.1665 |
| natal:pluto | 16 | 0.3556 | 0.0291 | 15.3876 |
| natal:ceres | 17 | 0.3778 | 0.0287 | 7.2686 |
| moving:ceres | 16 | 0.3556 | 0.0287 | 5.5448 |

### B. Transit-to-Natal

Aktif pattern graph: 46 düğüm, 354 temas.

| moving_node | natal_node | aspect | aspect_label_tr | orb_deg | MOVING_NODE_NATAL_OVERLAY_HOUSE | CONTACTED_NATAL_NODE_HOUSE | applying | separating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sun | sun | 120 | üçgen | 0.224 | 5 | 12 | False | True |
| sun | moon | 60 | sekstil | 1.1346 | 5 | 6 | False | True |
| sun | jupiter | 45 | 45 | 1.479 | 5 | 6 | True | False |
| sun | saturn | 30 | yarı-sekstil | 0.6176 | 5 | 5 | False | True |
| sun | uranus | 72 | 72 | 3.82 | 5 | 6 | True | False |
| sun | ceres | 60 | sekstil | 2.5959 | 5 | 6 | True | False |
| sun | vesta | 150 | quincunx | 1.2474 | 5 | 10 | False | True |
| sun | chiron | 120 | üçgen | 4.8444 | 5 | 12 | True | False |
| sun | dsc | 72 | 72 | 3.9011 | 5 | 7 | True | False |
| sun | nn | 60 | sekstil | 2.588 | 5 | 2 | False | True |
| sun | sn | 120 | üçgen | 2.588 | 5 | 8 | False | True |
| moon | moon | 72 | 72 | 2.0774 | 4 | 6 | True | False |
| moon | mercury | 90 | kare | 3.9004 | 4 | 1 | True | False |
| moon | venus | 150 | quincunx | 0.4493 | 4 | 11 | False | True |
| moon | mars | 30 | yarı-sekstil | 4.048 | 4 | 5 | False | True |
| moon | jupiter | 60 | sekstil | 0.5781 | 4 | 6 | False | True |
| moon | saturn | 45 | 45 | 2.6747 | 4 | 5 | False | True |
| moon | uranus | 90 | kare | 1.2371 | 4 | 6 | False | True |
| moon | pluto | 45 | 45 | 5.4287 | 4 | 6 | True | False |
| moon | ceres | 72 | 72 | 3.5388 | 4 | 6 | True | False |

| id | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- |
| moving:jupiter | 0.4222 | 0.0385 | 20.7783 |
| natal:nn | 0.4 | 0.0348 | 50.9507 |
| moving:lilith (black moon) | 0.4 | 0.0329 | 14.3546 |
| moving:mercury | 0.4 | 0.0325 | 5.601 |
| natal:pluto | 0.3778 | 0.0304 | 5.7069 |
| moving:moon | 0.4 | 0.0303 | 10.418 |
| natal:sn | 0.3556 | 0.0266 | 50.2826 |
| moving:neptune | 0.3556 | 0.0261 | 45.9359 |
| natal:mars | 0.3556 | 0.0251 | 28.1786 |
| moving:nn | 0.3556 | 0.025 | 44.7323 |
| natal:jupiter | 0.3333 | 0.0245 | 9.0312 |
| moving:uranus | 0.3556 | 0.0231 | 5.2917 |

| cluster_id | size | moving_nodes | natal_nodes |
| --- | --- | --- | --- |
| 1 | 46 | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] | ['asc', 'ceres', 'chiron', 'dsc', 'ic', 'juno', 'jupiter', 'lilith (asteroid)', 'lilith (black moon)', 'mars', 'mc', 'mercury', 'moon', 'neptune', 'nn', 'pallas', 'pluto', 'saturn', 'sn', 'sun', 'uranus', 'venus', 'vesta'] |

| id | degree | degree_centrality | betweenness_centrality | weighted_degree |
| --- | --- | --- | --- | --- |
| moving:jupiter | 19 | 0.4222 | 0.0385 | 20.7783 |
| natal:nn | 18 | 0.4 | 0.0348 | 50.9507 |
| moving:lilith (black moon) | 18 | 0.4 | 0.0329 | 14.3546 |
| moving:mercury | 18 | 0.4 | 0.0325 | 5.601 |
| natal:pluto | 17 | 0.3778 | 0.0304 | 5.7069 |
| moving:moon | 18 | 0.4 | 0.0303 | 10.418 |
| natal:sn | 16 | 0.3556 | 0.0266 | 50.2826 |
| moving:neptune | 16 | 0.3556 | 0.0261 | 45.9359 |
| natal:mars | 16 | 0.3556 | 0.0251 | 28.1786 |
| moving:nn | 16 | 0.3556 | 0.025 | 44.7323 |

### Shared Nodes ve Validation

| natal_node | keywords_tr |
| --- | --- |
| asc | görünüm, başlatma ekseni |
| ceres | besleme, bakım, sürdürülebilirlik |
| chiron | kırılganlık, ustalık, onarım |
| dsc | karşı eksen, ilişki alanı |
| ic | temel, kök, iç yapı |
| juno | bağlılık, sözleşme, karşılıklılık |
| jupiter | genişleme, inanç, fırsat, büyüme |
| lilith (asteroid) | temsili lilith varyantı |
| lilith (black moon) | ham dürtü, dışlanan içerik |
| mars | dürtü, mücadele, uygulama, ayrışma |
| mc | kamusal yön, zirve, kariyer |
| mercury | zihin, yazışma, ticaret, analitik süreç |
| moon | duygusal ritim, ihtiyaç, alışkanlık |
| neptune | belirsizlik, ideal, çözünme, geçirgenlik |
| nn | yön, gelişim vektörü |
| pallas | örüntü zekâsı, strateji, tasarım |
| pluto | yoğunlaşma, güç, eliminasyon, dönüşüm |
| saturn | yapı, yükümlülük, sınır, kurumsallaşma |
| sn | geçmiş örüntü, boşalma hattı |
| sun | irade, amaç, merkez |

Progressed validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 45 | 47 | 45 |
| 135 | 40 | 135 |
| 150 | 39 | quincunx |
| 90 | 38 | kare |
| 60 | 36 | sekstil |
| 30 | 35 | yarı-sekstil |
| 0 | 35 | kavuşum |
| 72 | 33 | 72 |
| 120 | 30 | üçgen |
| 180 | 26 | karşıtlık |

Transit validation özeti:

| aspect | count | label_tr |
| --- | --- | --- |
| 60 | 48 | sekstil |
| 120 | 46 | üçgen |
| 30 | 40 | yarı-sekstil |
| 45 | 38 | 45 |
| 150 | 37 | quincunx |
| 90 | 35 | kare |
| 135 | 35 | 135 |
| 72 | 34 | 72 |
| 180 | 21 | karşıtlık |
| 0 | 20 | kavuşum |

### Teknik Tematik Özet

Bu fazın teknik matrisi yeni 29 yıllık yapısal döngü eşiği eksenini öne çıkarıyor. En yoğun temas alanları: iş rutini, hizmet, sağlık rejimi, teknik bakım; ortaklıklar, kontratlar, açık muhataplar; yaratıcılık, aşk, sahne, üretken ifade. Aktif natal düğüm imzası: ham dürtü, dışlanan içerik; belirsizlik, ideal, çözünme, geçirgenlik; duygusal ritim, ihtiyaç, alışkanlık; yön, gelişim vektörü. Biyografik doğrulamada tekil olay aramak yerine, rol tanımı, iş-akış mimarisi, ilişki kontratları, kaynak yönetimi ve iç/dış yönelim dengesinde gözlenen yapısal yeniden dağılımlar izlenmeli.

## Döngü Sentezi

Bu yaklaşık 29 yıllık döngü boyunca tekrar eden natal düğümler ve ev kümeleri, gelişimin tek bir olay çizgisi yerine tekrarlanan yapısal stres noktaları ve entegrasyon eşikleri üzerinden çalıştığını gösteriyor.

- Tekrarlayan natal düğümler: lilith (black moon) (688), vesta (431), ic (414), moon (414), saturn (413), mc (401), sun (399), uranus (398), dsc (398), asc (396)
- En çok aktive olan natal evler: 6. ev (1930), 7. ev (1458), 5. ev (1162), 10. ev (832), 1. ev (770), 8. ev (769), 12. ev (760), 11. ev (754)
- Hareketli düğümlerin natal overlay yoğunluğu: 8. ev (1285), 6. ev (1261), 5. ev (1177), 12. ev (1078), 11. ev (793), 10. ev (756), 1. ev (607), 2. ev (578)
- Yapısal geçiş mantığı: yeniay eksenlerinde kapanış/başlatma, karelerde zorunlu yeniden yapılandırma, dolunayda karşılıklılık ve dış görünürlük, balsamik alanda ise çözülme ve sadeleşme baskın.
- Biyografik validasyon odağı: kariyer/otorite mimarisi, ortaklık ve kontrat örüntüleri, kök-aile ile kamusal yön arasındaki eksen, gelir-paylaşılan kaynaklar ve çalışma rejimi yeniden dağılımları.
- En tutarlı teknik imza, aynı natal düğümlerin hem progressed hem transit katmanda tekrarlı eşzamanlı temas almasıdır; bu düğümler sonraki döngü başında da ana yönlendirici olarak izlenmelidir.

## Fazlar Arası Hızlı Özet

| phase | target_angle_deg | event_utc | event_local | progressed_contacts | transit_contacts | shared_natal_nodes |
| --- | --- | --- | --- | --- | --- | --- |
| İlerletilmiş Yeniay | 0 | 1997-05-23T10:51:31.193435Z | 1997-05-23T13:51:31.193435+03:00 | 342 | 348 | asc, ceres, chiron, dsc, ic, juno, jupiter, lilith (asteroid) |
| 30° Fazı | 30 | 1999-07-08T21:33:27.119183Z | 1999-07-09T00:33:27.119183+03:00 | 340 | 354 | asc, ceres, chiron, dsc, ic, juno, jupiter, lilith (asteroid) |
| İlk Altmışlık | 60 | 2001-09-16T04:04:12.032884Z | 2001-09-16T07:04:12.032884+03:00 | 337 | 375 | asc, ceres, chiron, dsc, ic, juno, jupiter, lilith (asteroid) |
| İlk Kare | 90 | 2004-01-13T21:29:25.730005Z | 2004-01-13T23:29:25.730005+02:00 | 343 | 348 | asc, ceres, chiron, dsc, ic, juno, jupiter, lilith (asteroid) |
| Büyüyen Üçgen | 120 | 2006-07-09T11:54:58.090679Z | 2006-07-09T14:54:58.090679+03:00 | 345 | 371 | asc, ceres, chiron, dsc, ic, juno, jupiter, lilith (asteroid) |
| Büyüyen Quincunx | 150 | 2009-02-21T14:02:48.922205Z | 2009-02-21T16:02:48.922205+02:00 | 350 | 379 | asc, ceres, chiron, dsc, ic, juno, jupiter, lilith (asteroid) |
| İlerletilmiş Dolunay | 180 | 2011-11-12T04:35:13.137426Z | 2011-11-12T06:35:13.137426+02:00 | 353 | 344 | asc, ceres, chiron, dsc, ic, juno, jupiter, lilith (asteroid) |
| Dağılan 30° | 210 | 2014-08-17T22:43:08.150422Z | 2014-08-18T01:43:08.150422+03:00 | 346 | 366 | asc, ceres, chiron, dsc, ic, juno, jupiter, lilith (asteroid) |
| Dağılan Üçgen | 240 | 2017-05-10T16:05:30.413728Z | 2017-05-10T19:05:30.413728+03:00 | 350 | 359 | asc, ceres, chiron, dsc, ic, juno, jupiter, lilith (asteroid) |
| Son Kare | 270 | 2019-12-14T06:58:19.184864Z | 2019-12-14T09:58:19.184864+03:00 | 367 | 356 | asc, ceres, chiron, dsc, ic, juno, jupiter, lilith (asteroid) |
| Dağılan Sekstil | 300 | 2022-05-08T09:09:32.078780Z | 2022-05-08T12:09:32.078780+03:00 | 355 | 363 | asc, ceres, chiron, dsc, ic, juno, jupiter, lilith (asteroid) |
| Balsamik Ön Evre | 330 | 2024-07-27T08:29:22.564831Z | 2024-07-27T11:29:22.564831+03:00 | 358 | 360 | asc, ceres, chiron, dsc, ic, juno, jupiter, lilith (asteroid) |
| Sonraki İlerletilmiş Yeniay | 360 | 2026-09-10T03:19:14.623301Z | 2026-09-10T06:19:14.623301+03:00 | 359 | 354 | asc, ceres, chiron, dsc, ic, juno, jupiter, lilith (asteroid) |
