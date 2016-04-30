
from fixture.db import DbFixture


#Second Db for users --working
db = DbFixture (host="127.0.0.1", name= "addressbook", user="root", password="")

try:
   users=db.get_user_list()
   for user in users:
       print(user)
   print(len(users))

finally:
    db.destroy()


#First -working
# import mysql.connector
#
# connection = mysql.connector.connect (host="127.0.0.1", database= "addressbook",
#                                       user="root", password="")
#
# try:
#     cursor = connection.cursor()
#     cursor.execute("select * from group_list")
#     for row in cursor.fetchall():
#         print(row)
#
# finally:
#     connection.close()
