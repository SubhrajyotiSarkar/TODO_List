from tkinter import *
from tkinter import messagebox
import json


class Add_data:
    def add(self, date, title, desc):
        if len(date) == 0 or len(title) == 0 or len(desc) == 0:
            messagebox.showinfo(
                title="Warning", message="Don't keep empty parameter fields!"
            )
        else:

            new_data = {
                date: [
                    {
                        "title": title,
                        "description": desc,
                    }
                ]
            }

            try:
                with open("data.json", "r") as file:
                    # Reading old data
                    data = json.load(file)

            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                if date in data:
                    data[date].append({"title": title, "description": desc})
                    # updating data by appending same date tasks
                    data.update(data)
                else:
                    # normally updating tasks of different dates
                    data.update(new_data)
                with open("data.json", "w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
