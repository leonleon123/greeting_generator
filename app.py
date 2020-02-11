from flask import Flask, request, redirect
from flask import render_template
import json
from generateText import generate, error

app = Flask(__name__, static_folder="static")
language="EN"

@app.route("/")
def index():
    return redirect("/EN")
@app.route("/EN")
def indexEN():
    return render_template("/indexEN.html")

@app.route("/SI")
def indexSI():
    return render_template("/indexSI.html")

@app.route("/input", methods=["POST"])
def post():
    data=json.loads(request.data)
    language=data["lang"]
    generated = generate(data["value"].split(","),int(data["length"]),50, language)
    if generated == error[language]:
        return json.dumps({"value":generated})
    with open(f"data{language}.txt","a") as file:
        file.write(generated+"\n")
    return json.dumps({"value":generated})

