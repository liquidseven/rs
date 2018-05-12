from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index:
    return render_template('resume.html')

if __name__name = '__main__':
    app.run()
