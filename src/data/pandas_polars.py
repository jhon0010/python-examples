import pandas as pd
import polars as pl
import time

csv_path = "resources/orders_2025_500.csv"

#######################
# ✅ Pandas Analysis
#######################

start = time.time()

csv = pd.read_csv(csv_path)

# 🔍 Quick profiling: check nulls & schema
print("🔍 Null values by column:")
print(csv.isnull().sum())

# 🧠 Convert to datetime first for accurate processing
csv["order_date"] = pd.to_datetime(csv["order_date"])

# ✨ Filter and aggregate
highvalue_pd = (
    csv[csv["order_total"] > 500]
    .assign(year=lambda d: d["order_date"].dt.year)
    .groupby("year")
    .agg(
        avg_total=("order_total", "mean"),
        order_count=("order_id", "count"),
        max_total=("order_total", "max")
    )
    .reset_index()
)

print("\n📊 Pandas summary:")
print(highvalue_pd)

end = time.time()
print(f"⏱️ Pandas time: {end - start:.4f} sec")

#######################
# ✅ Polars Analysis (Lazy)
#######################

start = time.time()

ldf = (
    pl.scan_csv(csv_path)
      .filter(pl.col("order_total") > 500)
      .with_columns([
          pl.col("order_date").str.slice(0, 4).cast(pl.Int32).alias("year")
      ])
      .group_by("year")
      .agg([
          pl.col("order_total").mean().alias("avg_total"),
          pl.count().alias("order_count"),
          pl.col("order_total").max().alias("max_total")
      ])
)

highvalue_pl = ldf.collect()

print("\n📊 Polars summary:")
print(highvalue_pl)

end = time.time()
print(f"⏱️ Polars time: {end - start:.4f} sec")
