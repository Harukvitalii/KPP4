
from flask import Flask, render_template, request, url_for, flash, redirect
from app.loader import pgbotdb

CHAT_ID = 11
app = Flask(__name__)
app.config['SECRET_KEY'] = 'kdsjlksjfldjf'
 


messages1 = pgbotdb.get_chat_data(chat_id=CHAT_ID)

messages = []
for message in messages1: 
    m = {}
    m['title'] = message[2]
    m['content'] = message[3]
    messages.append(m)
print(messages)

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        print(content)
        pgbotdb.add_text(title,content,chat_id=CHAT_ID)
        if not title:
            flash('Name is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))

    return render_template('create.html')


