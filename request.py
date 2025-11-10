from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/queryDemo', methods =["POST"])
def queryDemo():
    return "Language is " + request.form.get('language') # requesting from client to give value  
    #  and return response to client by default calls GET method

@app.route('/takeData')
def takeData():
    return render_template('queryDemo.html')

if __name__=="__main__":
    app.run(debug=True)