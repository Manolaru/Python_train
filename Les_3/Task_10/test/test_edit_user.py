from model.user import User


def test_edit_user(app):
    if app.user.count() == 0:
        app.user.create(User(lname="Testman"))
    app.user.edit_first_user()

