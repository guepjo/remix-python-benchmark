# Machine Specifications

MacBook Pro: 2021
macOS version 12.4
Chip: Apple M1 Pro
Memory 32GB

# Remix App Benchmarks

### Benchmark 1: small payload

```
➜  remix-python-benchmark git:(main) ✗ oha -n 30 -c 100 http://localhost:3000/small-json-payload
Summary:
  Success rate:	1.0000
  Total:	0.1379 secs
  Slowest:	0.1354 secs
  Fastest:	0.0796 secs
  Average:	0.1116 secs
  Requests/sec:	217.5760

  Total data:	116.66 KiB
  Size/request:	3.89 KiB
  Size/sec:	846.08 KiB

Response time histogram:
  0.085 [1] |■■■■
  0.090 [2] |■■■■■■■■
  0.095 [0] |
  0.100 [4] |■■■■■■■■■■■■■■■■
  0.105 [2] |■■■■■■■■
  0.110 [3] |■■■■■■■■■■■■
  0.115 [4] |■■■■■■■■■■■■■■■■
  0.120 [8] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.125 [1] |■■■■
  0.130 [0] |
  0.135 [5] |■■■■■■■■■■■■■■■■■■■■

Latency distribution:
  10% in 0.0955 secs
  25% in 0.1016 secs
  50% in 0.1123 secs
  75% in 0.1184 secs
  90% in 0.1346 secs
  95% in 0.1349 secs
  99% in 0.1354 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0316 secs, 0.0034 secs, 0.0540 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0000 secs

Status code distribution:
  [200] 30 responses
```

### Benchmark 2: medium payload

```
➜  remix-python-benchmark git:(main) ✗ oha -n 30 -c 100 http://localhost:3000/medium-json-payload
Summary:
  Success rate:	1.0000
  Total:	0.1446 secs
  Slowest:	0.1380 secs
  Fastest:	0.1331 secs
  Average:	0.1354 secs
  Requests/sec:	207.4149

  Total data:	206.13 KiB
  Size/request:	6.87 KiB
  Size/sec:	1.39 MiB

Response time histogram:
  0.134 [1] |■■■■
  0.134 [0] |
  0.134 [0] |
  0.135 [5] |■■■■■■■■■■■■■■■■■■■■
  0.135 [8] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.136 [7] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.136 [5] |■■■■■■■■■■■■■■■■■■■■
  0.137 [2] |■■■■■■■■
  0.137 [1] |■■■■
  0.138 [0] |
  0.138 [1] |■■■■

Latency distribution:
  10% in 0.1346 secs
  25% in 0.1350 secs
  50% in 0.1353 secs
  75% in 0.1359 secs
  90% in 0.1366 secs
  95% in 0.1366 secs
  99% in 0.1380 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0290 secs, 0.0044 secs, 0.0329 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0002 secs

Status code distribution:
  [200] 30 responses
```

### Benchmark 3: large payload

```
➜  remix-python-benchmark git:(main) oha -n 30 -c 100 http://localhost:3000/large-json-payload
Summary:
  Success rate:	1.0000
  Total:	0.1910 secs
  Slowest:	0.1861 secs
  Fastest:	0.1437 secs
  Average:	0.1661 secs
  Requests/sec:	157.0332

  Total data:	499.69 KiB
  Size/request:	16.66 KiB
  Size/sec:	2.55 MiB

Response time histogram:
  0.148 [4] |■■■■■■■■■■■■■■■■
  0.151 [4] |■■■■■■■■■■■■■■■■
  0.155 [0] |
  0.159 [1] |■■■■
  0.163 [2] |■■■■■■■■
  0.167 [1] |■■■■
  0.171 [2] |■■■■■■■■
  0.175 [8] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.178 [3] |■■■■■■■■■■■■
  0.182 [1] |■■■■
  0.186 [4] |■■■■■■■■■■■■■■■■

Latency distribution:
  10% in 0.1471 secs
  25% in 0.1508 secs
  50% in 0.1711 secs
  75% in 0.1754 secs
  90% in 0.1848 secs
  95% in 0.1854 secs
  99% in 0.1861 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0290 secs, 0.0080 secs, 0.0485 secs
  DNS-lookup:	0.0001 secs, 0.0000 secs, 0.0024 secs

Status code distribution:
  [200] 30 responses
```

# Flask App Benchmarks

### Benchmark 1: small payload

➜ remix-python-benchmark git:(main) oha -n 30 -c 100 http://127.0.0.1:5000/small-json-payload
Summary:
Success rate: 1.0000
Total: 0.1009 secs
Slowest: 0.0848 secs
Fastest: 0.0509 secs
Average: 0.0690 secs
Requests/sec: 297.3757

Total data: 565.66 KiB
Size/request: 18.86 KiB
Size/sec: 5.48 MiB

Response time histogram:
0.054 [3] |■■■■■■■■■■■■■■■■■■■
0.057 [1] |■■■■■■
0.060 [1] |■■■■■■
0.063 [4] |■■■■■■■■■■■■■■■■■■■■■■■■■
0.066 [1] |■■■■■■
0.069 [3] |■■■■■■■■■■■■■■■■■■■
0.073 [5] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
0.076 [4] |■■■■■■■■■■■■■■■■■■■■■■■■■
0.079 [4] |■■■■■■■■■■■■■■■■■■■■■■■■■
0.082 [2] |■■■■■■■■■■■■
0.085 [2] |■■■■■■■■■■■■

Latency distribution:
10% in 0.0567 secs
25% in 0.0623 secs
50% in 0.0701 secs
75% in 0.0759 secs
90% in 0.0790 secs
95% in 0.0837 secs
99% in 0.0848 secs

Details (average, fastest, slowest):
DNS+dialup: 0.0306 secs, 0.0103 secs, 0.0427 secs
DNS-lookup: 0.0000 secs, 0.0000 secs, 0.0001 secs

Status code distribution:
[200] 30 responses

```

### Benchmark 2: medium payload

```

➜ remix-python-benchmark git:(main) oha -n 30 -c 100 http://127.0.0.1:5000/medium-json-payload
Summary:
Success rate: 1.0000
Total: 0.1011 secs
Slowest: 0.0863 secs
Fastest: 0.0448 secs
Average: 0.0681 secs
Requests/sec: 296.6091

Total data: 1.32 MiB
Size/request: 45.13 KiB
Size/sec: 13.07 MiB

Response time histogram:
0.049 [1] |■■■■
0.052 [0] |
0.056 [5] |■■■■■■■■■■■■■■■■■■■■■■
0.060 [2] |■■■■■■■■■
0.064 [0] |
0.067 [6] |■■■■■■■■■■■■■■■■■■■■■■■■■■■
0.071 [2] |■■■■■■■■■
0.075 [7] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
0.079 [2] |■■■■■■■■■
0.082 [3] |■■■■■■■■■■■■■
0.086 [2] |■■■■■■■■■

Latency distribution:
10% in 0.0541 secs
25% in 0.0591 secs
50% in 0.0702 secs
75% in 0.0747 secs
90% in 0.0805 secs
95% in 0.0849 secs
99% in 0.0863 secs

Details (average, fastest, slowest):
DNS+dialup: 0.0366 secs, 0.0075 secs, 0.0486 secs
DNS-lookup: 0.0000 secs, 0.0000 secs, 0.0001 secs

Status code distribution:
[200] 30 responses

```

### Benchmark 3: large payload

```

➜ remix-python-benchmark git:(main) oha -n 30 -c 100 http://127.0.0.1:5000/large-json-payload
Summary:
Success rate: 1.0000
Total: 0.1474 secs
Slowest: 0.1293 secs
Fastest: 0.0628 secs
Average: 0.1091 secs
Requests/sec: 203.5419

Total data: 6.23 MiB
Size/request: 212.67 KiB
Size/sec: 42.27 MiB

Response time histogram:
0.069 [1] |■■■■
0.075 [0] |
0.081 [0] |
0.087 [0] |
0.093 [2] |■■■■■■■■■
0.099 [4] |■■■■■■■■■■■■■■■■■■
0.105 [4] |■■■■■■■■■■■■■■■■■■
0.111 [2] |■■■■■■■■■
0.117 [7] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
0.123 [6] |■■■■■■■■■■■■■■■■■■■■■■■■■■■
0.129 [4] |■■■■■■■■■■■■■■■■■■

Latency distribution:
10% in 0.0933 secs
25% in 0.0991 secs
50% in 0.1131 secs
75% in 0.1193 secs
90% in 0.1258 secs
95% in 0.1289 secs
99% in 0.1293 secs

Details (average, fastest, slowest):
DNS+dialup: 0.0273 secs, 0.0031 secs, 0.0485 secs
DNS-lookup: 0.0000 secs, 0.0000 secs, 0.0005 secs

Status code distribution:
[200] 30 responses

```

```
