from flask import Flask, render_template, request, redirect, url_for
from common.tweet import tweet_run

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        tweet_run(request.form['tweet_body'])
        return redirect(url_for('index'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
