from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Data Quality Framework") \
    .getOrCreate()

df = spark.read.csv(
    "data/raw_customer.csv",
    header=True,
    inferSchema=True
)

clean_df = df.dropDuplicates()

clean_df = clean_df.na.drop()

clean_df.write.mode("overwrite").csv(
    "data/validated_customer.csv",
    header=True
)

print("Data Quality Checks Completed")

spark.stop()
