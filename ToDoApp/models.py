from ToDoApp import db

class Taskdata(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    taskdes = db.Column(db.String(200) ,nullable=False)
    date = db.Column(db.String(100) , nullable = False)
# id , taskdes and date are called class variables

    #the return is a string 
    #__repr__ is responsible to take a class obj and display it as a string
    def __repr__(self):
        return f"User('{self.taskdes}', '{self.date}')" 


