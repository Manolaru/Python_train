# -*- coding: utf-8 -*-
from model.user import User
from sys import maxsize

def test_add_user(app):
    old_users=app.user.get_user_list()
    user=User(fname="Jana", lname="Geddis", title="Manager", company="KPMG", address="Moscow, Smolenskaya emb.", phoneh="9876612",
                         email="jana.geddis@kpmg.com", byear= "1988")
    app.user.create(user)
    new_users=app.user.get_user_list()
    assert len(old_users) + 1 == len (new_users)
    old_users.append(user)
    def id_or_max(us):
        if us.id:
            return (us.id)
        else:
            return maxsize
    assert sorted(old_users,key=User.id_or_max) == sorted(new_users,key=User.id_or_max)







