import requests
from PIL import Image
from google.cloud import bigquery

import os 
import pandas as pd 

def map_images(): 
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './bigquery-test-project-283805-f9190991acc2.json'
    client = bigquery.Client() 

    dataset = client.get_dataset('bigquery-public-data.geo_openstreetmap')
    tables = list(client.list_tables(dataset))
    print([table.table_id for table in tables])

    sql = """
    SELECT nodes.*
    FROM `bigquery-public-data.geo_openstreetmap.planet_nodes` AS nodes
    JOIN UNNEST(all_tags) AS tags
    WHERE tags.key = 'amenity'
    AND tags.value IN ('hospital',
        'clinic',
        'doctors')
    LIMIT 10
    """

    # Set up the query
    query_job = client.query(sql)

    # Make an API request  to run the query and return a pandas DataFrame
    df = query_job.to_dataframe()


    def google_maps_from_coords(lat, lon):
        return "https://maps.googleapis.com/maps/api/staticmap?center="+str(lat)+",+"+str(lon)+"&zoom=17&scale=1&size=600x300&maptype=satellite&format=png&visual_refresh=true"

    GOOGLE_MAPS_STATIC_API_KEY="AIzaSyD4Hwvz-wcXXa44NOZz-RAK3GBr6Zl-gBA"

    for _, row in df.iterrows():
        url = google_maps_from_coords(row['latitude'], row['longitude']) + "&key=" + GOOGLE_MAPS_STATIC_API_KEY
        req = requests.get(url, stream=True) 
        img = Image.open(req.raw)
        
        img.save(f"{row['latitude']}_{row['longitude']}.png")
