# Databricks notebook source
# Create widgets to pass variables to SQL context
table_name = "students"
schema_name = "default"
dbutils.widgets.text("table_name", table_name)
dbutils.widgets.text("schema_name", schema_name)

%sql
spark.sql(f"SELECT * FROM {schema_name}.{table_name}"

# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC

# COMMAND ----------

df = spark.table(f"{schema_name}.{table_name}")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from df;
