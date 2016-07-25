import csv

class Movie:

    def get_movies(self):
        movies = []
        with open('u.item', encoding='latin_1') as f:
            movies_reader = csv.reader(f, delimiter='|')
            for row in movies_reader:
                movies.append(row)
                return movies

    def __init__(self, row):
        self.movie_id = int(row[0])
        self.movie_title = row[1]
        self.release_date = row[2]
        self.video_release = row[3]
        self.imdb_link = row[4]

    def __str__(self):
        print("Movie ID: {}, Moving Title: {}, Release Date: {}, Video Release: {}.".format(self.user_id, self.user_age, self.user_sex, self.user_occ, self.user_zip))


    genre_dict = {0: 'unknown', 1: 'Action', 2: 'Adventure', 3: 'Animation',
    4: 'Children\'s', 5: 'Comedy',6: 'Crime', 7: 'Documentary', 8: 'Drama',
    9: 'Fantasy', 10: 'Film-Noir', 11: 'Horror', 12: 'Musical', 13: 'Mystery',
    14: 'Romance', 15: 'Sci-Fi', 16: 'Thriller', 17: 'War', 18: 'Western'}


class Ratings:

    def get_ratings(self):
        ratings = []
        with open(filename, encoding='latin_1') as f:
            ratings_reader = csv.reader(f, delimiter='\t')
            for row in ratings_reader:
                ratings.append(row)
                return ratings

    def __init__(self, row):
        self.user_id = row[0]
        self.movie_id = row[1]
        self.movie_rtg = row[2]
        self.time_stamp = row[3]

    def __str__(self):
        print("User ID: {}, Movie ID: {}, Moving Rating: {}, Time Stamp: {}.".format(self.user_id, self.movie_id, self.movie_rtg, self.timestamp))



class User:

    def get_users(self):
        users = []
        with open('u.user', encoding='latin_1') as f:
            users_reader = csv.reader(f, delimiter='|')
            for row in users_reader:
                users.append(row)
                return users

    def __init__(self, row):
            self.user_id = int(row[0])
            self.user_age = int(row[1])
            self.user_sex = row[2]
            self.user_occ = row[3]
            self.user_zip = row[4]

    def __str__(self):
        print("User ID: {}, User Age: {}, User Gender: {}, User Occupation: {}, User Zip Code: {}.".format(self.user_id, self.user_age, self.user_sex, self.user_occ, self.user_zip))


def main():
    users = User.read('u.user')
    movies = Movie.read('u.item')
    ratings = Ratings.read('u.data')
#
#
# if __name__ == '__main__':
#     main()
