import re

def test_emails_on_home_page(app):
    contact_from_home_page = app.user.get_user_list()[0]
    contact_from_edit_page = app.user.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.email == clear(contact_from_edit_page.email)
    assert contact_from_home_page.email1 == clear(contact_from_edit_page.email1)
    assert contact_from_home_page.email2 == clear(contact_from_edit_page.email2)

def clear(s):
    return re.sub("[()-]","",s)

# def test_emails_on_contact_view_page(app):
#     contact_from_view_page = app.user.get_contact_from_view_page(0)
#     contact_from_edit_page = app.user.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.email == contact_from_edit_page.email
#     assert contact_from_view_page.email1 == contact_from_edit_page.email1
#     assert contact_from_view_page.email2 == contact_from_edit_page.email2