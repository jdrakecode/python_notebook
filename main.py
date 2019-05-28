from datetime import date
"""
Note Book app

Notes will have three parts
ID
Content
Date/Time
"""
counter = 1
notebook = []
now = date.today()

while counter <=5:
    content = input("What is the note \n> ")
    note_id = counter
    note = (note_id, str(now), content)
    notebook.append(note)
    counter += 1
    print(notebook)
