# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture()
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin",password="secret")
    app.create_group(Group(name="students_group",header="Logo",footer="comment"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin",password="secret")
    app.create_group(Group(name="empty", header="",footer=""))
    app.logout()

