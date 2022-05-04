"""
A program that sores below book information:
Title, Author
Year, ISBN

User can:
    1. View all records
    2. Search an entry
    3. Add new entry
    4. Update an entry
    5. Delete an entry
    6. Close the program
"""

from tkinter import *
from book_store_backend import Database

database = Database("books.db")


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        entry1.delete(0, END)
        entry1.insert(END, selected_tuple[1])
        entry2.delete(0, END)
        entry2.insert(END, selected_tuple[2])
        entry3.delete(0, END)
        entry3.insert(END, selected_tuple[3])
        entry4.delete(0, END)
        entry4.insert(END, selected_tuple[4])
    except IndexError:
        pass
    pass


def view_command():
    # Ensure the list1 is empty before printing new information
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)
    pass


def search_command():
    list1.delete(0, END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)
        pass
    pass


def delete_command():
    database.delete(selected_tuple[0])
    pass


def update_command():
    database.update(selected_tuple[0], title_text.get(), author_text.get(),
                    year_text.get(), isbn_text.get())
    pass


def insert_command():
    database.insert(
        title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(),
                 year_text.get(), isbn_text.get()))
    pass


window = Tk()
window.wm_title("BookStore")

# Labels
label1 = Label(window, text="Title")
label1.grid(row=0, column=0)

label2 = Label(window, text="Author")
label2.grid(row=0, column=2)

label3 = Label(window, text="Year")
label3.grid(row=1, column=0)

label4 = Label(window, text="ISBN")
label4.grid(row=1, column=2)

# Entries
title_text = StringVar()
entry1 = Entry(window, textvariable=title_text)
entry1.grid(row=0, column=1)

author_text = StringVar()
entry2 = Entry(window, textvariable=author_text)
entry2.grid(row=0, column=3)

year_text = StringVar()
entry3 = Entry(window, textvariable=year_text)
entry3.grid(row=1, column=1)

isbn_text = StringVar()
entry4 = Entry(window, textvariable=isbn_text)
entry4.grid(row=1, column=3)

# Listbox
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# Add a scrolbar for listbox
scrollbar1 = Scrollbar(window)
scrollbar1.grid(row=2, column=2, rowspan=6)

# Configure the scrollbar to listbox
list1.configure(yscrollcommand=scrollbar1.set)
scrollbar1.configure(command=list1.yview)

# bn
list1.bind('<<ListboxSelect>>', get_selected_row)

# Add the buttons
button1 = Button(window, text="View All", width=12, command=view_command)
button1.grid(row=2, column=3)

button2 = Button(window, text="Search Entry", width=12, command=search_command)
button2.grid(row=3, column=3)

button3 = Button(window, text="Add Entry", width=12, command=insert_command)
button3.grid(row=4, column=3)

button4 = Button(window, text="Update Selected",
                 width=12, command=update_command)
button4.grid(row=5, column=3)

button5 = Button(window, text="Delete Selected",
                 width=12, command=delete_command)
button5.grid(row=6, column=3)

button6 = Button(window, text="Close", width=12, command=window.destroy)
button6.grid(row=7, column=3)

window.mainloop()
