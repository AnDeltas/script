#!/home/cyr/anaconda3/bin/python

import sys
import docx

name = sys.argv[1]

docx = docx.Document(f'{name}.docx')
docText = '\n'.join([paragraph.text for paragraph in docx.paragraphs])
print(docText)
