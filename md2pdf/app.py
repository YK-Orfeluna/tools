# coding: utf-8

from md2pdf import *

def __main() :

	fType = [("markdown", "*.md")]
	markdown = filedialog.askopenfilename(title="Choose your Markdown-file", filetypes=fType)

	if markdown != "" :
		
		try :
			fontsize = float(E1.get())
			pdf = E2.get()

			app = App(markdown, fontsize, pdf)
			app.main()

			messagebox.showinfo("INFORMATION", "%s is written." %app.pdf)
		except ValueError :
			messagebox.showwarning("WARNING", "Your Inputed Font-size is not 'int' or 'float'.")

def __done() :
	import sys
	sys.exit()

if __name__ == "__main__" :

	from tkinter import *
	from tkinter import Tk, ttk, messagebox, filedialog

	w = 40

	root = Tk()
	root.title("md2pdf")
	root.geometry("400x150")

	B1 = ttk.Button(root, text="To convert", command=__main, width=w)
	B1.pack()

	L1 = ttk.Label(root, text="Font-size")
	L1.pack()

	E1 = ttk.Entry(root, font=("1.0", 12), justify="center", width=w)
	E1.insert(0, "1.0")
	E1.pack()

	L2 = ttk.Label(root, text="PDF's name (default is same as markdown's name")
	L2.pack()

	E2 = ttk.Entry(root, font=("1.0", 12), justify="center", width=w)
	E2.pack()

	B2 = ttk.Button(root, text="EXIT", command=__done, width=w)
	B2.pack()

	root.mainloop()
