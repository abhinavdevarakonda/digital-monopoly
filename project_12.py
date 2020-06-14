from tkinter import *
from tkinter import messagebox
import random
import time
from PIL import Image,ImageTk
import mysql.connector as myco
import tkinter.font as font
import tkinter.messagebox

mydb = myco.connect(host = 'localhost',user = 'root',passwd = 'root',database = 'monopoly')
cur = mydb.cursor(buffered = True)
root1=Tk()
myFont=font.Font(size=15)
var=StringVar()
p_name=[]
k = 0
in_jail = 0
prisoner = []
turn_count = 0
def win1():
    global root
    root.destroy()
    root=Tk()
    root.geometry('800x800')
    root.title('Monopoly')
    root.configure(bg='black')

def win():
    global root1
    root1.destroy()
    root1=Tk()
    root1.geometry('1000x400')
    root1.title('Monopoly')
    root1.configure(bg='black')
    
def img():
    load=Image.open('newhome.png')
    ren=ImageTk.PhotoImage(load)
    image=Label(root1,image=ren,borderwidth=0)
    image.image=ren
    image.pack(side='top',anchor=CENTER)
 

def home():
    global root1
    root1.destroy()
    root1=Tk()
    root1.geometry('800x800')
    root1.title('Homepage')
    root1.configure(bg='black')

    logo=Image.open('monopolylogo.jpg')
    ren=ImageTk.PhotoImage(logo)
    image=Label(root1,image=ren,borderwidth=0)
    image.image=ren
    image.pack(side="top",pady=10,anchor=CENTER)
    
    myFont=font.Font(size=15)
    label=Label(root1,textvariable=var,bg="black",fg="white")    
    var.set("Select Number Of Players")

    p1=Button(root1,text='2 Players',padx=50,pady=20,bg='black',fg="white",borderwidth=0,command=lobby2)
    p2=Button(root1,text='3 Players',padx=50,pady=20,bg='black',fg="white",borderwidth=0,command=lobby3)
    p3=Button(root1,text='4 Players',padx=50,pady=20,bg='black',fg="white",borderwidth=0,command=lobby4)

    label.pack(side="top",anchor=CENTER)
    label['font']=myFont

    p1.pack(side="top",pady=10,anchor=CENTER)
    p2.pack(side="top",pady=10,anchor=CENTER)
    p3.pack(side="top",pady=10,anchor=CENTER)
 
def lobby2():
    global root1
    global e1
    global e2
    global p_name
    
    var2=StringVar()
    answer=tkinter.messagebox.askyesno(title="Confirmation", message="You have selected 2 players")
    global myFont
    if answer==True:
        win()        
        label=Label(root1,text="Enter player 1 name",bg="black",fg="white",font=myFont,pady=10)
        label.pack(side="top",anchor=CENTER,pady=5)
        e1=Entry(root1)
        e1.pack(side="top",anchor=CENTER,pady=10)
        label=Label(root1,text="Enter player 2 name",bg="black",fg="white",font=myFont,pady=10)
        label.pack(side="top",anchor=CENTER,pady=5)
        e2=Entry(root1)
        e2.pack(side="top",anchor=CENTER,pady=10)
        Button(root1,text="Submit",command=P_lobby2).pack(side="top",anchor=CENTER,pady=20)

def lobby3():
    global root1
    global e1
    global e2
    global e3
    global p_name

    answer=tkinter.messagebox.askyesno(title="Confirmation", message="You have selected 3 players")
    global myFont
    if answer==True:
        win()            
        Label(root1,text="Enter player 1 name",bg="black",fg="white",font=myFont,pady=10).pack(side="top",anchor=CENTER,pady=5)
        e1=Entry(root1)
        e1.pack(side="top",anchor=CENTER,pady=10)
        Label(root1,text="Enter player 2 name",bg="black",fg="white",font=myFont,pady=10).pack(side="top",anchor=CENTER,pady=5)
        e2=Entry(root1)
        e2.pack(side="top",anchor=CENTER,pady=10)
        Label(root1,text="Enter player 3 name",bg="black",fg="white",font=myFont,pady=10).pack(side="top",anchor=CENTER,pady=5)
        e3=Entry(root1)
        e3.pack(side="top",anchor=CENTER,pady=10)
        Button(root1,text="Submit",command=P_lobby3).pack(side="top",anchor=CENTER,pady=20)
    
def lobby4():
    global root1
    global e1
    global e2
    global e3
    global e4
    global p_name

    answer=tkinter.messagebox.askyesno(title="Confirmation", message="You have selected 4 players")
    global myFont
    if answer==True:
        win()
        Label(root1,text="Enter player 1 name",bg="black",fg="white",font=myFont,pady=10).pack(side="top",anchor=CENTER,pady=5)
        e1=Entry(root1)
        e1.pack(side="top",anchor=CENTER,pady=10)
        Label(root1,text="Enter player 2 name",bg="black",fg="white",font=myFont,pady=10).pack(side="top",anchor=CENTER,pady=5)
        e2=Entry(root1)
        e2.pack(side="top",anchor=CENTER,pady=10)
        Label(root1,text="Enter player 3 name",bg="black",fg="white",font=myFont,pady=10).pack(side="top",anchor=CENTER,pady=5)
        e3=Entry(root1)
        e3.pack(side="top",anchor=CENTER,pady=10)
        Label(root1,text="Enter player 4 name",bg="black",fg="white",font=myFont,pady=10).pack(side="top",anchor=CENTER,pady=5)
        e4=Entry(root1)
        e4.pack(side="top",anchor=CENTER,pady=10)
        Button(root1,text="Submit",command=P_lobby4).pack(side="top",anchor=CENTER,pady=20)

def P_lobby2():
    global e1

    global p_name   
    player1=e1.get()
    p_name.append(player1)

    global e2    
    player2=e2.get()
    p_name.append(player2)
    root1.destroy()

def P_lobby3():
    global e1

    global p_name
    player1=e1.get()
    p_name.append(player1)

    global e2
    player2=e2.get()
    p_name.append(player2)

    global e3
    player3=e3.get()
    p_name.append(player3)
    root1.destroy()

def P_lobby4():
    global root
    global e1

    global p_name
    player1=e1.get()
    p_name.append(player1)

    global e2
    player2=e2.get()
    p_name.append(player2)

    global e3
    player3=e3.get()
    p_name.append(player3)

    global e4
    player4=e4.get()
    p_name.append(player4)
    root1.destroy()

def load():
    global k 
    k=1
    root1.destroy()
    pass

def rules():
    pass

def about():
    about_window = Toplevel()
    load=Image.open('about_us.png')
    render=ImageTk.PhotoImage(load)
    image=Label(about_window,image=render,borderwidth=0)
    image.image=render
    image.pack(side='top',anchor=CENTER)

win()
img()
t1='''ABOUT THE
CREATORS'''
t2='''HOW TO 
PLAY'''

newgame=Button(root1,text='NEW GAME',padx=35,pady=8,borderwidth=0,font='Bahnschrift 10',bg='white',fg='red',command=home)
continuegame=Button(root1,text='CONTINUE GAME',padx=16,pady=8,borderwidth=0,font='Bahnschrift 10',bg='white',fg='red',command=load)
rules=Button(root1,text=t2,padx=4,pady=10,width=13,borderwidth=0,font='Bahnschrift 10',bg='white',fg='purple',command=rules)
about=Button(root1,text=t1,padx=4,pady=15,width=12,borderwidth=0,font='Bahnschrift 10',bg='white',fg='blue',command=about)

newgame.place(x=371,y=118)
continuegame.place(x=375,y=174)
about.place(x=725,y=136)
rules.place(x=727,y=283) 

root1.mainloop()


root = Tk()
win1()
root.title('                                                                                                                                                                                                 MONOPOLY                                 ')
root.configure(bg='#36393e')
root.geometry('1270x735')

load = Image.open("monopoly_template.png")
render = ImageTk.PhotoImage(load)
img = Label(root,image=render)
img.image = render
img.place(x = 350,y = 65)

topframe = Frame(root)
bottomframe = Frame(root)

colour_set_brown = ['MEDITERRANEAN AVENUE','BALTIC AVENUE']
colour_set_lightblue = ['ORIENTAL AVENUE','VERMONT AVENUE','CONNECTICUT AVENUE']
colour_set_pink = ['ST. CHARLES PLACE','STATES AVENUE','VIRGINIA AVENUE']
colour_set_orange = ['ST. JAMES PLACE','TENNESSEE AVENUE','NEW YORK AVENUE']
colour_set_red = ['KENTUCKY AVENUE','INDIANA AVENUE','ILLINOIS AVENUE']
colour_set_yellow = ['ATLANTIC AVENUE','VENTNOR AVENUE','MARVIN GARDENS']
colour_set_green = ['PACIFIC AVENUE','NORTH CAROLINA AVENUE','PENNSYLVANIA AVENUE']
colour_set_blue = ['PARK PLACE','BOARDWALK']
colour = ['salmon2','skyblue','hotpink1','orange','brown1','light goldenrod','green yellow','dodgerblue2']

colour_set_list = [colour_set_brown,colour_set_lightblue,colour_set_pink,colour_set_orange,colour_set_red,colour_set_yellow,colour_set_green,colour_set_blue]
place_colour = ['brown','lightblue','pink','orange','red','yellow','green','blue']

order =  ['GO','MEDITERRANEAN AVENUE','COMMUNITY CHEST','BALTIC AVENUE','INCOME TAX','READING RAILROAD','ORIENTAL AVENUE','CHANCE','VERMONT AVENUE',

          'CONNECTICUT AVENUE','JUST VISITING','ST. CHARLES PLACE','ELECTRIC COMPANY','STATES AVENUE','VIRGINIA AVENUE','PENNSYLVANIA RAILROAD',

          'ST. JAMES PLACE','COMMUNITY CHEST','TENNESSEE AVENUE','NEW YORK AVENUE','FREE PARKING','KENTUCKY AVENUE','CHANCE','INDIANA AVENUE','ILLINOIS AVENUE',

          'B&O RAILROAD','ATLANTIC AVENUE','VENTNOR AVENUE','WATER WORKS','MARVIN GARDENS','GO TO JAIL','PACIFIC AVENUE','NORTH CAROLINA AVENUE','COMMUNITY CHEST',

          'PENNSYLVANIA AVENUE','SHORT LINE','CHANCE','PARK PLACE','LUXURY TAX','BOARDWALK']


coordinates = [[870,585],[809,599],[763,596],[717,596],[671,596],[625,596],[579,596],[533,596],[486,596],[441,596],[353,611],[368,524],[368,478],[368,432],[368,386],
                     [368,340],[368,293],[368,247],[368,201],[368,155],[380,95],[440,83],[486,83],[532,83],[578,83],[625,83],[671,83],[717,83],[763,83],[808,83],[870,93],[882,155],
                     [884,201],[882,247],[882,293],[882,339],[882,385],[882,432],[882,478],[882,524]]
places = []
place_query = 'select place from properties'
cur.execute(place_query)
cursor_result = cur.fetchall()
for place in cursor_result:
    places.append(place[0])
    
railroads = []
railroad_query = 'select Railroad from Railroads'
cur.execute(railroad_query)
cursor_result = cur.fetchall()
for railroad in cursor_result:
    railroads.append(railroad[0])
    
companies = ['ELECTRIC COMPANY','WATER WORKS']

place_price = [60,60,100,100,120,140,140,160,180,180,200,220,220,240,260,260,280,300,300,320,350,400]
railroad_price = [200,200,200,200]
company_price = [150,150]

rent_prices_places = []
cur.execute('select Nohouse from properties')
cursor_result = cur.fetchall()
for price in cursor_result:
    rent_prices_places.append(int(price[0]))

rent_prices_railroads = []
cur.execute('select OneRailRoad from Railroads')
cursor_result = cur.fetchall()
for price in cursor_result:
    rent_prices_railroads.append(int(price[0]))
    
house_price = []
cur.execute('select HouseCost from properties')
cursor_result = cur.fetchall()
for price in cursor_result:
    house_price.append(int(price[0]))

hotel_price = []
cur.execute('select HotelCost from properties')
cursor_result = cur.fetchall()
for price in cursor_result:
    hotel_price.append(int(price[0]))

##################


if k == 0:   
    property_state = ['sale','sale','sale','sale','sale','sale','sale','sale','sale','sale','sale','sale','sale','sale','sale','sale','sale','sale','sale','sale','sale','sale']
    railroad_state = ['sale','sale','sale','sale']
    company_state = ['sale','sale']
    landed = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    money1,money2,money3,money4 = (1500,1500,1500,1500)
    owned1 = []
    owned2 = []
    owned3 = []
    owned4 = []
    pos1,pos2,pos3,pos4 = (0,0,0,0)

    players = []
    for i in p_name:
        players.append(i)

    sets1,sets2,sets3,sets4 = [],[],[],[]
    list_of_players = []
    if len(p_name) == 2:
        p1 = [players[0],money1, owned1, pos1, sets1]
        p2 = [players[1],money2, owned2, pos2, sets2]
        list_of_players = [p1,p2]

    elif len(p_name) == 3:
        p1 = [players[0],money1, owned1, pos1, sets1]
        p2 = [players[1],money2, owned2, pos2, sets2]
        p3 = [players[2],money3, owned3, pos3, sets3]
        list_of_players = [p1,p2,p3]

    elif len(p_name) == 4:
        p1 = [players[0],money1, owned1, pos1, sets1]
        p2 = [players[1],money2, owned2, pos2, sets2]
        p3 = [players[2],money3, owned3, pos3, sets3]
        p4 = [players[3],money4, owned4, pos4, sets4]
        list_of_players = [p1,p2,p3,p4]

elif k == 1:
    property_state = []
    railroad_state = []
    company_state = []
    cur.execute('select PLAYER FROM PLAYER_INFO_1')
    cursor_result = cur.fetchall()
    for i in cursor_result:
        p_name.append(i)

    states = []
    cur.execute('select STATE from PROPERTY_INFO_1')
    cursor_result = cur.fetchall()
    for i in cursor_result:
        states.append(i)

    for i in range(22):
        property_state.append(states[i][0])

    for i in range(22,25):
        railroad_state.append(states[i][0])

    company_state = [states[26][0],states[27][0]]

    

    
    
    player_names = []
    cur.execute('select PLAYER from PLAYER_INFO_1')
    cursor_result = cur.fetchall()
    for i in cursor_result:
        player_names.append(i[0])
    player_money = []
    cur.execute('select MONEY from PLAYER_INFO_1')
    cursor_result = cur.fetchall()
    for i in cursor_result:
        player_money.append(i[0])

    position = []
    cur.execute('select POSITION from PLAYER_INFO_1')
    cursor_result = cur.fetchall()
    for i in cursor_result:
        position.append(i[0])       
    
    
    owned = [[],[],[],[]]
    query = "select PLACES from PROPERTY_INFO_1 WHERE HOLDER = '{}'".format(player_names[0])
    cur.execute(query)
    cursor_result = cur.fetchall()
    for i in cursor_result:
        owned[0].append(i[0])
    query = "select PLACES from PROPERTY_INFO_1 WHERE HOLDER = '{}'".format(player_names[1])
    cur.execute(query)
    cursor_result = cur.fetchall()
    for i in cursor_result:
        owned[1].append(i[0])

    if len(p_name) == 3:
        query = "select PLACES from PROPERTY_INFO_1 WHERE HOLDER = '{}'".format(player_names[2])
        cur.execute(query)
        for i in cursor_result:
            owned[2].append(i[0])

    elif len(p_name) == 4:
        query = "select PLACES from PROPERTY_INFO_1 WHERE HOLDER = '{}'".format(player_names[3])
        cur.execute(query)
        for i in cursor_result:
            owned[3].append(i[0])



    cur.execute("select COUNT(*) from PLAYER_INFO_1")
    no_of_players = cur.fetchall()


    sets1,sets2,sets3,sets4 = ['','','','']
    if no_of_players[0][0] == 2:
        p1 = [player_names[0],player_money[0], owned[0], position[0], sets1]
        p2 = [player_names[1],player_money[1], owned[1], position[1], sets2]
        list_of_players = [p1,p2] 

    elif no_of_players[0][0] == 3:
        p1 = [player_names[0],player_money[0], owned[0], position[0], sets1]
        p2 = [player_names[1],player_money[1], owned[1], position[1], sets2]
        p3 = [player_names[2],player_money[2], owned[2], position[2], sets3]
        list_of_players = [p1,p2,p3]
    
    else:
        p1 = [player_names[0],player_money[0], owned[0], position[0], sets1]
        p2 = [player_names[1],player_money[1], owned[1], position[1], sets2]
        p3 = [player_names[2],player_money[2], owned[2], position[2], sets3]
        p4 = [player_names[3],player_money[3], owned[3], position[3], sets4]
        list_of_players = [p1,p2,p3,p4]



n=4  #no of players

players=[]  #correct order of player names

money_start=1500  #starting money

load = Image.open("monopoly_player_icons\\player_1.png")
render = ImageTk.PhotoImage(load)
P1 = Label(root,image=render)
P1.image = render
P1.place(x=855,y=570,height = 20,width = 20)

load = Image.open("monopoly_player_icons\\player_2.png")
render = ImageTk.PhotoImage(load)
P2 = Label(root,image=render)
P2.image = render
P2.place(x=885,y=570,height = 20,width = 20)

load = Image.open("monopoly_player_icons\\player_3.png")
render = ImageTk.PhotoImage(load)
P3 = Label(root,image=render)
P3.image = render
P3.place(x=855,y=600,height = 20,width = 20)

load = Image.open("monopoly_player_icons\\player_4.png")
render = ImageTk.PhotoImage(load)
P4 = Label(root,image=render)
P4.image = render
P4.place(x=885,y=600,height = 20,width = 20)

def buttons(PLACE):
    global owner
    global picture_popup
    picture_popup = Toplevel()
    image_load = Image.open('propertycards\\'+PLACE+'.png')
    Render = ImageTk.PhotoImage(image_load)
    image_label = Label(picture_popup,image=Render)
    image_label.image = Render
    image_label.pack()
    for owner in list_of_players:
        if PLACE in owner[2]:
            if PLACE in places:
                if property_state[places.index(PLACE)] == 'bought' or property_state[places.index(PLACE)] in ['1','2','3','4','hotel','colour_set']:
                    Button(picture_popup,text = 'MORTGAGE',command = lambda:mortgage(owner,PLACE)).pack()
                else:
                    Button(picture_popup,text = 'UNMORTGAGE',command = lambda:mortgage(owner,PLACE)).pack()
            elif PLACE in railroads:
                if railroad_state[railroads.index(PLACE)] == 'bought' or railroad_state[railroads.index(PLACE)] in ['1','2','3','4','hotel','colour_set']:
                    Button(picture_popup,text = 'MORTGAGE',command = lambda:mortgage(owner,PLACE)).pack()
                else:
                    Button(picture_popup,text = 'UNMORTGAGE',command = lambda:mortgage(owner,PLACE)).pack()
            else:
                if company_state[companies.index(PLACE)] == 'bought' or company_state[companies.index(PLACE)] in ['1','2','3','4','hotel','colour_set']:
                    Button(picture_popup,text = 'MORTGAGE',command = lambda:mortgage(owner,PLACE)).pack()
                else:
                    Button(picture_popup,text = 'UNMORTGAGE',command = lambda:mortgage(owner,PLACE)).pack()
        else:
            image_label.after(5000,lambda:image_label.destroy())
#====================================================PURCHASING A PROP.=========================================================================
def purchase(PLACE,current_player):
    current_player[2].append(PLACE)
   #NEW
    if PLACE in places:
        property_state[places.index(PLACE)] = 'bought'


        for Set in colour_set_list:
            if PLACE in Set:
                if set(Set).intersection(set(current_player[2])) == set(Set):
                    for i in Set:
                        rent_prices_places[places.index(i)] = rent_prices_places[places.index(i)]*(2)
                        
                        property_state[places.index(i)] = 'colour_set'

                    messagebox.showinfo(current_player[0].upper()+"'S TURN!","ACHIEVED COLOUR SET FOR :"+place_colour[colour_set_list.index(Set)].upper())

    elif PLACE in railroads:
        railroad_state[railroads.index(PLACE)] = 'bought'
    elif PLACE in companies:
        company_state[companies.index(PLACE)] = 'bought'
        
    if PLACE in places:
        current_player[1] = current_player[1] - place_price[places.index(PLACE)]

    elif PLACE in railroads:
        current_player[1] = current_player[1] - railroad_price[railroads.index(PLACE)]
    
    elif PLACE in companies:
        current_player[1] = current_player[1] - company_price[companies.index(PLACE)]     
    display()          
#====================================================PURCHASING A PROP.===================================================================#
#########################################################################################################################################################
#==========================================================PLACE=========================================================================#
def place(PLACE,current_player):
    def property_popup(PLACE,current_player):

        def yes():
            purchase(PLACE,current_player)
            property_available_window.destroy() 

        def no():
            property_available_window.destroy()

        property_available_window = Toplevel()
        
        if PLACE in places:
            for i in colour_set_list:
                if PLACE in i:
                    COLOUR = colour[colour_set_list.index(i)]
                    property_available_window.configure(bg = COLOUR)
        elif PLACE in railroads:
            COLOUR = 'slate gray'
            property_available_window.configure(bg = COLOUR)
        else:
            COLOUR = 'gold'
            property_available_window.configure(bg = COLOUR)

        property_available_window.title(current_player[0].upper()+"'S TURN!")
        image_load = Image.open('propertycards\\'+PLACE+'.png')
        Render = ImageTk.PhotoImage(image_load)
        image_label = Label(property_available_window,image=Render)
        image_label.image = Render
        image_label.pack(side = LEFT)
        Label(property_available_window,text = 'DO YOU WANT TO PURCHASE '+PLACE+"?",font = 'calibri 14 bold',bg = COLOUR,fg = 'green').pack(side = TOP)
        if PLACE in places:
            Label(property_available_window,text = 'PRICE --> '+str(place_price[places.index(PLACE)])+'$',font = 'calibri 20 bold',bg = COLOUR,fg = 'green').pack()
        
        elif PLACE in railroads:
            Label(property_available_window,text = 'PRICE --> '+str(railroad_price[railroads.index(PLACE)])+'$',font = 'calibri 20 bold',bg = COLOUR,fg = 'green').pack()
        
        else:
            Label(property_available_window,text = 'PRICE --> '+str(company_price[companies.index(PLACE)])+'$',font = 'calibri 20 bold',bg = COLOUR,fg = 'green').pack()
        
        Label(property_available_window,text = "BALANCE: "+str(current_player[1])+"$",font = 'calibri 20 bold',bg = COLOUR,fg = 'black').pack(side = BOTTOM)
        
        Button(property_available_window,text = 'YES',command = yes,height = 5,width = 23,font = 'calibri 14 bold',bg = 'white',fg = 'green').pack(side = LEFT)
        Button(property_available_window,text = 'NO',command = no,height = 5,width = 23,font = 'calibri 14 bold',bg = 'white',fg = 'red').pack(side = LEFT)
        property_available_window.mainloop()

    #PLACE is the button of the current property
    if PLACE in places:
        if property_state[places.index(PLACE)] == 'sale':
            property_popup(PLACE,current_player)

    elif PLACE in companies:
        if company_state[companies.index(PLACE)] == 'sale': 
            property_popup(PLACE,current_player)

    elif PLACE in railroads:
        if railroad_state[railroads.index(PLACE)] == 'sale':        
            property_popup(PLACE,current_player)
#==========================================================PLACE=========================================================================#
#########################################################################################################################################
#=========================================================HOUSE==========================================================================#
rent_1_house = []
rent_2_house = []
rent_3_house = []
rent_4_house = []
rent_hotel = []
query_1 = 'select OneHouse from properties'
query_2 = 'select TwoHouses from properties'
query_3 = 'select ThreeHouses from properties'
query_4 = 'select FourHouses from properties'
query_hotel = 'select Hotel from properties'

cur.execute(query_1)
cursor_result = cur.fetchall()
for rent in cursor_result:
    rent_1_house.append(int(rent[0]))

cur.execute(query_2)
cursor_result = cur.fetchall()
for rent in cursor_result:
    rent_2_house.append(int(rent[0]))

cur.execute(query_3)
cursor_result = cur.fetchall()
for rent in cursor_result:
    rent_3_house.append(int(rent[0]))

cur.execute(query_4)
cursor_result = cur.fetchall()
for rent in cursor_result:
    rent_4_house.append(int(rent[0]))
    

cur.execute(query_hotel)
cursor_result = cur.fetchall()
for rent in cursor_result:
    rent_hotel.append(int(rent[0]))

def house(PLACE,current_player):
    if len(PLACE) > 0 :
        properties=[]
        p_state=[]
        available_properties=[]
        max_h = 0
        temp_prop = []
        property_state1 = []
        for i in property_state:
            if i == 'colour_set':
                property_state1.append(0)
            elif i == '1' or i == '2' or i == '3' or i == '4':
                property_state1.append(int(i))
            elif i == 'hotel':
                property_state1.append(5)
            else:
                property_state1.append(i)
                
        for i in PLACE:
            temp_prop=[]
            prop=[]
            p_state=[]
            if i == colour_set_brown:
                prop = colour_set_brown
                p_state = property_state1[0:2]
            elif i == colour_set_lightblue:
                prop = colour_set_lightblue
                p_state = property_state1[2:5]
            elif i == colour_set_pink:
                prop = colour_set_pink
                p_state = property_state1[5:8]
            elif i == colour_set_orange:
                prop = colour_set_orange
                p_state = property_state1[8:11]
            elif i == colour_set_red:
                prop = colour_set_red
                p_state = property_state1[11:14]
            elif i == colour_set_yellow:
                prop = colour_set_yellow
                p_state = property_state1[14:17]
            elif i == colour_set_green:
                prop = colour_set_green
                p_state = property_state1[17:20]
            elif i == colour_set_blue:
                prop = colour_set_blue
                p_state = property_state1[20:22]
            print("P_state",p_state)
            print("prop",prop)
            max_h = max(p_state)
            print("Max_p" , max_h)
            k=0
            for j in prop:
                m = p_state[k]
                if m < max_h:
                    temp_prop.append(j)
                k+=1
            print(temp_prop)
            if len(temp_prop) != 0:
                for j in temp_prop:
                    available_properties.append(j)
            else:
                for j in prop:
                    available_properties.append(j)
        house_window = Toplevel()
        Label(house_window,text = 'WHICH PROPERTY DO YOU WANT TO BUILD A HOUSE IN?').pack(side = TOP)
        for j in available_properties:
            image_load = Image.open('propertycards/'+j+'.png')
            Render = ImageTk.PhotoImage(image_load)
            image_load = Button(house_window,image=Render,command = lambda:house_from_button(j))
            image_load.image = Render
            image_load.pack(side = LEFT)
    elif len(PLACE) == 0:
        messagebox.showinfo(current_player[0]+"'s turn!","you don't have any colour sets to build a house!")

    elif property_state[places.index(PLACE)] == 'colour_set':
        result = messagebox.askquestion("You have already purchased "+PLACE+"!","DO YOU WANT TO BUILD A HOUSE?",type = 'yesno')
        if result == 'yes':
            if property_state[places.index(PLACE)].isdigit():
                result = messsagebox.askquestion("confirmation","The price of a house in "+PLACE+' is ' + str(house_price[places.index(PLACE)])+" Are you sure you want to buy a house?",type = 'yesno')
                if result == 'yes':
                     property_state[places.index(PLACE)]+= 1
                     current_player[3] - house_price[places.index(PLACE)]

                     if int(property_state[places.index(PLACE)]) == 5:
                         property_state[places.index(PLACE)] = 'hotel'
                         current_player[3] - hotel_price[places.index(PLACE)] #hotel_price
                         
                     elif int(property_state[places.index(PLACE)]) == 2:
                         rent_prices_places[places.index(PLACE)] = rent_2_house[places.index(PLACE)]
                         
                     elif int(property_state[places.index(PLACE)]) == 3:
                        rent_prices_places[places.index(PLACE)] = rent_3_house[places.index(PLACE)]

                     elif int(property_state[places.index(PLACE)]) == 4:
                        rent_prices_places[places.index(PLACE)] = rent_4_house[places.index(PLACE)]
                                         
            else:
                result = messagebox.askquestion("confirmation","The price of a house in "+PLACE +" is "+str(house_price[places.index(PLACE)])+" Are you sure you want to buy a house?",type = 'yesno') 
                if result == 'yes':
                    property_state[places.index(PLACE)] = '1'
                    rent_prices_places[places.index(PLACE)] = rent_1_house[places.index(PLACE)]
    
    def house_from_button(PLACE):
        house_window.destroy()
        result = messagebox.askquestion(current_player[0]+"'s turn!","are you sure you want to build a house in "+PLACE+"?")
        if result == 'yes':
            if property_state[places.index(PLACE)].isdigit():
                result = messsagebox.askquestion("confirmation","The price of a house in "+PLACE+' is ' + str(house_price[places.index(PLACE)])+" Are you sure you want to buy a house?",type = 'yesno')
                if result == 'yes':
                     property_state[places.index(PLACE)]+= 1
                     current_player[3] - house_price[places.index(PLACE)]

                     if int(property_state[places.index(PLACE)]) == 5:
                         property_state[places.index(PLACE)] = 'hotel'
                         current_player[3] - hotel_price[places.index(PLACE)] #hotel_price
                         
                     elif int(property_state[places.index(PLACE)]) == 2:
                         rent_prices_places[places.index(PLACE)] = rent_2_house[places.index(PLACE)]
                         
                     elif int(property_state[places.index(PLACE)]) == 3:
                        rent_prices_places[places.index(PLACE)] = rent_3_house[places.index(PLACE)]

                     elif int(property_state[places.index(PLACE)]) == 4:
                        rent_prices_places[places.index(PLACE)] = rent_4_house[places.index(PLACE)]
                                         
            else:
                result = messagebox.askquestion("confirmation","The price of a house in "+PLACE +" is "+str(house_price[places.index(PLACE)])+" Are you sure you want to buy a house?",type = 'yesno') 
                if result == 'yes':
                    property_state[places.index(PLACE)] = '1'
                    rent_prices_places[places.index(PLACE)] = rent_1_house[places.index(PLACE)]
        
        
#=========================================================HOUSE==========================================================================#    
#########################################################################################################################################################
def sets(current_player):
    if current_player == list_of_players[len(p_name)-1]:
        current_player = list_of_players[0]
    else:
        current_player = list_of_players[list_of_players.index(current_player) + 1]
    colour_list = []
    if set(colour_set_brown).intersection(set(current_player[2])) == set(colour_set_brown):
        current_player[4].append('brown')
        colour_list.append(colour_set_brown)

    if set(colour_set_lightblue).intersection(set(current_player[2])) == set(colour_set_lightblue):
        current_player[4].append('lightblue')
        colour_list.append(colour_set_lightblue)
    
    if set(colour_set_lightblue).intersection(set(current_player[2])) == set(colour_set_pink):
        current_player[4].append('pink')
        colour_list.append(colour_set_pink)
    
    if set(colour_set_lightblue).intersection(set(current_player[2])) == set(colour_set_orange):
        current_player[4].append('orange')
        colour_list.append(colour_set_orange)
    
    if set(colour_set_lightblue).intersection(set(current_player[2])) == set(colour_set_red):
        current_playe[4].append('red')
        colour_list.append(colour_set_red)
    
    if set(colour_set_lightblue).intersection(set(current_player[2])) == set(colour_set_yellow):
        current_player[4].append('yellow')
        colour_list.append(colour_set_yellow)
    
    if set(colour_set_lightblue).intersection(set(current_player[2])) == set(colour_set_green):
        curernt_player[4].append('green')
        colour_list.append(colour_set_green)
    
    if set(colour_set_lightblue).intersection(set(current_player[2])) == set(colour_set_blue):
        current_player[4].append('blue')
        colour_list.append(colour_set_blue)

    house(colour_list,current_player)
#==========================================================RENT===========================================================================#
def rent(PLACE,current_player,rent_price):
    def rent_popup(PLACE,current_player,owner,rent_price):

        #
        def Destroy():
            if PLACE in places:
                if property_state[places.index(PLACE)] == 'mortgaged':
                    pass

                else:
                    current_player[1] = current_player[1] - rent_price
                    owner[1] = owner[1] + rent_price
                    display()
                    rent_window.destroy()

            if PLACE in railroads:
                if railroad_state[railroads.index(PLACE)] == 'mortgaged':
                    pass

                else:
                    current_player[1] = current_player[1] - rent_price
                    owner[1] = owner[1] + rent_price
                    display()
                    rent_window.destroy()
            if PLACE in companies:
                if company_state[companies.index(PLACE)] == 'mortgaged':
                    pass
                else:
                    current_player[1] = current_player[1] - rent_price
                    owner[1] = owner[1] + rent_price
                    display()
                    rent_window.destroy()
        #    
        
        rent_window = Toplevel()
        rent_window.configure(bg = 'white')
        rent_window.title(current_player[0].upper()+"'S TURN!")
        if PLACE in places:
            if property_state[places.index(PLACE)] == 'mortgaged':
                Label(rent_window,text = "THIS PROPERTY IS MORTGAGED",font = 'calibri 20 bold',bg = 'white',fg = 'black').pack()
                Label(rent_window,text = "PAY NOTHING",font = 'calibri 18 bold',bg = 'white',fg = 'black').pack()
                Button(rent_window,text = 'yay',command = Destroy,font = 'calibri 14 bold',bg = 'white',fg = 'black').pack()
            else:
                Label(rent_window,text = "THIS PROPERTY IS ALREADY OWNED BY "+owner[0].upper(),font = 'calibri 20 bold',bg = 'white',fg = 'orangered').pack()
                Label(rent_window,text = " PAY "+str(rent_price)+"$"+" TO CONTINUE",font = 'calibri 18 bold',bg = 'white',fg = 'orangered').pack()
                Label(rent_window,text = "BALANCE: "+str(current_player[1]),font = 'calibri 20 bold',bg = 'white',fg = 'black').pack()
                Button(rent_window,text = 'OKAY',command = Destroy,font = 'calibri 14 bold',bg = 'white',fg = 'black').pack()

        elif PLACE in railroads:
            if railroad_state[railroads.index(PLACE)] == 'mortgaged':
                Label(rent_window,text = "THIS PROPERTY IS MORTGAGED",font = 'calibri 20 bold',bg = 'white',fg = 'black').pack()
                Label(rent_window,text = "PAY NOTHING",font = 'calibri 18 bold',bg = 'white',fg = 'black').pack()
                Button(rent_window,text = 'yay',command = Destroy,font = 'calibri 14 bold',bg = 'white',fg = 'black').pack()
            else:
                Label(rent_window,text = "THIS RAILROAD IS ALREADY OWNED BY "+owner[0].upper(),font = 'calibri 20 bold',bg = 'white',fg = 'orangered').pack()
                Label(rent_window,text = " PAY "+str(rent_price)+"$"+" TO CONTINUE",font = 'calibri 18 bold',bg = 'white',fg = 'orangered').pack()
                Label(rent_window,text = "BALANCE: "+str(current_player[1]),font = 'calibri 20 bold',bg = 'white',fg = 'black').pack()
                Button(rent_window,text = 'OKAY',command = Destroy,font = 'calibri 14 bold',bg = 'white',fg = 'black').pack()
            
        elif PLACE in companies:
            if company_state[companies.index(PLACE)] == 'mortgaged':
                Label(rent_window,text = "THIS PROPERTY IS MORTGAGED",font = 'calibri 20 bold',bg = 'white',fg = 'black').pack()
                Label(rent_window,text = "PAY NOTHING",font = 'calibri 18 bold',bg = 'white',fg = 'black').pack()
                Button(rent_window,text = 'yay',command = Destroy,font = 'calibri 14 bold',bg = 'white',fg = 'black').pack()
            else:
                Label(rent_window,text = "THIS COMPANY IS ALREADY OWNED BY "+owner[0].upper(),font = 'calibri 20 bold',bg = 'white',fg = 'orangered').pack()
                Label(rent_window,text = " PAY "+str(rent_price)+"$"+" TO CONTINUE",font = 'calibri 18 bold',bg = 'white',fg = 'orangered').pack()
                Label(rent_window,text = "BALANCE: "+str(current_player[1]),font = 'calibri 20 bold',bg = 'white',fg = 'black').pack()
                Button(rent_window,text = 'OKAY',command = Destroy,font = 'calibri 14 bold',bg = 'white',fg = 'black').pack()

        rent_window.mainloop()
        
    #IF A PLAYER LANDS ON HIS OWN PROPERTY
    if PLACE in current_player[2]:
        if PLACE in places:
            house(PLACE,current_player)
    else:
        #
        for owner in list_of_players:
            if PLACE in owner[2]: 
                #IF IT'S A PLACE
                if PLACE in places:
                    if property_state[places.index(PLACE)] == 'mortgaged':
                        rent_popup(PLACE,current_player,owner,0)
                    else:
                        rent_popup(PLACE,current_player,owner,rent_price)

                #IF IT'S A RAILROAD
                elif PLACE in railroads:
                    rent_multiple = 0
                    for i in owner[2]:
                        if i in railroads:
                            if rent_multiple == 0:
                                rent_multiple+=1
                            else:
                                rent_multiple = rent_multiple*2
                    if railroad_state[railroads.index(PLACE)] == 'mortgaged':
                        rent_popup(PLACE,current_player,owner,0)
                    else:
                        rent_popup(PLACE,current_player,owner,(rent_price*rent_multiple))

                #IF IT'S A COMPANY
                elif PLACE in companies:
                    #NUMBER OF UTILITIES FEATURE
                    company_count = 0
                    for i in companies:
                        if i in owner[2]:
                            company_count  += 1
                    
                    if company_state[companies.index(PLACE)] == 'mortgaged':
                        rent_popup(PLACE,current_player,owner,0)

                    elif company_count == 1:
                        rent_popup(PLACE,current_player,owner,dice*4)
                    
                    elif company_count == 2:
                        rent_popup(PLACE,current_player,owner,dice*10)

def unmortgage(current_player,PLACE):
    result = messagebox.askquestion(current_player[0]+"'s turn!","are you sure you want to rebuy the property?",type = 'yesno')
    if result == 'yes':
        if PLACE in places:
            property_state[places.index(PLACE)] = 'unmortgaged'
            messagebox.showinfo(current_player[0]+"'s turn!","you must pay "+str(place_price[places.index(PLACE)]/2 + (place_price[places.index(PLACE)]/2)/10))
            current_player[1] += place_price[places.index(PLACE)]/2 + (place_price[places.index(PLACE)]/2)/10
        elif PLACE in railroads:
            railroad_state[railroads.index(PLACE)] = 'unmortgaged'
            messagebox.showinfo(current_player[0]+"'s turn!","you must pay "+str(railroad_price[railroads.index(PLACE)]/2 + (railroad_price[railroads.index(PLACE)]/2)/10))
            current_player[1] += railroad_price[railroads.index(PLACE)]/2 + (railroad_price[railroads.index(PLACE)]/2)/10
        else:
            company_state[companies.index(PLACE)] = 'unmortgaged'
            messagebox.showinfo(current_player[0]+"'s turn!","you must pay "+str(company_price[companies.index(PLACE)]/2 + (company_price[companies.index(PLACE)]/2)/10))
            current_player[1] += company_price[companies.index(PLACE)]/2 + (company_price[companies.index(PLACE)]/2)/10


def mortgage(current_player,PLACE):
    mortgage_window = Toplevel()
    def confirmed(props,current_player,mortgage_window):
        mortgage_window.destroy()
        if props in places:
            if property_state[places.index(props)] in ['1','2','3','4','hotel']:
                result = messagebox.askquestion(current_player+"'s turn!","you have houses in this property! you must first sell the houses back at half price.")
                if result == 'yes':
                    if property_state[places.index(props)].isdigit():
                        current_player[1] += ((house_price[places.index(props)])*int(property_state[places.index(props)]))/2
                    else:
                        current_player[1] += hotel_price[places.index(props)]/2

            for Set in colour_set_list:
                if props in Set:
                    if set(Set).intersection(set(current_player[2])) == set(Set):
                        for i in Set:
                            rent_prices_places[places.index(i)] = rent_prices_places[places.index(i)]/2
                            property_state[places.index(i)] = 'colour_set'

            property_state[places.index(props)] = 'mortgaged'
            current_player[1] += place_price[places.index(props)]/2

        elif props in railroads:
            railroad_state[railroads.index(props)] = 'mortgaged'
            current_player[1] += railroad_price[railroads.index(props)]/2

        else:
            company_state[companies.index(props)] = 'mortgaged'
            current_player[1] += company_price[companies.index(props)]/2

            
    if PLACE in order:
        
        if PLACE in places:
            if property_state[places.index(PLACE)] == 'mortgaged':
                unmortgage(current_player,PLACE)
        elif PLACE in railroads:
            if railroad_state[railroads.index(PLACE)] == 'mortgaged':
                unmortgage(current_player,PLACE)
        else:
            if company_state[companies.index(PLACE)] == 'mortgaged':
                unmortgage(current_player,PLACE)
        picture_popup.destroy()
        if list_of_players.index(current_player) < len(p_name)-1:
            current_player = list_of_players[list_of_players.index(current_player)+1]
        else:
            current_player = list_of_players[0]

        if current_player[1] <= 0:
            messagebox.showinfo(current_player[0]+"'s turn!","YOU HAVE NO MONEY LEFT!")
            result = messagebox.askquestion(current_player[0]+"'s turn!","Do you want to mortgage a property?",type = 'yesno')
            if result == "yes":
                #
                Label(mortgage_window,text = 'CHOOSE THE PROPERTY YOU WOULD LIKE TO MORTGAGE:').pack(side = TOP)
                for props in current_player[2]:
                    load = Image.open("propertycards\\"+props+".png")
                    render = ImageTk.PhotoImage(load)
                    prop = Button(mortgage_window,image=render,command = lambda:confirmed(props,current_player))
                    prop.image = render
                    prop.pack(side = LEFT)
                    messagebox.showinfo(current_player[0]+"'s turn!","YOU HAVE CHOSEN TO MORTGAGE "+PLACE.upper()+"!")
        else:
            if PLACE in places:
                if property_state[places.index(PLACE)] in ['bought','1','2','3','4','hotel']:
                    messagebox.showinfo(current_player[0]+"'s turn!","YOU HAVE CHOSEN TO MORTGAGE "+PLACE.upper()+"!")
                    confirmed(PLACE,current_player,mortgage_window)       
            elif PLACE in railroads:
                if railroad_state[railroads.index(PLACE)] in ['bought','1','2','3','4','hotel']:
                    messagebox.showinfo(current_player[0]+"'s turn!","YOU HAVE CHOSEN TO MORTGAGE "+PLACE.upper()+"!")
                    confirmed(PLACE,current_player,mortgage_window)
            else:
                if company_state[companies.index(PLACE)] in ['bought','1','2','3','4','hotel']:
                    messagebox.showinfo(current_player[0]+"'s turn!","YOU HAVE CHOSEN TO MORTGAGE "+PLACE.upper()+"!")
                    confirmed(PLACE,current_player,mortgage_window)

    else:
        #mortgage_window = Toplevel()
        if list_of_players.index(current_player) < len(p_name)-1:
            current_player = list_of_players[list_of_players.index(current_player)+1]
        else:
            current_player = list_of_players[0]

        result = messagebox.askquestion(current_player[0]+"'s turn!","Do you want to mortgage a property?",type = 'yesno')
        if result == "yes":
           #mortgage_window = Toplevel()
            Label(mortgage_window,text = 'CHOOSE THE PROPERTY YOU WOULD LIKE TO MORTGAGE:').pack(side = TOP)
            for props in current_player[2]:
                load = Image.open("propertycards\\"+props+".png")
                render = ImageTk.PhotoImage(load)
                prop = Button(mortgage_window,image=render,command = lambda:confirmed(props,current_player,mortgage_window))
                prop.image = render
                prop.pack(side = LEFT)
#==========================================================RENT=================================================================
#=========================================================START=================================================================
def start(n1):
    start_window = Tk()
    messagebox.showinfo("Welcome!","This is a test run, which will decide the order in which you players will be taking turns (highest to lowest): \n")
    l=[]  #list which has (first roll (to start),player name)
    players=[p1_name,p2_name,p3_name,p4_name] #list with players which we will use only in this funcion as we will switch to other later which has the order also
    for i in range(n1):
        print("Player" , (i+1) , ",please roll the dice (Press enter)")
        t1=input()
        a=[]  #temporary list
        a.append((random.randint(1,6)+random.randint(1,6)))
        #Every time a player rolls a dice we need to add two randint functions to simulate two dice and add up the total
        #Instead of just randomising a number between 1 & 12
        #Eg:3 on one and 4 on the other would amount to a roll of 7
        print("You rolled a", a[0])
        a.append(p[i])
        l.append(a)
    l.sort()
    for i in range(n1):
        players.append(l[i][1])
    print("The order of players is: \n")
    for i in range(n1):
        print(players[i])

        

def display():
    x=0
    y=0
    for i in range(len(p_name)):
        if i == 0:
            player_color = 'firebrick2'
            x=40
            y=50
        elif i == 1:
            player_color = 'deepskyblue2'
            x=40
            y=370
        elif i == 2:
            player_color = 'spring green4'
            x=1000
            y=50
        elif i == 3:
            player_color = 'gold'
            x=1000
            y=370
        p1_label=Label(root,text=p_name[i],bg='#36393e',fg=player_color,font="TkDefaultFont 30 bold",anchor=W)
        p1_label.place(x=x,y=y,height=60,width=290)

        p1_money_label=Label(root,text="Money - " + str(list_of_players[i][1]),bg='#36393e',fg=player_color,font="TkDefaultFont 12 bold",anchor=W)
        p1_money_label.place(x=x,y=y+70,height=30,width=290)

        p1_location_label=Label(root,text="Location - " + order[(list_of_players[i][3])],bg='#36393e',fg=player_color,font="TkDefaultFont 12 bold",anchor=W)
        p1_location_label.place(x=x,y=y+110,height=30,width=290)

        p1_properties_label=Label(root,text="Properties Owned - "+str(len(list_of_players[i][2])),bg='#36393e',fg=player_color,font="TkDefaultFont 12 bold",anchor=W)
        p1_properties_label.place(x=x,y=y+150,height=30,width=290)

        display_properties(x,y+190,i)

    
def display_properties(x1,y1,i):
    f1=Frame(root,bg="#36393e")
    f1.place(x=x1,y=y1,height=80,width=188)
        
    if places[0] in list_of_players[i][2]:
        Button(f1,text="",bg="saddle brown",relief="solid",borderwidth=0.5,command = lambda:buttons('MEDITERRANEAN AVENUE')).place(x=8,y=8,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=8,y=8,height=10,width=10)
    if places[1] in list_of_players[i][2]:
        Button(f1,text="",bg="saddle brown",relief="solid",borderwidth=0.5,command = lambda:buttons('BALTIC AVENUE')).place(x=8,y=26,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=8,y=26,height=10,width=10)
    if places[2] in list_of_players[i][2]:
        Button(f1,text="",bg="light sky blue",relief="solid",borderwidth=0.5,command = lambda:buttons('ORIENTAL AVENUE')).place(x=26,y=8,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=26,y=8,height=10,width=10)
    if places[3] in list_of_players[i][2]:
        Button(f1,text="",bg="light sky blue",relief="solid",borderwidth=0.5,command = lambda:buttons('VERMONT AVENUE')).place(x=26,y=26,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=26,y=26,height=10,width=10)
    if places[4] in list_of_players[i][2]:
        Button(f1,text="",bg="light sky blue",relief="solid",borderwidth=0.5,command = lambda:buttons('CONNECTICUT AVENUE')).place(x=26,y=44,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=26,y=44,height=10,width=10)
    if places[5] in list_of_players[i][2]:
        Button(f1,text="",bg="deep pink3",relief="solid",borderwidth=0.5,command = lambda:buttons('ST. CHARLES PLACE')).place(x=44,y=8,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=44,y=8,height=10,width=10)
    if places[6] in list_of_players[i][2]:
        Button(f1,text="",bg="deep pink3",relief="solid",borderwidth=0.5,command = lambda:buttons('STATES AVENUE')).place(x=44,y=26,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=44,y=26,height=10,width=10)
    if places[7] in list_of_players[i][2]:
        Button(f1,text="",bg="deep pink3",relief="solid",borderwidth=0.5,command = lambda:buttons('VIRGINIA AVENUE')).place(x=44,y=44,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=44,y=44,height=10,width=10)
    if places[8] in list_of_players[i][2]:
        Button(f1,text="",bg="dark orange",relief="solid",borderwidth=0.5,command = lambda:buttons('ST. JAMES PLACE')).place(x=62,y=8,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=62,y=8,height=10,width=10)
    if places[9] in list_of_players[i][2]:
        Button(f1,text="",bg="dark orange",relief="solid",borderwidth=0.5,command = lambda:buttons('TENNESSEE AVENUE')).place(x=62,y=26,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=62,y=26,height=10,width=10)
    if places[10] in list_of_players[i][2]:
        Button(f1,text="",bg="dark orange",relief="solid",borderwidth=0.5,command = lambda:buttons('NEW YORK AVENUE')).place(x=62,y=44,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=62,y=44,height=10,width=10)
    if places[11] in list_of_players[i][2]:
        Button(f1,text="",bg="red2",relief="solid",borderwidth=0.5,command = lambda:buttons('KENTUCKY AVENUE')).place(x=80,y=8,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=80,y=8,height=10,width=10)
    if places[12] in list_of_players[i][2]:
        Button(f1,text="",bg="red2",relief="solid",borderwidth=0.5,command = lambda:buttons('INDIANA AVENUE')).place(x=80,y=26,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=80,y=26,height=10,width=10)
    if places[13] in list_of_players[i][2]:
        Button(f1,text="",bg="red2",relief="solid",borderwidth=0.5,command = lambda:buttons('ILLINOIS AVENUE')).place(x=80,y=44,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=80,y=44,height=10,width=10)
    if places[14] in list_of_players[i][2]:
        Button(f1,text="",bg="yellow2",relief="solid",borderwidth=0.5,command = lambda:buttons('ATLANTIC AVENUE')).place(x=98,y=8,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=98,y=8,height=10,width=10)
    if places[15] in list_of_players[i][2]:
        Button(f1,text="",bg="yellow2",relief="solid",borderwidth=0.5,command = lambda:buttons('VENTNOR AVENUE')).place(x=98,y=26,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=98,y=26,height=10,width=10)
    if places[16] in list_of_players[i][2]:
        Button(f1,text="",bg="yellow2",relief="solid",borderwidth=0.5,command = lambda:buttons('MARVIN GARDENS')).place(x=98,y=44,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=98,y=44,height=10,width=10)
    if places[17] in list_of_players[i][2]:
        Button(f1,text="",bg="forest green",relief="solid",borderwidth=0.5,command = lambda:buttons('PACIFIC AVENUE')).place(x=116,y=8,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=116,y=8,height=10,width=10)
    if places[18] in list_of_players[i][2]:
        Button(f1,text="",bg="forest green",relief="solid",borderwidth=0.5,command = lambda:buttons('NORTH CAROLINA AVENUE')).place(x=116,y=26,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=116,y=26,height=10,width=10)
    if places[19] in list_of_players[i][2]:
        Button(f1,text="",bg="forest green",relief="solid",borderwidth=0.5,command = lambda:buttons('PENNSYLVANIA AVENUE')).place(x=116,y=44,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=116,y=44,height=10,width=10)
    if places[20] in list_of_players[i][2]:
        Button(f1,text="",bg="dodgerblue3",relief="solid",borderwidth=0.5,command = lambda:buttons('PARK PLACE')).place(x=134,y=8,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=134,y=8,height=10,width=10)
    if places[21] in list_of_players[i][2]:
        Button(f1,text="",bg="dodgerblue3",relief="solid",borderwidth=0.5,command = lambda:buttons('BOARDWALK')).place(x=134,y=26,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=134,y=26,height=10,width=10)
    if railroads[0] in list_of_players[i][2]:
        Button(f1,text="",bg="grey10",relief="solid",borderwidth=0.5,command = lambda:buttons('READING RAILROAD')).place(x=152,y=8,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=152,y=8,height=10,width=10)
    if railroads[1] in list_of_players[i][2]:
        Button(f1,text="",bg="grey10",relief="solid",borderwidth=0.5,command = lambda:buttons('PENNSYLVANIA RAILROAD')).place(x=152,y=26,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=152,y=26,height=10,width=10)
    if railroads[2] in list_of_players[i][2]:
        Button(f1,text="",bg="grey10",relief="solid",borderwidth=0.5,command = lambda:buttons('B&O RAILROAD')).place(x=152,y=44,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=152,y=44,height=10,width=10)
    if railroads[3] in list_of_players[i][2]:
        Button(f1,text="",bg="grey10",relief="solid",borderwidth=0.5,command = lambda:buttons('SHORT LINE')).place(x=152,y=62,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=152,y=62,height=10,width=10)
    if companies[0] in list_of_players[i][2]:
        Button(f1,text="",bg="sandy brown",relief="solid",borderwidth=0.5,command = lambda:buttons('ELECTRIC COMPANY')).place(x=170,y=8,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=170,y=8,height=10,width=10)
    if companies[1] in list_of_players[i][2]:
        Button(f1,text="",bg="sandy brown",relief="solid",borderwidth=0.5,command = lambda:buttons('WATER WORKS')).place(x=170,y=26,height=10,width=10)
    else:
        Label(f1,text="",bg="white",relief="solid",borderwidth=0.5).place(x=170,y=26,height=10,width=10)
    
display()
#====================================================START===================================================================#
###########################################################################################################################################
#=====================================================GO=====================================================================#
def GO(current_player):
    pass
#=====================================================GO=====================================================================#
###########################################################################################################################################
#===================================================PARKING===================================================================#
def parking(current_player):
    pass
#===================================================PARKING====================================================================#
#############################################################################################################################################
#====================================================CHANCE===================================================================#
def chance(current_player):
    pass
#====================================================CHANCE======================================================================#
################################################################################################################################################
#=====================================================CHEST======================================================================#
def chest(current_player):
    pass
#=====================================================CHEST======================================================================#
###############################################################################################################################################
#======================================================TAX========================================================================#
def tax(current_player,tax_amount):
        messagebox.showinfo("LANDED ON TAX","PAY"+str(tax_amount)+"$!")
        current_player[1] = current_player[1] - tax_amount
#======================================================TAX========================================================================#
################################################################################################################################################
#===================================================GO TO JAIL=====================================================================#
#################################################################################################################################
#=======================================================ROW-1=====================================================================#
#these labels/places are in order of the board from free parking as top right in the board
Free_Parking = Button(root,text = '',command = lambda:parking(current_player),bg = 'thistle3',fg = 'black')
Free_Parking.place(x = 352,y=48,height=20,width=75)



Kentucky_Avenue = Button(root,text = '',command = lambda:buttons('KENTUCKY AVENUE'),bg = 'red2',fg = 'black')
Kentucky_Avenue.place(x=427,y=48,height=20,width=46)



Chance_2 = Button(root,text = '',command = lambda:chance(current_player),bg = 'salmon2',fg = 'black')
Chance_2.place(x=473,y=48,height=20,width=46)



Indiana_Avenue =  Button(root,text = '',command = lambda:buttons('INDIANA AVENUE'),bg = 'red2',fg = 'black')
Indiana_Avenue.place(x=519,y=48,height=20,width=46)



Illinois_Avenue = Button(root,text = '',command = lambda:buttons('ILLINOIS AVENUE'),bg = 'red2',fg = 'black')
Illinois_Avenue.place(x=565,y=48,height=20,width=46)



BO_Railroad = Button(root,text = '',command = lambda:buttons('B&O RAILROAD'),bg = 'grey10',fg = 'black')
BO_Railroad.place(x=611,y=48,height=20,width=46)



Atlantic_Avenue =  Button(root,text = '',command = lambda:buttons('ATLANTIC AVENUE'),bg = 'yellow2',fg = 'black')
Atlantic_Avenue.place(x=657,y=48,height=20,width=46)



Ventnor_Avenue = Button(root,text = '',command = lambda:buttons('VENTNOR AVENUE'),bg = 'yellow2',fg = 'black')
Ventnor_Avenue.place(x=703,y=48,height=20,width=46)



Water_Works = Button(root,text = '',command = lambda:buttons('WATER WORKS'),bg = 'sandy brown',fg = 'black')
Water_Works.place(x=749,y=48,height=20,width=46)



Marvin_Gardens = Button(root,text = '',command = lambda:buttons('MARVIN GARDENS'),bg = 'yellow2',fg = 'black')
Marvin_Gardens.place(x=795,y=48,height=20,width=46) 



Go_To_Jail = Button(root,text = '',bg = 'thistle3',fg = 'black')
Go_To_Jail.place(x=841,y=48,height=20,width=75)
#======================================================ROW-1====================================================================#
##############################################################################################################################################
#======================================================ROW-2====================================================================#

New_York_Avenue = Button(root,text = '',command = lambda:buttons('NEW YORK AVENUE'),bg = 'dark orange',fg = 'black')
New_York_Avenue.place(x=333,y=142,height=46,width=20)



Tennessee_Avenue = Button(root,text = '',command = lambda:buttons('TENNESSEE AVENUE'),bg = 'dark orange',fg = 'black')
Tennessee_Avenue.place(x=333,y=188,height=46,width=20)



Community_Chest_2 = Button(root,text = '',command = lambda:chest('COMMUNITY CHEST',current_player,10),bg = 'gold2',fg = 'black')
Community_Chest_2.place(x=333,y=234,height=46,width=20)



StJames_Place = Button(root,text = '',command = lambda:buttons('ST. JAMES PLACE'),bg = 'dark orange',fg = 'black')
StJames_Place.place(x=333,y=280,height=46,width=20)



Pennsylvania_Railroad = Button(root,text = '',command = lambda:buttons('PENNSYLVANIA RAILROAD'),bg = 'grey10',fg = 'black')
Pennsylvania_Railroad.place(x=333,y=326,height=46,width=20)



Virginia_Avenue = Button(root,text = '',command = lambda:buttons('VIRGINIA AVENUE'),bg = 'deep pink3',fg = 'black')
Virginia_Avenue.place(x=333,y=372,height=46,width=20)



States_Avenue = Button(root,text = '',command = lambda:buttons('STATES AVENUE'),bg = 'deep pink3',fg = 'black')
States_Avenue.place(x=333,y=418,height=46,width=20)



Electric_Company = Button(root,text = '',command = lambda:buttons('ELECTRIC COMPANY'),bg = 'sandy brown',fg = 'black')
Electric_Company.place(x=333,y=464,height=46,width=20)



StCharles_Place = Button(root,text = '',command = lambda:buttons('ST. CHARLES PLACE'),bg = 'deep pink3',fg = 'black')
StCharles_Place.place(x=333,y=510,height=46,width=20)
#====================================================ROW-2==================================================================#
##########################################################################################################################################
#====================================================ROW-3==================================================================#
Just_Visiting_Jail = Button(root,text = '',command = lambda:start(current_player),bg = 'thistle3',fg = 'black')
Just_Visiting_Jail.place(x=352,y=631,height=20,width=75)



Connecticut_Avenue = Button(root,text = '',command = lambda:buttons('CONNECTICUT AVENUE'),bg = 'light sky blue',fg = 'black')
Connecticut_Avenue.place(x=427,y=631,height=20,width=46)



Vermont_Avenue = Button(root,text = '',command = lambda:buttons('VERMONT AVENUE'),bg = 'light sky blue',fg = 'black')
Vermont_Avenue.place(x=473,y=631,height=20,width=46)



Chance_1 = Button(root,text = '',command = lambda:chance(current_player),bg = 'salmon2',fg = 'black')
Chance_1.place(x=519,y=631,height=20,width=46)



Oriental_Avenue = Button(root,text = '',command = lambda:buttons('ORIENTAL AVENUE'),bg = 'light sky blue',fg = 'black')
Oriental_Avenue.place(x=565,y=631,height=20,width=46)



Reading_Railroad = Button(root,text = '',command = lambda:buttons('READING RAILROAD'),bg = 'grey10',fg = 'black')
Reading_Railroad.place(x=611,y=631,height=20,width=46)



Income_Tax = Button(root,text = '',command = lambda:tax(current_player,200),bg = 'orange red',fg = 'black')
Income_Tax.place(x=657,y=631,height=20,width=46)



Baltic_Avenue = Button(root,text = '',command = lambda:buttons('BALTIC AVENUE'),bg = 'saddle brown',fg = 'black')
Baltic_Avenue.place(x=703,y=631,height=20,width=46)



Community_Chest_1 = Button(root,text = '',command = lambda:chest(current_player),bg = 'gold2',fg = 'black')
Community_Chest_1.place(x=749,y=631,height=20,width=46)



Mediterranean_Avenue = Button(root,text = '',command = lambda:buttons('MEDITERRANEAN AVENUE'),bg = 'saddle brown',fg = 'black')
Mediterranean_Avenue.place(x=795,y=631,height=20,width=46)



GO = Button(root,text = '',command = lambda:GO(current_player),bg = 'thistle3',fg = 'black')
GO.place(x=841,y=631,height=20,width=75)
#================================================ROW-3==================================================================#
######################################################################################################################################
#================================================ROW-4==================================================================#
#
Pacific_Avenue = Button(root,text = '',command = lambda:buttons('PACIFIC AVENUE'),bg = 'forest green',fg = 'black')
Pacific_Avenue.place(x=916,y=142,height=46,width=20)



North_Carolina_Avenue = Button(root,text = '',command = lambda:buttons('NORTH CAROLINA AVENUE'),bg = 'forest green',fg = 'black')
North_Carolina_Avenue.place(x=916,y=188,height=46,width=20)



Community_Chest_3 = Button(root,text = '',command = lambda:chest(current_player),bg = 'gold2',fg = 'black')
Community_Chest_3.place(x=916,y=234,height=46,width=20)



Pennsylvania_Avenue = Button(root,text = '',command = lambda:buttons('PENNSYLVANIA AVENUE'),bg = 'forest green',fg = 'black')
Pennsylvania_Avenue.place(x=916,y=280,height=46,width=20)



Short_Line = Button(root,text = '',command = lambda:buttons('SHORT LINE'),bg = 'grey10',fg = 'black')
Short_Line.place(x=916,y=326,height=46,width=20)



Chance_3 = Button(root,text = '',command = lambda:chance(current_player),bg = 'salmon2',fg = 'black')
Chance_3.place(x=916,y=372,height=46,width=20)

Park_Place = Button(root,text = '',command = lambda:buttons('PARK PLACE'),bg = 'dodgerblue3',fg = 'black')
Park_Place.place(x=916,y=418,height=46,width=20)

Luxury_Tax = Button(root,text = '',command = lambda:buttons(current_player,75),bg = 'orange red',fg = 'black')
Luxury_Tax.place(x=916,y=464,height=46,width=20)

Boardwalk = Button(root,text = '',command = lambda:buttons('BOARDWALK'),bg = 'dodgerblue3',fg = 'black')
Boardwalk.place(x=916,y=510,height=46,width=20)

mortgage_button = Button(root,text = 'MORTGAGE',command = lambda:mortgage(current_player,'not_a_place'),bg = 'black',fg = 'white')
mortgage_button.place(x=473,y=685,height=20,width=40)

house_button = Button(root,text = 'BUY A HOUSE',command = lambda:sets(current_player))
house_button.place(x=550,y=685,height=20,width=40)

quit = Button(root,text = 'QUIT',command = lambda:quit(list_of_players,property_state,railroad_state,company_state),bg = 'red',fg = 'black')
quit.place(x = 1230,y = 0)
#================================================ROW-3==================================================================#
######################################################################################################################################
#===============================================RUNNING=================================================================#
def quit(list_of_players,property_state,railroad_state,company_state):
    global save_game_window

    def confirm_save(player_info_query,property_info_query):
        save_game_window.destroy()
        for player in list_of_players:
            query = "insert into PLAYER_INFO_1 values('{}',{},{})".format(player[0],player[1],player[3])
            cur.execute(query)
            mydb.commit()
######
        for PLACE in places:
            query = "insert into PROPERTY_INFO_1(PLACES,STATE) values('{}','{}')".format(PLACE,property_state[places.index(PLACE)]) 
            cur.execute(query)
            mydb.commit()

        for player in list_of_players:
            for PLACE in player[2]:
                query = "update PROPERTY_INFO_1 set HOLDER = '{}' where PLACES = '{}'".format(player[0],PLACE)
                cur.execute(query)
                mydb.commit()
        #

        for PLACE in railroads:
            query = "insert into PROPERTY_INFO_1(PLACES,STATE) values('{}','{}')".format(PLACE,railroad_state[railroads.index(PLACE)])
            cur.execute(query)
            mydb.commit()

        for player in list_of_players:
            for PLACE in player[2]:
                query = "update PROPERTY_INFO_1 set HOLDER = '{}' where PLACES = '{}'".format(player[0],PLACE)
                cur.execute(query)
                mydb.commit()


        for PLACE in companies:
            query = "insert into PROPERTY_INFO_1(PLACES,STATE) values('{}','{}')".format(PLACE,company_state[companies.index(PLACE)])
            cur.execute(query)
            mydb.commit()

        for player in list_of_players:
            for PLACE in player[2]:
                query = "update PROPERTY_INFO_1 set HOLDER = '{}' where PLACES = '{}'".format(player[0],PLACE)
                cur.execute(query)
                mydb.commit()
   


    result = messagebox.askquestion('QUIT','DO YOU WISH TO SAVE THIS GAME?',type = 'yesno')
    if result == 'yes':
        root.destroy()
        save_game_window = Toplevel()
        save_game_window.configure(bg = '#36393e')
        
        cur.execute("select count(*) from information_schema.tables where table_name = '{}'".format('player_info_1'))
        player_table = cur.fetchone()
        cur.execute("select count(*) from information_schema.tables where table_name = '{}'".format('property_info_1'))
        property_table = cur.fetchone()
        if property_table[0] == 1 and player_table[0] == 1:
            cur.execute("drop table PLAYER_INFO_1")
            cur.execute("drop table PROPERTY_INFO_1")
            mydb.commit()

        player_info_query = "create table if not exists PLAYER_INFO_1(PLAYER char(70),MONEY float,POSITION int)"
        property_info_query = "create table if not exists PROPERTY_INFO_1(PLACES char(70),STATE char(70),HOLDER char(70))"

        cur.execute(player_info_query)
        cur.execute(property_info_query)

        confirm_save(player_info_query,property_info_query)
    else:
        root.destroy()
    def confirm_save(player_info_query,property_info_query):
        save_game_window.destroy()
        for player in list_of_players:
            query = "insert into PLAYER_INFO_1 values('{}',{},{})".format(player[0],player[1],player[3])
            cur.execute(query)
            mydb.commit()

#======================================================GAMESAVE====================================================================#

button_clicks = 0
def run_call():
    global button_clicks
    button_clicks += 1
    if button_clicks > len(p_name):
        button_clicks = 1

    running(button_clicks)
    display()

def jail(player):
    global prisoner
    global turn_count
    messagebox.showinfo(player[0]+"'s turn",'you have landed in jail!')
    result = messagebox.askquestion(player[0]+"'s turn","do you want to bail out?",type = 'yesno')
    if result == 'no':
        turn_count = 0
        prisoner.append(player)

        if current_player == p1:
            P1.place(x=coordinates[10][0],y=coordinates[10][1])
        elif current_player == p2:
            P2.place(x=coordinates[10][0],y=coordinates[10][1])
        elif current_player == p2:
            P3.place(x=coordinates[10][0],y=coordinates[10][1])
        elif current_player == p4:
            P4.place(x=coordinates[10][0],y=coordinates[10][1])

def movement(current_player,dice):
    if current_player == p1:
        for i in range(1,dice+1):
            time.sleep(0.4)
            if current_player[3]+i >=40:
                P1.place(x=coordinates[current_player[3]+i-40][0],y=coordinates[current_player[3]+i-40][1])
            else:
                P1.place(x=coordinates[current_player[3]+i][0],y=coordinates[current_player[3]+i][1])
            root.update()
        DICE.place(x=565,y=326)
        display()

    elif current_player == p2:
        for i in range(1,dice+1):
            time.sleep(0.4)
            if(current_player[3]+i>=40):
                P2.place(x=coordinates[current_player[3]+i-40][0],y=coordinates[current_player[3]+i-40][1])
            else:
                P2.place(x=coordinates[current_player[3]+i][0],y=coordinates[current_player[3]+i][1])
            root.update()
        DICE.place(x=565,y=326)
        display()

    elif current_player == p3:
        for i in range(1,dice+1):
            time.sleep(0.4)
            if(current_player[3]+i>=40):    
                P3.place(x=coordinates[current_player[3]+i-40][0],y=coordinates[current_player[3]+i-40][1])
            else:
                P3.place(x=coordinates[current_player[3]+i][0],y=coordinates[current_player[3]+i][1])
            root.update()
        DICE.place(x=565,y=326)
        display()

    elif current_player == p4:
        for i in range(1,dice+1):
            time.sleep(0.4)
            if(current_player[3]+i>=40):
                P4.place(x=coordinates[current_player[3]+i-40][0],y=coordinates[current_player[3]+i-40][1])
            else:
                P4.place(x=coordinates[current_player[3]+i][0],y=coordinates[current_player[3]+i][1])
            root.update()
        DICE.place(x=565,y=326)
        display()

def running(button_clicks):
    global turn_count
    global clicked
    global current_player
    global dice
    
    current_player = list_of_players[button_clicks-1] 
    #DICE
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    dice = die1 + die2
    dice = 1
    messagebox.showinfo(current_player[0]+"'s turn","You rolled a "+str(dice))
    DICE.place(x=5000,y=5000)
    print('prisoner....',prisoner)
    print('current player....',current_player)
    if current_player in prisoner:
        print('a')
        turn_count += 1
        if turn_count == 3:
            movement(current_player,dice)
            current_player[3] += dice
    else:        
        movement(current_player,dice)
        current_player[3] += dice

    #DICE
#
    #PASSING GO
    if current_player[3]>39:
        current_player[3] -=40
        messagebox.showinfo(current_player[0]+"'s turn","COLLECT 200$")
        current_player[1] += 200
    
    #PASSING GO
    
    if order[current_player[3]] == 'GO TO JAIL':
        jail(current_player)

    #PLACES
    if order[current_player[3]] in places:
        if property_state[places.index(order[current_player[3]])] == 'sale':
            place(order[current_player[3]],current_player)
            
        elif property_state[places.index(order[current_player[3]])] == 'bought' or property_state[places.index(order[current_player[3]])] == 'colour_set' or property_state[places.index(order[current_player[3]])] == 'mortgaged' or property_state[places.index(order[current_player[3]])] in ['1','2','3','4','hotel']:
            rent(order[current_player[3]],current_player,rent_prices_places[places.index(order[current_player[3]])])

    #RAILROADS
    elif order[current_player[3]] in railroads:
        if railroad_state[railroads.index(order[current_player[3]])] == 'sale':
            place(order[current_player[3]],current_player)
    
        elif railroad_state[railroads.index(order[current_player[3]])] == 'bought' or railroad_state[railroads.index(order[current_player[3]])] == 'mortgaged':
            rent(order[current_player[3]],current_player,rent_prices_railroads[railroads.index(order[current_player[3]])])
    #COMPANIES
    elif order[current_player[3]] in companies:
        if company_state[companies.index(order[current_player[3]])] == 'sale':
            place(order[current_player[3]],current_player)

        elif company_state[companies.index(order[current_player[3]])] == 'bought' or company_state[companies.index(order[current_player[3]])] == 'mortgaged':
            rent(order[current_player[3]],current_player,1)
#
    


    #TAX
    if current_player[3] == 4 :
        tax(current_player,200)
        
    elif current_player[3] == 38:
        tax(current_player,75)
    #TAX
#running()
#===============================================RUNNING=================================================================#
dice_image = ImageTk.PhotoImage(file = 'dice_image.png')
DICE = Button(root,image=dice_image,command = lambda:run_call(),bg = 'black')
DICE.place(x = 565,y = 326)
root.mainloop()
#


