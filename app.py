from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html") 

@app.route('/student/<int:student_id>')
def display_student(student_id):
	return	render_template("home.html", id=student_id)

@app.route('/student/<string:student_name>')
def moreinfo(student_name):
	student1 = query_by_name(student_name)
	return render_template("student.html", student=student1)

if __name__ == '__main__':
    app.run(debug=True)