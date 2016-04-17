import re
import random

def test_random_user_data(app):

    contact_list_from_home_page = app.user.get_user_list()
    index = random.randint(1, len(contact_list_from_home_page))-1

    contact_from_home_page = contact_list_from_home_page[index]
    contact_from_edit_page = app.user.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert clear_space (contact_from_home_page.all_emails_from_home_page) == merge_emails_like_on_home_page(contact_from_edit_page)
    assert clear_space (contact_from_home_page.address) == clear_space (contact_from_edit_page.address)


def clear(s):
    return re.sub("[() -]","",s)

def clear_space(s):
    return re.sub("[ ]","",s)


def merge_phones_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [user.home, user.mobile, user.work]))))

def merge_emails_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [user.email, user.email2, user.email3]))))
# def test_phones_on_contact_view_page(app):
#     contact_from_view_page = app.user.get_contact_from_view_page(0)
#     contact_from_edit_page = app.user.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.home == contact_from_edit_page.home
#     assert contact_from_view_page.work == contact_from_edit_page.work
#     assert contact_from_view_page.mobile == contact_from_edit_page.mobile
