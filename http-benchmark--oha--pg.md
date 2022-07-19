# Machine Specifications

MacBook Pro: 2021
macOS version 12.4
Chip: Apple M1 Pro
Memory 32GB

# Remix App Benchmarks

node version: 14.17.5

### Benchmark 1: small payload

```
➜  remix-python-benchmark git:(main) oha -z 10s -c 100 --http-version 1.1 http://localhost:3000/small-json-payload
Summary:
  Success rate:	1.0000
  Total:	10.0038 secs
  Slowest:	0.4303 secs
  Fastest:	0.0978 secs
  Average:	0.1916 secs
  Requests/sec:	517.9015

  Total data:	22.39 MiB
  Size/request:	4.42 KiB
  Size/sec:	2.24 MiB

Response time histogram:
  0.128 [218]  |■■■
  0.158 [2003] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.189 [917]  |■■■■■■■■■■■■■■
  0.219 [477]  |■■■■■■■
  0.249 [640]  |■■■■■■■■■■
  0.279 [401]  |■■■■■■
  0.309 [301]  |■■■■
  0.340 [70]   |■
  0.370 [99]   |■
  0.400 [53]   |
  0.430 [2]    |

Latency distribution:
  10% in 0.1351 secs
  25% in 0.1464 secs
  50% in 0.1665 secs
  75% in 0.2338 secs
  90% in 0.2796 secs
  95% in 0.3062 secs
  99% in 0.3703 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0059 secs, 0.0025 secs, 0.0106 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0002 secs

Status code distribution:
  [200] 5181 responses

```

### Benchmark 2: medium payload

```
➜  remix-python-benchmark git:(main) ✗ oha -z 10s -c 100 --http-version 1.1 http://localhost:3000/medium-json-payload
Summary:
  Success rate:	1.0000
  Total:	10.0024 secs
  Slowest:	7.2092 secs
  Fastest:	0.0146 secs
  Average:	0.8076 secs
  Requests/sec:	47.1886

  Total data:	3.47 MiB
  Size/request:	7.53 KiB
  Size/sec:	355.34 KiB

Response time histogram:
  0.234 [352] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.453 [44]  |■■■■
  0.671 [0]   |
  0.890 [0]   |
  1.109 [0]   |
  1.328 [35]  |■■■
  1.547 [3]   |
  1.766 [0]   |
  1.985 [0]   |
  2.204 [0]   |
  2.423 [38]  |■■■

Latency distribution:
  10% in 0.1124 secs
  25% in 0.1270 secs
  50% in 0.1587 secs
  75% in 0.2380 secs
  90% in 1.2471 secs
  95% in 7.0385 secs
  99% in 7.1921 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0046 secs, 0.0021 secs, 0.0103 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0000 secs

Status code distribution:
  [200] 472 responses
```

### Benchmark 3: large payload

```
➜  remix-python-benchmark git:(main) ✗ oha -z 10s -c 100 --http-version 1.1 http://localhost:3000/large-json-payload
Summary:
  Success rate:	1.0000
  Total:	10.0023 secs
  Slowest:	1.1633 secs
  Fastest:	0.1676 secs
  Average:	0.5301 secs
  Requests/sec:	183.7570

  Total data:	31.36 MiB
  Size/request:	17.47 KiB
  Size/sec:	3.14 MiB

Response time histogram:
  0.258 [12]  |
  0.349 [285] |■■■■■■■■■■■■■■
  0.439 [634] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.530 [261] |■■■■■■■■■■■■■
  0.620 [86]  |■■■■
  0.711 [143] |■■■■■■■
  0.801 [96]  |■■■■
  0.892 [211] |■■■■■■■■■■
  0.982 [36]  |■
  1.073 [63]  |■■■
  1.163 [11]  |

Latency distribution:
  10% in 0.3145 secs
  25% in 0.3721 secs
  50% in 0.4362 secs
  75% in 0.6972 secs
  90% in 0.8632 secs
  95% in 0.9032 secs
  99% in 1.0469 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0061 secs, 0.0031 secs, 0.0110 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0001 secs

Status code distribution:
  [200] 1838 responses
```

# Flask App Benchmarks

### Benchmark 1: small payload

```
➜  remix-python-benchmark git:(main) ✗ oha -z 10s -c 100 --http-version 1.1 http://127.0.0.1:5000/small-json-payload
Summary:
  Success rate:	1.0000
  Total:	10.0026 secs
  Slowest:	0.5153 secs
  Fastest:	0.0452 secs
  Average:	0.1449 secs
  Requests/sec:	685.8203

  Total data:	134.17 MiB
  Size/request:	20.03 KiB
  Size/sec:	13.41 MiB

Response time histogram:
  0.081 [256]  |■■■
  0.116 [1731] |■■■■■■■■■■■■■■■■■■■■■■■
  0.151 [2364] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.187 [1498] |■■■■■■■■■■■■■■■■■■■■
  0.222 [602]  |■■■■■■■■
  0.258 [221]  |■■
  0.293 [82]   |■
  0.328 [36]   |
  0.364 [32]   |
  0.399 [10]   |
  0.435 [28]   |

Latency distribution:
  10% in 0.0895 secs
  25% in 0.1114 secs
  50% in 0.1374 secs
  75% in 0.1661 secs
  90% in 0.2028 secs
  95% in 0.2315 secs
  99% in 0.3296 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0006 secs, 0.0001 secs, 0.0191 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0012 secs

Status code distribution:
  [200] 6860 responses

```

### Benchmark 2: medium payload

```
➜  remix-python-benchmark git:(main) ✗ oha -z 10s -c 100 --http-version 1.1 http://127.0.0.1:5000/medium-json-payload
Summary:
  Success rate:	1.0000
  Total:	10.0067 secs
  Slowest:	6.7978 secs
  Fastest:	0.0050 secs
  Average:	0.3322 secs
  Requests/sec:	137.2083

  Total data:	64.40 MiB
  Size/request:	48.03 KiB
  Size/sec:	6.44 MiB

Response time histogram:
  0.095 [446] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.185 [433] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.275 [177] |■■■■■■■■■■■■
  0.366 [98]  |■■■■■■■
  0.456 [105] |■■■■■■■
  0.546 [67]  |■■■■
  0.636 [12]  |
  0.726 [2]   |
  0.816 [0]   |
  0.906 [0]   |
  0.997 [33]  |■■

Latency distribution:
  10% in 0.0215 secs
  25% in 0.0672 secs
  50% in 0.1395 secs
  75% in 0.2548 secs
  90% in 0.4320 secs
  95% in 0.5028 secs
  99% in 6.7402 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.1621 secs, 0.0001 secs, 6.7095 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0003 secs

Status code distribution:
  [200] 1373 responses
```

### Benchmark 3: large payload

```
➜  remix-python-benchmark git:(main) ✗ oha -z 10s -c 100 --http-version 1.1 http://127.0.0.1:5000/large-json-payload
Summary:
  Success rate:	1.0000
  Total:	10.0055 secs
  Slowest:	0.8908 secs
  Fastest:	0.0575 secs
  Average:	0.4838 secs
  Requests/sec:	198.8903

  Total data:	444.80 MiB
  Size/request:	228.88 KiB
  Size/sec:	44.46 MiB

Response time histogram:
  0.133 [16]   |
  0.209 [15]   |
  0.285 [21]   |
  0.361 [111]  |■■■
  0.436 [249]  |■■■■■■
  0.512 [1174] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.588 [238]  |■■■■■■
  0.664 [17]   |
  0.739 [33]   |
  0.815 [80]   |■■
  0.891 [36]   |

Latency distribution:
  10% in 0.3768 secs
  25% in 0.4579 secs
  50% in 0.4849 secs
  75% in 0.5066 secs
  90% in 0.5356 secs
  95% in 0.7460 secs
  99% in 0.8572 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0027 secs, 0.0001 secs, 0.0251 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0003 secs

Status code distribution:
  [200] 1967 responses
  [500] 23 responses
```
