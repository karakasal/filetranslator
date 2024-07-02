from translate import Translator

translator= Translator(to_lang="ja")

with open("text.txt", mode="r", encoding="utf-8") as file:
    text = file.read()
    translated_text = translator.translate(text)
    with open("text.txt", mode="a", encoding="utf-8") as file:
        file.write(f"\n{translated_text}")
