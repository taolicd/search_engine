from flask import Flask, render_template, request
from elasticsearch import Elasticsearch
import os
os.chdir('c:\\ELK\\')
app = Flask(__name__)
es = Elasticsearch('127.0.0.1', port=9200)

if __name__ == '_main__':
 app.run('127.0.0.1', debug=True)

@app.route('/')
def home():
 return render_template('search.html')

@app.route('/search/results', methods=['GET','POST'])
def request_search():
 search_term = request.form["input"]
 res = es.search(
 index='test',
 body={
 "query" : {"match": {"content": search_term}},
 "highlight" : {"pre_tags" : ["<b>"] , "post_tags" : ["</b>"], "fields" : {"content":{}}}})
 res['ST']=search_term

 for hit in res['hits']['hits']:
     hit['good_summary']='….'.join(hit['highlight']['content'][1:])
     return render_template('results.html', res=res)


