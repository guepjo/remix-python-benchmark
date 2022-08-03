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
  Total:	10.0023 secs
  Slowest:	0.2334 secs
  Fastest:	0.0307 secs
  Average:	0.0587 secs
  Requests/sec:	1699.7163

  Total data:	331.99 MiB
  Size/request:	20.00 KiB
  Size/sec:	33.19 MiB

Response time histogram:
  0.044 [5421] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.057 [3281] |■■■■■■■■■■■■■■■■■■■
  0.070 [3356] |■■■■■■■■■■■■■■■■■■■
  0.084 [3466] |■■■■■■■■■■■■■■■■■■■■
  0.097 [851]  |■■■■■
  0.110 [277]  |■
  0.123 [185]  |■
  0.136 [52]   |
  0.150 [40]   |
  0.163 [29]   |
  0.176 [43]   |

Latency distribution:
  10% in 0.0339 secs
  25% in 0.0393 secs
  50% in 0.0562 secs
  75% in 0.0737 secs
  90% in 0.0826 secs
  95% in 0.0906 secs
  99% in 0.1227 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0152 secs, 0.0049 secs, 0.0178 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0001 secs

Status code distribution:
  [200] 17001 responses

```

### Benchmark 2: medium payload

```
➜  remix-python-benchmark git:(main) ✗ oha -z 10s -c 100 --http-version 1.1 http://localhost:3000/medium-json-payload
Summary:
  Success rate:	1.0000
  Total:	10.0028 secs
  Slowest:	0.2903 secs
  Fastest:	0.0475 secs
  Average:	0.0768 secs
  Requests/sec:	1297.2420

  Total data:	586.30 MiB
  Size/request:	46.27 KiB
  Size/sec:	58.61 MiB

Response time histogram:
  0.064 [6146] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.081 [2090] |■■■■■■■■■■
  0.097 [1497] |■■■■■■■
  0.114 [2022] |■■■■■■■■■■
  0.131 [675]  |■■■
  0.147 [243]  |■
  0.164 [131]  |
  0.180 [63]   |
  0.197 [61]   |
  0.214 [7]    |
  0.230 [41]   |

Latency distribution:
  10% in 0.0517 secs
  25% in 0.0537 secs
  50% in 0.0669 secs
  75% in 0.0973 secs
  90% in 0.1129 secs
  95% in 0.1263 secs
  99% in 0.1716 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0159 secs, 0.0064 secs, 0.0188 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0001 secs

Status code distribution:
  [200] 12976 responses
```

### Benchmark 3: large payload

```
➜  remix-python-benchmark git:(main) ✗ oha -z 10s -c 100 --http-version 1.1 http://localhost:3000/large-json-payload
Summary:
  Success rate:	1.0000
  Total:	10.0041 secs
  Slowest:	0.6474 secs
  Fastest:	0.1824 secs
  Average:	0.2453 secs
  Requests/sec:	402.1357

  Total data:	840.00 MiB
  Size/request:	213.81 KiB
  Size/sec:	83.97 MiB

Response time histogram:
  0.225 [1367] |■■■■■■■■■■■■■■■■■■■■■■
  0.267 [1985] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.309 [469]  |■■■■■■■
  0.351 [87]   |■
  0.394 [37]   |
  0.436 [21]   |
  0.478 [15]   |
  0.521 [10]   |
  0.563 [10]   |
  0.605 [10]   |
  0.647 [12]   |

Latency distribution:
  10% in 0.2014 secs
  25% in 0.2157 secs
  50% in 0.2396 secs
  75% in 0.2578 secs
  90% in 0.2902 secs
  95% in 0.3093 secs
  99% in 0.4950 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0138 secs, 0.0048 secs, 0.0163 secs
  DNS-lookup:	0.0001 secs, 0.0000 secs, 0.0006 secs

Status code distribution:
  [200] 4023 responses
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
