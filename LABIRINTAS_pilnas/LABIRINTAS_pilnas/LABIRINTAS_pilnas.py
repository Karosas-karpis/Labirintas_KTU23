import customtkinter
import pygame
import random

#Kuriama grafinė sąsaja, pagrindinis langas, mygtukai
customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme('dark-blue')
langas=customtkinter.CTk()
langas.geometry('500x400')
langas.title('Labirintas')
remas=customtkinter.CTkFrame(langas)
remas.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
zaid_pav=customtkinter.CTkLabel(remas, text='LABIRINTAS', font=('Silkscreen',52))
zaid_pav.pack(pady=25, padx=10)
zaid_kr=customtkinter.CTkLabel(remas, text='')
langas.resizable(False,False)

#Sukuriama funkcija, kuri leist nustatyti lango išvaizdą (Dark, Light)
def lango_nust(choice):
    if choice=='Light':
        customtkinter.set_appearance_mode('Light')
    else:
        customtkinter.set_appearance_mode('Dark')
#Sukuriamas ComboBox
sarasas=['Dark','Light']
combobox_pas=customtkinter.StringVar(value='Dark')
pasirinkimas=customtkinter.CTkComboBox(langas, values=sarasas, command=lango_nust, variable=combobox_pas, height=20, width=75)
combobox_pas.set('Dark')    
pasirinkimas.place(relx=0.83, rely=0.02)

#Funkcija išjungianti langą
def baigti():
    langas.destroy()
    
#Pirmojo lygio funkcija
def level_1():
    global l, labirintas, player, langas, zaid, mygt5, mygt6, mygt7
    pygame.init()
    #Aprašomi lango pakeitimai, sukuriami nauji mygtukai, jiems priskiriamos funkcijos
    langas.geometry('550x590')
    zaid=customtkinter.CTkFrame(remas)
    zaid.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.87)
    mygt5=customtkinter.CTkButton(remas, text='Kitas lygis', command=level_2, fg_color='#1b145e')
    mygt6=customtkinter.CTkButton(remas, text='Baigti', command=baigti, fg_color='#1b145e')
    mygt5.place(relx=0.6, rely=0.89, relwidth=0.19)
    mygt6.place(relx=0.8, rely=0.89, relwidth=0.18)
    l=customtkinter.CTkCanvas(remas,bg="white")
    zaid_pav.place(relx=1, rely=1)
    mygt1.place(relx=1, rely=0.5)
    mygt2.place(relx=1, rely=0.6)
    mygt3.place(relx=1, rely=0.7)
    mygt7.destroy()
    pasirinkimas.place(relx=1, rely=0)    
    #Sukuriama žaidėjo ikona
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
    
#Sukuriama antro lygio funkcija, joje aprašomi lango pakeitimai ir suformatojamas naujas labirintas 
def level_2():
    global mygt7
    mygt5.configure(text='Kitas lygis', command=level_3)
    mygt7=customtkinter.CTkButton(remas, text='Ankstesnis lygis', command=level_1, fg_color='#1b145e')
    mygt7.place(relx=0.39, rely=0.89, relwidth=0.2)
    l=customtkinter.CTkCanvas(remas,bg="white")
    l.place(x=15,y=15,width=630,height=595)

#Sukuriama trečio lygio funkcija, kurioje aprašomi lango pakeitimai ir kuriamas paskutinis labirintas
def level_3():
    global labirintas, l, player
    mygt5.configure(text='Žaist iš naujo', command=level_1)
    mygt7.configure(command=level_2)
    l=customtkinter.CTkCanvas(remas,bg="white")
    l.place(x=15,y=15,width=630,height=595)
    player=l.create_oval(10,250,30,270,fill="green")
    stulp=18
    eil=17
    lang=34.5
    x=4
    y=4
    labirintas=[]
    for i in range(0, stulp+1):
        x_k=i*lang+x
        for j in range(0,eil+1):
            y_k=j*lang+y
            labirintas.append((x_k,y_k))
    # print(labirintas)            
    #Braižomi labirinto rėmai
    l.create_line(x,y,x+(18*lang),y, fill='black', width=5)
    l.create_line(x,y,x,y+(7*lang), fill='black', width=5)    
    l.create_line(x,y+(8*lang),x,y+(17*lang), fill='black', width=5)
    l.create_line(x+(18*lang),y, x+(18*lang),y+(6*lang), fill='black', width=5)
    l.create_line(x+(18*lang),y+(7*lang), x+(18*lang),y+(17*lang), fill='black', width=5)
    l.create_line(x,y+(17*lang),x+(18*lang),y+(17*lang), fill='black', width=5)

    l.create_line(x+(8*lang),y,x+(8*lang),y+lang, fill='black', width=5)
    l.create_line(x+(11*lang),y,x+(11*lang),y+(2*lang), fill='black', width=5)
    l.create_line(x+(14*lang),y,x+(14*lang),y+lang, fill='black', width=5)
    l.create_line(x+lang,y+lang,x+lang,y+(4*lang), fill='black', width=5)
    l.create_line(x+(2*lang),y+lang,x+(3*lang), y+lang, fill='black', width=5)
    l.create_line(x+(4*lang),y+lang,x+(8*lang), y+lang, fill='black', width=5)
    l.create_line(x+(9*lang),y+lang,x+(10*lang), y+lang, fill='black', width=5)
    l.create_line(x+(14*lang),y+lang,x+(17*lang), y+lang, fill='black', width=5)
    l.create_line(x+(3*lang),y+lang,x+(3*lang), y+(4*lang), fill='black', width=5)
    l.create_line(x+(6*lang),y+lang,x+(6*lang), y+(4*lang), fill='black', width=5)
    l.create_line(x+(9*lang),y+lang,x+(9*lang), y+(2*lang), fill='black', width=5)
    l.create_line(x+(12*lang),y+lang,x+(12*lang), y+(3*lang), fill='black', width=5)
    l.create_line(x+(13*lang),y+lang,x+(13*lang), y+(2*lang), fill='black', width=5)
    l.create_line(x+(3*lang),y+(2*lang),x+(5*lang), y+(2*lang), fill='black', width=5)
    l.create_line(x+(7*lang),y+(2*lang),x+(9*lang), y+(2*lang), fill='black', width=5)
    l.create_line(x+(10*lang),y+(2*lang),x+(12*lang), y+(2*lang), fill='black', width=5)
    l.create_line(x+(13*lang),y+(2*lang),x+(17*lang), y+(2*lang), fill='black', width=5)
    l.create_line(x+(2*lang),y+(2*lang),x+(2*lang), y+(3*lang), fill='black', width=5)
    l.create_line(x+(5*lang),y+(2*lang),x+(5*lang), y+(3*lang), fill='black', width=5)
    l.create_line(x+(7*lang),y+(2*lang),x+(7*lang), y+(5*lang), fill='black', width=5)
    l.create_line(x+(10*lang),y+(2*lang),x+(10*lang), y+(3*lang), fill='black', width=5)
    l.create_line(x+(16*lang),y+(2*lang),x+(16*lang), y+(7*lang), fill='black', width=5)
    l.create_line(x+(17*lang),y+(2*lang),x+(17*lang), y+(3*lang), fill='black', width=5)
    l.create_line(x+(1*lang),y+(3*lang),x+(2*lang), y+(3*lang), fill='black', width=5)
    l.create_line(x+(8*lang),y+(3*lang),x+(10*lang), y+(3*lang), fill='black', width=5)
    l.create_line(x+(13*lang),y+(3*lang),x+(15*lang), y+(3*lang), fill='black', width=5)
    l.create_line(x+(4*lang),y+(3*lang),x+(4*lang), y+(5*lang), fill='black', width=5)
    l.create_line(x+(11*lang),y+(3*lang),x+(11*lang), y+(4*lang), fill='black', width=5)
    l.create_line(x+(14*lang),y+(3*lang),x+(14*lang), y+(7*lang), fill='black', width=5)
    l.create_line(x+(15*lang),y+(3*lang),x+(15*lang), y+(4*lang), fill='black', width=5)
    l.create_line(x,y+(4*lang),x+(1*lang), y+(4*lang), fill='black', width=5)
    l.create_line(x+(2*lang),y+(4*lang),x+(3*lang), y+(4*lang), fill='black', width=5)
    l.create_line(x+(5*lang),y+(4*lang),x+(6*lang), y+(4*lang), fill='black', width=5)
    l.create_line(x+(7*lang),y+(4*lang),x+(8*lang), y+(4*lang), fill='black', width=5)
    l.create_line(x+(9*lang),y+(4*lang),x+(13*lang), y+(4*lang), fill='black', width=5)
    l.create_line(x+(16*lang),y+(4*lang),x+(17*lang), y+(4*lang), fill='black', width=5)
    l.create_line(x+(2*lang),y+(4*lang),x+(2*lang), y+(5*lang), fill='black', width=5)
    l.create_line(x+(5*lang),y+(4*lang),x+(5*lang), y+(5*lang), fill='black', width=5)
    l.create_line(x+(9*lang),y+(4*lang),x+(9*lang), y+(5*lang), fill='black', width=5)
    l.create_line(x+(13*lang),y+(4*lang),x+(13*lang), y+(6*lang), fill='black', width=5)
    l.create_line(x+(1*lang),y+(5*lang),x+(5*lang), y+(5*lang), fill='black', width=5)
    l.create_line(x+(6*lang),y+(5*lang),x+(7*lang), y+(5*lang), fill='black', width=5)
    l.create_line(x+(8*lang),y+(5*lang),x+(9*lang), y+(5*lang), fill='black', width=5)
    l.create_line(x+(10*lang),y+(5*lang),x+(12*lang), y+(5*lang), fill='black', width=5)
    l.create_line(x+(15*lang),y+(5*lang),x+(16*lang), y+(5*lang), fill='black', width=5)
    l.create_line(x+(17*lang),y+(5*lang),x+(18*lang), y+(5*lang), fill='black', width=5)
    l.create_line(x+(6*lang),y+(5*lang),x+(6*lang), y+(6*lang), fill='black', width=5)
    l.create_line(x+(8*lang),y+(5*lang),x+(8*lang), y+(6*lang), fill='black', width=5)
    l.create_line(x+(10*lang),y+(5*lang),x+(10*lang), y+(6*lang), fill='black', width=5)
    l.create_line(x+(17*lang),y+(5*lang),x+(17*lang), y+(6*lang), fill='black', width=5)
    l.create_line(x+(1*lang),y+(6*lang),x+(2*lang), y+(6*lang), fill='black', width=5)
    l.create_line(x+(3*lang),y+(6*lang),x+(6*lang), y+(6*lang), fill='black', width=5)
    l.create_line(x+(7*lang),y+(6*lang),x+(8*lang), y+(6*lang), fill='black', width=5)
    l.create_line(x+(9*lang),y+(6*lang),x+(10*lang), y+(6*lang), fill='black', width=5)
    l.create_line(x+(11*lang),y+(6*lang),x+(13*lang), y+(6*lang), fill='black', width=5)
    l.create_line(x+(14*lang),y+(6*lang),x+(15*lang), y+(6*lang), fill='black', width=5)
    l.create_line(x+(1*lang),y+(6*lang),x+(1*lang), y+(8*lang), fill='black', width=5)
    l.create_line(x+(4*lang),y+(6*lang),x+(4*lang), y+(11*lang), fill='black', width=5)
    l.create_line(x+(9*lang),y+(6*lang),x+(9*lang), y+(9*lang), fill='black', width=5)
    l.create_line(x+(11*lang),y+(6*lang),x+(11*lang), y+(7*lang), fill='black', width=5)
    l.create_line(x+(2*lang),y+(7*lang),x+(3*lang), y+(7*lang), fill='black', width=5)
    l.create_line(x+(5*lang),y+(7*lang),x+(12*lang), y+(7*lang), fill='black', width=5)
    l.create_line(x+(13*lang),y+(7*lang),x+(14*lang), y+(7*lang), fill='black', width=5)
    l.create_line(x+(15*lang),y+(7*lang),x+(18*lang), y+(7*lang), fill='black', width=5)
    l.create_line(x+(2*lang),y+(7*lang),x+(2*lang), y+(9*lang), fill='black', width=5)
    l.create_line(x+(7*lang),y+(7*lang),x+(7*lang), y+(8*lang), fill='black', width=5)
    l.create_line(x+(12*lang),y+(7*lang),x+(12*lang), y+(10*lang), fill='black', width=5)
    l.create_line(x+(13*lang),y+(7*lang),x+(13*lang), y+(10*lang), fill='black', width=5)
    l.create_line(x+(15*lang),y+(7*lang),x+(15*lang), y+(8*lang), fill='black', width=5)
    l.create_line(x,y+(8*lang),x+(1*lang), y+(8*lang), fill='black', width=5)
    l.create_line(x+(3*lang),y+(8*lang),x+(6*lang), y+(8*lang), fill='black', width=5)
    l.create_line(x+(10*lang),y+(8*lang),x+(11*lang), y+(8*lang), fill='black', width=5)
    l.create_line(x+(14*lang),y+(8*lang),x+(15*lang), y+(8*lang), fill='black', width=5)
    l.create_line(x+(6*lang),y+(8*lang),x+(6*lang), y+(9*lang), fill='black', width=5)
    l.create_line(x+(8*lang),y+(8*lang),x+(8*lang), y+(9*lang), fill='black', width=5)
    l.create_line(x+(10*lang),y+(8*lang),x+(10*lang), y+(11*lang), fill='black', width=5)
    l.create_line(x+(11*lang),y+(8*lang),x+(11*lang), y+(9*lang), fill='black', width=5)
    l.create_line(x+(14*lang),y+(8*lang),x+(14*lang), y+(10*lang), fill='black', width=5)
    l.create_line(x+(16*lang),y+(8*lang),x+(16*lang), y+(9*lang), fill='black', width=5)
    l.create_line(x+(17*lang),y+(8*lang),x+(17*lang), y+(13*lang), fill='black', width=5)
    l.create_line(x+(1*lang),y+(9*lang),x+(4*lang), y+(9*lang), fill='black', width=5)
    l.create_line(x+(6*lang),y+(9*lang),x+(8*lang), y+(9*lang), fill='black', width=5)
    l.create_line(x+(15*lang),y+(9*lang),x+(17*lang), y+(9*lang), fill='black', width=5)
    l.create_line(x+(1*lang),y+(9*lang),x+(1*lang), y+(10*lang), fill='black', width=5)
    l.create_line(x+(5*lang),y+(9*lang),x+(5*lang), y+(12*lang), fill='black', width=5)
    l.create_line(x+(15*lang),y+(9*lang),x+(15*lang), y+(10*lang), fill='black', width=5)
    l.create_line(x,y+(10*lang),x+(1*lang), y+(10*lang), fill='black', width=5)
    l.create_line(x+(2*lang),y+(10*lang),x+(3*lang), y+(10*lang), fill='black', width=5)
    l.create_line(x+(5*lang),y+(10*lang),x+(13*lang), y+(10*lang), fill='black', width=5)
    l.create_line(x+(14*lang),y+(10*lang),x+(15*lang), y+(10*lang), fill='black', width=5)
    l.create_line(x+(2*lang),y+(10*lang),x+(2*lang), y+(11*lang), fill='black', width=5)
    l.create_line(x+(16*lang),y+(10*lang),x+(16*lang), y+(14*lang), fill='black', width=5)
    l.create_line(x+(1*lang),y+(11*lang),x+(2*lang), y+(11*lang), fill='black', width=5)
    l.create_line(x+(3*lang),y+(11*lang),x+(4*lang), y+(11*lang), fill='black', width=5)
    l.create_line(x+(6*lang),y+(11*lang),x+(7*lang), y+(11*lang), fill='black', width=5)
    l.create_line(x+(9*lang),y+(11*lang),x+(10*lang), y+(11*lang), fill='black', width=5)
    l.create_line(x+(11*lang),y+(11*lang),x+(16*lang), y+(11*lang), fill='black', width=5)
    l.create_line(x+(1*lang),y+(11*lang),x+(1*lang), y+(15*lang), fill='black', width=5)
    l.create_line(x+(3*lang),y+(11*lang),x+(3*lang), y+(12*lang), fill='black', width=5)
    l.create_line(x+(6*lang),y+(11*lang),x+(6*lang), y+(13*lang), fill='black', width=5)
    l.create_line(x+(7*lang),y+(11*lang),x+(7*lang), y+(12*lang), fill='black', width=5)
    l.create_line(x+(8*lang),y+(11*lang),x+(8*lang), y+(14*lang), fill='black', width=5)
    l.create_line(x+(9*lang),y+(11*lang),x+(9*lang), y+(12*lang), fill='black', width=5)
    l.create_line(x+(11*lang),y+(11*lang),x+(11*lang), y+(12*lang), fill='black', width=5)
    l.create_line(x+(2*lang),y+(12*lang),x+(3*lang), y+(12*lang), fill='black', width=5)
    l.create_line(x+(4*lang),y+(12*lang),x+(5*lang), y+(12*lang), fill='black', width=5)
    l.create_line(x+(10*lang),y+(12*lang),x+(11*lang), y+(12*lang), fill='black', width=5)
    l.create_line(x+(12*lang),y+(12*lang),x+(15*lang), y+(12*lang), fill='black', width=5)
    l.create_line(x+(2*lang),y+(12*lang),x+(2*lang), y+(14*lang), fill='black', width=5)
    l.create_line(x+(4*lang),y+(12*lang),x+(4*lang), y+(17*lang), fill='black', width=5)
    l.create_line(x+(10*lang),y+(12*lang),x+(10*lang), y+(13*lang), fill='black', width=5)
    l.create_line(x+(12*lang),y+(12*lang),x+(12*lang), y+(13*lang), fill='black', width=5)
    l.create_line(x+(15*lang),y+(12*lang),x+(15*lang), y+(14*lang), fill='black', width=5)
    l.create_line(x+(3*lang),y+(13*lang),x+(4*lang), y+(13*lang), fill='black', width=5)
    l.create_line(x+(5*lang),y+(13*lang),x+(10*lang), y+(13*lang), fill='black', width=5)
    l.create_line(x+(11*lang),y+(13*lang),x+(12*lang), y+(13*lang), fill='black', width=5)
    l.create_line(x+(13*lang),y+(13*lang),x+(14*lang), y+(13*lang), fill='black', width=5)
    l.create_line(x+(5*lang),y+(13*lang),x+(5*lang), y+(16*lang), fill='black', width=5)
    l.create_line(x+(13*lang),y+(13*lang),x+(13*lang), y+(14*lang), fill='black', width=5)
    l.create_line(x+(2*lang),y+(14*lang),x+(3*lang), y+(14*lang), fill='black', width=5)
    l.create_line(x+(5*lang),y+(14*lang),x+(7*lang), y+(14*lang), fill='black', width=5)
    l.create_line(x+(8*lang),y+(14*lang),x+(13*lang), y+(14*lang), fill='black', width=5)
    l.create_line(x+(14*lang),y+(14*lang),x+(15*lang), y+(14*lang), fill='black', width=5)
    l.create_line(x+(16*lang),y+(14*lang),x+(18*lang), y+(14*lang), fill='black', width=5)
    l.create_line(x+(3*lang),y+(14*lang),x+(3*lang), y+(16*lang), fill='black', width=5)
    l.create_line(x+(9*lang),y+(14*lang),x+(9*lang), y+(15*lang), fill='black', width=5)
    l.create_line(x+(12*lang),y+(14*lang),x+(12*lang), y+(16*lang), fill='black', width=5)
    l.create_line(x+(14*lang),y+(14*lang),x+(14*lang), y+(16*lang), fill='black', width=5)
    l.create_line(x+(0*lang),y+(15*lang),x+(2*lang), y+(15*lang), fill='black', width=5)
    l.create_line(x+(6*lang),y+(15*lang),x+(8*lang), y+(15*lang), fill='black', width=5)
    l.create_line(x+(10*lang),y+(15*lang),x+(11*lang), y+(15*lang), fill='black', width=5)
    l.create_line(x+(12*lang),y+(15*lang),x+(17*lang), y+(15*lang), fill='black', width=5)
    l.create_line(x+(8*lang),y+(15*lang),x+(8*lang), y+(17*lang), fill='black', width=5)
    l.create_line(x+(10*lang),y+(15*lang),x+(10*lang), y+(17*lang), fill='black', width=5)
    l.create_line(x+(1*lang),y+(16*lang),x+(2*lang), y+(16*lang), fill='black', width=5)
    l.create_line(x+(5*lang),y+(16*lang),x+(7*lang), y+(16*lang), fill='black', width=5)
    l.create_line(x+(9*lang),y+(16*lang),x+(10*lang), y+(16*lang), fill='black', width=5)
    l.create_line(x+(11*lang),y+(16*lang),x+(12*lang), y+(16*lang), fill='black', width=5)
    l.create_line(x+(15*lang),y+(16*lang),x+(17*lang), y+(16*lang), fill='black', width=5)
    l.create_line(x+(2*lang),y+(16*lang),x+(2*lang), y+(17*lang), fill='black', width=5)
    l.create_line(x+(13*lang),y+(16*lang),x+(13*lang), y+(17*lang), fill='black', width=5)
    l.create_line(x+(15*lang),y+(16*lang),x+(15*lang), y+(17*lang), fill='black', width=5)

#Funkcija aprašanti žaidėjo ikonos judėjimą
def move(event):
    x_k,y_k=0, 0
    if event.keysym=="Up":
        y_k=-10
    elif event.keysym=="Down":
        y_k=10
    elif event.keysym=="Left":
        x_k=-10
    elif event.keysym=="Right":
        x_k=10  
        
    x1,y1,x2,y2 = l.bbox(player)
    n_x1,n_y1,n_x2,n_y2=x1+x_k,y1+y_k,x2+x_k,y2+y_k
    
    for sien in labirintas:
        (sien_x1, sien_y1, sien_x2, sien_y2)= sien
        if (
            n_x1 < sien_x2
            and n_x2 > sien_x1
            and n_y1 < sien_y2
            and n_y2 > sien_y1
        ):
            return     
    l.move(player,x_k,y_k)

langas.bind_all("<Key>",move)

#Pagrindinio lango mygtukai

mygt1=customtkinter.CTkButton(langas, text='Pradėti žaidimą', command=level_1, fg_color='#1b145e')
mygt1.place(relx=0.36, rely=0.55)

mygt2=customtkinter.CTkButton(langas, text='Išeiti', command=baigti, fg_color='#1b145e')
mygt2.place(relx=0.36, rely=0.65)

mygt3=customtkinter.CTkButton(langas, text='Nugalėtojai', fg_color='#1b145e')
mygt3.place(relx=0.36, rely=0.85)

mygt7=customtkinter.CTkButton(langas, text='Ankstesnis lygis', command=level_1)


langas.mainloop()
