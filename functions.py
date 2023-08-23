import csv
import json
from datetime import datetime, timedelta, date
import random

def default(o):
    if isinstance(o, (date, datetime)):
        return o.isoformat()

def get_random_id(char = 10):
    taskiid = ""
    idChrCtr = 0
    while True:
        nchr = random.choice(range(0, 10))
        taskiid += str(nchr)
        idChrCtr += 1
        if idChrCtr == 10:
            return int(taskiid)


def date_convert(date):
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    omonth = int(date.split('-')[1])
    nmonth = months[omonth-1]
    new_date = date.replace(date.split('-')[1], nmonth)
    return new_date

# NEEDS TO BE UPDATED TO OBJECT ORIENTATED PROGRAMMING
class Functions:
    def __init__(self):
        return
    def register(username, password, name):
        username = username.lower()
        with open('data.json', 'r') as f:
            users = json.load(f)
        if username in users:
            return "Account Already Exists"
        else:
            users[username] = {}
            users[username]["Username"] = username
            users[username]["Name"] = name
            users[username]["Password"] = password
            users[username]["tdList"] = {}
            users[username]["journal"] = {}
            with open('data.json', 'w') as f:
                json.dump(users, f, indent=4)
    def check_username(username):
        with open('data.json', 'r') as f:
            users = json.load(f)
        if username in users:
            return False
        else:
            return True

    def check_creds_for_login(username, password):
        with open('data.json', 'r') as f:
            users = json.load(f)
        if username in users:
            if users[username]["Password"] == password:
                return True
            else:
                return False
        else:
            return False

    def get_user(username):
        with open('data.json', 'r') as f:
            users = json.load(f)
        user = users[username]
        return user

    def create_task(username, taskName):
        timeCreation = datetime.utcnow()
        with open('data.json', 'r') as f:
            users = json.load(f)
        ctr = 1
        for i in users[username]["tdList"]:
            ctr += 1
        valid = True
        while True:
            taskId = get_random_id()
            with open('usedIds.csv', 'r') as f:
                reader = csv.DictReader(f)
                csvData = list(reader)
            print("Stage 2")
            for val in csvData:
                print(val["ids"])
                if val["ids"] != taskId:
                    found = True
                    with open('usedIds.csv', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([taskId])
                    break
            if found:
                break
        users[username]["tdList"][taskName] = {}
        users[username]["tdList"][taskName]["id"] = int(taskId)
        users[username]["tdList"][taskName]["primaryKey"] = ctr
        users[username]["tdList"][taskName]["Status"] = "incomplete"
        users[username]["tdList"][taskName]["timeCreation"] = timeCreation
        users[username]["tdList"][taskName]["endTime"] = timeCreation + timedelta(1)
        with open('data.json', 'w') as f:
            json.dump(users, f, default=default, indent=4)

    def remove_task(username, taskId):
        with open('data.json', 'r') as f:
            users = json.load(f)

        copied = users
        for i in copied[username]["tdList"]:
            if users[username]["tdList"][i]["id"] == taskId:
                del users[username]["tdList"][i]
                break
        with open('data.json', 'w') as f:
            json.dump(users, f, indent=4)

    def remove_user(username):
        with open('data.json', 'r') as f:
            users = json.load(f)
        if username in users:
            del users[username]
        with open('data.json', 'w') as f:
            json.dump(users, f, indent=4)

    def get_task_by_name(username, taskName):
        with open('data.json', 'r') as f:
            users = json.load(f)
        copied = users
        task = users[username]["tdList"][taskName]
        return task

    def get_task(username, taskId):
        with open('data.json', 'r') as f:
            users = json.load(f)
        copied = users
        for i in copied[username]["tdList"]:
            if users[username]["tdList"][i]["id"] == taskId:
                task = users[username]["tdList"][i]
                break
        return task

    def update_status(username, taskId, choice):
        with open('data.json', 'r') as f:
            users = json.load(f)
        copied = users
        for i in copied[username]["tdList"]:
            if users[username]["tdList"][i]["id"] == taskId:
                task = i
                break
        if choice == 1:
            users[username]["tdList"][task]["Status"] = "complete"
        elif choice == 2:
            users[username]["tdList"][task]["Status"] = "incomplete"
        elif choice == 3:
            users[username]["tdList"][task]["Status"] = "delayed"
        with open('data.json', 'w') as f:
            json.dump(users, f, indent=4)

    def get_tdlist(username):
        with open('data.json', 'r') as f:
            users = json.load(f)
        if username in users:
            tdlist = users[username]["tdList"]
            return tdlist
        else:
            return False


    def get_journal_date(username, date):
        with open('data.json', 'r') as f:
            users = json.load(f)
        if username in users:
            if date in users[username]["journal"]:
                day = users[username]["journal"][date]
                return day
            else:
                return False
        else:
            return False

    def create_journal_entry(username, entry, title):
        username = username.lower()
        date_creation = datetime.today().date()
        time_creation = datetime.today()
        day = date_creation.day
        month = date_creation.month
        year = date_creation.year
        date12 = f"{day}-{month}-{year}"
        hour = time_creation.hour
        minute = time_creation.minute
        time1 = f"{hour}:{minute}-D-{date12}"
        date1 = date_convert(date12)
        with open('data.json', 'r') as f:
            users = json.load(f)
        ctr = 1
        for i in users[username]["journal"]:
            ctr += 1
        if date1 not in users[username]["journal"]:
            users[username]["journal"][date1] = {}
        users[username]["journal"][date1][title] = {}
        users[username]["journal"][date1][title]["id"] = ctr
        users[username]["journal"][date1][title]["entry"] = entry
        users[username]["journal"][date1][title]["timeCreation"] = time1

        with open('data.json', 'w') as f:
            json.dump(users, f, indent=4)
