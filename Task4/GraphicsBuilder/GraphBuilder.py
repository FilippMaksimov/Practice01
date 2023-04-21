from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt

from Task4.GraphicsBuilder.DataLoader import csharp50_loader, csharp100_loader, csharp200_loader, java50_loader, \
    java100_loader, java200_loader, python50_loader, python200_loader, python100_loader

root = Tk()
root.title('Graphics Builder')
root.geometry('700x700')

canvas = Canvas(root, height=500, width=600)
canvas.pack()


def btn_int_click():
    dpi = 80
    # ZERO THREADS
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    # C#
    plt.plot([csharp50_loader()[1], csharp100_loader()[1], csharp200_loader()[1]],
             [csharp50_loader()[0], csharp100_loader()[0], csharp200_loader()[0]], 'ro-')
    # Java
    plt.plot([java50_loader()[1], java100_loader()[1], java200_loader()[1]],
             [java50_loader()[0], java100_loader()[0], java200_loader()[0]], 'go-')
    # Python
    plt.plot([python50_loader()[1], python100_loader()[1], python200_loader()[1]],
             [python50_loader()[0], python100_loader()[0], python200_loader()[0]], 'bo-')
    plt.legend(['CShrap', 'Java', 'Python'], loc='upper left')
    fig.savefig('integer_zero.png')
    plt.show()
    img1 = canvas.create_image(0, 0, anchor=NW, image='integer_zero.png')


def btn_bigint_click():
    messagebox.showinfo(message="h2")


def btn_float_int():
    messagebox.showinfo(message='h')


def btn_reset():
    messagebox.showinfo(message='h3')


btn_int = Button(root, text='Load Graphic for Integer', command=btn_int_click)
btn_int.pack()
btn_bigint = Button(root, text='Load Graphic for BigInt', command=btn_bigint_click)
btn_bigint.pack()
btn_float = Button(root, text='Load Graphics for Floats(Double)', command=btn_float_int)
btn_float.pack()
btn_reset = Button(root, text='Reset', command=btn_reset)
btn_reset.pack()

root.mainloop()

