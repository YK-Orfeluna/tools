# coding: utf-8

from md2pdf import *

def __main() :

	fType = [("markdown", "*.md")]
	markdown = filedialog.askopenfilename(title="Choose your Markdown-file", filetypes=fType)

	if markdown != "" :
		
		None




if __name__ == "__main__" :

	from tkinter import *
	from tkinter import Tk, ttk, messagebox, filedialog

	w = 40

	root = Tk()
	root.title("md2pdf")
	root.geometry("400x150")

	B1 = ttk.Button(root, text="To convert", command=__main, width=w)
	B1.pack()

	L1 = ttk.Label(root, text="Font-size (default=1.0)")
	L1.pack()

	E1 = ttk.Entry(root, font=("1.0", 12), justify="center", width=w, exportselection="1")
	E1.pack()

	L2 = ttk.Label(root, text="PDF's name (default is same as maekdown's name")
	L2.pack()

	E2 = ttk.Entry(root, font=("1.0", 12), justify="center", width=w)
	E2.pack()

	root.mainloop()
