import os
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'D:\\Git Repos\\aspirin\\big_query_tests\\demoprojectangel-c66d9a3cd5ea.json'

try:
    print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])
except:
    print("nope")

client = bigquery.Client()
QUERY = ('select url From `demo_dataset_angel_proba1.yahoo_test`')
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row.url)
