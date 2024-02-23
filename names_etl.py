# This script defines a custom Python function for ETL (Extract, Transform, Load) process.
# It reads data from a CSV file stored in Google Cloud Storage (GCS), performs data cleaning,
# and then saves the cleaned data back to GCS.

import csv
import pandas as pd 
import re
from google.cloud import storage

def extract_transform_load():
    # Read data from the CSV file in GCS
    data = pd.read_csv("gs://etl-with-composerflow/data_files/data.csv")
    
    # Select only the columns needed
    data = data[["Name", "Gender", "Count"]]
    
    # Remove null values
    data.dropna(inplace=True)
    
    # Remove duplicates
    data.drop_duplicates(inplace=True)
    
    # Define a regular expression pattern to match non-English letters
    non_english_pattern = re.compile(r'[^a-zA-Z\s]', re.UNICODE)
    
    # Clean each string column using the pattern
    cleaned_data = data.map(lambda x: non_english_pattern.sub(',', str(x)))
    
    # Print the first 3 rows and columns of cleaned data (for debugging)
    print(cleaned_data.head(3))
    print(cleaned_data.columns)
    
    # Save the cleaned DataFrame to a new CSV file on Google Cloud Storage
    cleaned_data.to_csv("gs://etl-with-composerflow/data_files/new_data.csv", index=False, header=True, sep=',', encoding='utf-8', quoting=csv.QUOTE_ALL)
    
    # Change content type from application/octet-stream to text/plain for compatibility with GCS API
    storage_client = storage.Client()
    bucket = storage_client.bucket("etl-with-composerflow")
    blob = bucket.blob("data_files/new_data.csv")

    # Set the Content-Type metadata
    blob.content_type = "text/csv"
    blob.patch()
