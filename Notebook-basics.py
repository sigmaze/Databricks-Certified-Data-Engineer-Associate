# Databricks notebook source
print("test")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC To jest Kolejna [czesc](url)
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT " Hello from sql"

# COMMAND ----------

_sqldf.show()

# COMMAND ----------

# MAGIC %run ./includes_dask/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %md
# MAGIC Filesystem [](url)

# COMMAND ----------

# MAGIC %fs ls 

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'
