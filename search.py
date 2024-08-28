from tkinter import *
from tkinter import messagebox
import json


class Find:
    def __init__(self):
        pass

    def search(self, date):

        try:
            with open("data.json") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")

        else:
            if date in data:
                str = ""
                c = 1
                for dict in data[date]:
                    title = dict["title"]
                    description = dict["description"]
                    str = (
                        f" {str}\n "
                        + f" \nTask - {c}"
                        + f" \nTitle : {title} "
                        + f" \nDescription: {description} \n"
                    )
                    c = c + 1
                messagebox.showinfo(title=date, message=f"List of Tasks\n {str}")

            else:
                messagebox.showinfo(title="Error", message="No such todo exist")
