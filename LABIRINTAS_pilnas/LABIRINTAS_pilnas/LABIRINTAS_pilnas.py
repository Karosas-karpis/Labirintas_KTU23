import customtkinter
import pygame
from random import choice

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('dark-blue')
langas=customtkinter.CTk()
langas.geometry('500x350')
langas.title('Labirintas')
remas=customtkinter.CTkFrame(langas)
remas.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
zaid_pav=customtkinter.CTkLabel(remas, text='LABIRINTAS', font=('Silkscreen',52))
zaid_pav.pack(pady=25, padx=10)
zaid_kr=customtkinter.CTkLabel(remas, text='')

def baigti():
    langas.destroy()
    
def level_1():
    global l, labirintas, player, langas, zaid, mygt1, mygt2
    pygame.init()
    zaid_pav.destroy()
    langas.geometry('550x585')
    zaid=customtkinter.CTkFrame(remas)
    zaid.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.87)
    mygt1.configure(text='Kitas lygis', command=level_2)
    mygt2.configure(text='Baigti', command=baigti)
    mygt1.configure(fg_color='#1b145e')
    mygt2.configure(fg_color='#1b145e')
    mygt1.place(relx=0.68, rely=0.9, relwidth=0.18)
    mygt2.place(relx=0.86, rely=0.9, relwidth=0.18)
    l=customtkinter.CTkCanvas(remas,bg="white")
    l.place(x=15,y=15,width=630,height=595)
    player=l.create_oval(10,290,30,310,fill="green")
    labirintas=[
    (4,4,630,4),
    (35,35,70,35),(105,35,175,35),(249,35,280,35),(385,35,420,35),(490,35,525,35),
    (0,70,35,70),(175,70,245,70),(315,70,385,70),(420,70,490,70),(560,70,595,70),
    (0,105,175,105),(245,105,315,105),(385,105,420,105),(490,105,560,105),
    (35,140,70,140),(280,140,315,140),(350,140,420,140),(455,140,560,140),
    (70,175,105,175),(140,175,280,175),(315,175,385,175),(420,175,455,175),(525,175,595,175),
    (0,210,70,210),(210,210,315,210),(350,210,385,210),(455,210,630,210),
    (140,245,175,245),(245,245,280,245),(350,245,455,245),(490,245,525,245),(560,245,630,245),
    (35,280,105,280),(175,280,210,280),(280,280,315,280),(385,280,420,280),(455,280,525,280),
    (0,315,35,315),(70,315,175,315),(315,315,350,315),(420,315,455,315),
    (0,350,210,350),(350,350,420,350),(455,350,560,350),
    (105,385,245,385),(315,385,350,385),(420,385,455,385),(490,385,525,385),(560,385,595,385),
    (0,420,105,420),(280,420,315,420),(385,420,420,420),(455,420,490,420),(525,420,595,420),
    (35,455,175,455),(210,455,280,455),(420,455,525,455),
    (0,490,105,490),(175,490,210,490),(245,490,280,490),(420,490,490,490),
    (105,525,175,525),(210,525,245,525),(350,525,595,525),
    (70,560,105,560),(140,560,315,560),(385,560,560,560),
    (0,590,630,590),
    (4,0,4,280),(4,315,4,595),
    (35,175,35,210),(35,245,35,315),(35,385,35,420),(35,490,35,525),(35,560,35,595),
    (70,35,70,105),(70,140,70,175),(70,210,70,245),(70,350,70,385),(70,525,70,560),
    (105,35,105,70),(105,140,105,280),(105,490,105,560),
    (140,35,140,315),(140,385,140,420),(140,455,140,490),
    (175,105,175,140),(175,210,175,245),(175,385,175,455),(175,490,175,525),
    (210,0,210,35),(210,105,210,175),(210,210,210,350),(210,420,210,490),(210,525,210,560),
    (245,35,245,105),(245,140,245,175),(245,245,245,455),(245,490,245,525),
    (280,35,280,70),(280,105,280,140),(280,280,280,420),
    (315,0,315,70),(315,140,315,280),(315,315,315,385),(315,420,315,595),
    (350,35,350,140),(350,280,350,350),(350,385,350,595),
    (385,0,385,35),(385,70,385,105),(385,175,385,210),(385,245,385,315),(385,385,385,420),(385,455,385,525),
    (420,35,420,70),(420,140,420,245),(420,315,420,385),(420,420,420,490),
    (455,0,455,35),(455,70,455,140),(455,245,455,280),(455,385,455,420),
    (490,70,490,105),(490,140,490,175),(490,210,490,245),(490,280,490,315),
    (525,0,525,70),(525,175,525,210),(525,315,525,455),(525,490,525,525),
    (560,35,560,105),(560,245,560,350),(560,455,560,525),(560,560,560,595),
    (595,35,595,70),(595,105,595,175),(595,280,595,490),(595,525,595,560),
    (625,0,625,280),(625,315,625,595)]
    l.create_line(0,4,630,4,fill="black",width=5) 
    l.create_line(35,35,70,35,fill="black",width=5)
    l.create_line(105,35,175,35,fill="black",width=5)
    l.create_line(245,35,280,35,fill="black",width=5)
    l.create_line(385,35,420,35,fill="black",width=5)
    l.create_line(490,35,525,35,fill="black",width=5)
    l.create_line(0,70,35,70,fill="black",width=5)
    l.create_line(175,70,245,70,fill="black",width=5)
    l.create_line(315,70,385,70,fill="black",width=5)
    l.create_line(420,70,490,70,fill="black",width=5)
    l.create_line(560,70,595,70,fill="black",width=5)
    l.create_line(0,105,175,105,fill="black",width=5)
    l.create_line(245,105,315,105,fill="black",width=5)
    l.create_line(385,105,420,105,fill="black",width=5)
    l.create_line(490,105,560,105,fill="black",width=5)
    l.create_line(35,140,70,140,fill="black",width=5)
    l.create_line(280,140,315,140,fill="black",width=5)
    l.create_line(350,140,420,140,fill="black",width=5)
    l.create_line(455,140,560,140,fill="black",width=5)
    l.create_line(70,175,105,175,fill="black",width=5)
    l.create_line(140,175,280,175,fill="black",width=5)
    l.create_line(315,175,385,175,fill="black",width=5)
    l.create_line(420,175,455,175,fill="black",width=5)
    l.create_line(525,175,595,175,fill="black",width=5)
    l.create_line(0,210,70,210,fill="black",width=5)
    l.create_line(210,210,315,210,fill="black",width=5)
    l.create_line(350,210,385,210,fill="black",width=5)
    l.create_line(455,210,630,210,fill="black",width=5)
    l.create_line(140,245,175,245,fill="black",width=5)
    l.create_line(245,245,280,245,fill="black",width=5)
    l.create_line(350,245,455,245,fill="black",width=5)
    l.create_line(490,245,525,245,fill="black",width=5)
    l.create_line(560,245,630,245,fill="black",width=5)
    l.create_line(35,280,105,280,fill="black",width=5)
    l.create_line(175,280,210,280,fill="black",width=5)
    l.create_line(280,280,315,280,fill="black",width=5)
    l.create_line(385,280,420,280,fill="black",width=5)
    l.create_line(455,280,525,280,fill="black",width=5)
    l.create_line(0,315,35,315,fill="black",width=5)
    l.create_line(70,315,175,315,fill="black",width=5)
    l.create_line(315,315,350,315,fill="black",width=5)
    l.create_line(420,315,455,315,fill="black",width=5)
    l.create_line(0,350,210,350,fill="black",width=5)
    l.create_line(350,350,420,350,fill="black",width=5)
    l.create_line(455,350,560,350,fill="black",width=5)
    l.create_line(105,385,245,385,fill="black",width=5)
    l.create_line(315,385,350,385,fill="black",width=5)
    l.create_line(420,385,455,385,fill="black",width=5)
    l.create_line(490,385,525,385,fill="black",width=5)
    l.create_line(560,385,595,385,fill="black",width=5)
    l.create_line(0,420,105,420,fill="black",width=5)
    l.create_line(280,420,315,420,fill="black",width=5)
    l.create_line(385,420,420,420,fill="black",width=5)
    l.create_line(455,420,490,420,fill="black",width=5)
    l.create_line(525,420,595,420,fill="black",width=5)
    l.create_line(35,455,175,455,fill="black",width=5)
    l.create_line(210,455,280,455,fill="black",width=5)
    l.create_line(420,455,525,455,fill="black",width=5)
    l.create_line(0,490,105,490,fill="black",width=5)
    l.create_line(175,490,210,490,fill="black",width=5)
    l.create_line(245,490,280,490,fill="black",width=5)
    l.create_line(420,490,490,490,fill="black",width=5)
    l.create_line(105,525,175,525,fill="black",width=5)
    l.create_line(210,525,245,525,fill="black",width=5)
    l.create_line(350,525,595,525,fill="black",width=5)
    l.create_line(70,560,105,560,fill="black",width=5)
    l.create_line(140,560,315,560,fill="black",width=5)
    l.create_line(385,560,560,560,fill="black",width=5)
    l.create_line(0,590,630,590,fill="black",width=5)
    l.create_line(4,0,4,280,fill="black",width=5)
    l.create_line(4,315,4,595,fill="black",width=5)
    l.create_line(35,175,35,210,fill="black",width=5)
    l.create_line(35,245,35,315,fill="black",width=5)
    l.create_line(35,385,35,420,fill="black",width=5)
    l.create_line(35,490,35,525,fill="black",width=5)
    l.create_line(35,560,35,595,fill="black",width=5)
    l.create_line(70,35,70,105,fill="black",width=5)
    l.create_line(70,140,70,175,fill="black",width=5)
    l.create_line(70,210,70,245,fill="black",width=5)
    l.create_line(70,350,70,385,fill="black",width=5)
    l.create_line(70,525,70,560,fill="black",width=5)
    l.create_line(105,35,105,70,fill="black",width=5)
    l.create_line(105,140,105,280,fill="black",width=5)
    l.create_line(105,490,105,560,fill="black",width=5)
    l.create_line(140,35,140,315,fill="black",width=5)
    l.create_line(140,385,140,420,fill="black",width=5)
    l.create_line(140,455,140,490,fill="black",width=5)
    l.create_line(175,105,175,140,fill="black",width=5)
    l.create_line(175,210,175,245,fill="black",width=5)
    l.create_line(175,385,175,455,fill="black",width=5)
    l.create_line(175,490,175,525,fill="black",width=5)
    l.create_line(210,0,210,35,fill="black",width=5)
    l.create_line(210,105,210,175,fill="black",width=5)
    l.create_line(210,210,210,350,fill="black",width=5)
    l.create_line(210,420,210,490,fill="black",width=5)
    l.create_line(210,525,210,560,fill="black",width=5)
    l.create_line(245,35,245,105,fill="black",width=5)
    l.create_line(245,140,245,175,fill="black",width=5)
    l.create_line(245,245,245,455,fill="black",width=5)
    l.create_line(245,490,245,525,fill="black",width=5)
    l.create_line(280,35,280,70,fill="black",width=5)
    l.create_line(280,105,280,140,fill="black",width=5)
    l.create_line(280,280,280,420,fill="black",width=5)
    l.create_line(315,0,315,70,fill="black",width=5)
    l.create_line(315,140,315,280,fill="black",width=5)
    l.create_line(315,315,315,385,fill="black",width=5)
    l.create_line(315,420,315,595,fill="black",width=5)
    l.create_line(350,35,350,140,fill="black",width=5)
    l.create_line(350,280,350,350,fill="black",width=5)
    l.create_line(350,385,350,595,fill="black",width=5)
    l.create_line(385,0,385,35,fill="black",width=5)
    l.create_line(385,70,385,105,fill="black",width=5)
    l.create_line(385,175,385,210,fill="black",width=5)
    l.create_line(385,245,385,315,fill="black",width=5)
    l.create_line(385,385,385,420,fill="black",width=5)
    l.create_line(385,455,385,525,fill="black",width=5)
    l.create_line(420,35,420,70,fill="black",width=5)
    l.create_line(420,140,420,245,fill="black",width=5)
    l.create_line(420,315,420,385,fill="black",width=5)
    l.create_line(420,420,420,490,fill="black",width=5)
    l.create_line(455,0,455,35,fill="black",width=5)
    l.create_line(455,70,455,140,fill="black",width=5)
    l.create_line(455,245,455,280,fill="black",width=5)
    l.create_line(455,385,455,420,fill="black",width=5)
    l.create_line(490,70,490,105,fill="black",width=5)
    l.create_line(490,140,490,175,fill="black",width=5)
    l.create_line(490,210,490,245,fill="black",width=5)
    l.create_line(490,280,490,315,fill="black",width=5)
    l.create_line(525,0,525,70,fill="black",width=5)
    l.create_line(525,175,525,210,fill="black",width=5)
    l.create_line(525,315,525,455,fill="black",width=5)
    l.create_line(525,490,525,525,fill="black",width=5)
    l.create_line(560,35,560,105,fill="black",width=5)
    l.create_line(560,245,560,350,fill="black",width=5)
    l.create_line(560,455,560,525,fill="black",width=5)
    l.create_line(560,560,560,595,fill="black",width=5)
    l.create_line(595,35,595,70,fill="black",width=5)
    l.create_line(595,105,595,175,fill="black",width=5)
    l.create_line(595,280,595,490,fill="black",width=5)
    l.create_line(595,525,595,560,fill="black",width=5)
    l.create_line(625,0,625,280,fill="black",width=5)
    l.create_line(625,315,625,595,fill="black",width=5)
def level_2():
    mygt1.configure(text='Kitas lygis')
    mygt2.configure(text='Baigti', command=baigti)
    mygt3.configure(fg_color='#1b145e')
    mygt3.place(relx=0.39, rely=0.8779, relwidth=0.2)
    l=customtkinter.CTkCanvas(remas,bg="white")
    l.place(x=15,y=15,width=630,height=595)
def move(event):
    x,y=0, 0
    if event.keysym=="Up":
        y=-10
    elif event.keysym=="Down":
        y=10
    elif event.keysym=="Left":
        x=-10
    elif event.keysym=="Right":
        x=10  
        
    x1,y1,x2,y2 = l.bbox(player)
    n_x1,n_y1,n_x2,n_y2=x1+x,y1+y,x2+x,y2+y
    
    for sien in labirintas:
        sien_x1, sien_y1, sien_x2, sien_y2 = sien
        if (
            n_x1 < sien_x2
            and n_x2 > sien_x1
            and n_y1 < sien_y2
            and n_y2 > sien_y1
        ):
            return     
    l.move(player,x,y)

langas.bind_all("<Key>",move)

mygt1=customtkinter.CTkButton(langas, text='Pradėti žaidimą', command=level_1)
mygt1.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)

mygt2=customtkinter.CTkButton(langas, text='Išeiti', command=baigti)
mygt2.place(relx=0.5, rely=0.65, anchor=customtkinter.CENTER)

mygt3=customtkinter.CTkButton(langas, text='Ankstesnis lygis', command=level_1)

langas.mainloop()
