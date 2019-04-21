#created by Soham Pathak
from flask import Flask,render_template,url_for,flash,redirect

app = Flask(__name__)
#app.debug = True
#app variable is set to set clss it says where flask to look for template __name__ returns main
#/ is just the root page
#@app.route are also known as decorater
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'



@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html',title='Home Page')







if __name__ == '__main__':
    app.run(debug=True)    