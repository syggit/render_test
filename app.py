from flask import Flask
app = Flask(__name__)
cnt=0

@app.route('/')
def hello_world():
    global cnt
    cnt += 1
    return 'Hello World! %d' % cnt
