import pytest
from fixture.application import Application
from model.group import Group

def test_modify_group_name(app):
    app.session.login(username="admin",password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="testing"))
    app.group.modify_first_group(Group(name="NewGroup"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login(username="admin",password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="testing"))
    app.group.modify_first_group(Group(header="New header"))
    app.session.logout()

def test_modify_group_footer(app):
    app.session.login(username="admin",password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="testing"))
    app.group.modify_first_group(Group(footer="New footer"))
    app.session.logout()