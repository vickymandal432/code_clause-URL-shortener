import os
import datetime
from tkinter import*

root = Tk()
root.geometry("400x200")
root.title("URL Shortener")
root.configure(bg="#49A")
url = stringVar()
url_address = stringvar()
def urlshortener():
    urladdress=url.get()
    url_short = pyshorteners.shortener().tinyurl.short(urladdress)
    url_address.set(url_short)
def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)
Label(root, text = "my url shortener", font= "poppins").pack(pady=10)
Entry (root, textvariable=url).pack(pady = 5)
Button(root,text = "Generate Short URL", command=urlshortener).pack(pady=7)
Entry(root, textvariables=url_address).pack(pady=5)
Button(roor,text= "Copy URL" , command = copyurl).pack(pady=5)
root.mainloop()
