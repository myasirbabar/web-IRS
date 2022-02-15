from flask import Flask,render_template,request,redirect
from IRS import *

app = Flask(__name__)


@app.route('/')
@app.route('/index.html') #IF in brower there is localhost:5000 or localhost:5000/index.html... call this function
def index():
    return render_template('index.html') 


#IF in brower there is localhost:5000/IRS ... call this function
@app.route('/IRS', methods = ['POST', 'GET']) 
def IRS():
    if request.method == 'GET':
        return redirect('/index.html')
    else:
        search = request.form['search']
        results = start(search)
        if results == -1:
            return render_template('index.html', text = "No such Result Found", search = search)
        else:
            return render_template('index.html', text = results, search = search)


if __name__ == "__main__":
    app.run(debug=True)