import httpx 
import pydoc 
import os 
import subprocess
from pathlib import Path

from app.exceptions import ErrorPageNotFound, ErrorItemAlreadyExistInDb
from app.schemas import ManPageDisplayFullSchema, ManPageCreateSchema
from app.settings import BASE_URL, FILENAME, TEMPLATE
from app.utils import get_dict_manpage_from_textfile

# POST  -----------------------------------------------------------------------------------------------
def create_page(filename: str = FILENAME, template: str = TEMPLATE , base_url: str = BASE_URL):
    try:
        path_file = Path(filename) 
        path_file.write_text(template)

        rc = subprocess.run(['vim', filename])
        if rc.returncode != 0:
            print('subprocess failed, try again...')
            return 

        page_schema = ManPageCreateSchema(**get_dict_manpage_from_textfile(filename))
    finally:
        path_file.unlink(missing_ok=True) #type: ignore

    r = httpx.post(base_url, json=page_schema.model_dump())
    if r.status_code == 409:
        raise ErrorItemAlreadyExistInDb
    # leve une erreur HTTPStatusError si 4xx ou 5xx 
    r.raise_for_status()
   
    print('item created!')




# GET  -----------------------------------------------------------------------------------------------
def get_all_manpage_titles(filter: str|None = None):
    r = httpx.get(BASE_URL + (f'?filter={filter}' if filter is not None else '')) 
    pages = [ ManPageDisplayFullSchema.model_validate(d) for d in r.json() ] 
    if r.status_code == 404:
        raise ErrorPageNotFound
    r.raise_for_status()

    if filter:
        print(f'------ filter: {filter} -----------')
    else:
        print('------ all pages -----------')

    if not pages:
        print('no data!')
        return 
    for page in pages: 
        print(f'-> {page.title}')


def get_detail_page_by_title_service(title: str):
    r = httpx.get(BASE_URL + title) 
    if r.status_code == 404:
        raise ErrorPageNotFound(title)
    page = ManPageDisplayFullSchema.model_validate(r.json()) 
    os.environ.setdefault('PAGER', 'less -c')
    pydoc.pager(page.text)


# PATCH  -----------------------------------------------------------------------------------------------
def update_page_by_title(title: str):
    pass
     


# DELETE  -----------------------------------------------------------------------------------------------

def delete_page_by_title(title: str): 
    r = httpx.delete(BASE_URL + (title if title else ''))
    if r.status_code == 404:
        raise ErrorPageNotFound(title)
    r.raise_for_status() 
    print(f'entry \'{title}\' DELETED')


def delete_validation(title: str):
    while True:
        res = input(f'Are you sure to delete \'{title}\'? ( "yes" or "no" ):\n') 
        if res == 'yes': 
            delete_page_by_title(title)
            break
        elif res == 'no':
            print('Abord of the deleted!')
            break 
        else:
            continue



