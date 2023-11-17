from flask import Flask, render_template
import os
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", page_title="Home")


@app.route("/about")
def about():
    data = []
    with open ("data/company.json","r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers(): 
    return render_template("careers.html", page_title="Career")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("ip","0.0.0.0"),
        port=int(os.environ.get("PORT","5000")),
        debug=True)


        