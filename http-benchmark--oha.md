# Machine Specifications

MacBook Pro: 2021
macOS version 12.4
Chip: Apple M1 Pro
Memory 32GB

# Remix App Benchmarks

### Benchmark 1: small payload

```
➜  remix-python-benchmark git:(main) oha -n 30 -c 100 --http-version 1.1 http://localhost:3000/small-json-payload
Summary:
  Success rate:	1.0000
  Total:	0.0988 secs
  Slowest:	0.0963 secs
  Fastest:	0.0591 secs
  Average:	0.0743 secs
  Requests/sec:	303.5724

  Total data:	116.66 KiB
  Size/request:	3.89 KiB
  Size/sec:	1.15 MiB

Response time histogram:
  0.062 [2]  |■■■■
  0.066 [0]  |
  0.069 [1]  |■■
  0.073 [15] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.076 [6]  |■■■■■■■■■■■■
  0.079 [1]  |■■
  0.083 [1]  |■■
  0.086 [0]  |
  0.090 [2]  |■■■■
  0.093 [0]  |
  0.096 [2]  |■■■■

Latency distribution:
  10% in 0.0696 secs
  25% in 0.0697 secs
  50% in 0.0720 secs
  75% in 0.0755 secs
  90% in 0.0890 secs
  95% in 0.0961 secs
  99% in 0.0963 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0305 secs, 0.0068 secs, 0.0556 secs
  DNS-lookup:	0.0001 secs, 0.0000 secs, 0.0009 secs

Status code distribution:
  [200] 30 responses
```

### Benchmark 2: medium payload

```
➜  remix-python-benchmark git:(main) oha -n 30 -c 100 --http-version 1.1 http://localhost:3000/medium-json-payload
Summary:
  Success rate:	1.0000
  Total:	0.0968 secs
  Slowest:	0.0917 secs
  Fastest:	0.0476 secs
  Average:	0.0794 secs
  Requests/sec:	309.7688

  Total data:	206.13 KiB
  Size/request:	6.87 KiB
  Size/sec:	2.08 MiB

Response time histogram:
  0.052 [3]  |■■■■
  0.056 [0]  |
  0.060 [0]  |
  0.064 [0]  |
  0.068 [0]  |
  0.072 [0]  |
  0.076 [0]  |
  0.080 [0]  |
  0.084 [24] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.088 [1]  |■
  0.092 [2]  |■■

Latency distribution:
  10% in 0.0811 secs
  25% in 0.0815 secs
  50% in 0.0821 secs
  75% in 0.0827 secs
  90% in 0.0841 secs
  95% in 0.0917 secs
  99% in 0.0917 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0288 secs, 0.0036 secs, 0.0423 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0001 secs

Status code distribution:
  [200] 30 responses
```

### Benchmark 3: large payload

```
➜  remix-python-benchmark git:(main) ✗ oha -n 30 -c 100 --http-version 1.1 http://localhost:3000/large-json-payload
Summary:
  Success rate:	1.0000
  Total:	0.1564 secs
  Slowest:	0.1545 secs
  Fastest:	0.1511 secs
  Average:	0.1532 secs
  Requests/sec:	191.7598

  Total data:	499.69 KiB
  Size/request:	16.66 KiB
  Size/sec:	3.12 MiB

Response time histogram:
  0.151 [2] |■■■■■■■■
  0.152 [0] |
  0.152 [1] |■■■■
  0.152 [6] |■■■■■■■■■■■■■■■■■■■■■■■■
  0.153 [1] |■■■■
  0.153 [0] |
  0.153 [1] |■■■■
  0.154 [3] |■■■■■■■■■■■■
  0.154 [8] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.154 [3] |■■■■■■■■■■■■
  0.154 [5] |■■■■■■■■■■■■■■■■■■■■

Latency distribution:
  10% in 0.1521 secs
  25% in 0.1523 secs
  50% in 0.1537 secs
  75% in 0.1539 secs
  90% in 0.1543 secs
  95% in 0.1543 secs
  99% in 0.1545 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0311 secs, 0.0206 secs, 0.0335 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0001 secs

Status code distribution:
  [200] 30 responses
```

# Flask App Benchmarks

### Benchmark 1: small payload

```
➜  remix-python-benchmark git:(main) ✗ oha -n 30 -c 100 --http-version 1.1 http://127.0.0.1:5000/small-json-payload
Summary:
  Success rate:	1.0000
  Total:	0.0728 secs
  Slowest:	0.0632 secs
  Fastest:	0.0341 secs
  Average:	0.0476 secs
  Requests/sec:	412.0316

  Total data:	565.66 KiB
  Size/request:	18.86 KiB
  Size/sec:	7.59 MiB

Response time histogram:
  0.037 [1] |■■■■■
  0.039 [2] |■■■■■■■■■■
  0.042 [2] |■■■■■■■■■■
  0.045 [6] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.047 [6] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.050 [3] |■■■■■■■■■■■■■■■■
  0.053 [4] |■■■■■■■■■■■■■■■■■■■■■
  0.055 [2] |■■■■■■■■■■
  0.058 [1] |■■■■■
  0.061 [2] |■■■■■■■■■■
  0.063 [1] |■■■■■

Latency distribution:
  10% in 0.0414 secs
  25% in 0.0433 secs
  50% in 0.0465 secs
  75% in 0.0516 secs
  90% in 0.0586 secs
  95% in 0.0586 secs
  99% in 0.0632 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0249 secs, 0.0077 secs, 0.0427 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0003 secs

Status code distribution:
  [200] 30 responses
```

### Benchmark 2: medium payload

```
➜  remix-python-benchmark git:(main) ✗ oha -n 30 -c 100 --http-version 1.1 http://127.0.0.1:5000/medium-json-payload
Summary:
  Success rate:	1.0000
  Total:	0.1003 secs
  Slowest:	0.0820 secs
  Fastest:	0.0544 secs
  Average:	0.0687 secs
  Requests/sec:	299.0176

  Total data:	1.32 MiB
  Size/request:	45.13 KiB
  Size/sec:	13.18 MiB

Response time histogram:
  0.057 [3] |■■■■■■■■■■■■■■■■
  0.059 [4] |■■■■■■■■■■■■■■■■■■■■■
  0.062 [0] |
  0.064 [2] |■■■■■■■■■■
  0.067 [3] |■■■■■■■■■■■■■■■■
  0.069 [2] |■■■■■■■■■■
  0.072 [6] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.074 [1] |■■■■■
  0.077 [3] |■■■■■■■■■■■■■■■■
  0.080 [3] |■■■■■■■■■■■■■■■■
  0.082 [3] |■■■■■■■■■■■■■■■■

Latency distribution:
  10% in 0.0573 secs
  25% in 0.0627 secs
  50% in 0.0706 secs
  75% in 0.0754 secs
  90% in 0.0796 secs
  95% in 0.0808 secs
  99% in 0.0820 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0336 secs, 0.0054 secs, 0.0514 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0001 secs

Status code distribution:
  [200] 30 responses
```

### Benchmark 3: large payload

```
➜  remix-python-benchmark git:(main) ✗ oha -n 30 -c 100 --http-version 1.1 http://127.0.0.1:5000/large-json-payload
Summary:
  Success rate:	1.0000
  Total:	0.1643 secs
  Slowest:	0.1514 secs
  Fastest:	0.0648 secs
  Average:	0.1158 secs
  Requests/sec:	182.6238

  Total data:	6.23 MiB
  Size/request:	212.67 KiB
  Size/sec:	37.93 MiB

Response time histogram:
  0.073 [2] |■■■■■■■■■■■■
  0.081 [1] |■■■■■■
  0.088 [1] |■■■■■■
  0.096 [4] |■■■■■■■■■■■■■■■■■■■■■■■■■
  0.104 [2] |■■■■■■■■■■■■
  0.112 [3] |■■■■■■■■■■■■■■■■■■■
  0.120 [2] |■■■■■■■■■■■■
  0.128 [4] |■■■■■■■■■■■■■■■■■■■■■■■■■
  0.136 [2] |■■■■■■■■■■■■
  0.144 [4] |■■■■■■■■■■■■■■■■■■■■■■■■■
  0.151 [5] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Latency distribution:
  10% in 0.0845 secs
  25% in 0.0939 secs
  50% in 0.1228 secs
  75% in 0.1378 secs
  90% in 0.1475 secs
  95% in 0.1510 secs
  99% in 0.1514 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0359 secs, 0.0134 secs, 0.0383 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0001 secs

Status code distribution:
  [200] 30 responses
```
