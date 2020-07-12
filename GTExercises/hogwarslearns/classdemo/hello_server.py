from flask import Flask,request

# Flask�����������
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route("/request",methods=['post','get'])
def hellp():
    # �õ�request ����
    query = request.args
    # �õ�request form
    post = request.form
    # �ֱ��ӡ�õ��Ĳ�����form
    return f"query:{query}\n"\
            f"post:{post}"

'''
###�򵥷������Ĵ
Administrator@19BXVNE26XTAXMJ MINGW64 /d/Projects/GTExercises/hogwarslearns/classdemo (master)
$ export FLASK_APP=hello_server.py

Administrator@19BXVNE26XTAXMJ MINGW64 /d/Projects/GTExercises/hogwarslearns/classdemo (master)
$ flask run
 * Serving Flask app "hello_server.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

'''