from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from app import mail

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def sending_email():
    app = current_app._get_current_object()
    msg = Message('test from flask code', sender='mike.python.testing@gmail.com', recipients=['mike.python.testing@gmail.com'])
    msg.body = 'another test from flask code'
    msg.html = 'another test from flask code'
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr