from model.user import User
import random

def test_modify_user_lname(app, db, check_ui):
    if app.user.count() == 0:
        app.user.create(User(lname="Testman"))
    #app.user.modify_first_user(User(lname="New lastname"))
    old_users=db.get_user_list()
    user = random.choice(old_users)
    list_index = old_users.index(user)
    user.lname = "New Lastname"
    app.user.modify_user_by_id(user)
    new_users=db.get_user_list()
    assert len(old_users)  == len(new_users)
    old_users[list_index]=user
    assert old_users == new_users
    if check_ui:
        new = sorted(new_users, key=User.id_or_max)
        ui= sorted(app.user.get_user_list(), key=User.id_or_max)
        assert new == ui


def test_modify_user_fname(app, db, check_ui):
    if app.user.count() == 0:
        app.user.create(User(fname="Testman"))
    #app.user.modify_first_user(User(lname="New lastname"))
    old_users=db.get_user_list()
    user = random.choice(old_users)
    list_index = old_users.index(user)
    user.fname = "New Firstname"
    app.user.modify_user_by_id(user)
    new_users=db.get_user_list()
    assert len(old_users)  == len(new_users)
    old_users[list_index]=user
    assert old_users == new_users
    if check_ui:
        new = sorted(new_users, key=User.id_or_max)
        ui= sorted(app.user.get_user_list(), key=User.id_or_max)
        assert new == ui

def test_modify_user_address(app, db, check_ui):
    if app.user.count() == 0:
        app.user.create(User(address="TestAddress"))
    #app.user.modify_first_user(User(lname="New lastname"))
    old_users=db.get_user_list()
    user = random.choice(old_users)
    list_index = old_users.index(user)
    user.address = "New Address"
    app.user.modify_user_by_id(user)
    new_users=db.get_user_list()
    assert len(old_users)  == len(new_users)
    old_users[list_index]=user
    assert old_users == new_users
    if check_ui:
        new = sorted(new_users, key=User.id_or_max)
        ui= sorted(app.user.get_user_list(), key=User.id_or_max)
        assert new == ui


# def test_modify_user_firstname(app):
#     if app.user.count() == 0:
#         app.user.create(User(lname="Testman"))
#     app.user.modify_first_user(User (fname ="New firstname"))
#
#
# def test_modify_user_address(app):
#     if app.user.count() == 0:
#         app.user.create(User(lname="Testman"))
#     app.user.modify_first_user(User (address="New address"))
