from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator
from googletrans import LANGUAGES


app = Flask(__name__)

turkısh_language = {
    "en": "English",
    "tr": "Turkish",
    "de": "German",
    "fr": "French",
    "es": "Spanish",
    "it": "Italian",
    "ru": "Russian",
    "zh-cn": "Chinese (Simplified)",
    "ja": "Japanese",
    "ko": "Korean",
    "ar": "Arabic",
    "pt": "Portuguese",
    "hi": "Hindi",
    "nl": "Dutch",
    "sv": "Swedish",
    "el": "Greek",
    "pl": "Polish",
    "no": "Norwegian",
    "da": "Danish",
    "fi": "Finnish",
    "cs": "Czech",
    "ro": "Romanian",
    "hu": "Hungarian",
    "he": "Hebrew",
    "th": "Thai",
    "vi": "Vietnamese",
}


@app.route("/")
def index():
    return render_template("index.html", LANGUAGES=turkısh_language)


@app.route("/translate", methods=["POST"])
def translate_text():
    data = request.get_json()
    text = data.get("text")
    source_lang = data.get("source_lang", "en")
    destination_lang = data.get("destination_lang", "tr")

    if not text:
        return jsonify({"error": "Text to translate is required"}), 400

    try:
        translated_text = GoogleTranslator(
            source=source_lang, target=destination_lang
        ).translate(text)
        return jsonify({"translated_text": translated_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
