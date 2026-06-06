from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("Null Check") \
    .getOrCreate()

df = spark.read.csv(
    "data/raw_customer.csv",
    header=True,
    inferSchema=True
)

null_records = df.filter(
    col("name").isNull() |
    col("email").isNull()
)

print("Null Records Found:")
null_records.show()

spark.stop()
