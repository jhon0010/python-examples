import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import csv
import io
from datetime import datetime

# ---- Helper to parse CSV lines into dicts ----
def parse_csv(line):
    # Header must match your file
    headers = [
        "order_id", "order_date", "customer_id", "product_id", "product_name",
        "quantity", "unit_price", "order_total", "payment_method",
        "shipping_country", "shipping_city", "status"
    ]
    # Handle weird formatting with csv reader
    reader = csv.reader(io.StringIO(line))
    fields = next(reader)
    return dict(zip(headers, fields))

# ---- Clean + Transform ----
def to_month_keyed_dict(order):
    try:
        order_total = float(order["order_total"])
        order_date = datetime.strptime(order["order_date"], "%Y-%m-%d")
        month = order_date.strftime("%Y-%m")
        return (month, order_total)
    except Exception as e:
        return ("invalid", 0.0)

# ---- Beam Pipeline ----
def run():
    options = PipelineOptions()
    with beam.Pipeline(options=options) as p:
        (
            p
            | "Read CSV File" >> beam.io.ReadFromText("resources/orders_2025_500.csv", skip_header_lines=1)
            | "Parse CSV" >> beam.Map(parse_csv)
            | "Filter High-Value Orders" >> beam.Filter(lambda d: float(d["order_total"]) > 500)
            | "Extract Month + Value" >> beam.Map(to_month_keyed_dict)
            | "Group by Month" >> beam.CombinePerKey(sum)
            | "Format Result" >> beam.Map(lambda kv: f"{kv[0]},{kv[1]:.2f}")
            | "Write Output" >> beam.io.WriteToText("resources/output/high_value_orders_by_month", file_name_suffix=".csv")
        )

if __name__ == "__main__":
    run()
