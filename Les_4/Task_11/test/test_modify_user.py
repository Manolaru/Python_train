from model.user import User

def test_modify_user_fname(app):
    if app.user.count() == 0:
        app.user.create(User(lname="Testman"))
    app.user.modify_first_user(User(fname="New firstname"))


def test_modify_user_lastname(app):
    if app.user.count() == 0:
        app.user.create(User(lname="Testman"))
    app.user.modify_first_user(User (lname ="New lastname"))


def test_modify_user_address(app):
    if app.user.count() == 0:
        app.user.create(User(lname="Testman"))
    app.user.modify_first_user(User (address="New address"))
