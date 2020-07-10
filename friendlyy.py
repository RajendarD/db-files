import sqlite3

dbase = sqlite3.connect('new_frindly.db') 

#print ('Database opend')

#dbase.execute(''' CREATE TABLE  super_marker(
#        ID  INT PRIMARY KEY NOT NULL,
#        NAME TEXT NOT NULL,
#        PRODUCT INT NOT NULL,
#        PRICE INT NOT NULL)''');
#Print ('Tables created')
#print  ('batabase closed')
#dbase.execute(''' INSERT INTO super_marker(ID,NAME,PRODUCT,PRICE)
#        VALUES(2,'rice',"25kgs",1150)
#        ''');
#def insert_record(ID,NAME,PRODUCT,PRICE):
#    dbase.execute('''insert into super_marker(ID,NAME,PRODUCT,PRICE)
#            VALUES(?,?,?,?)''',(ID,NAME,PRODUCT,PRICE))
#    dbase.commit()
#    print("REcord inserted")
#insert_record(6,'wheat',"5kgs",500)    
#dbase.commit()
#print ('REcord inserted')
##def read_data():
##    data = dbase.execute('''SElECT * FROM super_marker ORDER BY NAME''')
##   for recoord in data:
##        print ('ID : '+ str(record[0])+'\n')
##        print ('NAME : '+ str(record[1])+'\n')
##       print ('PRODUCT :'+ str(record[2])+'\n')
##        print ('PRICE : '+ str(record[3])+'\n\n')
read_data()

#def update_record():
#    dbase.execute('''UPDATE super_marker set PRODUCT=25 WHERE ID =2''')
#    dbase.commit()
#    print('updated')
#update_record()    

#def delete_record():
#    dbase.execute('''DELETE from super_marker WHERE ID = 2''')
#    dbase.commit()
#    print('deleted')
#delete_record()
#dbase.close ()
#print ('batabase closed')
#cursor = dbase.execute( )
#def check_data():
#    data = cursor.execute('''SElECT NAME FROM super_marker WHERE ID = 1''')
#    X = data.fetchall()
#    print(x)

a=2
def add():
b=3
c=a+b
print(c)
#add()