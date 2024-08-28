from tkinter import *
from add import Add_data
from search import Find
from datetime import date

# get current date
today = date.today()
date_value = today.strftime("%d/%m/%Y")

# Color palette
BLUE = "#3F899B"

add = Add_data()
search = Find()

window = Tk()
window.title("TODO")
window.config(padx=20, pady=30)


# background
bg = PhotoImage(file="background.png")
bg_label = Label(window, image=bg)
bg_label.place(x=-80, y=-40)


# logo import
canvas = Canvas(height=120, width=120, highlightthickness=0)
logo = PhotoImage(file="Todo logo.png")
canvas.create_image(60, 60, image=logo)
canvas.grid(row=0, column=1, padx=30, pady=40)

# Labels
info_label = Label(
    text="Create TODOs. Manage TODOs.\nAll at one place!",
    bg=BLUE,
    fg="white",
    width=25,
    font=("Roboto", 11, "bold"),
)
info_label.grid(row=1, column=1)
date_label = Label(
    text="Date:", bg=BLUE, fg="white", width=15, font=("Arial", 9, "bold")
)
date_label.grid(row=2, column=0)
title_label = Label(
    text="Title:", bg=BLUE, fg="white", width=15, font=("Arial", 9, "bold")
)
title_label.grid(row=3, column=0)
description_label = Label(
    text="Description:", bg=BLUE, fg="white", width=15, font=("Arial", 9, "bold")
)
description_label.grid(row=4, column=0)
search_label = Label(
    text="Search TODO by date:",
    bg=BLUE,
    fg="white",
    width=24,
    font=("Arial", 9, "bold"),
)
search_label.grid(row=5, column=1, columnspan=2)


# Entries
date_entry = Entry(width=55)
date_entry.grid(row=2, column=1, columnspan=3, pady=10)
date_entry.insert(0, date_value)
title_entry = Entry(width=55)
title_entry.grid(row=3, column=1, columnspan=3, pady=10)
description_entry = Entry(width=55)
description_entry.grid(row=4, column=1, columnspan=3, pady=10)
search_entry = Entry(width=12)
search_entry.grid(row=5, column=2)
search_entry.insert(0, date_value)


def on_add():
    global date_entry
    global title_entry
    global description_entry
    add.add(date_entry.get(), title_entry.get(), description_entry.get())
    title_entry.delete(0, END)
    description_entry.delete(0, END)


def on_search():
    global search_entry
    search.search(search_entry.get())


# Buttons
add_button = Button(
    text="Add to TODO List",
    width=15,
    command=on_add,
    fg="white",
    bg="dark blue",
    font=("Arial", 9, "bold"),
)
add_button.grid(row=5, column=0)
search_button = Button(
    text="🔍", width=2, command=on_search, fg="white", bg="dark blue"
)
search_button.grid(row=5, column=3)

window.mainloop()
