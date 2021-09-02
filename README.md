# Hello World microservice with Flask API
## Steps required:
1. Create a requirements.txt for list of dependencies
2. Create an app.yaml for cloud resource configuration
3. Create a main.py file for returning a basic Hello World JSON response
4. Deploy it to cloud machine using Google App Engine using below commands in Cloud Shell
   a. git clone git@github.com:{username}/content-extract-v1.git
   b. pip install -r requirements.txt
   c. python main.py
   d. gcloud config set project {google-project-id}
   e. gcloud app deploy
