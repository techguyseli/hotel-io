import re
from bs4 import BeautifulSoup




# returns a list of each hotel div
def get_hotels_divs(page_source):
    # parse the file with bs4
    soup = BeautifulSoup(page_source, 'html.parser')
    initial_divs = soup.find_all("c-wiz")
    divs = []
    for div in initial_divs:
        try:
            if 'TNNk1' in div["class"] and 'nzwZbc' in div["class"]:
                divs.append(div)
        except:
            continue
    return divs




# get all the basic hotel info from the hotel divs [link (for later use), name, price, list of images, city] if they have ratings
def get_hotels_info(hotels_divs):
    hotels = []
    for hotel_div in hotels_divs:
        # if there are no reviews then skip
        reviews = hotel_div.select('span.jdzyld.XLC8M')
        if len(reviews) == 0:
            continue

        # get hotel webpage link
        hotel_link = 'https://www.google.com' + hotel_div.find('a').attrs["href"]
        
        # get hotel name 
        hotel_name = hotel_div.find('h2').text 
        
        # iterate through spans to find the price span
        spans = hotel_div.find_all("span")
        price = None
        for span in spans:
            search = re.search('^MAD\\s.*\\d$', span.text)
            if search: 
                price = search.group().split("\xa0")[1].replace(",", "")
                break

        # get the images
        images_elements = hotel_div.find_all("img")
        images = []
        for image_elm in images_elements:
            if 'data-src' in image_elm.attrs.keys():
                images.append(image_elm.attrs["data-src"])
                continue
            images.append(image_elm.attrs["src"])

        # create a hotel dict
        hotel = {
                'link' : hotel_link,
                'name' : hotel_name.replace(',', ''),
                'price' : price,
                'images' : images
                }

        # add the hotel to the hotels list
        hotels.append(hotel)

    return hotels




# the main function
def main():
    # html source files relative path
    files = {
            'Marrakesh' : './data/html_source/marakesh.html',
            'Tangier' : './data/html_source/tangier.html'
            }

    with open("./data/csv_data/hotels.csv", 'w') as hotels_file:
        hotels_file.write('link,name,price,city\n')

    with open('./data/csv_data/images.csv', 'w') as images_file:
        images_file.write('hotel_link,image_link\n')

    # iterate through the files
    for city, file_path in files.items():
        
        # open the file in read mode 
        with open(file_path, "r") as f:

            # read the file
            page_source = f.read()

            
            # get a list of the hotel divs
            hotels_divs = get_hotels_divs(page_source)

            # get all the basic hotel info from the hotel divs [name, price, list of images, city] if they have ratings
            hotels = get_hotels_info(hotels_divs)
            
            # write hotels data and images to files
            with open("./data/csv_data/hotels.csv", 'a') as hotels_file:
                with open('./data/csv_data/images.csv', 'a') as images_file:

                    # write each hotel to hotels csv
                    for hotel in hotels:
                        hotel_str = str(hotel['link']) + "," + str(hotel['name']) + "," + str(hotel['price']) + "," + city + "\n"
                        hotels_file.write(hotel_str)

                        # write each image to images csv
                        for image in hotel['images']:
                            image_str = str(hotel['link']) + "," + str(image) + '\n'
                            images_file.write(image_str)

    print('done')
 



main()
