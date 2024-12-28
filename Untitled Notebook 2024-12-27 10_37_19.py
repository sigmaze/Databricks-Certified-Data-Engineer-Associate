# Databricks notebook source
df = spark.table("sigmaze_eastus_databricks.quiz.enrollments")

# COMMAND ----------

df.show()
