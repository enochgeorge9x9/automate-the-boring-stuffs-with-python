#! python3
#bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
import pyperclip

##text = pyperclip.paste()
text = 'Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars'
#TODO: Seperate lines and add stars.

lines = text.split('\n')
for i in range(len(lines)):  # loop through all indexed in the 'lines' list
    lines[i] = '*' + lines[i]# add star to each string in 'lines' list
text = '\n'.join(lines)
print(text)


print(pyperclip.copy(text))

    
