from sys import maxsize


class User:
    def __init__(self, fname=None, lname=None, id=None, home=None,
                 mobile=None, work=None, email=None, email2=None, email3=None):

        self.fname = fname
        self.lname = lname
        self.id = id
        self.home = home
        self.mobile = mobile
        self.work = work
        self.email = email
        self.email2 = email2
        self.email3= email3


    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.id, self.lname, self.fname, self.home, self.email)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.lname == other.lname and self.fname == other.fname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


