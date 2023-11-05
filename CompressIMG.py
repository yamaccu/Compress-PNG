from PIL import Image
import tkinter
from tkinter import filedialog

tk = tkinter
tk.Tk().withdraw()

type = [('PNG','*.png')]
path = tk.filedialog.askopenfilenames(filetypes = type)

for p in path:
    img = Image.open(p)
    #img = img.convert("P", palette=Image.ADAPTIVE, colors=256)
    img = img.quantize(256)

    index1 = p.rfind(r'/')
    index2 = p.rfind('.')
    filename = p[index1+1:index2]
    exportpath = p[0:index1] + "\\" + filename + "-min.png"
    img.save(exportpath)