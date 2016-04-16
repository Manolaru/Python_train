from model.user import User
import random
import string



def random_string (prefix, maxlen):
    symbols= string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
        User(fname=random_string("fname", 10), lname=random_string("lname", 10),
         address=random_string("home", 40),
         home=random_string("home", 10), mobile=random_string("mobile", 10),
         work=random_string("work", 10), email=random_string("email", 10),
         email2=random_string("email2", 10), email3=random_string("email3", 10))
    for i in range(4)
]