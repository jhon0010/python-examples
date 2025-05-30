import pandas as pd
import matplotlib.pyplot as plt

#######################
# ✅ Plot Results (Pandas-based for now)
#######################


# Load full order dataset
csv_path = "resources/orders_2025_500.csv"
df = pd.read_csv(csv_path)

# Convert date column
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

# Extract month (period is better for grouping)
df["month"] = df["order_date"].dt.to_period("M")

# Group by month
monthly_summary = (
    df.groupby("month")
      .agg(
          total_orders=("order_id", "count"),
          total_revenue=("order_total", "sum"),
          avg_order_value=("order_total", "mean")
      )
      .reset_index()
)

# Convert Period -> String for plotting
monthly_summary["month"] = monthly_summary["month"].astype(str)

# Show DataFrame
print("📊 Monthly Summary:")
print(monthly_summary)

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(monthly_summary["month"], monthly_summary["total_revenue"], label="Total Revenue", marker='o')
plt.plot(monthly_summary["month"], monthly_summary["avg_order_value"], label="Avg Order Value", marker='s', linestyle='--')
plt.plot(monthly_summary["month"], monthly_summary["total_orders"], label="Order Count", marker='^')

plt.title("📈 Orders Summary by Month (2025)")
plt.xlabel("Month")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()