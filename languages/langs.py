
import json

def load_lang_data(page_name, lang = 'en'):
    languages = json.load(open(
            f'languages/{lang}.json',
            'r', 
            errors='ignore',
            encoding='utf-8'
        )
    )
    
    for i in range(len(languages['web_pages'])):
        try:
            return languages['web_pages'][i][page_name]
        except:
            pass
