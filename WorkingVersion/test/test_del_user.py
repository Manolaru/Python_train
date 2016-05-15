from model.user import User
import random



def test_delete_some_user(app,db,check_ui):
    if app.user.count() == 0:
        app.user.create(User(lname="Testman"))
    old_users = db.get_user_list()
    user = random.choice(old_users)
    app.user.delete_user_by_id(user.id)
    new_users = db.get_user_list()
    assert len(old_users) - 1 == len (new_users)
    old_users.remove(user)
    assert old_users == new_users
    if check_ui:
        new = sorted(new_users, key=User.id_or_max)
        ui= sorted(app.user.get_user_list(), key=User.id_or_max)
        assert new == ui
