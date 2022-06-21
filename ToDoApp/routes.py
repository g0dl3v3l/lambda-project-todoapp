from ToDoApp import app , db
from flask import render_template, url_for, flash, redirect ,request
from ToDoApp.models import Taskdata
from ToDoApp.forms import EditForm



db.create_all()

@app.route("/")
def home():
    posts = Taskdata.query.all()
    return  render_template('post.html' ,display = posts)




@app.route("/" , methods =['POST', 'GET'])
def add_task():

    task = Taskdata(taskdes = request.form.get('taskdes'), date = request.form.get('date'))  # creating of a data entries for a perticular task 
    if task.taskdes != '':
        db.session.add(task)
        db.session.commit()
    else:
        flash('please fill the task description')       
    
    posts = Taskdata.query.all()
    return  render_template('post.html' , display = posts)
def display_task():
    posts = Taskdata.query.all()
    return  render_template('post.html' , display = posts)



@app.route("/display/<int:taskdata_id>" , methods =['POST', 'GET'])
def displaypage(taskdata_id):

    editTask = Taskdata.query.get_or_404(taskdata_id)

    # form = EditForm()

    # if form.validate_on_submit():
    #     editTask.taskdes = form.edittask.data
    #     editTask.date = form.edittask.data
    #     db.session.commit()
    #     return redirect(url_for('add_task'))
    

    return render_template('displaypage.html' , editTask = editTask)




    # if form.validate_on_submit():
    #     editTask.taskdes = request.form.get('edittasks')

    #     editTask.taskdes = request.form.get('editdate')
    #     db.session.commit()
    #     return redirect(url_for('post'))

   
@app.route("/display/<int:taskdata_id>/update" , methods =['POST', 'GET'])
def edit(taskdata_id):

    editTasks = Taskdata.query.get_or_404(taskdata_id)

    form = EditForm()

    if form.validate_on_submit():
        editTasks.taskdes = form.edittask.data
        editTasks.date = request.form.get('taskdate')
        db.session.commit()
        # taskdata_id = editTasks.id)
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.edittask.data = editTasks.taskdes
    return render_template('edit.html', form=form, editTasks = editTasks)
    
    
   
@app.route("/display/<int:taskdata_id>/delete" , methods =['POST' , 'GET'])
def delete(taskdata_id):

    editTasks = Taskdata.query.get_or_404(taskdata_id)

    db.session.delete(editTasks)
    db.session.commit()
    return redirect(url_for('home'))





    