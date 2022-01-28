from GUI.GUI import *  # importing GUI class.
from File_Manipulation.File_Manipulation import *  # importing file manipulation functions: find files(searches for
# files in directory) and mergepdf() function which merges the pdfs

if __name__ == '__main__':
    window = GUI()  # creating object of GUI class
    window.add_label(x=0, y=1, text='File Browser and PDF Merging Tool', font="comicsans 20")  # adding title
    window.add_label(x=1, y=0, text='Directory to Search')  # Adding another label

    file_directory_var = StringVar()  # variable to store the directory entered by user.
    file_directory_var.set("") # setting the directory to be empty at the start of program.
    status = StringVar()  # status variable, this tells the status of GUI.
    status.set("Ready for processing") # setting the status to be Ready initially.

    window.human_input(x=1, y=1, textvariable=file_directory_var) # calling human_input function which creates a
    # Entry Widget.

    # Files Found
    window.add_label(x=3, y=0, text="Files Found")   # adding a label
    text_box = window.add_text_box(x=3, y=1)  # creating and receiving the text box. This text box stores the files
    # found.

    pdf_list = []  # list containing the pdfs. will be passed to the search button (so that we can store pdf files
    # found) and merge button(so that we can merge these files)

    # Search Button

    window.add_button(2, 0, file_Search, 'Search', file_directory_var, status, text_box, pdf_list) # creating search
    # button. Passing it file_search method which will find all the files in a particular directory.

    # Merge Button

    window.add_button(4, 0, merge_pdfs, "Merge PDFs", pdf_list) # creating merge button. Passing it merge_pdfs function.

    # status bar

    window.add_label(x=5, y=0, pady=100, text='Status')
    window.add_label(x=5, y=1, pady=100, textvariable=status) # label storing the status of GUI.

    window.mainloop()
