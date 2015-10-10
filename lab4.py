import os, MySQLdb, urllib, urllib2, requests
from flask import Flask, jsonify, abort, make_response, request
from flask import render_template, json, url_for
app = Flask(__name__, static_url_path='/static')

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
	return jsonify(result="THis function would Get Server Results")

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
	task = [task for task in tasks if task['id'] == task_id]
	if len(task) == 0:
		abort(404)
	return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/post', methods=['POST'])
def create_task():
	if not request.json or not 'title' in request.json:
		abort(400)
	return jsonify(result="This function would POST Entry Results"), 201

@app.route('/todo/api/v1.0/tasks/put/<int:task_id>', methods=['PUT'])
def put_task(task_id):
	return jsonify(result="This function would PUT Entry Results")

@app.route('/todo/api/v1.0/tasks/delete', methods=['GET'])
def delete_task():
	return jsonify(result="This function would Delete Entry Results"), 201


@app.route('/nyt/api/search', methods=['GET'])
def get_result():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, "static/data", "result.json")
	data = json.load(open(json_url))
	return jsonify(result="This function would return search results", response=data), 201

@app.route('/nyt/search/<data>', methods=['GET'])
def get_results(data):
	url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q=" + data + "&api-key=16544f21c00fca2a33169b99b96a4668%3A16%3A72957421"
	data = requests.get(url).json()
	return jsonify(result="This function would return search results", response=data), 201 

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def hello_world():
	# db = MySQLdb.connect(host="dursley.socs.uoguelph.ca", # our host, do not modify
	# 				user="vyong", # your username (same as in lab)
	# 				passwd="0744993", # your password (your student id number)
	# 				db="vyong") # name of the data base, your username, do not modify
	# cur = db.cursor()
	# CREATE TABLE results(ID INT NOT NULL AUTO_INCREMENT,searchText TEXT, resultsJSON text, PRIMARY KEY (ID));
	# INSERT INTO results(searchText, resultsJSON) VALUES ('hello', 'db noticed hello keyword and it should return this');
	# INSERT INTO results(searchText, resultsJSON) VALUES ('testing', 'db noticed testing keyword and it should return this');
	return render_template('index.html')

# @app.route('/_add_numbers')
# def add_numbers():
#     a = request.args.get('a', 0, type=int)
#     b = request.args.get('b', 0, type=int)
#     return jsonify(result=a + b)

if __name__ == '__main__':
	app.run(debug=True)
