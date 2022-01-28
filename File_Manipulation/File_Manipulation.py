import PyPDF2
import os
from tkinter import *
import tkinter.messagebox as tmsg

from logger.logger import *

log_obj = Logger(filename="log.log")  # creating log object.


def file_Search(*args):
    """function responsible for searching files in a directory. Directory is stored in file_directory_var which we
    will receive as args[0][0]. """

    # args[0][0] is file_directory_var
    # args[0][1] is the status
    # args[0][2] is the text box

    try:
        log_obj.add_log("file search method called")
        file_directory_var = args[0][0]  # Getting file_directory_var. This variable keeps track of the directory
        # entered by human.
        status = args[0][1]  # Getting the status of GUI. This variable tracks the status of GUI.
        text_box = args[0][2]  # Getting the text box. This text box stores the found files.
        pdf_list = args[0][3]  # pdf list. stores the pdfs found in the directory.

        directory = file_directory_var.get()  # getting directory from where we want to find the files.
        total_files = 0  # total files found in the directory.

        status.set("Processing " + directory)  # updating the status variable.
        log_obj.add_log("Processing for {}".format(directory))

        for x, dirs, files in os.walk(directory, topdown=False):  # performing walk on the directory to get all the
            # files.
            for name in files:

                file = os.path.join(x, name)
                text_box.insert(END, file + "\n")
                total_files += 1

                if file.split('.')[-1] == 'pdf': # checking if file is pdf.
                    pdf_list.append(file)

            for name in dirs:
                file = os.path.join(x, name)

                text_box.insert(END, file + "\n")
                total_files += 1

                if file.split('.')[-1] == 'pdf':  # checking if file is pdf.
                    pdf_list.append(file)

        status.set("Done!!!") # updating the status variable.
        tmsg.showinfo("Done Processing", "Found {} files".format(str(total_files)))
        log_obj.add_log("Processing successful. Found {} files".format(str(total_files)))

    except Exception as e:
        log_obj.add_log("Error occurred", mode='error')
        log_obj.add_log(str(e), mode='error')


def merge_pdfs(*args):
    """ function responsible for merging the pdf files."""
    try:
        pdf_list = args[0][0]

        log_obj.add_log("merge_pdfs method called")

        if len(pdf_list) == 0:
            tmsg.showinfo("NO PDFS!!!", "No pdf files. Please Do another directory search  !!!!")
            log_obj.add_log(" No PDFs present here")


        else:

            final_path = os.path.join(os.curdir, "result.pdf")

            if os.path.exists(final_path):
                os.remove(final_path)

            merger = PyPDF2.PdfFileMerger(strict=False) # object responsible for merging the pdfs.

            for pdf in pdf_list:

                try:
                    merger.append(pdf)
                except:
                    continue

            merger.write(final_path)

            tmsg.showinfo("PDFs Merged",
                          "Found PDFs have been merged. The Final file can be found at {}".format(final_path))
            log_obj.add_log("PDFs merged successfully")

    except Exception as e:
        log_obj.add_log("Error occurred", mode='error')
        log_obj.add_log(str(e), mode='error')
