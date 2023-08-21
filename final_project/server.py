from translator import englishToFrench, frenchToEnglish
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    try:
        french_translation = englishToFrench(textToTranslate)
        return textToTranslate + " was translated to " + french_translation
    except Exception as e:
        return str(e)

@app.route("/frenchToEnglish")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    try:
        english_translation = frenchToEnglish(textToTranslate)
        return textToTranslate + " was translated to " + english_translation
    except Exception as e:
        return str(e)

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
