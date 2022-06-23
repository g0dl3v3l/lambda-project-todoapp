from ToDoApp import app , db
from flask import render_template, url_for, flash, redirect ,request
from ToDoApp.models import Taskdata ,User
from ToDoApp.forms import EditForm ,UserForm
from flask_login import login_user, current_user,logout_user




db.create_all()

# user_main = User(username='Dheeraj' , email = 'dheeraj@dh.com', password='dheeraj')
# db.session.add(user_main)
# db.session.commit()






@app.route("/register", methods=['POST', 'GET'])
# def register_display():
#     return render_template('register.html')


def register():
    #This end point is reponsible for the registration page


    form = UserForm()

    if form.validate_on_submit():
        #taking input from the from field in the registration page
        user = User(username=form.username.data , email= form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('login'))

    return render_template('register.html',form = form) 




@app.route("/", methods=['POST', 'GET'])
def login():
   #this page is responsible for the login page

    user = User.query.filter_by(username=request.form.get('users')).first() # the first() function will get the obj from the list ,first() is very important
    
    # checking if the user obj exists and if the password typed in the text field and the password with which that paerticular user has registered matches
    if user and user.password == request.form.get('pwd'):
        
        login_user(user)
    
        # flash(f'the current user is {current_user}')
        return redirect(url_for('home'))
    # else:
    #     flash('Login Unsuccessful . Please check email and password')
    
    return render_template('login.html')



@app.route("/home")

#display of the all the task disreptions of the current user logined is displayed 
def home():
    posts = current_user.tasks
    return  render_template('post.html' , display = posts ,current_user = current_user.username)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/home" , methods =['POST', 'GET'])
def add_task():

    task = Taskdata(taskdes = request.form.get('taskdes'), date = request.form.get('date'), user_id=current_user.id)  # creating of a data entries for a perticular task 
    if task.taskdes != '' and task.date != '':
        db.session.add(task)
        db.session.commit()
    else:
        flash('please fill the task description')       
    
    posts = Taskdata.query.filter_by(user_id = current_user.id).all()
    return  render_template('post.html' , display = posts ,current_user = current_user.username)


def display_task():
    posts = current.tasks
    # flash(f'{posts}')
    return  render_template('post.html' , display = posts ,current_user = current_user.username)


#displays the perticual task selected for updation or deleting
@app.route("/display/<int:taskdata_id>" , methods =['POST', 'GET'])
def displaypage(taskdata_id):

    editTask = Taskdata.query.get_or_404(taskdata_id)

   
    return render_template('displaypage.html' , editTask = editTask ,current_user = current_user.username)

   
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
    return render_template('edit.html', form=form, editTasks = editTasks,current_user = current_user.username)
    
    
   
@app.route("/display/<int:taskdata_id>/delete" , methods =['POST' , 'GET'])
def delete(taskdata_id):

    editTasks = Taskdata.query.get_or_404(taskdata_id)

    db.session.delete(editTasks)
    db.session.commit()
    return redirect(url_for('home'))





    