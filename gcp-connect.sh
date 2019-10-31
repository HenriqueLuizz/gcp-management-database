#!/bin/bash

apt-get update && apt-get install curl gnupg2 -y && export CLOUD_SDK_REPO="cloud-sdk-bionic" && echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && apt-get update -y && apt-get install google-cloud-sdk -y

gcloud auth activate-service-account --key-file /smarterp/fine-justice-257413-afff1ee60996.json

export GOOGLE_APPLICATION_CREDENTIALS="/smarterp/fine-justice-257413-afff1ee60996.json"

ACCESS_TOKEN="$(gcloud auth application-default print-access-token)"