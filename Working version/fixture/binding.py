from model.group import Group
from model.user import User


class BindingHelper:
   def __init__(self,app):
        self.app = app

   def select_group_from_binding_drop_down(self, item_nmb):
       wd = self.app.wd
       wd.find_element_by_xpath("//div[@class='right']/select//option[" + str(item_nmb) + "]").click()

   def select_group_from_view_drop_down(self, item_nmb):
       wd = self.app.wd
       wd.find_element_by_xpath("//form[@id='right']/select//option[" + str(item_nmb) + "]").click()

   def bind_user_and_group(self, user_id, group_item_number):
        wd = self.app.wd
        self.app.user.open_home_page()
        self.app.user.select_user_by_id(user_id)
        self.select_group_from_binding_drop_down(group_item_number)
        wd.find_element_by_name("add").click()
        self.app.user.open_home_page()

   def remove_user_and_group_binding(self, user_id, group_item_number):
        wd = self.app.wd
        self.app.user.open_home_page()
        self.select_group_from_view_drop_down(1)
        self.select_group_from_view_drop_down(group_item_number+2)
        self.app.user.select_user_by_id(user_id)
        wd.find_element_by_name("remove").click()
        self.app.user.open_home_page()
        self.select_group_from_view_drop_down(1)
