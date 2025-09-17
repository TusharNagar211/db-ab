# Databricks notebook source
# setup_unity_catalog.py
spark.sql("CREATE CATALOG IF NOT EXISTS bronze_tbd MANAGED LOCATION 'abfss://unity-catalog-storage@dbstoragezwbsqsptedmwu.dfs.core.windows.net/4091704180100433'")
spark.sql("CREATE SCHEMA IF NOT EXISTS bronze_tbd.sap_ecc")
spark.sql("GRANT USE_CATALOG, USE_SCHEMA, APPLY_TAG ON CATALOG bronze_tbd TO `hemali.riaan@gmail.com`")

spark.sql("""
          CREATE TABLE IF NOT EXISTS bronze_tbd.sap_ecc.DD07L (
          DOMNAME STRING,
          VALPOS STRING,
          AS4VERS STRING)
        """)

spark.sql("CREATE EXTERNAL VOLUME bronze_tbd.sap_ecc.my_external_volume""")
