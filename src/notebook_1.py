# Databricks notebook source
# setup_unity_catalog.py
spark.sql("CREATE CATALOG IF NOT EXISTS bronze_tbd MANAGED LOCATION 'abfss://unity-catalog-storage@dbstoragezwbsqsptedmwu.dfs.core.windows.net/4091704180100433'")
spark.sql("CREATE SCHEMA IF NOT EXISTS bronze_tbd.my_schema")

spark.sql("GRANT USE_CATALOG, USE_SCHEMA, APPLY_TAG ON CATALOG bronze_tbd TO `hemali.riaan@gmail.com`")
