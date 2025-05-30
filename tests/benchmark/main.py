# python3 tests/benchmark/main.py 
import pytest, sys
sys.exit(pytest.main([
    "tests/benchmark/test_benchmark_math.py",
    "--benchmark-only",  # optional
    "--benchmark-save=baseline",
    "--benchmark-compare",
    "-q"                 # quiet output
]))
