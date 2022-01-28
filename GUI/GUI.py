from logger.logger import Logger
from tkinter import *
import tkinter.messagebox as tmsg
from functools import partial
from File_Manipulation.File_Manipulation import *


class GUI(Tk):
    """Implements the GUI class"""

    __log_obj = Logger(filename="log.log") # creating log file object

    def __init__(self, geo_width="1200", geo_height="600",
                 geo_max_width=1200, geo_max_height=600,
                 geo_min_width=1200, geo_min_height=600,
                 icon_path="icon.ico", title="File Browser and PDF Merging Tool", bg="black"):
        super(GUI, self).__init__()  # calling parent class constructor
        self.title(title) # setting the title of GUI object
        self.geometry("{}x{}".format(geo_height, geo_width)) # setting the geometry of GUI object.
        self.maxsize(geo_max_width, geo_max_height) # setting the maxsize of GUI object.
        self.minsize(geo_min_width, geo_min_height) # setting the minsize of GUI object.
        self.iconbitmap(icon_path) # setting the icon of GUI
        self.config(bg=bg) # setting the background of GUI

        GUI.__log_obj.add_log("GUI Initialized") # adding the log

    def add_label(self, x, y, text="",
                  bg="Pink", fg="black", font="comicsans 10",
                  relief=SUNKEN, pady=20, padx=10, textvariable=None):
        """Function responsible for creating any label within the GUI."""
        try:
            if textvariable == None:
                self.label = Label(self, text=text, bg=bg, fg=fg, font=font, relief=relief) # creating a label for
                # GUI object.
                GUI.__log_obj.add_log("Label {} created".format(text))
            else:
                self.label = Label(self, textvariable=textvariable, bg=bg, fg=fg, font=font, relief=relief) # creating a label
                # for GUI object
                GUI.__log_obj.add_log("Label {} created".format(textvariable))

            self.label.grid(row=x, column=y, pady=pady, padx=padx)


        except Exception as e:
            GUI.__log_obj.add_log("Error occured", mode='error')
            GUI.__log_obj.add_log(str(e), mode='error')

    def human_input(self, x, y, textvariable, borderwidth=2, relief=SUNKEN, padx=10, pady=20):
        """function responsible for creating Entry Widgets"""
        try:
            self.entry_widget = Entry(self, textvariable=textvariable, borderwidth=borderwidth, relief=relief) # creating the entry widget
            self.entry_widget.grid(row=x, column=y, pady=pady, padx=padx)
            GUI.__log_obj.add_log("Entry widget with name : {} initialized".format(textvariable))


        except Exception as e:
            GUI.__log_obj.add_log("Error occured", mode='error')
            GUI.__log_obj.add_log(str(e), mode='error')

    def add_button(self, x, y, command, text, *args, bg='pink', fg='black', padx=10, pady=20):
        """function responsible for creating and adding buttons to GUI object."""
        try:
            self.button = Button(self, text=text, command=partial(command, args), bg=bg, fg=fg)
            self.button.grid(row=x, column=y, padx=padx, pady=pady)
            GUI.__log_obj.add_log("button with name {} created".format(text))
        except Exception as e:
            GUI.__log_obj.add_log("Error occured", mode='error')
            GUI.__log_obj.add_log(str(e), mode='error')

    def add_text_box(self, x, y, width=90, height=5, padx=10, pady=20):
        """function responsible for creating and adding text boxes."""
        try:
            text_box = Text(self, width=width, height=height) # creating the text box.
            text_box.grid(row=x, column=y, padx=padx, pady=pady)
            GUI.__log_obj.add_log("Text Box created")
            return text_box
        except Exception as e:
            GUI.__log_obj.add_log("Error occured", mode='error')
            GUI.__log_obj.add_log(str(e), mode='error')
