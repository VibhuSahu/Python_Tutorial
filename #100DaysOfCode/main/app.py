from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate', methods=['POST'])
def translate():
    translator = Translator()
    data = request.get_json()
    text = data['text']
    result = translator.translate(text, dest="en")  # Translate to English, change "en" to your desired language code

    return {'translation': result.text}


if __name__ == '__main__':
    app.run()
