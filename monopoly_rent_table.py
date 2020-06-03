import mysql.connector as myco
mydb=myco.connect(host='localhost',user='root',passwd='root')
cur=mydb.cursor()

#creating database

cur.execute('create database monopoly')
cur.execute('use monopoly')

#table for properties

cur.execute('create table Properties (Place char(70), HouseCost int, HotelCost int, Nohouse int, OneHouse int, TwoHouses int, ThreeHouses int, FourHouses int, Hotel int,Mortgage int)')
cur.execute('insert into Properties values("MEDITERRANEAN AVENUE",50,50,2,10,30,90,160,250,30)')
cur.execute('insert into Properties values("BALTIC AVENUE",50,50,4,20,60,180,320,450,30)')
cur.execute('insert into Properties values("ORIENTAL AVENUE",50,50,6,30,90,270,400,550,50)')
cur.execute('insert into Properties values("VERMONT AVENUE",50,50,6,30,90,270,400,550,50)')
cur.execute('insert into Properties values("CONNECTICUT AVENUE",50,50,8,40,100,300,450,600,60)')
cur.execute('insert into Properties values("ST. CHARLES PLACE",100,100,10,50,150,450,625,750,70)')
cur.execute('insert into Properties values("STATES AVENUE",100,100,10,50,150,450,625,750,70)')
cur.execute('insert into Properties values("VIRGINIA AVENUE",100,100,12,60,180,500,700,900,80)')
cur.execute('insert into Properties values("ST. JAMES PLACE",100,100,14,70,200,550,750,950,90)')
cur.execute('insert into Properties values("TENNESSEE AVENUE",100,100,14,70,200,550,750,950,90)')
cur.execute('insert into Properties values("NEW YORK AVENUE",100,100,16,80,220,600,800,1000,100)')
cur.execute('insert into Properties values("KENTUCKY AVENUE",150,150,18,90,250,700,875,1050,110)')
cur.execute('insert into Properties values("INDIANA AVENUE",150,150,18,90,250,700,875,1050,110)')
cur.execute('insert into Properties values("ILLINOIS AVENUE",150,150,20,100,300,750,925,1100,120)')
cur.execute('insert into Properties values("ATLANTIC AVENUE",150,150,22,110,330,800,975,1150,130)')
cur.execute('insert into Properties values("VENTNOR AVENUE",150,150,22,110,330,800,975,1150,130)')
cur.execute('insert into Properties values("MARVIN GARDENS",150,150,24,120,360,850,1025,1200,140)')
cur.execute('insert into Properties values("PACIFIC AVENUE",200,200,26,130,390,900,1100,1275,150)')
cur.execute('insert into Properties values("NORTH CAROLINA AVENUE",200,200,26,130,390,900,1100,1275,150)')
cur.execute('insert into Properties values("PENNSYLVANIA AVENUE",200,200,28,150,450,1000,1200,1400,160)')
cur.execute('insert into Properties values("PARK PLACE",200,200,35,175,500,1100,1300,1500,175)')
cur.execute('insert into Properties values("BOARDWALK",200,200,50,200,600,1400,1700,2000,200)')
mydb.commit()


#table for railroads

cur.execute('create table Railroads (Railroad char(40), OneRailRoad int, TwoRailRoads int, ThreeRailRoads int, FourRailRoads int, Mortgage int)')
cur.execute('insert into Railroads values("READING RAIROAD",25,50,100,200,100)')
cur.execute('insert into Railroads values("PENNSYLVANIA RAILROAD",25,50,100,200,100)')
cur.execute('insert into Railroads values("B&O RAILROAD",25,50,100,200,100)')
cur.execute('insert into Railroads values("SHORT LINE",25,50,100,200,100)')
mydb.commit()


mydb.close()
