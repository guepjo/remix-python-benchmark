# Machine Specifications

MacBook Pro: 2021
macOS version 12.4
Chip: Apple M1 Pro
Memory 32GB

# Remix App Benchmarks

### Benchmark 1: small payload

```
➜  ~ oha -n 30 -c 100 -q 10 --latency-correction --disable-keepalive http://localhost:3000/small-json-payload
Summary:
  Success rate:	1.0000
  Total:	2.9031 secs
  Slowest:	0.0477 secs
  Fastest:	0.0082 secs
  Average:	0.0318 secs
  Requests/sec:	10.3339

  Total data:	116.66 KiB
  Size/request:	3.89 KiB
  Size/sec:	40.18 KiB

Response time histogram:
  0.012 [2] |■■■■■■■■
  0.015 [0] |
  0.019 [0] |
  0.023 [3] |■■■■■■■■■■■■
  0.026 [0] |
  0.030 [3] |■■■■■■■■■■■■
  0.033 [8] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.037 [6] |■■■■■■■■■■■■■■■■■■■■■■■■
  0.041 [5] |■■■■■■■■■■■■■■■■■■■■
  0.044 [1] |■■■■
  0.048 [2] |■■■■■■■■

Latency distribution:
  10% in 0.0205 secs
  25% in 0.0277 secs
  50% in 0.0328 secs
  75% in 0.0371 secs
  90% in 0.0420 secs
  95% in 0.0472 secs
  99% in 0.0477 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0060 secs, 0.0022 secs, 0.0134 secs
  DNS-lookup:	0.0001 secs, 0.0000 secs, 0.0012 secs

Status code distribution:
  [200] 30 responses
```

### Benchmark 2: medium payload

```
➜  ~ oha -n 30 -c 100 -q 10 --latency-correction --disable-keepalive http://localhost:3000/medium-json-payload
Summary:
  Success rate:	1.0000
  Total:	2.9055 secs
  Slowest:	0.0467 secs
  Fastest:	0.0097 secs
  Average:	0.0335 secs
  Requests/sec:	10.3253

  Total data:	206.13 KiB
  Size/request:	6.87 KiB
  Size/sec:	70.95 KiB

Response time histogram:
  0.013 [2] |■■■■■■■
  0.016 [0] |
  0.020 [2] |■■■■■■■
  0.023 [1] |■■■
  0.027 [1] |■■■
  0.030 [1] |■■■
  0.033 [4] |■■■■■■■■■■■■■■
  0.037 [5] |■■■■■■■■■■■■■■■■■
  0.040 [9] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.043 [0] |
  0.047 [5] |■■■■■■■■■■■■■■■■■

Latency distribution:
  10% in 0.0185 secs
  25% in 0.0300 secs
  50% in 0.0354 secs
  75% in 0.0391 secs
  90% in 0.0458 secs
  95% in 0.0466 secs
  99% in 0.0467 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0075 secs, 0.0030 secs, 0.0141 secs
  DNS-lookup:	0.0001 secs, 0.0000 secs, 0.0003 secs

Status code distribution:
  [200] 30 responses
```

### Benchmark 3: large payload

```
➜  ~ oha -n 30 -c 100 -q 10 --latency-correction --disable-keepalive http://localhost:3000/large-json-payload
Summary:
  Success rate:	1.0000
  Total:	2.9041 secs
  Slowest:	0.0870 secs
  Fastest:	0.0142 secs
  Average:	0.0360 secs
  Requests/sec:	10.3302

  Total data:	499.69 KiB
  Size/request:	16.66 KiB
  Size/sec:	172.06 KiB

Response time histogram:
  0.021 [4] |■■■■■■■■■■■■■■■■■■
  0.027 [4] |■■■■■■■■■■■■■■■■■■
  0.034 [6] |■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.041 [7] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.047 [7] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.054 [0] |
  0.061 [0] |
  0.067 [0] |
  0.074 [0] |
  0.080 [0] |
  0.087 [2] |■■■■■■■■■

Latency distribution:
  10% in 0.0183 secs
  25% in 0.0266 secs
  50% in 0.0353 secs
  75% in 0.0417 secs
  90% in 0.0458 secs
  95% in 0.0855 secs
  99% in 0.0870 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0053 secs, 0.0027 secs, 0.0097 secs
  DNS-lookup:	0.0001 secs, 0.0000 secs, 0.0004 secs

Status code distribution:
  [200] 30 responses
```

# Flask App Benchmarks

### Benchmark 1: small payload

```
➜  ~ oha -n 30 -c 100 -q 10 --latency-correction --disable-keepalive http://127.0.0.1:5000/small-json-payload
Summary:
  Success rate:	1.0000
  Total:	2.9036 secs
  Slowest:	0.0214 secs
  Fastest:	0.0057 secs
  Average:	0.0145 secs
  Requests/sec:	10.3321

  Total data:	565.66 KiB
  Size/request:	18.86 KiB
  Size/sec:	194.82 KiB

Response time histogram:
  0.007 [2] |■■■■■■■■
  0.009 [2] |■■■■■■■■
  0.010 [1] |■■■■
  0.011 [1] |■■■■
  0.013 [1] |■■■■
  0.014 [3] |■■■■■■■■■■■■
  0.016 [6] |■■■■■■■■■■■■■■■■■■■■■■■■
  0.017 [8] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.019 [2] |■■■■■■■■
  0.020 [2] |■■■■■■■■
  0.021 [2] |■■■■■■■■

Latency distribution:
  10% in 0.0075 secs
  25% in 0.0128 secs
  50% in 0.0156 secs
  75% in 0.0166 secs
  90% in 0.0196 secs
  95% in 0.0200 secs
  99% in 0.0214 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0100 secs, 0.0038 secs, 0.0139 secs
  DNS-lookup:	0.0001 secs, 0.0000 secs, 0.0010 secs

Status code distribution:
  [200] 30 responses
```

### Benchmark 2: medium payload

```
➜  ~ oha -n 30 -c 100 -q 10 --latency-correction --disable-keepalive http://127.0.0.1:5000/medium-json-payload
Summary:
  Success rate:	1.0000
  Total:	2.9021 secs
  Slowest:	0.0234 secs
  Fastest:	0.0065 secs
  Average:	0.0164 secs
  Requests/sec:	10.3372

  Total data:	1.32 MiB
  Size/request:	45.13 KiB
  Size/sec:	466.48 KiB

Response time histogram:
  0.008 [2] |■■■■■■■
  0.010 [1] |■■■
  0.011 [0] |
  0.013 [2] |■■■■■■■
  0.014 [2] |■■■■■■■
  0.016 [1] |■■■
  0.017 [7] |■■■■■■■■■■■■■■■■■■■■■■■■
  0.019 [9] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.020 [4] |■■■■■■■■■■■■■■
  0.022 [1] |■■■
  0.023 [1] |■■■

Latency distribution:
  10% in 0.0126 secs
  25% in 0.0154 secs
  50% in 0.0177 secs
  75% in 0.0184 secs
  90% in 0.0199 secs
  95% in 0.0213 secs
  99% in 0.0234 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0101 secs, 0.0048 secs, 0.0153 secs
  DNS-lookup:	0.0001 secs, 0.0000 secs, 0.0002 secs

Status code distribution:
  [200] 30 responses
```

### Benchmark 3: large payload

```
➜  ~ oha -n 30 -c 100 -q 10 --latency-correction --disable-keepalive http://127.0.0.1:5000/large-json-payload
Summary:
  Success rate:	1.0000
  Total:	2.9038 secs
  Slowest:	0.0321 secs
  Fastest:	0.0091 secs
  Average:	0.0214 secs
  Requests/sec:	10.3315

  Total data:	6.23 MiB
  Size/request:	212.67 KiB
  Size/sec:	2.15 MiB

Response time histogram:
  0.011 [3] |■■■■■■■■■■■■
  0.013 [2] |■■■■■■■■
  0.015 [1] |■■■■
  0.017 [0] |
  0.020 [2] |■■■■■■■■
  0.022 [4] |■■■■■■■■■■■■■■■■
  0.024 [3] |■■■■■■■■■■■■
  0.026 [8] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.028 [6] |■■■■■■■■■■■■■■■■■■■■■■■■
  0.030 [0] |
  0.032 [1] |■■■■

Latency distribution:
  10% in 0.0114 secs
  25% in 0.0188 secs
  50% in 0.0239 secs
  75% in 0.0257 secs
  90% in 0.0272 secs
  95% in 0.0273 secs
  99% in 0.0321 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0094 secs, 0.0042 secs, 0.0133 secs
  DNS-lookup:	0.0001 secs, 0.0000 secs, 0.0012 secs

Status code distribution:
  [200] 30 responses
```
