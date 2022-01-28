
# File Browser and PDF Merger

This project aims to build a GUI. 
With this GUI, we can provide a directory and the
application will fetch all the files present in that directory.

Also we have a functionality where in, if there are pdf files in 
the provided directory, we can merge all the pdf files to a single pdf.





## Documentation

### Tech Stack:

1) Python
2) tkinter module to build GUI.
3) PyPDF2 module to merge pdfs.


### Navigation:

The project has been built in 2 ways. 

One way is built via OOPs, second way is by using
Scripting.


##### Files:



###### via OOPS:
1) main.py: Main file of the project. This is the entry point of the project. 
   Implements the objects of classes defined in GUI class in GUI package.


2) logger: Package containing functions and modules for logging.

3) GUI: Package containing the GUI class. This class implements all the functions for 
        widgets implemented in main.py .

4) File Manipulation: Package implementing the File Manipulation functions. Implements 
    the get_file function (which finds all the files in a directory) and merge_pdf function (merges the pdf files 
    found in the directory).

###### via Scripting

File Browser and PDF Merger.ipynb : Python notebook containing the scripting solution for building the GUI.



## Screenshots

![App Screenshot](/screenshots/1.jpg)

![App Screenshot](/screenshots/2.jpg)

![App Screenshot](/screenshots/3.jpg)


