from googletrans import Translator

# Initialize the Translator object
translator = Translator()

def translate_message(message, src_lang, dest_lang):
    translation = translator.translate(message, src=src_lang, dest=dest_lang)
    return translation.text

