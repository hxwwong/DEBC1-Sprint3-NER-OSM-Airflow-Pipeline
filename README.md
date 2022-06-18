# NER/OSM Data Pipeline with Apache Airflow & DAGs 
The data pipeline is catered to providing accesible, transformed, and normalized data for NLP/NER and Geospatial modelling data.

# Data Engineering Cohort 1
Sprint 3 Final Project 
Submitted by Hans Xavier Wong and Phoemela Ballaran 

# Setup 
After cloning/forking the repository, navigate to the airflow-local folder and run `docker compose up` to install the docker container locally. To open the Apache Airflow GUI, you can run https://localhost:8080 on your webrowser to view the accessible dags.

Within the scraper files, it is necessary for you to configure github secrets using a variables.json file, and set this manually during the Apache Airflow GUI.

Note that there are certain dags that are configured towards discord webhooks that may need to be modified or omitted. 

# Main use 
The relevant files are stored in the `dags` folder, with the `test_dag.py` containing a sample dag for testing. You can modify the name, and description of these dags by modifying the relevant strings in between the bash operators.

The main scrapers to be utilized are `scraper_dag.py` and `scraper_v2_dag.py`, which contain the main tasks and the runnable files. Street image.py is a sample script that obtains and stores the images of OSM, and is constructed for your reference. 

You can also increase the number of images / articles you scrape by modifying the `LIMIT` category in their respective queries.

The pipeline has five sets of tasks. It scrapes data from selected newspapers, transforms them by adding NER and word_count columns as a way to prepare the headlines/summaries for analysis, then uploads them to a GCS bucket defined by the credentials provided. Following this, the local copies of the data on your machine are wiped, minimizing redundancy and data costs every time the scraper DAG is run. 



# Challenges and Points for Improvement 
One of the main challenges here is ensuring data validation for our files. We focused more on ensuring that the ETL process was successful, as opposed to optimizing the data flow now. So we can work on ensuring the data we get is *normalized, possessing unique primary keys, and other pertinent features for creating a more robust and efficient data infrastructure. 

Second, we could work on optimizing our cleanup tasks. It's possible that bugs can occur when the pipeline prematurely deletes files that don't exist, which can occur when testing specific tasks or bugs that can crop up from other errors. We can fix this by timestamping the image files, and adding try-accpet catches for it.

Finally, I think we can work on making deploying this on the cloud. Our configuration is optimized mostly for developing them in the local machine, so learning how to configure the cloud VMs, the local docker files, and the github content can probably help when we want to scale up the use of this pipeline.


