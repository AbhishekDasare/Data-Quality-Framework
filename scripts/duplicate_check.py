from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Duplicate Check") \
    .getOrCreate()

df = spark.read.csv(
    "data/raw_customer.csv",
    header=True,
    inferSchema=True
)

duplicate_records = df.groupBy(
    "customer_id",
    "name",
    "email",
    "city"
).count().filter("count > 1")

print("Duplicate Records Found:")
duplicate_records.show()

spark.stop()
