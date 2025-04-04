# from googletrans import Translator

# def translate_text(text, target_lang):
#     translator = Translator()
#     translated = translator.translate(text, dest=target_lang)
#     return translated.text
from googletrans import Translator

def translate_text(text, target_lang):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except Exception as e:
        return f"Translation Error: {str(e)}"
