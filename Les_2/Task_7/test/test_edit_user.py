

def test_edit_user(app):
    app.session.login(username="admin",password="secret")
    app.user.edit_first_user()
    app.session.logout()
