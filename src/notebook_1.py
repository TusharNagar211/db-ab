# Databricks notebook source
# setup_unity_catalog.py
# spark.sql(f"CREATE CATALOG IF NOT EXISTS {spark.conf.get('taskCatalog')}")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {spark.conf.get('taskCatalog')}.{spark.conf.get('taskSchema')}")