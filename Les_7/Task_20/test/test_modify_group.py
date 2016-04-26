from model.group import Group
import random

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="testing"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    list_index = old_groups.index(group)
    group.name = "NewGroup"
    app.group.modify_group_by_id(group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len (new_groups)
    old_groups[list_index]=group
    assert old_groups == new_groups
    if check_ui:
        new = sorted(new_groups, key=Group.id_or_max)
        ui= sorted(app.group.get_group_list(), key=Group.id_or_max)
        assert new == ui

def test_modify_group_header(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="testing"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    list_index = old_groups.index(group)
    group.header = "NewHeader"
    app.group.modify_group_by_id(group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len (new_groups)
    old_groups[list_index]=group
    assert old_groups == new_groups
    if check_ui:
        new = sorted(new_groups, key=Group.id_or_max)
        ui= sorted(app.group.get_group_list(), key=Group.id_or_max)
        assert new == ui

def test_modify_group_footer(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="testing"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    list_index = old_groups.index(group)
    group.footer = "NewFooter"
    app.group.modify_group_by_id(group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len (new_groups)
    old_groups[list_index]=group
    assert old_groups == new_groups
    if check_ui:
        new = sorted(new_groups, key=Group.id_or_max)
        ui= sorted(app.group.get_group_list(), key=Group.id_or_max)
        assert new == ui

