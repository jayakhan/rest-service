# Deploy a Flask API in Google Kubernetes Engine

## Steps required:
1. Create a requirements.txt for list of dependencies
2. Create an app.yaml for cloud resource configuration
3. Create a main.py file for returning a web content from arxiv repo in JSON response
4. Deploy it to cloud machine using Google App Engine using below commands in Cloud Shell
      ```
         git clone git@github.com:{username}/content-extract-v1.git
         pip install -r requirements.txt
         python main.py
         gcloud config set project {google-project-id}
         gcloud app deploy
      ```
      ```
         gcloud builds submit --tag gcr.io// --project=
         gcloud run deploy --image gcr.io// --platform managed --project= --allow-unauthenticated --region us-east1
         gcloud iam service-accounts list --project=
         gcloud iam service-accounts keys create ./keys.json --iam-account email@address
         gcloud auth activate-service-account --key-file=keys.json
