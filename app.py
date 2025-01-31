from flask import Flask, render_template,request

app = Flask(__name__)

app.config["DEBUG"] = True


@app.route('/')
def index():
    return render_template("index.html")




@app.route('/contact',methods=["Post"])
def contact():
    first = request.form["first"]
    return first    

app.run()
