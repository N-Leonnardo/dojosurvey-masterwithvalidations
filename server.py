from flask import Flask, render_template, request, redirect, session, flash
from user import User

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/')

    print("Got Post Info")
    print(request.form)
    session['username'] = request.form['name']
    session['userlocation'] = request.form['location']
    session['userlanguage'] = request.form['language']
    session['usermessage'] = request.form['message']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html', name_on_template=session['username'], email_on_template=session['usermessage'])


if __name__=="__main__":
    app.run(debug=True)