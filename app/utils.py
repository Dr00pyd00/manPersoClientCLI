
from app.settings import COMMENT_PREFIX


def get_dict_manpage_from_textfile(filename: str) -> dict:
    page_dict: dict = {'tags':[],}

    with open(filename, 'r') as f:
        list_lines = f.readlines() 
        sep_ind = 0

        for ind, item in enumerate(list_lines):
            if item.strip() == '---':
                sep_ind = ind
                break 
        
        header_list = list_lines[:sep_ind] 
        text_list = list_lines[sep_ind + 1:]

    text_complet = '' 
    for l in text_list:
        if l.startswith(COMMENT_PREFIX):
            continue
        text_complet += l 
    page_dict['text'] = text_complet.strip()


    for l in header_list:
        if l.startswith('#'):
            continue 

        if l.startswith('title'):
            p1, sep, p2 = l.partition(':')
            title_input = p2.strip()
            page_dict['title'] = title_input

        if l.startswith('summary'):
            p1, sep, p2 = l.partition(':')
            summmary_input = p2.strip()
            page_dict['summary'] = summmary_input 
        
        if l.startswith('tags'):
            p1, sep, p2 = l.partition(':')
            tags_input_not_cleaned = p2.strip()
            tags_list = tags_input_not_cleaned.split(',')
            tags_input =  [ t.strip() for t in tags_list ] 
            page_dict['tags'] = tags_input 

    return page_dict


