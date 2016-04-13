# -*- coding: utf-8 -*-
from model.user import User
from sys import maxsize

def test_add_user(app):
    old_users=app.user.get_user_list()
    user=User(fname="Jana", lname="Geddis", home="554", mobile="2980622", work="8616252911")
    app.user.create(user)
    assert len(old_users) + 1 == app.user.count()
    new_users=app.user.get_user_list()
    old_users.append(user)
    assert sorted(old_users,key=User.id_or_max) == sorted(new_users,key=User.id_or_max)






