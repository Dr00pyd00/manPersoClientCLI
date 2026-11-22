

BASE_URL = 'http://127.0.0.1:8000/manpage/'

FILENAME = '/tmp/manpersotmp.manp'

COMMENT_PREFIX = '%/%'


TEMPLATE = f'''
{COMMENT_PREFIX} If line starts with '{COMMENT_PREFIX}' : this is a comment, invisible later.

{COMMENT_PREFIX} Enter the title of your page
title:  

{COMMENT_PREFIX} Enter the summary of your page 
summary:              

{COMMENT_PREFIX} Enter a tag or a list of tags
tags: 


--- 

{COMMENT_PREFIX} Start your page here , uncomment sections if you want 

{COMMENT_PREFIX}NAME 

{COMMENT_PREFIX}LIBRARY

{COMMENT_PREFIX}SYNOPSIS 

{COMMENT_PREFIX}DESCRIPTION

{COMMENT_PREFIX}RETURN VALUES 

{COMMENT_PREFIX}ERRORS 

{COMMENT_PREFIX}ATTRIBUTES 

{COMMENT_PREFIX}STANDARDS 

{COMMENT_PREFIX}HISTORY

{COMMENT_PREFIX}EXAMPLES

{COMMENT_PREFIX}SEE ALSO

'''

