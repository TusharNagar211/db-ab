import os
import glob

# Path to your SQL files inside the repo
sql_folder = "1_Test"

# Run step1 first
with open(os.path.join(sql_folder, "test.sql"), "r") as f:
    query1 = f.read()
spark.sql(query1)

# Then run step2 and display results
with open(os.path.join(sql_folder, "test2.sql"), "r") as f:
    query2 = f.read()
df = spark.sql(query2)
df.show()
