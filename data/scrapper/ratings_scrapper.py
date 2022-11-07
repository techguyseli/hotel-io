import re
from bs4 import BeautifulSoup



# get the contents of a file
def read_file(name):
    with open(name, 'r') as f:
        return f.read()



# add the ratings for the current html file to the passed ratings' list then return it
def get_hotel_ratings(hotel_num, hotel_link):
    ratings = []

    # getting the page source from the file
    page_source = read_file('./data/html_source/ratings/' + str(hotel_num) + '.html')

    # starting a BeautifulSoup object
    soup = BeautifulSoup(page_source, 'html.parser')

    # getting the comments' divs for the current ratings file
    comments_divs = soup.select('div.Svr5cf.bKhjM')

    # iterate through the divs
    for div in comments_divs:

        # continue if there is no comment span
        comment_spans = div.select("div.K7oBsc")[-1:][0].select('div span')
        if(len(comment_spans) == 0):
            continue

        # get the comment
        comment = comment_spans[0].get_text('\n')

        # clean the comment if it contains google translation additions
        translation_match = re.search('\\(Translated by Google\\)(.|\\n)*\\(Original\\)', comment)
        if translation_match is not None:
            comment = translation_match.group().replace('(Translated by Google) ', '').replace('(Original)', '')

        # get the rating
        rating = float(div.select('div.GDWaad')[0].get_text().split('/')[0])

        # create rating classes for the classification algorithm
        rating_class = None
        if rating <= 2:
            rating_class = '-1'
        elif rating == 3:
            rating_class = '0'
        else:
            rating_class = '+1'

        # append the hotel link, comment and rating dict to the comments list
        ratings.append({
            'hotel_link' : hotel_link,
            'comment' : comment.replace('\n', ' '),
            'rating' : rating_class
            })

    # return the collected comments
    return ratings




# the main function
def main():
    # custom separator
    sep = '/SEPARATOR/'

    # file mode
    fmode = 'w'

    # open the hotels file
    with open("./data/csv_data/hotels.csv", 'r') as hotels_file:

        # counter to call the file names of each hotels ratings page
        i = 0

        # ignore the header
        hotels_file.readline()
        
        # iterate through each line in the hotels csv file
        for line in hotels_file:

            # compensating for the inexistence of the file 180.html
            if i == 180:
                i +=1

            # getting the hotel link
            hotel_link = line.split(',')[0]

            # getting this hotel's list of ratings
            ratings = get_hotel_ratings(i, hotel_link)

            # write the data into a file
            with open('./data/csv_data/ratings.csv', fmode) as ratings_file:

                # first open write headers
                if fmode == 'w':
                    ratings_file.write('hotel_link' + sep + 'comment' + sep + 'rating\n')
                    fmode = 'a'

                # write the ratings
                for rating in ratings:
                    ratings_file.write(rating['hotel_link'] + sep + rating['comment'] + sep + rating['rating'] + '\n')

            print('file ' + str(i) + ' done processing.')

            i += 1

    print('done.')




main()
