from sys import maxsize
import re


class User:
    def __init__(self, fname=None, lname=None, id=None, address=None,
                 home=None, mobile=None, work=None,
                 all_phones_from_home_page=None,
                 email=None, email2=None, email3=None, all_emails_from_home_page =None):

        self.fname = fname
        self.lname = lname
        self.id = id
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email = email
        self.email2 = email2
        self.email3= email3
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lname, self.fname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.clear(self.lname) == self.clear(other.lname) \
               and self.clear(self.fname) == self.clear(other.fname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def clear(self, s):
        return re.sub("[ ]","",s)
