from tkinter import*
from PIL import Image,ImageTk
import pygame
import csv

#global variable to store the image & its value
# img=[]
# name=[]



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


#to display the image
def play_game():
    root.destroy()

    img = []
    name = []
    w_name = []

    def quit():
        win.destroy()

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
    win= Tk()
    win.geometry("1920x1080")
    win.resizable(600, 600)
    win.title("Kids Game")
    win.iconbitmap("cute-panda-superhero-vector.ico")

    f0 = Frame(win)
    f0.pack(side=TOP, fill="x")
    Label(f0, text="Watch the images ;)", font="georgia 30 bold italic ", bg="#77c442", fg="white", pady=10).pack(fill="x")

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
    # print(w_name)

    l = []
    f = open("database.csv", "r")
    a = csv.reader(f, delimiter=",")
    for i in range(0, 24):
        b = next(a)
        l.append(b)

    for i in range(len(l)):
        a, b = l[i]
        image = Image.open(f"{a}")
        image = image.resize((300, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image=image)
        img.append(photo)
        name.append(b)

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
    Button(f3, text="Next->", font="lucida 15 bold", bg="#77c442", fg="white", padx="10", pady="5", ).pack()

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