from model.user import User
import re

class UserHelper:
    def __init__(self,app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        #check current page
        #txt = wd.current_url
        if not (wd.current_url.endswith ("/addressbook/")
                and len(wd.find_elements_by_css_selector('input[type="button"]')) > 0):
                self.app.open_home_page()

    def create(self, user):
        wd = self.app.wd
        self.open_home_page()
        # open user form
        wd.find_element_by_link_text("add new").click()
        # fill user form
        self.fill_user_form(user)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.user_cache = None


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
        self.change_field_value("home", user.home)
        self.change_field_value("address", user.address)
        self.change_field_value("mobile", user.mobile)
        self.change_field_value("work", user.work)
        self.change_field_value("email", user.email)
        self.change_field_value("email2", user.email2)
        self.change_field_value("email3", user.email3)



        # self.change_field_value("title", user.title)
        # self.change_field_value("company", user.company)
        # self.change_field_value("address", user.address)
        # self.change_field_value("home", user.homephone)
        # self.change_field_value("email", user.email)
        # self.change_field_value("byear",user.byear)


    def edit_first_user(self):
        wd = self.app.wd
        self.open_home_page()
        # select first user
        wd.find_element_by_css_selector('img[alt="Edit"]').click()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Gedda")
        wd.find_element_by_name("update").click()
        self.user_cache = None


    def delete_first_user(self):
        self.delete_user_by_index(0)

    def delete_user_by_index(self,index):
        wd = self.app.wd
        self.open_home_page()
        self.select_user_by_index(index)
        # submit deletion
        wd.find_element_by_xpath ("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.user_cache = None

    def  delete_user_by_id(self,id):
        wd = self.app.wd
        self.open_home_page()
        self.select_user_by_id(id)
        # submit deletion
        wd.find_element_by_xpath ("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.user_cache = None


    def select_first_user(self):
        wd = self.app.wd
        # select first user
        wd.find_element_by_name("selected[]").click()
        # wd.find_elements_by_name("selected[]")[0].click()

    def select_user_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_user_by_id(self,id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


    def modify_first_user(self, new_user_data):
        self.modify_user_by_index(0,new_user_data)


    def modify_user_by_index(self, index, new_user_data):
        wd = self.app.wd
        self.open_home_page()
        # self.select_user_by_index(index)
        #open modification form
        edit_buttons = wd.find_elements_by_css_selector('img[alt="Edit"]')
        edit_buttons[index].click()
        #fill modification form
        self.fill_user_form(new_user_data)
        #submit modification
        wd.find_element_by_name("update").click()
        self.user_cache = None

    def modify_user_by_id(self, new_user_data):
        wd = self.app.wd
        self.open_home_page()
        #open modification form
        search_ref = 'a[href="edit.php?id=' + new_user_data.id + '"]'
        wd.find_element_by_css_selector(search_ref).click()
        #fill modification form
        self.fill_user_form(new_user_data)
        #submit modification
        wd.find_element_by_name("update").click()
        self.user_cache = None


    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    user_cache = None


    def get_user_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.user_cache =[]
            itemrow = False
            for element in wd.find_elements_by_css_selector ("tr"):
            # for element in wd.find_elements_by_name("entry"):
                if itemrow:
                    items = element.find_elements_by_css_selector ("td")
                    id = items[0].find_element_by_name("selected[]").get_attribute("value")
                    l_name = items[1].text
                    f_name = items[2].text
                    address = items[3].text
                    all_phones = items[5].text
                    all_emails = items[4].text
                    self.user_cache.append(User(id = id, lname=l_name, fname=f_name, address=address,
                                                all_phones_from_home_page = all_phones,
                                                all_emails_from_home_page=all_emails))
                itemrow = True
        return list(self.user_cache)



##Was done for task 5



    def open_contact_to_edit_by_index(self, index):
         wd = self.app.wd
         self.app.open_home_page()
         row = wd.find_elements_by_name ("entry")[index]
         cell= row.find_elements_by_tag_name ("td")[7]
         cell.find_element_by_tag_name ("a").click()

    def open_contact_view_by_index(self, index):
         wd = self.app.wd
         self.app.open_home_page()
         row = wd.find_elements_by_name ("entry")[index]
         cell= row.find_elements_by_tag_name ("td")[6]
         cell.find_element_by_tag_name ("a").click()

    def get_contact_info_from_edit_page (self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        fname=wd.find_element_by_name("firstname").get_attribute("value")
        lname=wd.find_element_by_name("lastname").get_attribute("value")
        id=wd.find_element_by_name("id").get_attribute("value")
        address=wd.find_element_by_name("address").get_attribute("value")
        home=wd.find_element_by_name("home").get_attribute("value")
        mobile=wd.find_element_by_name("mobile").get_attribute("value")
        work=wd.find_element_by_name("work").get_attribute("value")
        email=wd.find_element_by_name("email").get_attribute("value")
        email2=wd.find_element_by_name("email2").get_attribute("value")
        email3=wd.find_element_by_name("email3").get_attribute("value")

        return User(fname=fname,lname=lname,id=id,
                    address=address,home=home, mobile=mobile, work=work,
                    email=email, email2=email2, email3=email3)

    def get_contact_from_view_page (self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text=wd.find_element_by_id("content").text
        home=re.search("H: (.*)",text).group(1)
        mobile=re.search("M: (.*)",text).group(1)
        work=re.search("W: (.*)",text).group(1)

        return User(home=home,mobile=mobile, work=work)



