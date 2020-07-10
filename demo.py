import sqlite3

dbase = sqlite3.connect('demo.db')

#dbase.execute('''CREATE TABLE super_market(
#        SNO INT PRIMARY KEY NOT NULL,
#        NAME TEXT NOT NULL,
#        WEIGHT INT NOT NULL,
#        PRICE INT NOT NULL)''');
 

#dbase.execute('''INSERT INTO super_market(SNO,NAME,WEIGHT,PRICE)
#        VALUES(04,'sope',4,150)
#        ''');


#def insert_record(SNO,NAME,WEIGHT,PRICE):
#    dbase.execute('''insert into super_market(SNO,NAME,WEIGHT,PRICE)
#            VALUES(?,?,?,?)''',(SNO,NAME,WEIGHT,PRICE))
#    dbase.commit()
#    print("REcord inserted")
#insert_record(6,'wheat',"5kgs",500)

#def update_record():
#    dbase.execute('''UPDATE super_market set NAME='SANTHOOR' WHERE SNO =4''')
#    dbase.commit()
#    print('updated')
#update_record() 

def delete_record():
    dbase.execute('''DELETE from super_market WHERE SNO = 1''')
    dbase.commit()
    print('deleted')
delete_record()

dbase.commit()
print('REcord inserted')
print('table created')
dbase.close()
