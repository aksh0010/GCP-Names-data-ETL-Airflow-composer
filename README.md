# GCP-Twitter-data-ETL-composerflow

On Google Cloud Platform 

1) Create a Composer
   ![image](https://github.com/aksh0010/GCP-Names-data-ETL-Airflow-composer/assets/68304244/280d5fa1-5023-497b-8ed1-d119d741efe2)

2) Upload your Dataset on your preferred location on Google Cloud Bucket and copy the path
  ![image](https://github.com/aksh0010/GCP-Names-data-ETL-Airflow-composer/assets/68304244/9cf98544-32dd-4b9f-8580-66c9f76b95f0)

3) Create a Dataset on Bigquery ( you can ignore to create the table)
   
   ![image](https://github.com/aksh0010/GCP-Names-data-ETL-Airflow-composer/assets/68304244/fd40be75-d33c-4b8f-b0de-9faecdc7b800)

5) Upload your ETL.py and Dag.py on storage assigned to composer. Where to find the location is in below image
   ![image](https://github.com/aksh0010/GCP-Names-data-ETL-Airflow-composer/assets/68304244/c697e397-957d-45c9-8979-d56a9e5c2179)

  once you click the folder a Bucket will open up for dags, Upload your files there 
  ![image](https://github.com/aksh0010/GCP-Names-data-ETL-Airflow-composer/assets/68304244/d78ce77f-b547-475d-9acf-b9f8995a549b)

5) Once you upload your Files, click on airflow from composer console
   ![image](https://github.com/aksh0010/GCP-Names-data-ETL-Airflow-composer/assets/68304244/2e745daa-d8be-48db-9b5f-5007297333ea)

6) You shall see Airflow Dashboard, Wait for 3-5 mins and let airflow load your files
   ![image](https://github.com/aksh0010/GCP-Names-data-ETL-Airflow-composer/assets/68304244/c49a28a9-f794-409b-87c9-9a3eed07215b)

7) Now you can Track your progress.

## Note:
  - While transforming  the data, Make sure you clean your data well enough and see BigQuery syntax for tables. Sometimes when you don't handle Non-English characters, it wont allow you to write on Bigquery    
    table and throw errors.
  - Always check Datatypes before and after operation on google buckets for newly created files and existing ones. Newly created csv is converted into application/octet-stream in that case you have to change its     type like I did in the code ( data_etl.py)
