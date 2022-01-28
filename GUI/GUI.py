from logger.logger import Logger
from tkinter import *
import tkinter.messagebox as tmsg
from functools import partial
from File_Manipulation.File_Manipulation import *


class GUI(Tk):
    # text_box = Text(width=90, height=10)
    __log_obj = Logger(filename="log.log")

    def __init__(self, geo_width="1200", geo_height="600",
                 geo_max_width=1200, geo_max_height=600,
                 geo_min_width=1200, geo_min_height=600,
                 icon_path="icon.ico", title="File Browser and PDF Merging Tool", bg="black"):
        super(GUI, self).__init__()  # calling parent class constructor
        self.title(title)
        self.geometry("{}x{}".format(geo_height, geo_width))
        self.maxsize(geo_max_width, geo_max_height)
        self.minsize(geo_min_width, geo_min_height)
        self.iconbitmap(icon_path)
        self.config(bg=bg)

        GUI.__log_obj.add_log("GUI Initialized")

    def add_label(self, x, y, text="",
                  bg="Pink", fg="black", font="comicsans 10",
                  relief=SUNKEN, pady=20, padx=10, textvariable=None):
        try:
            if textvariable == None:
                self.label = Label(self, text=text, bg=bg, fg=fg, font=font, relief=relief)
                GUI.__log_obj.add_log("Label {} created".format(text))
            else:
                self.label = Label(self, textvariable=textvariable, bg=bg, fg=fg, font=font, relief=relief)
                GUI.__log_obj.add_log("Label {} created".format(textvariable))

            self.label.grid(row=x, column=y, pady=pady, padx=padx)


        except Exception as e:
            GUI.__log_obj.add_log("Error occured", mode='error')
            GUI.__log_obj.add_log(str(e), mode='error')

    def human_input(self, x, y, textvariable, borderwidth=2, relief=SUNKEN, padx=10, pady=20):
        try:
            self.entry_widget = Entry(self, textvariable=textvariable, borderwidth=borderwidth, relief=relief)
            self.entry_widget.grid(row=x, column=y, pady=pady, padx=padx)
            GUI.__log_obj.add_log("Entry widget with name : {} initialized".format(textvariable))


        except Exception as e:
            GUI.__log_obj.add_log("Error occured", mode='error')
            GUI.__log_obj.add_log(str(e), mode='error')

    def add_button(self, x, y, command, text, *args, bg='pink', fg='black', padx=10, pady=20):
        try:
            self.button = Button(self, text=text, command=partial(command, args), bg=bg, fg=fg)
            self.button.grid(row=x, column=y, padx=padx, pady=pady)
            GUI.__log_obj.add_log("button with name {} created".format(text))
        except Exception as e:
            GUI.__log_obj.add_log("Error occured", mode='error')
            GUI.__log_obj.add_log(str(e), mode='error')

    def add_text_box(self, x, y, width=90, height=5, padx=10, pady=20):
        try:
            text_box = Text(self, width=width, height=height)
            text_box.grid(row=x, column=y, padx=padx, pady=pady)
            GUI.__log_obj.add_log("Text Box created")
            return text_box
        except Exception as e:
            GUI.__log_obj.add_log("Error occured", mode='error')
            GUI.__log_obj.add_log(str(e), mode='error')
