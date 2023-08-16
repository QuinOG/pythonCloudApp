import machinetranslation
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    try:
        french_translation = english_to_french(textToTranslate)
        return "Translated text to French"
    except Exception as e:
        return str(e)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    try:
        english_translation = french_to_english(textToTranslate)
        return "Translated text to English"
    except Exception as e:
        return str(e)

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
