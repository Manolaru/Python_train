
import mysql.connector
from model.group import Group
from model.user import User

class DbFixture:

   def __init__(self, host, name, user, password):
       self.host = host
       self.name = name
       self.user = user
       self.password = password
       self.connection = mysql.connector.connect (host=host, database=name, user=user, password=password)
       self.connection.autocommit = True


   def get_group_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer)= row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list


   def get_group_list_sort(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list order by group_name")
            for row in cursor:
                (id, name, header, footer)= row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list


   def get_user_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email,email2,email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname,address, home, mobile, work, email,email2,email3) = row
                all_phones= home+mobile+work
                all_emails= email+email2+email3
                list.append(User(id=str(id), fname=firstname, lname=lastname, address=address, all_phones_from_home_page=all_phones,
                                 all_emails_from_home_page=all_emails))
        finally:
            cursor.close()
        return list

   def destroy(self):
        self.connection.close()


   def get_groups_by_user_id(self, user_id):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id from address_in_groups where id = "+user_id)
            for row in cursor:
                list.append(row[0])
        finally:
            cursor.close()
        return list
