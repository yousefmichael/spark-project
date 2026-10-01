from pyspark.sql import SparkSession
from pyspark_job import clean_data


spark = SparkSession.builder.appName("TestApp").getOrCreate()

def test_clean_data():
    # Create fake data covering all our test cases
    fake_data = [
        ("Alice", 100.0), 
        ("Bob", -50.0),  
        ("Charlie", 0.0),
        (None, 200.0)      
    ]
    columns = ["name", "amount"]
    
    df = spark.createDataFrame(fake_data, columns)
    
    #Run our cleaning function
    result_df = clean_data(df)
    
    # Bring the results back into a standard Python list so we can read it
    results = result_df.collect()
    
    # Use 'assert' to verify the results are exactly what we expect
    
    # Out of 4 rows, only 1 (Alice) should survive
    assert len(results) == 1 
    
    # Verify Alice's details are correct
    assert results[0]["name"] == "Alice"
    assert results[0]["amount"] == 100.0
    
    # Verify the math for the new column is correct (100 * 1.20 = 120.0)
    assert results[0]["amount_with_tax"] == 120.0