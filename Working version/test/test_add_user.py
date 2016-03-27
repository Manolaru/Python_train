# -*- coding: utf-8 -*-
from model.user import User


def test_add_user(app):
    app.session.login(username="admin",password="secret")
    app.user.create(User(fname="Jana", lname="Geddis", title="Manager", company="KPMG", address="Moscow, Smolenskaya emb.", phoneh="9876612",
                         email="jana.geddis@kpmg.com", byear= "1988"))
    app.session.logout()

