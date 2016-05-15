# -*- coding: utf-8 -*-
import random
from random import randrange


def test_add_user_to_group_remove_user_from_group(app, db):
    user_list = db.get_user_list()
    test_user = random.choice(user_list)
    group_list = db.get_group_list_sort()
    list_pos = randrange(len(group_list))
    test_group = group_list[list_pos]
    old_binds = db.get_groups_by_user_id(test_user.id)
    app.binding.bind_user_and_group(test_user.id, list_pos + 1)
    new_binds = db.get_groups_by_user_id(test_user.id)
    assert int(test_group.id) in new_binds
    app.binding.remove_user_and_group_binding(test_user.id, list_pos + 1)
    end_binds = db.get_groups_by_user_id(test_user.id)
    assert int(test_group.id) not in end_binds

