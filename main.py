# FLASK Tutorial 1 -- We show the bare bones code to get an app up and running

# imports
import os                 # os is used to get environment variables IP & PORT
from flask import Flask   # Flask is the web app that we will customize
from flask import render_template
from flask import request
from flask import redirect, url_for
from database import db
from models import Task as Task
from models import User as User
app = Flask(__name__)     # create an app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_task_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
# Bind SQLAlchemy db object to this Flask app
db.init_app(app)
# Setup models
with app.app_context():
    db.create_all()   # run under the app context
#tasks = {1:{'title': 'Create Task', 'description': 'User has to create task', 'status': 'backlog'}, 2: {'title': 'Edit Task', 'description': 
    #'User has to edit task', 'status': 'doing'},3:{'title': 'Delete Task', 'description': 'User has to create task' ,'status':'doing'}}
# @app.route is a decorator. It gives the function "index" special powers.
# In this case it makes it so anyone going to "your-url/" makes this function
# get called. What it returns is what is shown as the web page
@app.route('/')
@app.route('/index')
def index():
    a_user = db.session.query(User).filter_by(email='spyndi@uncc.edu').one()
    return render_template('index.html', user=a_user)
@app.route('/dashboard')
def viewTasks():
    a_user = db.session.query(User).filter_by(email='spyndi@uncc.edu').one()
    tasks = db.session.query(Task).all()
    return render_template('dashboard.html', user=a_user, tasks=tasks)
@app.route('/dashboard/<task_id>')
def viewTask(task_id):
  a_user =  db.session.query(User).filter_by(email='spyndi@uncc.edu').one()
  task = db.session.query(Task).filter_by(id=task_id).one()
  return render_template('task.html', user=a_user, task=task)
@app.route('/dashboard/new', methods=['GET', 'POST'])
def createTask():
 print('request method is', request.method)
 if request.method == 'POST':
    my_title = request.form['title']
    my_description = request.form['description']
    my_status = request.form['status']
    new_record = Task(my_title, my_description, my_status)
    db.session.add(new_record)
    db.session.commit()
    return redirect(url_for('viewTasks'))
 else:
    a_user = db.session.query(User).filter_by(email='spyndi@uncc.edu').one()
    return render_template('new.html', user=a_user)
app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)



# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000

# Note that we are running with "debug=True", so if you make changes and save it
# the server will automatically update. This is great for development but is a
# security risk for production.