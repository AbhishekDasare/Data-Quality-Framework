from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Schema Validation") \
    .getOrCreate()

df = spark.read.csv(
    "data/raw_customer.csv",
    header=True,
    inferSchema=True
)

print("Dataset Schema:")
df.printSchema()

spark.stop()
