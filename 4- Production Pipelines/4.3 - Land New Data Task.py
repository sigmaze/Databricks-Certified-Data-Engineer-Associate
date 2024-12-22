# Databricks notebook source
# MAGIC %run ../Includes/Copy-Datasets

# COMMAND ----------

load_new_json_data()

# COMMAND ----------

# %sql
# SELECT * from json.`${dataset.bookstore}/books-cdc/02.json`
