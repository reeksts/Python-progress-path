from flask import Flask, render_template

app = Flask(__name__)

name="Bob Smith"

@app.route("/")
def hello_world():
    return render_template(
        "jinja_intro.html",
        name=name,
        template_name="Jinja2"
    )