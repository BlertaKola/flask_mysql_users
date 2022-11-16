from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User

@app.route('/')
def dashboard():
    return render_template("dashboard.html")


@app.route('/createUser', methods = ['POST'])
def createUser():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    User.add_user(data)
    return redirect('/showInfo')


#this shows info about all users
@app.route('/showInfo')
def showInfo():
    users = User.getAllUsers()
    return render_template("showInfo.html", users = users)



#this shows info about a specific user which we get it by his id
@app.route('/showUser/<int:id>')
def userInfo(id):
    data = {
        'id' : id
    }
    
    return render_template("showUser.html", users = User.getUserById(data))

@app.route('/edit/<int:id>')
def functiontoedit(id):
    data = {
        'id': id
    }
    return render_template("editUser.html", users = User.getUserById(data))

@app.route('/editUser/<int:id>', methods = ['POST'])
def updateUser(id):
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'id': id
    }
    User.updateUser(data)
    return redirect('/showInfo')

@app.route('/deleteUser/<int:id>')
def deleteSomeUser(id):
    data = {
        'id': id
    }
    User.deleteUser(data)
    return redirect('/showInfo')


