from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:

     def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

     def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

     def destroy(self):
        self.wd.quit()



 #def return_to_groups_page(self):
 #       wd = self.app.wd
 #       wd.find_element_by_link_text("group page").click()


 # def create_user(self, user):
 #     wd = self.wd
  #    self.open_home_page()
   #     # open user form
    #    wd.find_element_by_link_text("add new").click()
  #      # fill user form
   #     wd.find_element_by_name("firstname").click()
    #    wd.find_element_by_name("firstname").clear()
     #   wd.find_element_by_name("firstname").send_keys(user.fname)
 #       wd.find_element_by_name("lastname").click()
 #       wd.find_element_by_name("lastname").clear()
 #       wd.find_element_by_name("lastname").send_keys(user.lname)
 #       wd.find_element_by_name("title").click()
 #       wd.find_element_by_name("title").clear()
 #       wd.find_element_by_name("title").send_keys(user.title)
 #       wd.find_element_by_name("company").click()
     #   wd.find_element_by_name("company").clear()
      #  wd.find_element_by_name("company").send_keys()
      #  wd.find_element_by_name("company").click()
      #  wd.find_element_by_name("company").clear()
      #  wd.find_element_by_name("company").send_keys(user.company)
      #  wd.find_element_by_name("address").click()
      #  wd.find_element_by_name("address").clear()
      #  wd.find_element_by_name("address").send_keys(user.address)
      #  wd.find_element_by_name("home").click()
      #  wd.find_element_by_name("home").clear()
      #  wd.find_element_by_name("home").send_keys(user.phoneh)
      #  wd.find_element_by_name("email").click()
      #  wd.find_element_by_name("email").clear()
      #  wd.find_element_by_name("email").send_keys(user.email)
      #  if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
      #      wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
      #  if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[7]").is_selected():
      #      wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[7]").click()
      #  wd.find_element_by_name("byear").click()
      #  wd.find_element_by_name("byear").clear()
      #  wd.find_element_by_name("byear").send_keys(user.byear)
      #  if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[3]").is_selected():
      #      wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[3]").click()
      #  # submit user creation
      #  wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


