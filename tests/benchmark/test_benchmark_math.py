import math
import time
import pytest   # ← missing in your snippet

# function to benchmark
def compute_heavy_math(n: int) -> float:
    result = 0.0
    for i in range(1, n):
        result += math.sqrt(i) * math.log(i + 1)
    return result

@pytest.mark.benchmark(# pytest-benchmark marker
    group="math-group",
    min_time=0.1,
    max_time=5,
    min_rounds=500,
    timer=time.time,
    disable_gc=True,
    warmup=False
)
def test_compute_heavy_math_speed(benchmark):
    result = benchmark(compute_heavy_math, 100_000)
    print(result)                       # debug only
    assert result > 0                   # simple sanity check
