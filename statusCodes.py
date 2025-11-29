from flask import Flask , render_template , request, abort
from http import HTTPStatus

app = Flask(__name__)

@app.route("/printStatus")
def printStatus():
    username = request.args.get('uname')
    if username == "admin":
        return render_template("showStatus.html", statuses = list(HTTPStatus))
    else:
        abort(403)

if __name__=="__main__":
    app.run(debug=True)