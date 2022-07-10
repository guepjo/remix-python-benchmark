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

Stat │ 2.5% │ 50% │ 97.5% │ 99% │ Avg │ Stdev │ Max

Latency │ 869 ms │ 13776 ms │ 26444 ms │ 26816 ms │ 13698.86 ms │ 7762.64 ms │ 27193 ms

---

Stat │ 1% │ 2.5% │ 50% │ 97.5% │ Avg │ Stdev │ Min

Req/Sec │ 1306 │ 1306 │ 1737 │ 1808 │ 1720.24 │ 92.35 │ 1306

Bytes/Sec │ 583 kB │ 583 kB │ 775 kB │ 806 kB │ 767 kB │ 41.2 kB │ 582 kB

### Benchmark 2: large payload

Stat │ 2.5% │ 50% │ 97.5% │ 99% │ Avg │ Stdev │ Max

Latency │ 858 ms │ 13636 ms │ 26357 ms │ 26733 ms │ 13635.34 ms │ 7716 ms │ 27110 ms

---

Stat │ 1% │ 2.5% │ 50% │ 97.5% │ Avg │ Stdev │ Min

eq/Sec │ 1342 │ 1342 │ 1729 │ 1786 │ 1716.64 │ 83.18 │ 1342

Bytes/Sec │ 1.61 MB │ 1.61 MB │ 2.07 MB │ 2.14 MB │ 2.05 MB │ 99.6 kB │ 1.61 MB
