import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()

#it returns true if it succesfully opens the link, otherwise false
webbrowser.open('https://www.google.com/maps/place/' + address)

#create a batch file for running this
@py.exe path of the file to run
make this above line in another file known as .bat (Batch file)
