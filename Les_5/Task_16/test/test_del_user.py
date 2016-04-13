from model.user import User
from random import randrange
import time


def test_delete_some_user(app):
    if app.user.count() == 0:
        app.user.create(User(lname="Testman"))
    old_users = app.user.get_user_list()
    index = randrange(len(old_users))
    app.user.delete_user_by_index(index)
    new_users = app.user.get_user_list()
    assert len(old_users) - 1 == len (new_users)
    old_users[index:index + 1] = []
    assert old_users == new_users

