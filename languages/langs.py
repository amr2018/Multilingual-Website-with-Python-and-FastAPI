
import json

def load_lang_data(page_name, lang = 'en'):
    languages = json.load(open(f'languages/{lang}.json', 'r'))
    return languages['web_pages'][0][page_name]

