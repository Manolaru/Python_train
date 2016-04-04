from sys import maxsize


class User:
    def __init__(self, fname=None, lname=None, title=None, company=None, address=None, phoneh=None, email=None, byear=None, id=None):
        self.fname = fname
        self.lname = lname
        self.title = title
        self.company = company
        self.address = address
        self. phoneh = phoneh
        self.email = email
        self.byear = byear
        self.id = id


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lname, self.fname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.lname == other.lname and self.fname == other.fname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


