from flask import Flask,render_template
from datetime import datetime

app=Flask(__name__)
@app.route('/greet/<username>')
def greet(username):
    currTime = datetime.now().hour

    if 6<=currTime<12:
        greeting = "GOOD MORNING"
    elif 12<=currTime<16:
        greeting = "GOOD AFTERNOON"
    elif 16<=currTime<21:
        greeting = "GOOD EVENING"
    else:
        greeting = "GOOD NIGHT"
    return greeting+ ", "+username
    

if __name__=="__main__":
    app.run(debug=True)

