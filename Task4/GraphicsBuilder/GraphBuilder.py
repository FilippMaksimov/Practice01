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

th_zero = Label(canvas, text='Not using threads')
th_zero.place(x=30, y=25)
th_two = Label(canvas, text='Using two threads')
th_two.place(x=350, y=25)
th_four = Label(canvas, text='Using four threads')
th_four.place(x=30, y=280)
th_eight = Label(canvas, text='Using eight threads')
th_eight.place(x=350, y=280)


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
    plt.xlabel('row x column')
    plt.ylabel('operation time, ms')
    plt.legend(['CShrap', 'Java', 'Python'], loc='upper left')
    fig.savefig('integer_zero.png')
    # plt.show()
    img1 = PhotoImage(file='integer_zero.png')
    img1 = img1.subsample(2, 2)
    label1 = Label(canvas)
    label1.image = img1
    label1['image'] = label1.image
    label1.place(x=20, y=50)

    # TWO THREADS
    fig2 = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    # C#
    plt.plot([csharp50_loader()[3], csharp100_loader()[3], csharp200_loader()[3]],
             [csharp50_loader()[2], csharp100_loader()[2], csharp200_loader()[2]], 'ro-')
    # Java
    plt.plot([java50_loader()[3], java100_loader()[3], java200_loader()[3]],
             [java50_loader()[2], java100_loader()[2], java200_loader()[2]], 'go-')
    # Python
    plt.plot([python50_loader()[3], python100_loader()[3], python200_loader()[3]],
             [python50_loader()[2], python100_loader()[2], python200_loader()[2]], 'bo-')
    plt.xlabel('row x column')
    plt.ylabel('operation time, ms')
    plt.legend(['CShrap', 'Java', 'Python'], loc='upper left')
    fig2.savefig('integer_two.png')
    # plt.show()
    img1 = PhotoImage(file='integer_two.png')
    img1 = img1.subsample(2, 2)
    label1 = Label(canvas)
    label1.image = img1
    label1['image'] = label1.image
    label1.place(x=350, y=50)

    # FOUR THREADS
    fig3 = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    # C#
    plt.plot([csharp50_loader()[5], csharp100_loader()[5], csharp200_loader()[5]],
             [csharp50_loader()[4], csharp100_loader()[4], csharp200_loader()[4]], 'ro-')
    # Java
    plt.plot([java50_loader()[5], java100_loader()[5], java200_loader()[5]],
             [java50_loader()[4], java100_loader()[4], java200_loader()[4]], 'go-')
    # Python
    plt.plot([python50_loader()[5], python100_loader()[5], python200_loader()[5]],
             [python50_loader()[4], python100_loader()[4], python200_loader()[4]], 'bo-')
    plt.xlabel('row x column')
    plt.ylabel('operation time, ms')
    plt.legend(['CShrap', 'Java', 'Python'], loc='upper left')
    fig3.savefig('integer_four.png')
    # plt.show()
    img1 = PhotoImage(file='integer_four.png')
    img1 = img1.subsample(2, 2)
    label1 = Label(canvas)
    label1.image = img1
    label1['image'] = label1.image
    label1.place(x=20, y=300)

    # EIGHT THREADS
    fig4 = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    # C#
    plt.plot([csharp50_loader()[7], csharp100_loader()[7], csharp200_loader()[7]],
             [csharp50_loader()[6], csharp100_loader()[6], csharp200_loader()[6]], 'ro-')
    # Java
    plt.plot([java50_loader()[7], java100_loader()[7], java200_loader()[7]],
             [java50_loader()[6], java100_loader()[6], java200_loader()[6]], 'go-')
    # Python
    plt.plot([python50_loader()[7], python100_loader()[7], python200_loader()[7]],
             [python50_loader()[6], python100_loader()[6], python200_loader()[6]], 'bo-')
    plt.xlabel('row x column')
    plt.ylabel('operation time, ms')
    plt.legend(['CShrap', 'Java', 'Python'], loc='upper left')
    fig4.savefig('integer_eight.png')
    # plt.show()
    img1 = PhotoImage(file='integer_eight.png')
    img1 = img1.subsample(2, 2)
    label1 = Label(canvas)
    label1.image = img1
    label1['image'] = label1.image
    label1.place(x=350, y=300)


def btn_bigint_click():
    dpi = 80
    # ZERO THREADS
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    # C#
    plt.plot([csharp50_loader()[9], csharp100_loader()[9], csharp200_loader()[9]],
             [csharp50_loader()[8], csharp100_loader()[8], csharp200_loader()[8]], 'ro-')
    # Java
    plt.plot([java50_loader()[9], java100_loader()[9], java200_loader()[9]],
             [java50_loader()[8], java100_loader()[8], java200_loader()[8]], 'go-')
    # Python
    plt.plot([python50_loader()[9], python100_loader()[9], python200_loader()[9]],
             [python50_loader()[8], python100_loader()[8], python200_loader()[8]], 'bo-')
    plt.xlabel('row x column')
    plt.ylabel('operation time, ms')
    plt.legend(['CShrap', 'Java', 'Python'], loc='upper left')
    fig.savefig('bigint_zero.png')
    # plt.show()
    img1 = PhotoImage(file='bigint_zero.png')
    img1 = img1.subsample(2, 2)
    label1 = Label(canvas)
    label1.image = img1
    label1['image'] = label1.image
    label1.place(x=20, y=50)

    # TWO THREADS
    fig2 = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    # C#
    plt.plot([csharp50_loader()[11], csharp100_loader()[11], csharp200_loader()[11]],
             [csharp50_loader()[10], csharp100_loader()[10], csharp200_loader()[10]], 'ro-')
    # Java
    plt.plot([java50_loader()[11], java100_loader()[11], java200_loader()[11]],
             [java50_loader()[10], java100_loader()[10], java200_loader()[10]], 'go-')
    # Python
    plt.plot([python50_loader()[11], python100_loader()[11], python200_loader()[11]],
             [python50_loader()[10], python100_loader()[10], python200_loader()[10]], 'bo-')
    plt.xlabel('row x column')
    plt.ylabel('operation time, ms')
    plt.legend(['CShrap', 'Java', 'Python'], loc='upper left')
    fig2.savefig('bigint_two.png')
    # plt.show()
    img1 = PhotoImage(file='bigint_two.png')
    img1 = img1.subsample(2, 2)
    label1 = Label(canvas)
    label1.image = img1
    label1['image'] = label1.image
    label1.place(x=350, y=50)

    # FOUR THREADS
    fig3 = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    # C#
    plt.plot([csharp50_loader()[13], csharp100_loader()[13], csharp200_loader()[13]],
             [csharp50_loader()[12], csharp100_loader()[12], csharp200_loader()[12]], 'ro-')
    # Java
    plt.plot([java50_loader()[13], java100_loader()[13], java200_loader()[13]],
             [java50_loader()[12], java100_loader()[12], java200_loader()[12]], 'go-')
    # Python
    plt.plot([python50_loader()[13], python100_loader()[13], python200_loader()[13]],
             [python50_loader()[12], python100_loader()[12], python200_loader()[12]], 'bo-')
    plt.xlabel('row x column')
    plt.ylabel('operation time, ms')
    plt.legend(['CShrap', 'Java', 'Python'], loc='upper left')
    fig3.savefig('bigint_four.png')
    # plt.show()
    img1 = PhotoImage(file='bigint_four.png')
    img1 = img1.subsample(2, 2)
    label1 = Label(canvas)
    label1.image = img1
    label1['image'] = label1.image
    label1.place(x=20, y=300)

    # EIGHT THREADS
    fig4 = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    # C#
    plt.plot([csharp50_loader()[15], csharp100_loader()[15], csharp200_loader()[15]],
             [csharp50_loader()[14], csharp100_loader()[14], csharp200_loader()[14]], 'ro-')
    # Java
    plt.plot([java50_loader()[15], java100_loader()[15], java200_loader()[15]],
             [java50_loader()[14], java100_loader()[14], java200_loader()[14]], 'go-')
    # Python
    plt.plot([python50_loader()[15], python100_loader()[15], python200_loader()[15]],
             [python50_loader()[14], python100_loader()[14], python200_loader()[14]], 'bo-')
    plt.xlabel('row x column')
    plt.ylabel('operation time, ms')
    plt.legend(['CShrap', 'Java', 'Python'], loc='upper left')
    fig4.savefig('bigint_eight.png')
    # plt.show()
    img1 = PhotoImage(file='bigint_eight.png')
    img1 = img1.subsample(2, 2)
    label1 = Label(canvas)
    label1.image = img1
    label1['image'] = label1.image
    label1.place(x=350, y=300)


def btn_float_int():
    dpi = 80
    # ZERO THREADS
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    # C#
    plt.plot([csharp50_loader()[17], csharp100_loader()[17], csharp200_loader()[17]],
             [csharp50_loader()[16], csharp100_loader()[16], csharp200_loader()[16]], 'ro-')
    # Java
    plt.plot([java50_loader()[17], java100_loader()[17], java200_loader()[17]],
             [java50_loader()[16], java100_loader()[16], java200_loader()[16]], 'go-')
    # Python
    plt.plot([python50_loader()[17], python100_loader()[17], python200_loader()[17]],
             [python50_loader()[16], python100_loader()[16], python200_loader()[16]], 'bo-')
    plt.xlabel('row x column')
    plt.ylabel('operation time, ms')
    plt.legend(['CShrap', 'Java', 'Python'], loc='upper left')
    fig.savefig('double_zero.png')
    # plt.show()
    img1 = PhotoImage(file='double_zero.png')
    img1 = img1.subsample(2, 2)
    label1 = Label(canvas)
    label1.image = img1
    label1['image'] = label1.image
    label1.place(x=20, y=50)

    # TWO THREADS
    fig2 = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    # C#
    plt.plot([csharp50_loader()[19], csharp100_loader()[19], csharp200_loader()[19]],
             [csharp50_loader()[18], csharp100_loader()[18], csharp200_loader()[18]], 'ro-')
    # Java
    plt.plot([java50_loader()[19], java100_loader()[19], java200_loader()[19]],
             [java50_loader()[18], java100_loader()[18], java200_loader()[18]], 'go-')
    # Python
    plt.plot([python50_loader()[19], python100_loader()[19], python200_loader()[19]],
             [python50_loader()[18], python100_loader()[18], python200_loader()[18]], 'bo-')
    plt.xlabel('row x column')
    plt.ylabel('operation time, ms')
    plt.legend(['CShrap', 'Java', 'Python'], loc='upper left')
    fig2.savefig('double_two.png')
    # plt.show()
    img1 = PhotoImage(file='double_two.png')
    img1 = img1.subsample(2, 2)
    label1 = Label(canvas)
    label1.image = img1
    label1['image'] = label1.image
    label1.place(x=350, y=50)

    # FOUR THREADS
    fig3 = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    # C#
    plt.plot([csharp50_loader()[21], csharp100_loader()[21], csharp200_loader()[21]],
             [csharp50_loader()[20], csharp100_loader()[20], csharp200_loader()[20]], 'ro-')
    # Java
    plt.plot([java50_loader()[21], java100_loader()[21], java200_loader()[21]],
             [java50_loader()[20], java100_loader()[20], java200_loader()[20]], 'go-')
    # Python
    plt.plot([python50_loader()[21], python100_loader()[21], python200_loader()[21]],
             [python50_loader()[20], python100_loader()[20], python200_loader()[20]], 'bo-')
    plt.xlabel('row x column')
    plt.ylabel('operation time, ms')
    plt.legend(['CShrap', 'Java', 'Python'], loc='upper left')
    fig3.savefig('double_four.png')
    # plt.show()
    img1 = PhotoImage(file='double_four.png')
    img1 = img1.subsample(2, 2)
    label1 = Label(canvas)
    label1.image = img1
    label1['image'] = label1.image
    label1.place(x=20, y=300)

    # EIGHT THREADS
    fig4 = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    # C#
    plt.plot([csharp50_loader()[23], csharp100_loader()[23], csharp200_loader()[23]],
             [csharp50_loader()[22], csharp100_loader()[22], csharp200_loader()[22]], 'ro-')
    # Java
    plt.plot([java50_loader()[23], java100_loader()[23], java200_loader()[23]],
             [java50_loader()[22], java100_loader()[22], java200_loader()[22]], 'go-')
    # Python
    plt.plot([python50_loader()[23], python100_loader()[23], python200_loader()[23]],
             [python50_loader()[22], python100_loader()[22], python200_loader()[22]], 'bo-')
    plt.xlabel('row x column')
    plt.ylabel('operation time, ms')
    plt.legend(['CShrap', 'Java', 'Python'], loc='upper left')
    fig4.savefig('double_eight.png')
    # plt.show()
    img1 = PhotoImage(file='double_eight.png')
    img1 = img1.subsample(2, 2)
    label1 = Label(canvas)
    label1.image = img1
    label1['image'] = label1.image
    label1.place(x=350, y=300)


btn_int = Button(root, text='Load Graphic for Integer', command=btn_int_click)
btn_int.pack()
btn_bigint = Button(root, text='Load Graphic for BigInt', command=btn_bigint_click)
btn_bigint.pack()
btn_float = Button(root, text='Load Graphics for Floats(Double)', command=btn_float_int)
btn_float.pack()

root.mainloop()
