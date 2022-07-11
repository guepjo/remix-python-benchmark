## Remix App Benchmarks

### Benchmark 1: small payload

Stat │ 2.5% │ 50% │ 97.5% │ 99% │ Avg │ Stdev │ Max │

Latency │ 144 ms │ 476 ms │ 768 ms │ 907 ms │ 449.14 ms │ 141 ms │ 1143 ms │

---

Stat │ 1% │ 2.5% │ 50% │ 97.5% │ Avg │ Stdev │ Min │

Req/Sec │ 856 │ 856 │ 2277 │ 2561 │ 2215.74 │ 332.22 │ 856 │

Bytes/Sec │ 438 kB │ 438 kB │ 1.16 MB │ 1.31 MB │ 1.13 MB │ 170 kB │ 437 kB │

### Benchmark 2: large payload

Stat │ 2.5% │ 50% │ 97.5% │ 99% │ Avg │ Stdev │ Max │

Latency │ 157 ms │ 429 ms │ 709 ms │ 828 ms │ 432.68 ms │ 179.43 ms │ 954 ms │

---

Stat │ 1% │ 2.5% │ 50% │ 97.5% │ Avg │ Stdev │ Min │

Req/Sec │ 1134 │ 1134 │ 2377 │ 2777 │ 2300.87 │ 336.83 │ 1134 │

Bytes/Sec │ 1.42 MB │ 1.42 MB │ 2.98 MB │ 3.48 MB │ 2.88 MB │ 422 kB │ 1.42 MB │

## Flask App Benchmarks

### Benchmark 1: small payload

```
➜  remix-python-benchmark git:(main) autocannon -c 100 -d 30 -p 10 http://127.0.0.1:5000/small-json-payload
Running 30s test @ http://127.0.0.1:5000/small-json-payload
100 connections with 10 pipelining factor


┌─────────┬────────┬──────────┬──────────┬──────────┬─────────────┬────────────┬──────────┐
│ Stat    │ 2.5%   │ 50%      │ 97.5%    │ 99%      │ Avg         │ Stdev      │ Max      │
├─────────┼────────┼──────────┼──────────┼──────────┼─────────────┼────────────┼──────────┤
│ Latency │ 802 ms │ 13870 ms │ 26484 ms │ 26854 ms │ 13797.32 ms │ 7723.85 ms │ 27210 ms │
└─────────┴────────┴──────────┴──────────┴──────────┴─────────────┴────────────┴──────────┘
┌───────────┬────────┬────────┬────────┬────────┬────────┬─────────┬────────┐
│ Stat      │ 1%     │ 2.5%   │ 50%    │ 97.5%  │ Avg    │ Stdev   │ Min    │
├───────────┼────────┼────────┼────────┼────────┼────────┼─────────┼────────┤
│ Req/Sec   │ 1481   │ 1481   │ 1742   │ 1843   │ 1712.1 │ 85.01   │ 1481   │
├───────────┼────────┼────────┼────────┼────────┼────────┼─────────┼────────┤
│ Bytes/Sec │ 661 kB │ 661 kB │ 777 kB │ 822 kB │ 764 kB │ 37.9 kB │ 661 kB │
└───────────┴────────┴────────┴────────┴────────┴────────┴─────────┴────────┘

Req/Bytes counts sampled once per second.
# of samples: 30

566k requests in 30.2s, 22.9 MB read
41k errors (0 timeouts)
```

### Benchmark 2: large payload

Stat │ 2.5% │ 50% │ 97.5% │ 99% │ Avg │ Stdev │ Max

Latency │ 858 ms │ 13636 ms │ 26357 ms │ 26733 ms │ 13635.34 ms │ 7716 ms │ 27110 ms

---

Stat │ 1% │ 2.5% │ 50% │ 97.5% │ Avg │ Stdev │ Min

eq/Sec │ 1342 │ 1342 │ 1729 │ 1786 │ 1716.64 │ 83.18 │ 1342

Bytes/Sec │ 1.61 MB │ 1.61 MB │ 2.07 MB │ 2.14 MB │ 2.05 MB │ 99.6 kB │ 1.61 MB
