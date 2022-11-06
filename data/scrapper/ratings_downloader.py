from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time




# click the button with the css selector [css_selector] that has an inner text of [text]
def click_button_by_css_selector(driver, css_selector, text):
    buttons = driver.find_elements(By.CSS_SELECTOR, css_selector)
    for button in buttons:
        if button.text.lower() == text.lower():
            button.click()
            return




# scroll down the page to load more data
def scroll_down(driver, time_to_scroll_sec):
    # selecting the whole page to scroll
    page_to_scroll = driver.find_element(By.TAG_NAME, "html")
    
    # starting the timer and scrolling untill we reach the specified time
    clock_in_sec = time.perf_counter()
    while time.perf_counter() - clock_in_sec < time_to_scroll_sec:
        page_to_scroll.send_keys(Keys.DOWN)




# the main function
def main():
    # start the geckodriver
    s = Service(executable_path="./drivers/geckodriver")
    driver = webdriver.Firefox(service=s)

    # iterate through each hotel in the hotels csv
    with open('./data/csv_data/hotels.csv') as f:

        # pass the column names
        f.readline()

        # counter to label the output ratings' html source files
        i = 0

        # iterate through each hotel line
        for line in f:

            # temp
            if i <= 179:
                i += 1
                continue

            # get the hotel link
            hotel_link = line.split(',')[0] 

            # open the link in the browser
            try:
                driver.get(hotel_link)
            except:
                print('problem with link : ' + hotel_link)
                i += 1
                continue

            # click the reviews button in the hotel page to show reviews
            click_button_by_css_selector(driver, 'span.SxZPid.VZhFab', 'Reviews')

            # scroll down to load more reviews
            scroll_down(driver, 60)

            # create a file for the current hotel's ratings' html source
            with open('./data/html_source/ratings/' + str(i) + '.html', "w") as out_f:
                out_f.write(driver.page_source)

            i += 1

    # close the driver
    driver.close()

    print('Done.')

    


# execute the main function
main()
