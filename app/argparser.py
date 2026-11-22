import argparse 

parser = argparse.ArgumentParser() 
parser.add_argument('-l', '--list', action='store_true', help='Display all manpage')
parser.add_argument('-t','--tag', type=str, help='Filer for tag during --list')
parser.add_argument('-c','--create', action='store_true', help='Open vim for create new page')
parser.add_argument('-d', '--delete', type=str, help='Delete a page by title')
parser.add_argument('title', nargs='?', help='Display a detail page by title')
