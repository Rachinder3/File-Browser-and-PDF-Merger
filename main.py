from tkinter import *

from GUI.GUI import *
from File_Manipulation.File_Manipulation import *

if __name__ == '__main__':
    window = GUI()
    window.add_label(x=0, y=1, text='File Browser and PDF Merging Tool', font="comicsans 20")  # adding title
    window.add_label(x=1, y=0, text='Directory to Search')  # Adding another label

    file_directory_var = StringVar()
    file_directory_var.set("")
    status = StringVar()  # status variable
    status.set("Ready for processing")

    window.human_input(x=1, y=1, textvariable=file_directory_var)

    # Files Found
    window.add_label(x=3, y=0, text="Files Found")
    text_box = window.add_text_box(x=3, y=1)  # creating and receiving the text box

    pdf_list = []

    # Search Button

    window.add_button(2, 0, file_Search, 'Search', file_directory_var, status, text_box, pdf_list)

    # Merge Button

    window.add_button(4, 0, merge_pdfs, "Merge PDFs", pdf_list)

    # status bar

    window.add_label(x=5, y=0, pady=100, text='Status')
    window.add_label(x=5, y=1, pady=100, textvariable=status)

    window.mainloop()
