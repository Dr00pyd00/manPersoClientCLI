
import sys
import httpx
import pydantic

from app.argparser import parser
from app.services import (  
                          delete_page_by_title,
                          delete_validation,
                          get_all_manpage_titles, 
                          get_detail_page_by_title_service, 
                          create_page
                            )
from app.exceptions import ErrorItemAlreadyExistInDb, ErrorPageNotFound




args = parser.parse_args() 

try:

    if args.list:
        get_all_manpage_titles()

    elif args.tag:
        get_all_manpage_titles(filter=args.tag)

    elif args.title:
        get_detail_page_by_title_service(args.title)

    elif args.create:
            create_page()   
            print('page added!')

    elif args.delete:
        delete_validation(args.delete)


except ErrorPageNotFound as e:
    print(f'No entry for \'{e}\'')
    sys.exit(1)
except ErrorItemAlreadyExistInDb:
    print('ERROR: Title already exist...')
    sys.exit(1)
except pydantic.ValidationError as e:
    print(f'ERROR: pydantic \n-> {e}')
    sys.exit(1)
except httpx.HTTPStatusError as e:
    print(f'ERROR: Server said \n-> status_code: {e.response.status_code} \n->{e.response.text}')
    sys.exit(1)
except httpx.RequestError:
    print('ERROR: Server NOT responde.')
    sys.exit(1)




