#!/usr/bin/python3

from flask import (
Flask,
render_template,
request,
)

from secretkeygenerator.secretkeygenerator import secretkeygenerator


app=Flask(__name__)


@app.route('/')
def index():
    secret_key=secretkeygenerator()
    return render_template('index.html', secret_key=secret_key)


if __name__=='__main__':
	app.run(debug=True)
