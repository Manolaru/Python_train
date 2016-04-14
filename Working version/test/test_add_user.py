# -*- coding: utf-8 -*-
from model.user import User
import pytest
import random
import string
from sys import maxsize


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
#
@pytest.mark.parametrize("user", testdata, ids=[repr(x) for x in testdata])
def test_add_user(app, user):
      #  pass
    old_users=app.user.get_user_list()
   # user=User(fname="Jana", lname="Geddis", home="554", mobile="298-06-22", work="(86162)52911")
    app.user.create(user)
    assert len(old_users) + 1 == app.user.count()
    new_users=app.user.get_user_list()
    old_users.append(user)
    assert sorted(old_users,key=User.id_or_max) == sorted(new_users,key=User.id_or_max)






