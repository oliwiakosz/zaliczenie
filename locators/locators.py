class Locators:


    #Home page objects
    accept_message_xpath="//a[@href='#acceptAll']"
    login_icon_xpath="//a[@class ='account_link']"
    basket_icon_xpath="//div[@id='menu_basket_wrapper']"
    navbar_xpath= "//div[@id='menu_navbar']//a[@title]/.."
    nowosci_xpath = "//div[@id='menu_navbar']//a[@title='Nowości']/.."


    #Login page objects
    username_textbox_xpath = "//input[@id='user_login']"
    password_textbox_xpath = "//input[@id='user_pass']"
    login_button_xpath = "//button[contains(text(),'Zaloguj')]"
    popup_id="ck_dsclr_v2"
    popup_close_button_xpath = "//div[@id='ckdsclmrshtdwn_v2']/span"
    warning_message_xpath="//div[@id='return_error']//h3"
    uwaga_xpath="//li/span[text()='Uwaga']"

    #Nowości page objects
    picture_xpath = "//section[@id='search']/descendant::picture[1]/.."



    # Product page objects
    number_of_pieces_xpath="//span[@id='projector_amount']"
    list_of_items_xpath="//div[@class='projector_buy__number_wrapper']/div"
    # //div[@id='projector_buy_section']//ancestor::button[@type='button']
    list_of_items_input_xpath = "//input[@id='projector_number']"
    projektor_price_value_xpath="//strong[@id='projector_price_value']"
    picture_img_xpath = "//div[@data-product_first='true']//picture/img"
    add_to_basket="//button[@id='projector_button_basket']"

    # Pop up product page objects
    go_to_basket_xpath = "//div[@class='added__buttons']/a[1]"
    continue_shopping_xpath = "//div[@class='added__buttons']/a[2]"

    # Basket page objects
    amount_of_basket= "//div[@class='menu_basket_list']"
