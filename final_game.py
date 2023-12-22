from tkinter import*
from PIL import Image,ImageTk
import pygame
import csv


#menu of the game
def gamemenu(w):
    mainmenu = Menu(w)
    m1 = Menu(mainmenu, tearoff=0)
    m1.add_command(label="Play", command=music)
    m1.add_separator()
    m1.add_command(label="Pause", command=stop)
    w.config(menu=mainmenu)
    mainmenu.add_cascade(label="Music", menu=m1)

    m2 = Menu(mainmenu, tearoff=0)
    m2.add_command(label="Exit", command= w.quit)
    mainmenu.add_cascade(label="Exit", menu=m2)



#Music Playin and stoping
pygame.mixer.init()
def music():
    pygame.mixer.music.load("WhatsApp Audio 2022-10-29 at 1.28.20 AM.mpeg")
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()


def winner():
    pygame.mixer.music.load("l.mpeg")
    pygame.mixer.music.play(loops=0)
def loose():
    pygame.mixer.music.load("WhatsApp Audio 2022-11-04 at 1.05.07 AM.mpeg")
    pygame.mixer.music.play(loops=0)



#to display the image
def play_game():
    root.destroy()
    img = []
    name = []
    w_name = []

    def gamemenu(w):
        mainmenu = Menu(w)
        m1 = Menu(mainmenu, tearoff=0)
        m1.add_command(label="Play", command=music)
        m1.add_separator()
        m1.add_command(label="Pause", command=stop)
        w.config(menu=mainmenu)
        mainmenu.add_cascade(label="Music", menu=m1)
        m2 = Menu(mainmenu, tearoff=0)
        m2.add_command(label="Exit", command=quit)
        mainmenu.add_cascade(label="Exit", menu=m2)




    def quit():
        win.destroy()





    def option():

        win.destroy()

##################################################################
        def next_page():
            # win2.destroy()
            music()



            def next_opt():

                def answer():


                    ans = (check1.get() + check2.get() + check3.get() + check4.get()) // 6
                    if ans >= 3:
                        winner()
                    else:
                        loose()

                    l1 = Label(frame1, text=(f"Right answer = {ans} Wrong answer = {4 - ans}"),
                               font="lucida 22 bold", bg="green", fg="white")
                    l1.pack()
                    attempt = 1
                    Button(frame, text="Next->", font="lucida 15 bold", bg="#7fff00", fg="white",
                           command=next_pageActivate).grid(row=3, column=2)

                win3.destroy()
                win2 = Tk()
                win2.geometry("1920x1080")
                win2.resizable(600, 600)
                win2.title("Kids Game")
                win2.iconbitmap("cute-panda-superhero-vector.ico")
                gamemenu(win2)

                f0 = Frame(win2)
                f0.pack(fill="x")

                f2 = Frame(win2)
                f2.pack()
                backgound = Image.open("cute-panda-superhero-vector.jpg")
                pic = ImageTk.PhotoImage(backgound.resize((1400, 900), Image.ANTIALIAS))
                Label(f2, image=pic).pack()

                check1 = IntVar()
                check2 = IntVar()
                check3 = IntVar()
                check4 = IntVar()
                check5 = IntVar()
                check6 = IntVar()
                check7 = IntVar()
                check8 = IntVar()

                Label(f0, text="Chose the correct options ;)", font="georgia 30 bold italic ", bg="#77c442", fg="white",
                      pady=10).pack(fill="x")

                frame1 = LabelFrame(text="Scores", font="georgia 10 bold italic", bg="#77c442", fg="white", padx=10,
                                    pady=10)
                frame1.place(x=400, y=360)

                frame = LabelFrame(text="Options", font="georgia 10 bold italic", bg="#77c442", fg="white", padx=10,
                                   pady=10)
                frame.place(x=536, y=460)

                Checkbutton(frame, text=(f"{name[4]}"), font="bold", variable=check1, bg="#77c442", onvalue=6,
                            offvalue=0).grid(row=2, column=4)
                Checkbutton(frame, text=(f"{name[6]}"), font="bold", variable=check2, bg="#77c442", onvalue=6,
                            offvalue=0).grid(row=0, column=0)
                Checkbutton(frame, text=(f"{name[7]}"), font="bold", variable=check3, bg="#77c442", onvalue=6,
                            offvalue=0).grid(row=2, column=0)
                Checkbutton(frame, text=(f"{name[5]}"), font="bold", variable=check4, bg="#77c442", onvalue=6,
                            offvalue=0).grid(row=1, column=4)
                Checkbutton(frame, text=(f"{w_name[7]}"), font="bold", variable=check5, bg="#77c442", onvalue=6,
                            offvalue=0).grid(row=3, column=0)
                Checkbutton(frame, text=(f"{w_name[6]}"), font="bold", variable=check6, bg="#77c442", onvalue=6,
                            offvalue=0).grid(row=0, column=4)
                Checkbutton(frame, text=(f"{w_name[5]}"), font="bold", variable=check7, bg="#77c442", onvalue=6,
                            offvalue=0).grid(row=1, column=0)
                Checkbutton(frame, text=(f"{w_name[4]}"), font="bold", variable=check8, bg="#77c442", onvalue=6,
                            offvalue=0).grid(row=3, column=4)
                Button(frame, text="Submit", font="lucida 15 bold", bg="#ff0000", fg="white", command=answer).grid(
                    row=1, column=2)


                win2.mainloop()

            img = []
            # name = []
            # w_name = []

            win3 = Tk()
            win3.geometry("1920x1080")
            win3.resizable(600, 600)
            win3.title("Kids Game")
            win3.iconbitmap("cute-panda-superhero-vector.ico")

            f0 = Frame(win3)
            f0.pack(side=TOP, fill="x")
            Label(f0, text="Watch the images ;)", font="georgia 30 bold italic ", bg="#77c442", fg="white",
                  pady=10).pack(
                fill="x")




            l = []
            f = open("database.csv", "r")
            a = csv.reader(f, delimiter=",")
            for i in range(0, 24):
                b = next(a)
                l.append(b)
            print(l)

            for i in range(len(l)):
                a, b = l[i]
                image = Image.open(f"{a}")
                image = image.resize((300, 300), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image=image)
                img.append(photo)
                # name.append(b)

            print(img)
            print(name)

            f1 = Frame(win3, borderwidth=8, relief=SUNKEN)
            f1.pack(padx=100, pady=15, side=LEFT)
            f2 = Frame(win3, borderwidth=8, relief=SUNKEN)
            f2.pack(padx=100, pady=15, side=RIGHT)
            f3 = Frame(win3, borderwidth=6, bg="#77c442", padx=10, pady=5)
            f3.pack(side=TOP, pady=250)

            Label(f1, image=img[4]).pack()
            Label(f1, image=img[5]).pack()
            Label(f2, image=img[6]).pack()
            Label(f2, image=img[7]).pack()
            Button(f3, text="Next->", font="lucida 15 bold", bg="#77c442", fg="white", padx="10", pady="5", command= next_opt).pack()

            gamemenu(win3)

            win3.mainloop()
############################################################

        def answer():
            ans = (check1.get() + check2.get() + check3.get() + check4.get())//6
            if ans >=3:
                winner()
            else:
                loose()

            l1 = Label(frame1, text=(f"Right answer = {ans} Wrong answer = {4-ans}"),font="lucida 22 bold",bg="green",fg="white")
            l1.pack()
            attempt = 1
            Button(frame, text="Next->", font="lucida 15 bold", bg="#7fff00", fg="white",
                   command=next_pageActivate).grid(row=3, column=2)


            # win3 = Tk()
            # Label(win3,text=(f"right answer = {anss[0]}")).pack()
            # win3.mainloop()

        def next_pageActivate():
            win2.destroy()
            next_page()





        win2 = Tk()
        win2.geometry("1920x1080")
        win2.resizable(600, 600)
        win2.title("Kids Game")
        win2.iconbitmap("cute-panda-superhero-vector.ico")
        gamemenu(win2)

        f0 = Frame(win2)
        f0.pack( fill="x")

        f2 = Frame(win2)
        f2.pack()
        backgound = Image.open("cute-panda-superhero-vector.jpg")
        pic = ImageTk.PhotoImage(backgound.resize((1400, 900), Image.ANTIALIAS))
        Label(f2, image=pic).pack()


        check1 = IntVar()
        check2 = IntVar()
        check3 = IntVar()
        check4 = IntVar()
        check5 = IntVar()
        check6 = IntVar()
        check7 = IntVar()
        check8 = IntVar()


        Label(f0, text="Chose the correct options ;)", font="georgia 30 bold italic ", bg="#77c442", fg="white", pady=10).pack(fill="x")

        frame1 = LabelFrame(text="Scores", font="georgia 10 bold italic", bg="#77c442", fg="white", padx=10, pady=10)
        frame1.place(x=400, y=360)


        frame = LabelFrame(text="Options",font="georgia 10 bold italic",bg="#77c442",fg="white",padx=10,pady=10)
        frame.place(x=536,y=460)

        Checkbutton(frame,text=(f"{name[0]}"), font="bold", variable=check1, bg="#77c442", onvalue=6, offvalue=0).grid(row=1,column=0)
        Checkbutton(frame,text=(f"{name[1]}"), font="bold", variable=check2, bg="#77c442", onvalue=6, offvalue=0).grid(row=0,column=4)
        Checkbutton(frame,text=(f"{name[2]}"), font="bold", variable=check3, bg="#77c442", onvalue=6, offvalue=0).grid(row=3,column=0)
        Checkbutton(frame,text=(f"{name[3]}"), font="bold", variable=check4, bg="#77c442", onvalue=6, offvalue=0).grid(row=1,column=4)
        Checkbutton(frame,text=(f"{w_name[0]}"), font="bold", variable=check5, bg="#77c442", onvalue=6, offvalue=0).grid(row=2,column=0)
        Checkbutton(frame,text=(f"{w_name[1]}"), font="bold", variable=check6, bg="#77c442", onvalue=6, offvalue=0).grid(row=0,column=0)
        Checkbutton(frame,text=(f"{w_name[2]}"), font="bold", variable=check7, bg="#77c442", onvalue=6, offvalue=0).grid(row=2,column=4)
        Checkbutton(frame,text=(f"{w_name[3]}"), font="bold", variable=check8, bg="#77c442", onvalue=6, offvalue=0).grid(row=3,column=4)
        Button(frame, text="Submit", font="lucida 15 bold", bg="#ff0000", fg="white", command=answer).grid(row=1,column=2)


        win2.mainloop()

    win = Tk()
    win.geometry("1920x1080")
    win.resizable(600, 600)
    win.title("Kids Game")
    win.iconbitmap("cute-panda-superhero-vector.ico")

    f0 = Frame(win)
    f0.pack(side=TOP, fill="x")
    Label(f0, text="Watch the images ;)", font="georgia 30 bold italic ", bg="#77c442", fg="white", pady=10).pack(
        fill="x")

    # img = []
    # name = []

    wrong = []
    w_a = open("wrong_name_.csv", "r")
    a = csv.reader(w_a, delimiter=",")
    for i in range(0, 24):
        b = next(a)
        wrong.append(b)
    print(wrong)

    for i in range(len(wrong)):
        a, b = wrong[i]
        w_name.append(a)

    l = []
    f = open("database.csv", "r")
    a = csv.reader(f, delimiter=",")
    for i in range(0, 24):
        b = next(a)
        l.append(b)
    print(l)

    for i in range(len(l)):
        a, b = l[i]
        image = Image.open(f"{a}")
        image = image.resize((300, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image=image)
        img.append(photo)
        name.append(b)
    # print(img)
    # print(name)

    f1 = Frame(win, borderwidth=8, relief=SUNKEN)
    f1.pack(padx=100, pady=15, side=LEFT)
    f2 = Frame(win, borderwidth=8, relief=SUNKEN)
    f2.pack(padx=100, pady=15, side=RIGHT)
    f3 = Frame(win, borderwidth=6, bg="#77c442", padx=10, pady=5)
    f3.pack(side=TOP, pady=250)

    Label(f1, image=img[0]).pack()
    Label(f1, image=img[1]).pack()
    Label(f2, image=img[2]).pack()
    Label(f2, image=img[3]).pack()
    Button(f3, text="Next->", font="lucida 15 bold", bg="#77c442", fg="white", padx="10", pady="5", command=option ).pack()

    gamemenu(win)

    win.mainloop()

#main window of the game
root = Tk()
root.geometry("1920x1080")
root.resizable(600,600)
root.title("Kids Game")
root.iconbitmap("cute-panda-superhero-vector.ico")


f1= Frame(root)
f1.pack(fill="x")
f2= Frame(root)
f2.pack()


backgound = Image.open("cute-panda-superhero-vector.jpg")
pic= ImageTk.PhotoImage(backgound.resize((1400,900),Image.ANTIALIAS))
Label(f2,image=pic).pack()
Label(f1,text="Kids Learning Game",font=" georgia 33 bold italic", bg="red", fg="white", pady=10).pack(fill="x")
Button(text="Play Game",font="bold",pady=10,padx=10,bg="orange",command=play_game,activebackground="#77c442").place(x=600,y=600)


gamemenu(root)
music()

root.mainloop()