# -*- coding: utf-8 -*-


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin",password="secret")
    app.group.create(Group(name="students_group", header="Logo", footer="comment"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin",password="secret")
    app.group.create(Group(name="empty", header="", footer=""))
    app.session.logout()
