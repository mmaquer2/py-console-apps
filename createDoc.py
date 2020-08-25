

## ****To Do****
## Inculde a skip function if the user input is null

###SUMMMARY
## creates an empty document based on user format
from docx import Document

doc = Document()

docName = input('what is the name of your document? ')
docHeader = input('What is the paper Title?' )
docFontSize = input('What is the doc font size?' )
docFontType = input('What is the font type?' )

doc.add_heading(docHeader)
doc.save(docName)

open(docName)


