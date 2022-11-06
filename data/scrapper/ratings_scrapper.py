from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By



# get the contents of a file
def read_file(name):
    with open(name, 'r') as f:
        return f.read()



# return the ratings in a ratings html file as a list of ratings [hotel_url,comment,rating]
def get_hotel_ratings(hotel_num, hotel_link):
    # getting the page source from the file
    page_source = read_file('./data/html_source/ratings/' + str(hotel_num) + '.html')

    # starting a BeautifulSoup object
    soup = BeautifulSoup(page_source, 'html.parser')

    # getting the comments' divs
    comments_divs = soup.select('div.Svr5cf.bKhjM')

    # list to store the hotel link, comments and their rating in dicts
    comments = []

    # iterate through the divs
    for div in comments_divs:
        comment = div.select("div.K7oBsc")
        if len(comment) == 0:
            print('hkjl')
            for c in comment:
                print(c)
                print('-------')
            print('**********************')




# the main function
def main():
    # open the hotels file
    with open("./data/csv_data/hotels.csv", 'r') as hotels_file:

        # ignore the header
        hotels_file.readline()

        # counter to call the file names of each hotels ratings page
        i = 0
        
        # the ratings data structure
        ratings = []

        # iterate through each line in the hotels csv file
        for line in hotels_file:

            # compensating for the inexistence of the file 180.html
            if i == 180:
                i +=1

            # getting the hotel link
            hotel_link = line.split(',')[0]

            # getting this hotel's list of ratings
            this_hotel_ratings = get_hotel_ratings(i, hotel_link)

            print('file ' + str(i))

            i += 1

            #break

    print('done.')
     


main()
