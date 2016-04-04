from model.user import User


def test_modify_user_lname(app):
    if app.user.count() == 0:
        app.user.create(User(lname="Testman"))
    app.user.modify_first_user(User(lname="New lastname"))
    old_users=app.user.get_user_list()
    user=User (lname= "New Lastname", fname="" )
    user.id = old_users[0].id
    app.user.modify_first_user(user)
    new_users=app.user.get_user_list()
    assert len(old_users)  == len (new_users)
    old_users [0]=user
    assert sorted(old_users,key=User.id_or_max) == sorted(new_users,key=User.id_or_max)


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
