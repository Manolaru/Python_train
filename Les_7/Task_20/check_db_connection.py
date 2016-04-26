
#from fixture.orm import ORMFixture
from fixture.db import DbFixture
from model.group import Group
from model.user import User


# db = ORMFixture (host="127.0.0.1", name= "addressbook", user="root", password="")
#
# try:
#    u=db.get_users_not_in_group(Group(id="44"))
#    for item in u:
#        print(item)
#    print(len(u))
#
# finally:
#     pass
#     #  db.destroy()

#Fourth  for users
# db = ORMFixture (host="127.0.0.1", name= "addressbook", user="root", password="")
#
# try:
#    u=db.get_users_in_group(Group(id="44"))
#    for item in u:
#        print(item)
#    print(len(u))
#
# finally:
#     pass
#     #  db.destroy()

#Fourth  for users
# db = ORMFixture (host="127.0.0.1", name= "addressbook", user="root", password="")
#
# try:
#    l=db.get_user_list()
#    for item in l:
#        print(item)
#    print(len(l))
#
# finally:
#    pass
   # db.destroy()

#Third ORM for groups
# db = ORMFixture (host="127.0.0.1", name= "addressbook", user="root", password="")
#
# try:
#    l=db.get_group_list()
#    for item in l:
#        print(item)
#    print(len(l))
#
# finally:
#    pass
#    # db.destroy()

#Second Db for users
db = DbFixture (host="127.0.0.1", name= "addressbook",
                                      user="root", password="")

try:
   users=db.get_user_list()
   for user in users:
       print(user)
   print(len(users))

finally:
    db.destroy()





#First
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
