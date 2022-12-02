from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time


# click the button with the class [class_name] that has an inner text of [text]
def click_button_by_class(driver, class_name, text):
    buttons = driver.find_elements(By.CLASS_NAME, class_name)
    for button in buttons:
        if button.text.lower() == text.lower():
            button.click()
            return



# sort the hotels by most rated
def sort_by_ratings(driver):
    # click the sort by button
    click_button_by_class(driver, "m1GHmf", "sort by")

    # sort by most rated
    click_button_by_class(driver, "VfPpkd-V67aGc", "most reviewed")

    print("- sorting done.")



# scroll down the page to load more data
def scroll_down(driver):
    # time to scroll in seconds
    time_to_scroll_sec = 60

    # selecting the whole page to scroll
    page_to_scroll = driver.find_element(By.TAG_NAME, "html")
    
    # starting the timer and scrolling untill we reach the specified time
    clock_in_sec = time.perf_counter()
    while time.perf_counter() - clock_in_sec < time_to_scroll_sec:
        page_to_scroll.send_keys(Keys.DOWN)

    print("- scrolling done.")



# get the hotels page source
def get_hotels_page_source(driver, city):
    # get the page
    driver.get("https://www.google.com/travel/hotels/" + city)

    # sort the hotels by most rated
    sort_by_ratings(driver)

    # scroll down
    scroll_down(driver)

    return driver.page_source



# the main function
def main():
    # start the geckodriver
    s = Service(executable_path="./drivers/geckodriver")
    driver = webdriver.Firefox(service=s)

    # get the hotel divs
    hotels_webpages_by_city = {
            "tangier" : get_hotels_page_source(driver, "Tangier"),
            "marakesh" : get_hotels_page_source(driver, "Marrakesh")
    }

    # close the driver
    driver.close()

    # download data into files
    with open("./data/marakesh.html", "w") as f:
        f.write(hotels_webpages_by_city["marakesh"])
    with open("./data/tangier.html", "w") as f:
        f.write(hotels_webpages_by_city["tangier"])

    


# execute the main function
main()
