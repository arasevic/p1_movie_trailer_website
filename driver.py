import movie
import movie_trailer_generator

"""This script serves as the driver for the program"""

#generate instance of the movie class that will be displayed on the html page

gladiator = movie.Movie("Gladiator",
                         "http://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                         "https://www.youtube.com/watch?v=uwTKRz-WmHU")
    

bull_durham = movie.Movie("Bull Durham",
                      "http://upload.wikimedia.org/wikipedia/en/e/ef/Bull_Durham_film_poster.jpg",
                      "https://www.youtube.com/watch?v=dnJFndf-Krg")



field_of_dreams = movie.Movie("Field of Dreams", 
                             "http://upload.wikimedia.org/wikipedia/en/6/6b/Field_of_Dreams_poster.jpg",
                             "https://www.youtube.com/watch?v=vlTX_ckJ4nM")

donnie_brasco = movie.Movie("Donnie Brasco", 
                             "http://upload.wikimedia.org/wikipedia/en/b/bb/Donnie_brasco_ver2.jpg",
                             "https://www.youtube.com/watch?v=ShM8bGKVFXg")

goodfellas = movie.Movie("Goodfellas", 
                             "http://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",
                             "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

hamlet = movie.Movie("Hamlet", 
                             "http://upload.wikimedia.org/wikipedia/en/e/e9/Hamlet_1996_poster.jpg",
                             "https://www.youtube.com/watch?v=UjHXIWLTsOk")

#create array of movie instances to be passed as a paramterer to the open_movies_page method

movies = [gladiator, bull_durham, field_of_dreams, donnie_brasco, goodfellas, hamlet]

movie_trailer_generator.open_movies_page(movies)
