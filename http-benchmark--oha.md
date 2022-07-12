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
  Total:	10.0066 secs
  Slowest:	0.4309 secs
  Fastest:	0.0613 secs
  Average:	0.0953 secs
  Requests/sec:	1039.8102

  Total data:	39.51 MiB
  Size/request:	3.89 KiB
  Size/sec:	3.95 MiB

Response time histogram:
  0.082 [3994] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.102 [3931] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.123 [1416] |■■■■■■■■■■■
  0.143 [327]  |■■
  0.163 [604]  |■■■■
  0.184 [33]   |
  0.204 [0]    |
  0.225 [0]    |
  0.245 [0]    |
  0.266 [0]    |
  0.286 [100]  |

Latency distribution:
  10% in 0.0733 secs
  25% in 0.0779 secs
  50% in 0.0846 secs
  75% in 0.1007 secs
  90% in 0.1239 secs
  95% in 0.1496 secs
  99% in 0.1773 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0502 secs, 0.0244 secs, 0.0590 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0008 secs

Status code distribution:
  [200] 10405 responses
```

### Benchmark 2: medium payload

```
➜  remix-python-benchmark git:(main) ✗ oha -z 10s -c 100 --http-version 1.1 http://localhost:3000/medium-json-payload
Summary:
  Success rate:	1.0000
  Total:	10.0039 secs
  Slowest:	0.2339 secs
  Fastest:	0.0747 secs
  Average:	0.0966 secs
  Requests/sec:	1026.3960

  Total data:	68.90 MiB
  Size/request:	6.87 KiB
  Size/sec:	6.89 MiB

Response time histogram:
  0.089 [5131] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.104 [2973] |■■■■■■■■■■■■■■■■■■
  0.118 [1044] |■■■■■■
  0.133 [333]  |■■
  0.147 [313]  |■
  0.162 [142]  |
  0.176 [219]  |■
  0.190 [10]   |
  0.205 [4]    |
  0.219 [40]   |
  0.234 [59]   |

Latency distribution:
  10% in 0.0807 secs
  25% in 0.0834 secs
  50% in 0.0892 secs
  75% in 0.1000 secs
  90% in 0.1193 secs
  95% in 0.1423 secs
  99% in 0.1925 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0448 secs, 0.0321 secs, 0.0575 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0001 secs

Status code distribution:
  [200] 10268 responses
```

### Benchmark 3: large payload

```
➜  remix-python-benchmark git:(main) ✗ oha -z 10s -c 100 --http-version 1.1 http://localhost:3000/large-json-payload
Summary:
  Success rate:	1.0000
  Total:	10.0041 secs
  Slowest:	0.3776 secs
  Fastest:	0.1770 secs
  Average:	0.2435 secs
  Requests/sec:	407.1342

  Total data:	66.25 MiB
  Size/request:	16.66 KiB
  Size/sec:	6.62 MiB

Response time histogram:
  0.195 [53]   |
  0.213 [232]  |■■■■
  0.232 [812]  |■■■■■■■■■■■■■■■
  0.250 [1707] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.268 [933]  |■■■■■■■■■■■■■■■■■
  0.286 [185]  |■■■
  0.305 [37]   |
  0.323 [74]   |■
  0.341 [11]   |
  0.359 [27]   |
  0.378 [2]    |

Latency distribution:
  10% in 0.2174 secs
  25% in 0.2302 secs
  50% in 0.2423 secs
  75% in 0.2549 secs
  90% in 0.2642 secs
  95% in 0.2701 secs
  99% in 0.3229 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0312 secs, 0.0054 secs, 0.0661 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0006 secs

Status code distribution:
  [200] 4073 responses
```

# Flask App Benchmarks

### Benchmark 1: small payload

```
➜  remix-python-benchmark git:(main) ✗ oha -z 10s -c 100 --http-version 1.1 http://127.0.0.1:5000/small-json-payload
Summary:
  Success rate:	1.0000
  Total:	10.0028 secs
  Slowest:	0.1631 secs
  Fastest:	0.0565 secs
  Average:	0.0763 secs
  Requests/sec:	1301.7324

  Total data:	239.76 MiB
  Size/request:	18.86 KiB
  Size/sec:	23.97 MiB

Response time histogram:
  0.066 [56]   |
  0.076 [7888] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.086 [4119] |■■■■■■■■■■■■■■■■
  0.095 [719]  |■■
  0.105 [197]  |
  0.115 [22]   |
  0.124 [15]   |
  0.134 [3]    |
  0.144 [1]    |
  0.153 [0]    |
  0.163 [1]    |

Latency distribution:
  10% in 0.0704 secs
  25% in 0.0719 secs
  50% in 0.0742 secs
  75% in 0.0799 secs
  90% in 0.0845 secs
  95% in 0.0870 secs
  99% in 0.0992 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0014 secs, 0.0003 secs, 0.0576 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0020 secs

Status code distribution:
  [200] 13021 responses
```

### Benchmark 2: medium payload

```
➜  remix-python-benchmark git:(main) ✗ oha -z 10s -c 100 --http-version 1.1 http://127.0.0.1:5000/medium-json-payload
Summary:
  Success rate:	1.0000
  Total:	10.0015 secs
  Slowest:	0.1561 secs
  Fastest:	0.0732 secs
  Average:	0.0953 secs
  Requests/sec:	1041.3401

  Total data:	458.98 MiB
  Size/request:	45.13 KiB
  Size/sec:	45.89 MiB

Response time histogram:
  0.081 [2]    |
  0.088 [151]  |
  0.096 [6672] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.103 [2674] |■■■■■■■■■■■■
  0.111 [629]  |■■■
  0.118 [176]  |
  0.126 [68]   |
  0.134 [23]   |
  0.141 [11]   |
  0.149 [7]    |
  0.156 [2]    |

Latency distribution:
  10% in 0.0899 secs
  25% in 0.0911 secs
  50% in 0.0932 secs
  75% in 0.0984 secs
  90% in 0.1028 secs
  95% in 0.1055 secs
  99% in 0.1189 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0014 secs, 0.0003 secs, 0.0536 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0025 secs

Status code distribution:
  [200] 10415 responses
```

### Benchmark 3: large payload

```
➜  remix-python-benchmark git:(main) ✗ oha -z 10s -c 100 --http-version 1.1 http://127.0.0.1:5000/large-json-payload
Summary:
  Success rate:	1.0000
  Total:	10.0020 secs
  Slowest:	0.4228 secs
  Fastest:	0.0691 secs
  Average:	0.2435 secs
  Requests/sec:	404.8172

  Total data:	840.92 MiB
  Size/request:	212.67 KiB
  Size/sec:	84.07 MiB

Response time histogram:
  0.101 [18]   |
  0.133 [39]   |
  0.166 [87]   |
  0.198 [128]  |■
  0.230 [125]  |■
  0.262 [3312] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.294 [130]  |■
  0.326 [98]   |
  0.358 [68]   |
  0.391 [29]   |
  0.423 [15]   |

Latency distribution:
  10% in 0.2310 secs
  25% in 0.2389 secs
  50% in 0.2441 secs
  75% in 0.2498 secs
  90% in 0.2590 secs
  95% in 0.2967 secs
  99% in 0.3608 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0030 secs, 0.0003 secs, 0.1734 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0027 secs

Status code distribution:
  [200] 4049 responses
```
