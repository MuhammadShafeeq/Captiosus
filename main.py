import csv
import json
import random
from flask_apscheduler import APScheduler
from datetime import timedelta
from flask import Flask, render_template, request, session, flash, redirect, url_for
from functions import Functions,daily_quote


app = Flask(__name__)
app.secret_key = "IUhoUqojdJWAMKXSqddsoijfozmclkm1wafjwpaiojgubh"
app.permanent_session_lifetime = timedelta(hours=8)
schedule = APScheduler()

def choose_quote():
    print("Hey!!!!")
    with open('quotes.csv', 'r') as f:
        reader = csv.DictReader(f)
        csvData = list(reader)
    daily_quote = random.choice(csvData)
    with open('tquote.csv', 'w') as f:
        fieldnames= ["Author", "Quote"]
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(daily_quote)
    return daily_quote

daily_quote
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    if "User" in session:
        return redirect(url_for('dashboard'))
    else:
        if request.method == "POST":
            datao = request.data.decode('ASCII')
            data = json.loads(datao)
            username = data["Username"]
            name = data["Name"]
            password = data["Password"]
            if username and name and password:
                if Functions.check_username(username=username):
                    Functions.register(username=username, password=password, name=name)
                    return redirect(url_for('login'))
                else:
                    flash("Username already taken", 'danger')
                    return render_template('register.html')
            else:
                flash("Not all values were assigned", 'danger')
                return render_template('register.html')
        else:
            return render_template('register.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if "User" in session:
        flash("Already logged in", "info")
        return redirect(url_for('dashboard'))
    else:
        if request.method == "POST":
            rem = request.form.get('remember-me')
            if rem == 'on':
                session.permanent = True
            username = request.form.get('username').lower()
            password = request.form.get('password')
            auth = Functions.check_creds_for_login(username=username, password=password)
            if auth:
                session["User"] = Functions.get_user(username=username)
                return redirect(url_for('dashboard'))
            else:
                return redirect('login')
        else:
            return render_template('login.html')


@app.route("/logout")
def logout():
    if "User" in session:
        user = session["User"]
        session.pop("User", None)
        print(f"Logged out of {user['Username']}")
        return "Logged Out"
    else:
        return "Your Not Logged In"


@app.route('/dashboard')
def dashboard():
    if "User" not in session:
        flash("Log in first", "info")
        return redirect(url_for('login'))
    else:
        with open('tquote.csv', 'r') as f:
            reader = csv.DictReader(f)
            csvData = list(reader)
        daily_quote = random.choice(csvData)
        user = Functions.get_user(session['User']['Username'])
        tdlist = Functions.get_tdlist(username=user['Username'])
        return render_template('dashboard.html', user=user, tdlist=tdlist, quote=daily_quote)


@app.route('/organize', methods=["GET"])
def organize():
    if "User" in session:
        user = Functions.get_user(session['User']['Username'])
        tdlist = Functions.get_tdlist(username=user['Username'])
        return render_template('organize.html', tdlist=tdlist, session=user)
    else:
        flash("Login to see that process", "info")
        return redirect(url_for('login'))

@app.route('/organize/tdlist', methods=["GET", "POST"])
def tdlist():
    if "User" in session:
        user = Functions.get_user(session['User']['Username'])
        tdlist = Functions.get_tdlist(username=user['Username'])
        return render_template('tdlist/tdlist.html', tdlist=tdlist, session=user)
    else:
        flash("Login to see that process", "info")
        return redirect(url_for('login'))


@app.route('/remove', methods=["POST"])
def remove_task():
    data = request.json
    print(data)
    username = data['username']
    taskId = data['taskid']
    Functions.remove_task(username=username, taskId=taskId)
    print(f"Removed Task {taskId}")
    return {"Response": "Completed"}

@app.route('/status/change', methods=["POST"])
def status_change():
    data = request.json
    username = data['username']
    taskId = data['taskid']
    status = data['taskstatus']
    Functions.update_status(username=username, taskId=taskId, choice=status)
    return {"Response": "Completed"}


@app.route('/journal/')
def journal():
    if "User" in session:
        user = Functions.get_user(session['User']['Username'])
        journal = user["journal"]
        return render_template("journal/journal.html", user=user, journal=journal)
    else:
        return redirect(url_for('login'))



@app.route('/journal/<day>')
def content_journal(day):
    if "User" not in session:
        flash("Log in first", "info")
        return redirect(url_for('login'))
    else:
        date = Functions.get_journal_date(username=session["User"]["Username"], date=day)
        if date:
            return render_template('journal/journal_date.html', user=session["User"], date=date, day=day)
        else:
            return "No"


@app.route('/journal/entry/create', methods=["GET", "POST"])
def create_entry():
    if "User" not in session:
        flash("Log in first", "info")
        return redirect(url_for('login'))
    else:
        user = Functions.get_user(session["User"]["Username"])
        if request.method == "POST":
            if request.json['type'] == "journal-entry":
                title = request.json['title']
                body = request.json['body']
                Functions.create_journal_entry(username=user, title=title, entry=body)
                return {"type": 200}
        return render_template("journal/create.html")


@app.route('/create', methods=["POST"])
def create_task():
    data = request.json
    taskname = data['taskname']
    Functions.create_task(data['user'], taskname)
    return 200


if __name__ == '__main__':
    schedule.add_job(id="Quote", func=choose_quote, trigger="cron", day_of_week="mon,tue,wed,thu,fri,sat,sun", hour=1, minute=00)
    schedule.start()
    app.run(debug=True, use_reloader=False)