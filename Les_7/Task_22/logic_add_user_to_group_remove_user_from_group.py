

        # bind user and group  user id 11  group number 2 in list
        # select check box for user
        if not wd.find_element_by_id("11").is_selected():
            wd.find_element_by_id("11").click()
        # select group from bind drop down list
        if not wd.find_element_by_xpath("//div[@class='right']/select//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@class='right']/select//option[2]").click()
        click add button
        wd.find_element_by_name("add").click()
        # return home page
        wd.find_element_by_link_text("home").click()
        # check user group binding in database
        # remove user and group binding
        # select group from view drop down list, notice: item number + 2 (first is [all] and [none])
        # if not wd.find_element_by_xpath("//form[@id='right']/select//option[4]").is_selected():
            wd.find_element_by_xpath("//form[@id='right']/select//option[4]").click()
        # select check box for the bound user
        if not wd.find_element_by_id("11").is_selected():
           wd.find_element_by_id("11").click()
        click remove button
        wd.find_element_by_name("remove").click()
        # return home page
        wd.find_element_by_link_text("home").click()
        # remove group selection from the list
        if not wd.find_element_by_xpath("//form[@id='right']/select//option[2]").is_selected():
           wd.find_element_by_xpath("//form[@id='right']/select//option[2]").click()
        self.assertTrue(success)

