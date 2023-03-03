# import the spaCy library
import spacy

# load the English language model
nlp = spacy.load('en_core_web_md') # specifying the model we want to use.

# read the file with movie descriptions and store the data in a list
with open('movies.txt', 'r') as file:
    movies = file.readlines()

# store the description of the last watched movie into a variable
planet_hulk = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

# define a function
def watch_next(last_movie):
    """Returns which movies from the list a user would watch next based on the description the movie they have watched

    Parameters:
        last_movie (str): the description of the last watched movie

    Returns:
        next_movie_title (str): the title of the movie to watch next"""

    # declare a list variable to store the values of similarities
    similarities = []

    # process a last_movie string in preparation for spaCy manipulation - create a nlp object
    token = nlp(last_movie)

    # iterate over the list of movies
    # process each string in preparation for spaCy manipulation
    # compare the last_movie with each movie in the list and store the result into the corresponding list
    # find the highest similarity in the list, define the movie it refers to and return the title of the movie
    for movie in movies:
        token2 = nlp(movie)
        similarity = token.similarity(token2)
        similarities.append(similarity)
    highest_similarity = max(similarities)
    index = similarities.index(highest_similarity)
    next_movie = movies[index]
    next_movie_title = next_movie.split(":")[0]
    return next_movie_title

# print out the result of the function execution
print(watch_next(planet_hulk))