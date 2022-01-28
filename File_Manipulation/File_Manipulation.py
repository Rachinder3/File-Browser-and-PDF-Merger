import PyPDF2
import os
from tkinter import *
import tkinter.messagebox as tmsg

from logger.logger import *

log_obj = Logger(filename="log.log")


def file_Search(*args):
    # args[0][0] is file_directory_var
    # args[0][1] is the status
    # args[0][2] is the text box

    try:
        log_obj.add_log("file search method called")
        file_directory_var = args[0][0]
        status = args[0][1]
        text_box = args[0][2]
        pdf_list = args[0][3]

        directory = file_directory_var.get()
        total_files = 0

        status.set("Processing " + directory)
        log_obj.add_log("Processing for {}".format(directory))

        for x, dirs, files in os.walk(directory, topdown=False):
            for name in files:
                # print(os.path.join(x, name))
                file = os.path.join(x, name)
                text_box.insert(END, file + "\n")
                total_files += 1

                if file.split('.')[-1] == 'pdf':
                    pdf_list.append(file)

            for name in dirs:
                file = os.path.join(x, name)
                # print(os.path.join(x, name))
                text_box.insert(END, file + "\n")
                total_files += 1

                if file.split('.')[-1] == 'pdf':
                    pdf_list.append(file)

        status.set("Done!!!")
        tmsg.showinfo("Done Processing", "Found {} files".format(str(total_files)))
        log_obj.add_log("Processing successful. Found {} files".format(str(total_files)))

    except Exception as e:
        log_obj.add_log("Error occurred", mode='error')
        log_obj.add_log(str(e), mode='error')


def merge_pdfs(*args):
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

            merger = PyPDF2.PdfFileMerger(strict=False)

            for pdf in pdf_list:
                # print(pdf)
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
