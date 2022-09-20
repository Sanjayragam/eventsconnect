from calendar import month
from telnetlib import STATUS
from unicodedata import name
from click import style
from flask import Flask, render_template, request, redirect, url_for, session,flash, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os
import urllib.request
from jmespath import search
from werkzeug.utils import secure_filename
from flask import Flask
from flask_mail import Mail, Message

  
  
app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sanjayragam@ieee.org'
app.config['MAIL_PASSWORD'] = 'Ragam@57'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

  
UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app.secret_key = 'xyzsdfg'
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '8157'
app.config['MYSQL_DB'] = 'eventsconnect'
  
mysql = MySQL(app)




@app.route('/events', methods = ['POST', 'GET'])

def events():
    if request.method == 'GET':
        return "events "
     
    if request.method == 'POST':
        name = request.form['name']
        venue = request.form['venue']
        speaker = request.form['speaker']
        club = request.form['club']
        status= request.form['status']
        color = request.form['color']
        time = request.form['time']
        endtime = request.form['endtime']
        date = request.form['date']
        request_status = request.form['req_status']


        date1 = date.split("-")
        day=date1[2]
        month=date1[1]
        year=date1[0]

        prikey=date+time
        print(prikey)

        monthword="00"
        if month=="01":
           monthword="January"
        if month=="02":
           monthword="February"
        if month=="03":
           monthword="March"
        if month=="04":
           monthword="April"
        if month=="05":
           monthword="May"
        if month=="06":
           monthword="June"
        if month=="07":
           monthword="July"
        if month=="08":
           monthword="August"
        if month=="09":
           monthword="September"
        if month=="10":
           monthword="October"
        if month=="11":
           monthword="November"
        if month=="12":
           monthword="December"

        strday=str(day)
        stryear=str(year)

        from MySQLdb import IntegrityError
        try:
            
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO events (club, name, date, day, month, year, monthword, time, venue, speaker, color, status, endtime, req_status ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (club, name, date,  day, month, year, monthword, time, venue, speaker, color, status, endtime, request_status))
            mysql.connection.commit()
            cursor.close()
            
        except MySQLdb.IntegrityError:
            return render_template("alert.html")


        # msg = Message("Eventsconnect"+club, sender = 'sanjayragam@ieee.org', recipients = ['sanjayragam@gmail.com'])
        # msg.body = club+""" added an event

        #             Event details
        #             -------------
        #             Event name : """+name+"""
        #             Date : """+strday+" "+monthword+" "+stryear+"""
        #             Time : """+time+"""
        #             Ending time : """+endtime+"""
        #             venue : """+venue+"""
        #             speaker : """+speaker+"""

        #             review:
        #             http://127.0.0.1:5000/adminlogin"""

        
        # mail.send(msg)
        return redirect(url_for('login'))
        

        
# @app.route('/warning')
# def warning():

#     clubs=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     clubs.execute("select * from user")
#     clubdata=clubs.fetchall()

#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM events")
#     dataall= cur.fetchall()
#     return render_template("alert.html",data=dataall,clubdata=clubdata)

 
@app.route('/', methods =['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'

            global hai
            hai=user['name']
            
            c=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            c.execute("SELECT * FROM events where status='rejected' and club='%s'"%hai)
            curcount=c.rowcount

            a=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            a.execute("SELECT * FROM events where status='approved'and club='%s'"%hai)
            counta=a.rowcount

            p=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            p.execute("SELECT * FROM events where status='pending'and club='%s'"%hai)
            countp=p.rowcount

            r=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            r.execute("SELECT * FROM events where club='%s'"%hai)
            countr=r.rowcount

            datecur = mysql.connection.cursor()
            datecur.execute("SELECT * FROM events")
            date = datecur.fetchall()


            cur = mysql.connection.cursor()
            cur3 = mysql.connection.cursor()
            curs = mysql.connection.cursor()
            cursr = mysql.connection.cursor()

            cur.execute("SELECT * FROM events where club='%s'"%hai)
            curs.execute("SELECT * FROM events where status='approved'and club='%s'"%hai)
            cursr.execute("SELECT * FROM requests where club='%s'"%hai)
            cur3.execute("SELECT * FROM requests where club='%s'"%hai)

            data = cur.fetchall()
            datarequest = cursr.fetchall()
            dataapproved = curs.fetchall()
            cur.close()

            req=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            req.execute("SELECT * FROM requests where club='%s'"%hai)
            rcount=req.rowcount

            
            requestcursor=cursr = mysql.connection.cursor()
            requestcursor.execute("SELECT * FROM events where club!='%s'"%hai)
            requestcancellation=requestcursor.fetchall()



            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM events")
            dataall= cur.fetchall()
            cur.close()

            requests=mysql.connection.cursor()
            requests.execute("SELECT * FROM requests")
            requestss= requests.fetchall()
            


            return render_template('user.html',requestcancellation=requestcancellation,rcount=rcount,datarequest=datarequest, dataapproved=dataapproved,students=data, curcount=curcount,countr=countr,counta=counta, countp=countp,mesage = mesage,date=date,dataall=dataall,requestss=requestss )

        
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from events where status!='rejected'ORDER BY year,month,day ASC  ")
    all=cursor.fetchall()

    clubs=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    clubs.execute("select * from user")
    clubdata=clubs.fetchall()

    c=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # c.execute("SELECT * FROM events where club='%s'"%hai)
    c.execute("SELECT * FROM events where status!='rejected' ")
    total=c.rowcount

    clubs=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    clubs.execute("select * from user")
    clubdata=clubs.fetchall()



   

    


    return render_template("home.html",all=all,mesage = mesage,clubdata=clubdata,total=total)












@app.route('/login')
def loginpage():
    return render_template("login.html")

@app.route('/add')
def add():
    return render_template("eventadd.html")
  
  
@app.route('/home')
def home():
    return render_template('hai.html')
  



 

@app.route('/approved')
def approved():

    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from events where status='approved' ORDER BY year,month,day ASC")
    all=cursor.fetchall()

    clubs=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    clubs.execute("select * from user")
    clubdata=clubs.fetchall()

    c=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # c.execute("SELECT * FROM events where club='%s'"%hai)
    c.execute("SELECT * FROM events  where status='approved' ")
    total=c.rowcount


    return render_template("home.html",all=all,clubdata=clubdata,total=total)


  
@app.route('/pending')
def pending():

    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from events where status='pending' ORDER BY year,month,day ASC")
    all=cursor.fetchall()


    clubs=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    clubs.execute("select * from user")
    clubdata=clubs.fetchall()

    c=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # c.execute("SELECT * FROM events where club='%s'"%hai)
    c.execute("SELECT * FROM events  where status='pending' ")
    total=c.rowcount

    return render_template("home.html",all=all,clubdata=clubdata,total=total)
  





@app.route('/search',methods = ['POST', 'GET'])
def search():

    if request.method == 'POST':
        search = request.form['search']

    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from events where status!='rejected'and club='%s'"%search)
    all=cursor.fetchall()

    clubs=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    clubs.execute("select * from user")
    clubdata=clubs.fetchall()

    
    c=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    c.execute("select * from events where status!='rejected'and club='%s'"%search)
    total=c.rowcount

    return render_template("home.html",all=all,clubdata=clubdata,total=total)
  


@app.route('/month',methods = ['POST', 'GET'])
def month():

    if request.method == 'POST':
        month = request.form['month']

    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from events where status!='rejected'and monthword='%s'"%month)
    all=cursor.fetchall()

    clubs=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    clubs.execute("select * from user")
    clubdata=clubs.fetchall()

    
    c=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    c.execute("select * from events where status!='rejected'and club='%s'"%search)
    total=c.rowcount

    return render_template("home.html",all=all,clubdata=clubdata,total=total)





@app.route('/updated', methods =['GET', 'POST'])
def updated():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'

            global hai
            hai=user['name']
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM events where club='%s'"%hai)
    data = cur.fetchall()
    cur.close()
    return render_template('user.html', students=data )   
        

@app.route('/deleteall', methods = ['GET'])
def deleteall():
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM events WHERE id=%s", (id_data,))
    mysql.connection.commit()


    return render_template('updated.html')



@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM events WHERE id=%s", (id_data,))
    mysql.connection.commit()
    
    # cur1 = mysql.connection.cursor()
    # cur1.execute("SELECT  * FROM events")
    # data = cur1.fetchall()
    # cur1.close()

    # cur2 = mysql.connection.cursor()
    # cur2.execute("SELECT * FROM events where id=%s", (id_data,))
    # data2 = cur1.fetchall()
    # name=data2.name
    # cur2.close()


    # msg = Message("Eventsconnect"+name, sender = 'sanjayragam@ieee.org', recipients = ['sanjayragam@gmail.com'])
    # msg.body = """ deleted the event"""
    # mail.send(msg)


    return render_template('updated.html')









@app.route('/cal')
def cal():
    return render_template("eventadd.html")
    


@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        time = request.form['time']
        venue = request.form['venue']
        speaker = request.form['speaker']
        status = request.form['status']

        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE events
               SET name=%s, time=%s, venue=%s, speaker=%s, status=%s
               WHERE id=%s
            """, (name,time, venue, speaker, status, id_data))
        flash("Data Updated Successfully")
        
    # cur1 = mysql.connection.cursor()
    # cur1.execute("SELECT * FROM events where club='%s'"%hai)
    # data = cur1.fetchall()
    # cur1.close()
    # return render_template("cancell.html",students=data)
    return render_template("updated.html")
    



@app.route('/updatestatus',methods=['POST','GET'])
def updatestatus():

    if request.method == 'POST':
        id_data = request.form['id']
        status = request.form['status']


        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE events
               SET status=%s
               WHERE id=%s
            """, (status, id_data))
        flash("Data Updated Successfully")
   
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from events ORDER BY month,day ASC")
    data=cursor.fetchall()
    return render_template("updated.html",data=data)
    # return render_template('login.html', )





@app.route('/reject',methods=['POST','GET'])
def reject():

    if request.method == 'POST':
        id_data = request.form['id']
        status = request.form['status']


        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE events
               SET status=%s
               WHERE id=%s
            """, (status, id_data))
        flash("Data Updated Successfully")
   
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from events ORDER BY month,day ASC")
    data=cursor.fetchall()
    return render_template("updated.html",data=data)
    # return render_template('login.html', )


@app.route('/updatests',methods=['POST','GET'])
def updatests():

    if request.method == 'POST':
        id_data = request.form['id']
        # requests = request.form['requests']
        club=request.form['clubcancel']
        name = request.form['namecancel']
        date = request.form['datecancel']
        time = request.form['timecancel']
        club = request.form['clubcancel']
        requestedby = request.form['requestedby']
        request_status =request.form['req_status']

        # requests=" "+club+" requested to cancell the event"

        # requests=" "+club+" requested to cancell the event -"+name+" scheduled on "+date
        
        # mycursor = mysql.connection.cursor()
        # query = ("ALTER TABLE events ADD %s VARCHAR(100)"%club)


        # cur = mysql.connection.cursor() 
        # cur.execute("UPDATE events SET requests = %s WHERE id=%s", (requests, id_data))

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO requests (name, club, date, time, requestedby) VALUES (%s, %s, %s, %s, %s)", (name, club,  date, time, requestedby))


        cureq = mysql.connection.cursor()
        cureq.execute("""UPDATE events SET req_status=%s WHERE name=%s """, (request_status,name))

        # cursor.execute("INSERT INTO events (req_status) VALUES (%s)", (request_status))
        # mysql.connection.commit()
        # cursor.close()


        # clubs='fossgeci'
        # cursor = mysql.connection.cursor()
        # query = """Update events set %s = %s where id = %s"""
        # tuple1 = (clubs,requests, 1)
        # cursor.execute(query, tuple1)
        
        flash("Data Updated Successfully")
   
    # cur1 = mysql.connection.cursor()
    # cur1.execute("SELECT  * FROM events")
    # data = cur1.fetchall()
    # cur1.close()
    return render_template('updated.html')








@app.route('/admin', methods =['GET', 'POST'])
def adminlogin():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM admin WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'

            global hai
            hai=user['name']
            
            c=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            c.execute("SELECT * FROM events where status='rejected' and club='%s'"%hai)
            curcount=c.rowcount

            a=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            a.execute("SELECT * FROM events where status='approved'and club='%s'"%hai)
            counta=a.rowcount

            p=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            p.execute("SELECT * FROM events where status='pending'and club='%s'"%hai)
            countp=p.rowcount

            r=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            r.execute("SELECT * FROM requests where club='%s'"%hai)
            countr=r.rowcount

            datecur = mysql.connection.cursor()
            datecur.execute("SELECT * FROM events")
            date = datecur.fetchall()


            cur = mysql.connection.cursor()
            cur3 = mysql.connection.cursor()
            curs = mysql.connection.cursor()
            cursr = mysql.connection.cursor()

            cur.execute("SELECT * FROM events where club='%s'"%hai)
            curs.execute("SELECT * FROM events where status='pending'and club='%s'"%hai)
            cursr.execute("SELECT * FROM requests where club='%s'"%hai)
            cur3.execute("SELECT * FROM requests where club='%s'"%hai)

            data = cur.fetchall()
            datarequest = cursr.fetchall()
            dataapproved = curs.fetchall()
            cur.close()

            req=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            req.execute("SELECT * FROM requests where club='%s'"%hai)
            rcount=req.rowcount

            
            requestcursor=cursr = mysql.connection.cursor()
            requestcursor.execute("SELECT * FROM events where club!='%s'"%hai)
            requestcancellation=requestcursor.fetchall()



            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM events")
            dataall= cur.fetchall()
            cur.close()

            # return render_template('hai.html', students=data, curcount=curcount,counta=counta, countp=countp,mesage = mesage,date=date,dataall=dataall )
            return render_template('admin.html',requestcancellation=requestcancellation,rcount=rcount,datarequest=datarequest, dataapproved=dataapproved,students=data, curcount=curcount,counta=counta, countp=countp,mesage = mesage,date=date,dataall=dataall )

           
            

    else:
         mesage = 'Please enter correct email / password !'

    return render_template("adminlogin.html",mesage = mesage)
    # return render_template('login.html', )

        

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))



@app.route('/test')
def test():

    cur1 = mysql.connection.cursor()
    cur1.execute("SELECT  * FROM events")
    data = cur1.fetchall()
    cur1.close()
    return render_template('cancell.html', students=data )


  
@app.route('/register', methods =['GET', 'POST'])
def register():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not userName or not password or not email:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO user VALUES (NULL, % s, % s, % s)', (userName, email, password, ))
            mysql.connection.commit()

            # mycursor = mysql.connection.cursor()
            # query = ("ALTER TABLE events ADD %s VARCHAR(100)"%userName)
            # mycursor.execute(query)

            mesage = 'You have successfully registered !'
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'

    return render_template("signup.html",mesage = mesage)
    # return render_template('register.html', mesage = mesage)




@app.route('/adminregister', methods =['GET', 'POST'])
def adminregister():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM admin WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not userName or not password or not email:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO admin VALUES (NULL, % s, % s, % s)', (userName, email, password, ))
            mysql.connection.commit()
            mesage = 'You have successfully registered !'
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from user")
    data=cursor.fetchall()
    return render_template("adminsignup.html",data=data,mesage = mesage)

    







if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")


