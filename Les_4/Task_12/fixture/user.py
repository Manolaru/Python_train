from model.user import User

class UserHelper:
    def __init__(self,app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        #check current page
        #txt = wd.current_url
        if not (wd.current_url.endswith ("/addressbook/")):
                self.app.open_home_page()

    def create(self, user):
        wd = self.app.wd
        self.open_home_page()
        # open user form
        wd.find_element_by_link_text("add new").click()
        # fill user form
        self.fill_user_form(user)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
          wd.find_element_by_name(field_name).click()
          wd.find_element_by_name(field_name).clear()
          wd.find_element_by_name(field_name).send_keys(text)

    def fill_user_form(self, user):
        wd = self.app.wd
        self.change_field_value("firstname", user.fname)
        self.change_field_value("lastname", user.lname)
        self.change_field_value("title", user.title)
        self.change_field_value("company", user.company)
        self.change_field_value("address", user.address)
        self.change_field_value("home", user.phoneh)
        self.change_field_value("email", user.email)
        self.change_field_value("byear",user.byear)


    def edit_first_user(self):
        wd = self.app.wd
        self.open_home_page()
        # select first user
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Gedda")
        wd.find_element_by_name("update").click()

    def delete_first_user(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_user()
        # submit deletion
        wd.find_element_by_xpath ("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def select_first_user(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()

    def modify_first_user(self, new_user_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_user()
        #open modification form
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        #fill modification form
        self.fill_user_form(new_user_data)
        #submit modification
        wd.find_element_by_name("update").click()


    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_user_list(self):
        wd = self.app.wd
        self.open_home_page()
        user=[]
        for element in wd.find_element_by_css_selector ("td.center"):
            text=element.text
            id= element.find_element_by_name("selected[]").get_attribute("value")
            user.append(User(lname=text, id=id))
        return user