import logging
from flask.templating import render_template
import requests
from flask import json, jsonify
from __init__ import app
from urllib.request import urlopen
import xmltodict

@app.route('/', methods = ['GET'])
def get_research_materials():
  uri = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=10'
  try:
    uResponse = xmltodict.parse(requests.get(uri).text)
  except requests.ConnectionError:
    return "Connection Error"  
  return uResponse

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """An internal error occurred: <pre>{}</pre>See logs for full stacktrace.""".format(e), 500

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]
