from tkinter import *
import matplotlib.pyplot as plt

import DataLoader as dl


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
    plt.plot([dl.csharp50_loader()[1], dl.csharp100_loader()[1], dl.csharp200_loader()[1]],
             [dl.csharp50_loader()[0], dl.csharp100_loader()[0], dl.csharp200_loader()[0]], 'ro-')
    # Java
    plt.plot([dl.java50_loader()[1], dl.java100_loader()[1], dl.java200_loader()[1]],
             [dl.java50_loader()[0], dl.java100_loader()[0], dl.java200_loader()[0]], 'go-')
    # Python
    plt.plot([dl.python50_loader()[1], dl.python100_loader()[1], dl.python200_loader()[1]],
             [dl.python50_loader()[0], dl.python100_loader()[0], dl.python200_loader()[0]], 'bo-')
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
    plt.plot([dl.csharp50_loader()[3], dl.csharp100_loader()[3], dl.csharp200_loader()[3]],
             [dl.csharp50_loader()[2], dl.csharp100_loader()[2], dl.csharp200_loader()[2]], 'ro-')
    # Java
    plt.plot([dl.java50_loader()[3], dl.java100_loader()[3], dl.java200_loader()[3]],
             [dl.java50_loader()[2], dl.java100_loader()[2], dl.java200_loader()[2]], 'go-')
    # Python
    plt.plot([dl.python50_loader()[3], dl.python100_loader()[3], dl.python200_loader()[3]],
             [dl.python50_loader()[2], dl.python100_loader()[2], dl.python200_loader()[2]], 'bo-')
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
    plt.plot([dl.csharp50_loader()[5], dl.csharp100_loader()[5], dl.csharp200_loader()[5]],
             [dl.csharp50_loader()[4], dl.csharp100_loader()[4], dl.csharp200_loader()[4]], 'ro-')
    # Java
    plt.plot([dl.java50_loader()[5], dl.java100_loader()[5], dl.java200_loader()[5]],
             [dl.java50_loader()[4], dl.java100_loader()[4], dl.java200_loader()[4]], 'go-')
    # Python
    plt.plot([dl.python50_loader()[5], dl.python100_loader()[5], dl.python200_loader()[5]],
             [dl.python50_loader()[4], dl.python100_loader()[4], dl.python200_loader()[4]], 'bo-')
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
    plt.plot([dl.csharp50_loader()[7], dl.csharp100_loader()[7], dl.csharp200_loader()[7]],
             [dl.csharp50_loader()[6], dl.csharp100_loader()[6], dl.csharp200_loader()[6]], 'ro-')
    # Java
    plt.plot([dl.java50_loader()[7], dl.java100_loader()[7], dl.java200_loader()[7]],
             [dl.java50_loader()[6], dl.java100_loader()[6], dl.java200_loader()[6]], 'go-')
    # Python
    plt.plot([dl.python50_loader()[7], dl.python100_loader()[7], dl.python200_loader()[7]],
             [dl.python50_loader()[6], dl.python100_loader()[6], dl.python200_loader()[6]], 'bo-')
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
    plt.plot([dl.csharp50_loader()[9], dl.csharp100_loader()[9], dl.csharp200_loader()[9]],
             [dl.csharp50_loader()[8], dl.csharp100_loader()[8], dl.csharp200_loader()[8]], 'ro-')
    # Java
    plt.plot([dl.java50_loader()[9], dl.java100_loader()[9], dl.java200_loader()[9]],
             [dl.java50_loader()[8], dl.java100_loader()[8], dl.java200_loader()[8]], 'go-')
    # Python
    plt.plot([dl.python50_loader()[9], dl.python100_loader()[9], dl.python200_loader()[9]],
             [dl.python50_loader()[8], dl.python100_loader()[8], dl.python200_loader()[8]], 'bo-')
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
    plt.plot([dl.csharp50_loader()[11], dl.csharp100_loader()[11], dl.csharp200_loader()[11]],
             [dl.csharp50_loader()[10], dl.csharp100_loader()[10], dl.csharp200_loader()[10]], 'ro-')
    # Java
    plt.plot([dl.java50_loader()[11], dl.java100_loader()[11], dl.java200_loader()[11]],
             [dl.java50_loader()[10], dl.java100_loader()[10], dl.java200_loader()[10]], 'go-')
    # Python
    plt.plot([dl.python50_loader()[11], dl.python100_loader()[11], dl.python200_loader()[11]],
             [dl.python50_loader()[10], dl.python100_loader()[10], dl.python200_loader()[10]], 'bo-')
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
    plt.plot([dl.csharp50_loader()[13], dl.csharp100_loader()[13], dl.csharp200_loader()[13]],
             [dl.csharp50_loader()[12], dl.csharp100_loader()[12], dl.csharp200_loader()[12]], 'ro-')
    # Java
    plt.plot([dl.java50_loader()[13], dl.java100_loader()[13], dl.java200_loader()[13]],
             [dl.java50_loader()[12], dl.java100_loader()[12], dl.java200_loader()[12]], 'go-')
    # Python
    plt.plot([dl.python50_loader()[13], dl.python100_loader()[13], dl.python200_loader()[13]],
             [dl.python50_loader()[12], dl.python100_loader()[12], dl.python200_loader()[12]], 'bo-')
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
    plt.plot([dl.csharp50_loader()[15], dl.csharp100_loader()[15], dl.csharp200_loader()[15]],
             [dl.csharp50_loader()[14], dl.csharp100_loader()[14], dl.csharp200_loader()[14]], 'ro-')
    # Java
    plt.plot([dl.java50_loader()[15], dl.java100_loader()[15], dl.java200_loader()[15]],
             [dl.java50_loader()[14], dl.java100_loader()[14], dl.java200_loader()[14]], 'go-')
    # Python
    plt.plot([dl.python50_loader()[15], dl.python100_loader()[15], dl.python200_loader()[15]],
             [dl.python50_loader()[14], dl.python100_loader()[14], dl.python200_loader()[14]], 'bo-')
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
    plt.plot([dl.csharp50_loader()[17], dl.csharp100_loader()[17], dl.csharp200_loader()[17]],
             [dl.csharp50_loader()[16], dl.csharp100_loader()[16], dl.csharp200_loader()[16]], 'ro-')
    # Java
    plt.plot([dl.java50_loader()[17], dl.java100_loader()[17], dl.java200_loader()[17]],
             [dl.java50_loader()[16], dl.java100_loader()[16], dl.java200_loader()[16]], 'go-')
    # Python
    plt.plot([dl.python50_loader()[17], dl.python100_loader()[17], dl.python200_loader()[17]],
             [dl.python50_loader()[16], dl.python100_loader()[16], dl.python200_loader()[16]], 'bo-')
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
    plt.plot([dl.csharp50_loader()[19], dl.csharp100_loader()[19], dl.csharp200_loader()[19]],
             [dl.csharp50_loader()[18], dl.csharp100_loader()[18], dl.csharp200_loader()[18]], 'ro-')
    # Java
    plt.plot([dl.java50_loader()[19], dl.java100_loader()[19], dl.java200_loader()[19]],
             [dl.java50_loader()[18], dl.java100_loader()[18], dl.java200_loader()[18]], 'go-')
    # Python
    plt.plot([dl.python50_loader()[19], dl.python100_loader()[19], dl.python200_loader()[19]],
             [dl.python50_loader()[18], dl.python100_loader()[18], dl.python200_loader()[18]], 'bo-')
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
    plt.plot([dl.csharp50_loader()[21], dl.csharp100_loader()[21], dl.csharp200_loader()[21]],
             [dl.csharp50_loader()[20], dl.csharp100_loader()[20], dl.csharp200_loader()[20]], 'ro-')
    # Java
    plt.plot([dl.java50_loader()[21], dl.java100_loader()[21], dl.java200_loader()[21]],
             [dl.java50_loader()[20], dl.java100_loader()[20], dl.java200_loader()[20]], 'go-')
    # Python
    plt.plot([dl.python50_loader()[21], dl.python100_loader()[21], dl.python200_loader()[21]],
             [dl.python50_loader()[20], dl.python100_loader()[20], dl.python200_loader()[20]], 'bo-')
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
    plt.plot([dl.csharp50_loader()[23], dl.csharp100_loader()[23], dl.csharp200_loader()[23]],
             [dl.csharp50_loader()[22], dl.csharp100_loader()[22], dl.csharp200_loader()[22]], 'ro-')
    # Java
    plt.plot([dl.java50_loader()[23], dl.java100_loader()[23], dl.java200_loader()[23]],
             [dl.java50_loader()[22], dl.java100_loader()[22], dl.java200_loader()[22]], 'go-')
    # Python
    plt.plot([dl.python50_loader()[23], dl.python100_loader()[23], dl.python200_loader()[23]],
             [dl.python50_loader()[22], dl.python100_loader()[22], dl.python200_loader()[22]], 'bo-')
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
