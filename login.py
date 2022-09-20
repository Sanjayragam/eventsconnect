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

@app.route("/")
def index():
   bodyc="this is the body"
   msg = Message('Hello', sender = 'yourId@gmail.com', recipients = ['sanjayragam@gmail.com'])
   msg.body = bodyc
   mail.send(msg)
   return "Sent"


if __name__ == '__main__':
   app.run(debug = True)