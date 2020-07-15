import pickle
import time

from selenium import webdriver


def save_review_data(review_url, username, passowrd, num_of_page):
    """
    
    :param review_url: example: https://www.glassdoor.com/Reviews/Fidelity-Investments-Reviews-E2786. Note that mht is not included
    :param username: username to log on glassdoor
    :param passowrd: password
    :param num_of_page: how many pages of review you want to load
    :return: 
    """
    browser = webdriver.Chrome()
    browser.get("https://www.glassdoor.com/profile/login_input.htm")

    email_field = browser.find_element_by_name('username')
    password_field = browser.find_element_by_name('password')
    submit_btn = browser.find_element_by_xpath('//button[@type="submit"]')

    email_field.send_keys(username)
    password_field.send_keys(passowrd)
    submit_btn.click()

    time.sleep(3)

    page_list = [review_url + ".htm"]
    page_2_and_others = [f"{review_url}_P{i}.htm" for i in range(2, num_of_page + 1)]
    page_list.extend(page_2_and_others)

    print(page_list)

    result = []
    for index, p in enumerate(page_list):
        browser.get(p)
        content = browser.page_source

        result.append(content)
        time.sleep(3)

    with open("data.pickle", "wb") as file:
        pickle.dump(result, file)

save_review_data("https://www.glassdoor.com/Reviews/Fidelity-Investments-Reviews-E2786", "username",
                 "password", 5)
