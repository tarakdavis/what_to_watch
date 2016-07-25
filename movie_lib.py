import csv


class User:
    def __init__(self, row):
            self.user_id = int(row[0])
            self.user_age = int(row[1])
            self.user_sex = row[2]
            self.user_occ = row[3]
            self.user_zip = row[4]

    def __str__(self):
        return "User ID: {}, User Age: {}, User Gender: {}, User Occupation: {}, User Zip Code: {}.".format(self.user_id, self.user_age, self.user_sex, self.user_occ, self.user_zip)

    def get_user_lib():
        user_lib = {}
        with open('u.user') as f:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                key = (row[0])
                if key not in user_lib:
                    user_lib[key] = [(row[2])]
                else:
                    user_lib[key].append(row[2])


class Movie:

    def __init__(self, row):
        self.movie_id = int(row[0])
        self.movie_title = row[1]
        self.release_date = row[2]
        self.video_release = row[3]
        self.imdb_link = row[4]
        #self.genres =

    def __str__(self): "Movie ID: {}, Moving Title: {}, Release Date: {}, Video Release: {}.".format(self.user_id, self.user_age, self.user_sex, self.user_occ, self.user_zip)

    def get_movie_lib():

        with open('u.item', encoding = 'latin_1') as f:
            movie_lib = {}
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                movie_lib[row[2]] = Movie[row[2]]



    genre_dict = {0: 'unknown', 1: 'Action', 2: 'Adventure', 3: 'Animation',
    4: 'Children\'s',5: 'Comedy',6: 'Crime', 7: 'Documentary', 8: 'Drama',
    9: 'Fantasy', 10: 'Film-Noir', 11: 'Horror', 12: 'Musical', 13: 'Mystery',
    14: 'Romance', 15: 'Sci-Fi', 16: 'Thriller', 17: 'War', 18: 'Western'}


class Ratings:

    def __init__(self, row):
        self.user_id = row[0]
        self.movie_id = row[1]
        self.movie_rtg = row[2]
        self.time_stamp = row[3]

    def __str__(self):
        return "User ID: {}, Movie ID: {}, Moving Rating: {}, Time Stamp: {}.".format(self.user_id, self.movie_id, self.movie_rtg, self.timestamp)


    def get_user_ratings():
        with open('u.data') as f:
            reader = csv.reader(f, delimiter='\t')
            user_ratings = {}
            for row in reader:
                key = int(row[0])
                if key not in user_ratings:
                    user_ratings[key] = [int(row[2])]
                else:
                    user_ratings[key].append(int(row[2]))
        return user_ratings


def main():
    user_lib=User.get_user_lib()
    user_ratings=Ratings.get_user_ratings()
    movie_lib=Movie.get_movie_lib()


if __name__ == '__main__':
    main()
