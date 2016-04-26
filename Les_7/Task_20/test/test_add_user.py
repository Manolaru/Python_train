# -*- coding: utf-8 -*-
from model.user import User


def test_add_user(app, db, json_users, check_ui ):
    user = json_users
    old_users=db.get_user_list()
    app.user.create(user)
    assert len(old_users) + 1 == app.user.count()
    new_users=db.get_user_list()
    old_users.append(user)
    assert sorted(old_users,key=User.id_or_max) == sorted(new_users,key=User.id_or_max)
    if check_ui:
        new = sorted(new_users, key=User.id_or_max)
        ui= sorted(app.user.get_user_list(), key=User.id_or_max)
        assert new == ui


