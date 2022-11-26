# FLASK Tutorial 1 -- We show the bare bones code to get an app up and running

# imports
import os                 # os is used to get environment variables IP & PORT
from flask import Flask   # Flask is the web app that we will customize
from flask import render_template
app = Flask(__name__)     # create an app

# @app.route is a decorator. It gives the function "index" special powers.
# In this case it makes it so anyone going to "your-url/" makes this function
# get called. What it returns is what is shown as the web page
@app.route('/')
@app.route('/index')
def index():
    a_user = {'name': 'Sashank', 'email': 'spyndi@uncc.edu'}
    tasks = {1:{'title': 'Create Task', 'description': 'User has to create task'}, 2: {'title': 'Edit task', 'description': 
    'User has to edit task'}}
    return render_template('dashboard.html', user=a_user, tasks=tasks)
@app.route('/index/<task_id>')
def viewTask(task_id):
    a_user = {'name': 'Sashank', 'email': 'spyndi@uncc.edu'}
    tasks = {1:{'title': 'First note', 'description': 'This is my first note'}, 2: {'title': 'Second note', 'description': 
    'This is my second note'}}
    return render_template('task.html', user=a_user,task=tasks[int(task_id)])

app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)



# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000

# Note that we are running with "debug=True", so if you make changes and save it
# the server will automatically update. This is great for development but is a
# security risk for production.