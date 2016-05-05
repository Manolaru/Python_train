
from model.user import User



def test_user_list(app, db):
    ui_list_u = sorted (app.user.get_user_list(), key=User.id_or_max)
    db_list_u = sorted (db.get_user_list(), key=User.id_or_max)
    assert ui_list_u == db_list_u

