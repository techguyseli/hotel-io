# write the cleaned ratings for the current hotel
def write_cleaned_ratings(c_ratings_f, hotel_link, hotel_id, sep):

    # open the ratings file
    with open('./data/csv_data/ratings.csv', 'r') as ratings_f:

        # ignore the header
        ratings_f.readline()

        # iterate through dirty ratings file lines
        for line in ratings_f:

            # if the current rating is of the current hotel
            if line.split(sep)[0] == hotel_link:
                
                # write the cleaned rating to the new file
                new_line = str(hotel_id) + sep + line.split(sep)[1] + line.split(sep)[2]
                c_ratings_f.write(new_line)




# write the cleaned images for the passed hotel
def write_cleaned_images(c_images_f, hotel_link, hotel_id):
    
    # open the images file
    with open('./data/csv_data/images.csv', 'r') as images_f:

        # ignore the header
        images_f.readline()

        # iterate through dirty images file lines
        for line in images_f:

            # if the current image is of the current hotel
            if line.split(',')[0] == hotel_link:
                
                # write the cleaned images to the new file
                c_images_f.write(str(hotel_id) + ',' + line.split(',')[1])




# clean the hotels file
def clean_data():

    # open the hotels file for reading
    with open('./data/csv_data/hotels.csv', 'r') as hf:

        # ignore the header
        hf.readline()

        # create the cleaned_hotels.csv for writing
        with open('./data/csv_data/cleaned_hotels.csv', 'w') as chf:

            # write the header
            chf.write('hotel_id,name,price,city\n')

            # variable to keep track of the id
            i = 1

            # open the cleaned images file for writing
            c_images_f = open('./data/csv_data/cleaned_images.csv', 'w')

            # write the header of the cleaned images
            c_images_f.write('hotel_id,image_id\n')
            
            # open the cleaned ratings file for writing
            c_ratings_f = open('./data/csv_data/cleaned_ratings.csv', 'w')

            # the separator for the ratings files
            rating_sep = '/SEPARATOR/'

            # write the header of the cleaned ratings
            c_ratings_f.write('hotel_id' + rating_sep + 'comment' + rating_sep + 'rating\n')


            # iterate through each line in the dirty file
            for line in hf:
                
                # get the line and change the hotel link to a hotel id 
                cleaned_line = line.split(',')
                cleaned_line[0] = str(i)
                cleaned_line = ','.join(cleaned_line)

                # write the cleaned line into the cleaned hotels file
                chf.write(cleaned_line)

                # write the images of this hotel to a cleaned images file
                write_cleaned_images(c_images_f, line.split(',')[0], i)

                # write the ratings for the current hotel
                write_cleaned_ratings(c_ratings_f, line.split(',')[0], i, rating_sep)

                print('hotel ' + str(i) + ' data cleaned.')

                i += 1



# the main function
def main():

    # clean the data
    clean_data()
    print('done cleaning the files.')



main()

