from pyspark.sql import functions as F

def clean_data(df):
    # 1. Remove rows where amount <= 0 (keep only amount > 0)
    df = df.filter(F.col("amount") > 0)
    
    # 2. Remove rows where name is NULL
    df = df.filter(F.col("name").isNotNull())
    
    # 3. Add 'amount_with_tax' calculated as amount * 1.20
    df = df.withColumn("amount_with_tax", F.col("amount") * 1.20)
    
    return df