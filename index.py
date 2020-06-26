
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
students = [
    {
        'id' : 0,
        'name' : 'Donnukrit',
        'faculty' : 'Engineering',
        'register_subject' : [
            'Stat','Com Sec','OOP'
        ],
    },
    {
        'id' : 1,
        'name' : 'John',
        'faculty' : 'Engineering',
        'register_subject' : [
            'Client','Data Structure','OOP'
        ],
    },
    {
        'id' : 2,
        'name' : 'Jane',
        'faculty' : 'Engineering',
        'register_subject' : [
            'SDM','Web App','Intro Com'
        ],
    },
]

@app.route('/')
def index():
    return '<h1>This is FLASK Index.py</h1>'
@app.route('/api/students/')
def method_name():
    return jsonify(students)
@app.route('/api/students/<id>',methods=['GET'])
def getStudent(id) :
    sid = (int)(id)
    return jsonify(students[sid])
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
