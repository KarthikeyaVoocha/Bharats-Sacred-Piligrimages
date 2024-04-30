from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import json
from flask_mail import Mail


'''with open('config.json','r') as c:
    parms=json.load(c)["parms"]'''

local_server=True
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/bharat'


db = SQLAlchemy(app)

class Contactus(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    Name= db.Column(db.String(20), unique=False, nullable=False)
    Email= db.Column(db.String(30), unique=False, nullable=False)
    Message= db.Column(db.String(200), unique=False, nullable=False)

class Comments(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    Name= db.Column(db.String(30), unique=False, nullable=False)
    comment=db.Column(db.String(100),unique=False,nullable=False)
    slug=db.Column(db.String(40),unique=False,nullable=False)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/contactus",methods=['GET','POST'])
def contactus():
    if(request.method=="POST"):
        Name=request.form.get('name')
        Email=request.form.get('email')
        Message=request.form.get('message')
        entry=Contactus(Name=Name,Email=Email,Message=Message)
        db.session.add(entry)
        db.session.commit()
    return render_template('contactus.html')

@app.route("/karnataka",methods=['GET','POST'])
def comments():
   comments=Comments.query.filter_by(slug="karnataka").all()
   if(request.method=="POST"):
        Name=request.form.get('name')
        comment=request.form.get('comment')
        slug="karnataka"
        entry=Comments(Name=Name,comment=comment,slug=slug)
        db.session.add(entry)

        db.session.commit()
   return render_template('karnataka.html',comments=comments)

@app.route("/Tg",methods=['GET','POST'])
def commentstg():
   comments=Comments.query.filter_by(slug="tg").all()
   if(request.method=="POST"):
        Name=request.form.get('name')
        comment=request.form.get('comment')
        slug="tg"
        entry=Comments(Name=Name,comment=comment,slug=slug)
        db.session.add(entry)

        db.session.commit()
   return render_template('Tg.html',comments=comments)

@app.route("/ap",methods=['GET','POST'])
def commentsap():
   comments=Comments.query.filter_by(slug="ap").all()
   if(request.method=="POST"):
        Name=request.form.get('name')
        comment=request.form.get('comment')
        slug="ap"
        entry=Comments(Name=Name,comment=comment,slug=slug)
        db.session.add(entry)

        db.session.commit()
   return render_template('ap.html',comments=comments)

@app.route("/chhattisgarh",methods=['GET','POST'])
def commentsch():
   comments=Comments.query.filter_by(slug="ch").all()
   if(request.method=="POST"):
        Name=request.form.get('name')
        comment=request.form.get('comment')
        slug="ch"
        entry=Comments(Name=Name,comment=comment,slug=slug)
        db.session.add(entry)

        db.session.commit()
   return render_template('chhattisgarh.html',comments=comments)

@app.route("/Delhi",methods=['GET','POST'])
def commentsdel():
   comments=Comments.query.filter_by(slug="de").all()
   if(request.method=="POST"):
        Name=request.form.get('name')
        comment=request.form.get('comment')
        slug="de"
        entry=Comments(Name=Name,comment=comment,slug=slug)
        db.session.add(entry)

        db.session.commit()
   return render_template('Delhi.html',comments=comments)

@app.route("/goa",methods=['GET','POST'])
def commentsgoa():
   comments=Comments.query.filter_by(slug="go").all()
   if(request.method=="POST"):
        Name=request.form.get('name')
        comment=request.form.get('comment')
        slug="go"
        entry=Comments(Name=Name,comment=comment,slug=slug)
        db.session.add(entry)

        db.session.commit()
   return render_template('goa.html',comments=comments)

@app.route("/gujarat",methods=['GET','POST'])
def commentsguj():
   comments=Comments.query.filter_by(slug="gj").all()
   if(request.method=="POST"):
        Name=request.form.get('name')
        comment=request.form.get('comment')
        slug="gj"
        entry=Comments(Name=Name,comment=comment,slug=slug)
        db.session.add(entry)

        db.session.commit()
   return render_template('gujarat.html',comments=comments)

@app.route("/haryana",methods=['GET','POST'])
def commentsha():
   comments=Comments.query.filter_by(slug="har").all()
   if(request.method=="POST"):
        Name=request.form.get('name')
        comment=request.form.get('comment')
        slug="har"
        entry=Comments(Name=Name,comment=comment,slug=slug)
        db.session.add(entry)

        db.session.commit()
   return render_template('haryana.html',comments=comments)

@app.route("/himachal",methods=['GET','POST'])
def commentshim():
   comments=Comments.query.filter_by(slug="him").all()
   if(request.method=="POST"):
        Name=request.form.get('name')
        comment=request.form.get('comment')
        slug="him"
        entry=Comments(Name=Name,comment=comment,slug=slug)
        db.session.add(entry)

        db.session.commit()
   return render_template('himachal.html',comments=comments)

@app.route("/jammu",methods=['GET','POST'])
def commentsjam():
   comments=Comments.query.filter_by(slug="jam").all()
   if(request.method=="POST"):
        Name=request.form.get('name')
        comment=request.form.get('comment')
        slug="jam"
        entry=Comments(Name=Name,comment=comment,slug=slug)
        db.session.add(entry)

        db.session.commit()
   return render_template('jammu.html',comments=comments)

@app.route("/jharkhand",methods=['GET','POST'])
def commentsjhar():
   comments=Comments.query.filter_by(slug="jhar").all()
   if(request.method=="POST"):
        Name=request.form.get('name')
        comment=request.form.get('comment')
        slug="jhar"
        entry=Comments(Name=Name,comment=comment,slug=slug)
        db.session.add(entry)

        db.session.commit()
   return render_template('jharkhand.html',comments=comments)

@app.route("/maharastra",methods=['GET','POST'])
def commentsmaha():
   comments=Comments.query.filter_by(slug="mah").all()
   if(request.method=="POST"):
        Name=request.form.get('name')
        comment=request.form.get('comment')
        slug="mah"
        entry=Comments(Name=Name,comment=comment,slug=slug)
        db.session.add(entry)

        db.session.commit()
   return render_template('maharastra.html',comments=comments)

@app.route("/mp",methods=['GET','POST'])
def commentsmp():
   comments=Comments.query.filter_by(slug="mp").all()
   if(request.method=="POST"):
        Name=request.form.get('name')
        comment=request.form.get('comment')
        slug="mp"
        entry=Comments(Name=Name,comment=comment,slug=slug)
        db.session.add(entry)

        db.session.commit()
   return render_template('mp.html',comments=comments)

@app.route("/odisha",methods=['GET','POST'])
def commentsod():
   comments=Comments.query.filter_by(slug="od").all()
   if(request.method=="POST"):
        Name=request.form.get('name')
        comment=request.form.get('comment')
        slug="od"
        entry=Comments(Name=Name,comment=comment,slug=slug)
        db.session.add(entry)

        db.session.commit()
   return render_template('odisha.html',comments=comments)

@app.route("/punjab",methods=['GET','POST'])
def commentspb():
   comments=Comments.query.filter_by(slug="pb").all()
   if(request.method=="POST"):
        Name=request.form.get('name')
        comment=request.form.get('comment')
        slug="pb"
        entry=Comments(Name=Name,comment=comment,slug=slug)
        db.session.add(entry)

        db.session.commit()
   return render_template('punjab.html',comments=comments)

@app.route("/rajasthan",methods=['GET','POST'])
def commentsrj():
   comments=Comments.query.filter_by(slug="rj").all()
   if(request.method=="POST"):
        Name=request.form.get('name')
        comment=request.form.get('comment')
        slug="rj"
        entry=Comments(Name=Name,comment=comment,slug=slug)
        db.session.add(entry)

        db.session.commit()
   return render_template('rajasthan.html',comments=comments)

@app.route("/uttarp",methods=['GET','POST'])
def commentsut():
   comments=Comments.query.filter_by(slug="ut").all()
   if(request.method=="POST"):
        Name=request.form.get('name')
        comment=request.form.get('comment')
        slug="ut"
        entry=Comments(Name=Name,comment=comment,slug=slug)
        db.session.add(entry)

        db.session.commit()
   return render_template('uttarp.html',comments=comments)

app.run()

