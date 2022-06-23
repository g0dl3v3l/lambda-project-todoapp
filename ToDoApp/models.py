from ToDoApp import db ,login_manager

from flask_login import UserMixin #will contain IsAuthenticated , isactive , getID functions


#decorated function , resvise all class
@login_manager.user_loader
def load_user(user_id):
        return User.query.get(int(user_id))


#contains all the data points for a user
class User(db.Model , UserMixin):
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(20))
    email = db.Column(db.String(20))
    password = db.Column(db.String(60))
    tasks = db.relationship('Taskdata' , backref = 'author', lazy = True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}' , '{self.password}')" 

#contains all the data points for a tasks
class Taskdata(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    taskdes = db.Column(db.String(200) ,nullable=False)
    date = db.Column(db.String(100) , nullable = False)

    user_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable= False)# all the posts created by the current user will be pointed to the id of the user
# id , taskdes and date are called class variables

    #the return is a string 
    #__repr__ is responsible to take a class obj and display it as a string
    def __repr__(self):
        return f"User('{self.taskdes}', '{self.date}')" 


