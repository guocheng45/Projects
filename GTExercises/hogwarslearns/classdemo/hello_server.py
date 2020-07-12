from flask import Flask,request

# Flask服务器搭建代码
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route("/request",methods=['post','get'])
def hellp():
    # 拿到request 参数
    query = request.args
    # 拿到request form
    post = request.form
    # 分别打印拿到的参数和form
    return f"query:{query}\n"\
            f"post:{post}"

'''
###简单服务器的搭建
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