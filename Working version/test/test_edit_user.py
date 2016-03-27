import pytest
from fixture.application import Application
from model.user import User


def test_edit_user(app):
    app.session.login(username="admin",password="secret")
    if app.user.count() == 0:
        app.user.create(User(lname="Testman"))
    app.user.edit_first_user()
    app.session.logout()
