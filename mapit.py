#! python3
# Python Standard libraries
import webbrowser, sys

# 3rd-party liabraries
import pyperclip

# Local libraries

if len(sys.argv) >1:
    #Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    #Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)


