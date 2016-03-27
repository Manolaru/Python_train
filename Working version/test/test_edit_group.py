import pytest
from fixture.application import Application
from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin",password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="testing"))
    app.group.edit_first_group()
    app.session.logout()
