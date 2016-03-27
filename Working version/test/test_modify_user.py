from model.user import User

def test_modify_user_fname(app):
    app.session.login(username="admin",password="secret")
    if app.user.count() == 0:
        app.user.create(User(lname="Testman"))
    app.user.modify_first_user(User(fname="New firstname"))
    app.session.logout()

#def test_modify_user_lastname(app):
#    app.session.login(username="admin",password="secret")
#    if app.user.count() == 0:
#        app.user.create(User(lname="Testman"))
#    app.user.modify_first_user(User (lname="New lastname"))
#    app.session.logout()

#def test_modify_user_address(app):
#    app.session.login(username="admin",password="secret")
#    if app.user.count() == 0:
#        app.user.create(User(lname="Testman"))
#    app.user.modify_first_user(User (address="New address"))
#    app.session.logout()