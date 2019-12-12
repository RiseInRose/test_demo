# coding:utf-8
# author caturbhuja
# date   2019/8/26 11:10 AM 
# wechat chending2012
"""
flask 中文文档 https://dormousehole.readthedocs.io/en/latest/quickstart.html#id2

"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(
        port=5001
    )
