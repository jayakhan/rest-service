import logging
import requests
import xmltodict
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def get_research_materials():
  search_word = request.args.get('search_query')
  uri = 'http://export.arxiv.org/api/query?search_query=all:{}&start=0&max_results=10'.format(search_word)
  try:
    json = xmltodict.parse(requests.get(uri).text)
  except requests.ConnectionError:
    return "Connection Error"  
  return json

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during calling a request.')
    return """An internal error occurred: <pre>{}</pre>See logs for full stacktrace.""".format(e), 500

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    #app.run(host='127.0.0.1', port=8080, debug=True)
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))