# Machine Specifications

MacBook Pro: 2021
macOS version 12.4
Chip: Apple M1 Pro
Memory 32GB

# Remix App Benchmarks

node version: 14.17.5

### Benchmark 1: small payload

```
➜  remix-python-benchmark git:(main) ✗ oha -z 10s -c 100 --http-version 1.1 http://localhost:3000/small-json-payload
Summary:
  Success rate:	1.0000
  Total:	10.0022 secs
  Slowest:	0.5722 secs
  Fastest:	0.0445 secs
  Average:	0.0844 secs
  Requests/sec:	1181.6411

  Total data:	52.12 MiB
  Size/request:	4.52 KiB
  Size/sec:	5.21 MiB

Response time histogram:
  0.064 [5259] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.082 [2232] |■■■■■■■■■■■■■
  0.101 [1592] |■■■■■■■■■
  0.120 [964]  |■■■■■
  0.139 [683]  |■■■■
  0.158 [542]  |■■■
  0.177 [378]  |■■
  0.196 [43]   |
  0.215 [12]   |
  0.234 [11]   |
  0.253 [103]  |

Latency distribution:
  10% in 0.0512 secs
  25% in 0.0559 secs
  50% in 0.0677 secs
  75% in 0.0985 secs
  90% in 0.1360 secs
  95% in 0.1559 secs
  99% in 0.1978 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0042 secs, 0.0016 secs, 0.0102 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0001 secs

Status code distribution:
  [200] 11819 responses

```

### Benchmark 2: medium payload

```
➜  remix-python-benchmark git:(main) ✗ oha -z 10s -c 100 --http-version 1.1 http://localhost:3000/medium-json-payload
Summary:
  Success rate:	1.0000
  Total:	10.0025 secs
  Slowest:	0.3653 secs
  Fastest:	0.0632 secs
  Average:	0.1059 secs
  Requests/sec:	940.3619

  Total data:	69.17 MiB
  Size/request:	7.53 KiB
  Size/sec:	6.92 MiB

Response time histogram:
  0.086 [3266] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.109 [2945] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.133 [1436] |■■■■■■■■■■■■■■
  0.156 [1099] |■■■■■■■■■■
  0.179 [291]  |■■
  0.202 [207]  |■■
  0.225 [76]   |
  0.248 [20]   |
  0.271 [27]   |
  0.294 [9]    |
  0.318 [30]   |

Latency distribution:
  10% in 0.0751 secs
  25% in 0.0819 secs
  50% in 0.0967 secs
  75% in 0.1192 secs
  90% in 0.1488 secs
  95% in 0.1642 secs
  99% in 0.2115 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0045 secs, 0.0029 secs, 0.0104 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0001 secs

Status code distribution:
  [200] 9406 responses
```

### Benchmark 3: large payload

```
➜  remix-python-benchmark git:(main) ✗ oha -z 10s -c 100 --http-version 1.1 http://localhost:3000/large-json-payload
Summary:
  Success rate:	1.0000
  Total:	10.0021 secs
  Slowest:	0.9333 secs
  Fastest:	0.2147 secs
  Average:	0.3182 secs
  Requests/sec:	310.4360

  Total data:	53.09 MiB
  Size/request:	17.51 KiB
  Size/sec:	5.31 MiB

Response time histogram:
  0.280 [849]  |■■■■■■■■■■■■■■■■
  0.345 [1632] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.411 [451]  |■■■■■■■■
  0.476 [47]   |
  0.541 [32]   |
  0.607 [26]   |
  0.672 [19]   |
  0.737 [10]   |
  0.803 [10]   |
  0.868 [10]   |
  0.933 [19]   |

Latency distribution:
  10% in 0.2356 secs
  25% in 0.2750 secs
  50% in 0.3114 secs
  75% in 0.3394 secs
  90% in 0.3693 secs
  95% in 0.4434 secs
  99% in 0.7627 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0041 secs, 0.0021 secs, 0.0102 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0001 secs

Status code distribution:
  [200] 3105 responses
```

# Remix-Express App Benchmarks

node version: 14.17.5

### Benchmark 1: small payload

```
➜  remix-python-benchmark git:(main) ✗ oha -z 10s -c 100 --http-version 1.1 http://localhost:3000/small-json-payload
Summary:
  Success rate:	1.0000
  Total:	10.0022 secs
  Slowest:	0.5803 secs
  Fastest:	0.0422 secs
  Average:	0.0770 secs
  Requests/sec:	1294.5143

  Total data:	57.10 MiB
  Size/request:	4.52 KiB
  Size/sec:	5.71 MiB

Response time histogram:
  0.059 [6368] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.077 [2095] |■■■■■■■■■■
  0.094 [1467] |■■■■■■■
  0.111 [1189] |■■■■■
  0.128 [869]  |■■■■
  0.145 [263]  |■
  0.162 [261]  |■
  0.180 [232]  |■
  0.197 [83]   |
  0.214 [13]   |
  0.231 [108]  |

Latency distribution:
  10% in 0.0472 secs
  25% in 0.0504 secs
  50% in 0.0602 secs
  75% in 0.0908 secs
  90% in 0.1195 secs
  95% in 0.1475 secs
  99% in 0.1888 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0044 secs, 0.0025 secs, 0.0103 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0000 secs

Status code distribution:
  [200] 12948 responses

```

### Benchmark 2: medium payload

```
➜  remix-python-benchmark git:(main) ✗ oha -z 10s -c 100 --http-version 1.1 http://localhost:3000/medium-json-payload
Summary:
  Success rate:	1.0000
  Total:	10.0019 secs
  Slowest:	0.3908 secs
  Fastest:	0.0653 secs
  Average:	0.1130 secs
  Requests/sec:	880.6295

  Total data:	64.77 MiB
  Size/request:	7.53 KiB
  Size/sec:	6.48 MiB

Response time histogram:
  0.090 [3194] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.115 [2497] |■■■■■■■■■■■■■■■■■■■■■■■■■
  0.140 [1378] |■■■■■■■■■■■■■
  0.165 [917]  |■■■■■■■■■
  0.190 [344]  |■■■
  0.215 [184]  |■
  0.240 [212]  |■■
  0.264 [34]   |
  0.289 [6]    |
  0.314 [11]   |
  0.339 [31]   |

Latency distribution:
  10% in 0.0770 secs
  25% in 0.0843 secs
  50% in 0.1030 secs
  75% in 0.1302 secs
  90% in 0.1624 secs
  95% in 0.1947 secs
  99% in 0.2381 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0041 secs, 0.0027 secs, 0.0103 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0001 secs

Status code distribution:
  [200] 8808 responses
```

### Benchmark 3: large payload

```
➜  remix-python-benchmark git:(main) ✗ oha -z 10s -c 100 --http-version 1.1 http://localhost:3000/large-json-payload
Summary:
  Success rate:	1.0000
  Total:	10.0021 secs
  Slowest:	0.5471 secs
  Fastest:	0.2025 secs
  Average:	0.2914 secs
  Requests/sec:	338.0305

  Total data:	57.81 MiB
  Size/request:	17.51 KiB
  Size/sec:	5.78 MiB

Response time histogram:
  0.234 [278]  |■■■■■■■
  0.265 [483]  |■■■■■■■■■■■■■
  0.297 [1055] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.328 [1177] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.359 [314]  |■■■■■■■■
  0.390 [11]   |
  0.422 [15]   |
  0.453 [10]   |
  0.484 [10]   |
  0.516 [10]   |
  0.547 [18]   |

Latency distribution:
  10% in 0.2394 secs
  25% in 0.2709 secs
  50% in 0.2914 secs
  75% in 0.3153 secs
  90% in 0.3312 secs
  95% in 0.3458 secs
  99% in 0.4588 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0051 secs, 0.0027 secs, 0.0109 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0001 secs

Status code distribution:
  [200] 3381 responses
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
  Total:	10.0010 secs
  Slowest:	0.5482 secs
  Fastest:	0.0177 secs
  Average:	0.2114 secs
  Requests/sec:	467.7523

  Total data:	219.37 MiB
  Size/request:	48.02 KiB
  Size/sec:	21.94 MiB

Response time histogram:
  0.066 [1]    |
  0.114 [282]  |■■■■■■
  0.162 [1016] |■■■■■■■■■■■■■■■■■■■■■■■
  0.211 [1385] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.259 [942]  |■■■■■■■■■■■■■■■■■■■■■
  0.307 [509]  |■■■■■■■■■■■
  0.355 [291]  |■■■■■■
  0.404 [136]  |■■■
  0.452 [89]   |■■
  0.500 [26]   |
  0.548 [1]    |

Latency distribution:
  10% in 0.1239 secs
  25% in 0.1548 secs
  50% in 0.1994 secs
  75% in 0.2520 secs
  90% in 0.3169 secs
  95% in 0.3594 secs
  99% in 0.4347 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0003 secs, 0.0000 secs, 0.0542 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0002 secs

Status code distribution:
  [200] 4678 responses
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
