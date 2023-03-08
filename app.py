import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = request.form["question"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(question),
            temperature=0.70,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


@app.route("/dalle", methods = ("GET", "POST"))
def dalle(image):
    if request.method == "POST":
        image =  request.form["image"]
        response = openai.Image.create(
            prompt=image,
            n=1,
            size="1024x1024"
            )
        
        image_url = response['data'][0]['url']
        
        return redirect(url_for("dalle", image = image_url))
    
    image = request.args.get("image")
    return render_template("dall_e.hthml", image = image)

def generate_prompt(question):
        return """{}
Answer:""".format(
        question.capitalize()
    )
