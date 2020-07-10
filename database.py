
#import sqlite3
#conn = sqlite3.connect('example.db')
#c = conn.cursor()

#c = conn.cursor()

# Create table
#c.execute('''CREATE TABLE stocks
 #            (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
#c.execute("INSERT INTO stocks VALUES ('2020-07-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
#conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.


#c.execute('INSERT INTO stocks VALUES (2020-07-05,BUY,RHAT2,200,75.2)', purchases)
#conn.close()
 
  
 
   
#import sqlite3

#conn = sqlite3.connect('friendly test.db')

#print ("Opened database successfully");

#conn.execute('''INSERT INTO product details (Qr code,Name,weight,QTY,price) \
#     VALUES (101, 'sope', 50g, 1, 45 )''');

#conn.execute('''INSERT INTO COMPANY (Qr code,Name,weight,QTY,price) \
#     VALUES (102, 'rice', 25kg, 1, 800 )''');

#conn.execute('''INSERT INTO COMPANY (Qr code,Name,weight,QTY,price) \
#     VALUES (103, 'whet', 10kg, 1, 600 )''');

#conn.execute('''INSERT INTO COMPANY (Qr code,Name,weight,QTY,price) \
#     VALUES (104, 'ground nuts', 2kg, 1, 240 )''');

#conn.commit()
#print ("Records created successfully");
#conn.close()

'''

import random
min = 1
max = 6

roll_again = "yes"
for i in range [1,6]
# if < [4 5 6]
while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    #print (random.randint(min, max))
    print (random.randint(min, max))

    roll_again = input("Roll the dices again?")
 '''
 
import random
min = 1
max = 6

for i in range(1 , 5, 6):
    print("Current value of i is:", i)
    print ("Rolling the dices...")
    print ("The values are....")
    #print (random.randint(min, max))
    print (random.randint(min, max))

roll_again = input("Roll the dices again?")