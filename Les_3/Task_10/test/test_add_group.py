# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="students_group", header="Logo", footer="comment"))



def test_add_empty_group(app):
    app.group.create(Group(name="empty", header="", footer=""))


