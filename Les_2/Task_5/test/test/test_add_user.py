# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.user import User


@pytest.fixture()
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.login(username="admin",password="secret")
    app.create_user(User(fname="Jana", lname= "Geddis", title= "Manager", company= "KPMG", address= "Moscow, Smolenskaya emb.",phoneh= "9876612",
                         email="jana.geddis@kpmg.com", byear= "1988"))
    app.logout()

