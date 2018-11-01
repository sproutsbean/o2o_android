from com.ea.pages.menu_page import MenuPage
from com.ea.pages.my_customer_page import MyCustomerPage


def add_customer(driver, first_name, second_name, first_english_name, last_english_name, card_no, phone_no):
    menupage = MenuPage(driver)
    mycustomerpage = MyCustomerPage(driver)
    menupage.click_me_page()
    mycustomerpage.click_my_customer()
    mycustomerpage.click_add_button()
    mycustomerpage.click_next_button()
    mycustomerpage.send_first_name(first_name)
    mycustomerpage.send_second_name(second_name)
    mycustomerpage.send_first_english_name(first_english_name)
    mycustomerpage.send_second_english_name(last_english_name)
    mycustomerpage.input_cardno(card_no)
    mycustomerpage.click_card_expire_date()
    mycustomerpage.input_card_organization()
    mycustomerpage.send_phoneno(phone_no)
    mycustomerpage.click_save_button()
