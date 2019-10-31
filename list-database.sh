#!/bin/bash

$1

curl --header "Authorization: Bearer ${ACCESS_TOKEN}" -X GET https://www.googleapis.com/sql/v1beta4/projects/fine-justice-257413/instances

gcloud config set project fine-justice-257413


gcloud sql instances create [INSTANCE_NAME] --database-version=POSTGRES_9_6 \
       --cpu=[NUMBER_CPUS] --memory=[MEMORY_SIZE]

gcloud sql instances patch c2ws5l-development \
  --database-flags max_connections=150,\
  autovacuum=on,\
  work_mem=2621,\
  default_statistics_target=500,\
  random_page_cost=1.1,\
  checkpoint_completion_target=0.9

gcloud sql users set-password postgres no-host --instance=[INSTANCE_NAME] \
       --password=[PASSWORD]