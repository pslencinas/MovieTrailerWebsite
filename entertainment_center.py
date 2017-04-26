import media
import fresh_tomatoes

matrix = media.Movie("Matrix",
    "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

avatar = media.Movie("Avatar",
    "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=pPEm5agwjS8")

toy_story = media.Movie("Toy Story",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

fast8 = media.Movie("Fast & Furious 8",
    "https://upload.wikimedia.org/wikipedia/en/8/8f/Fast_and_Furious_Poster.jpg",
    "https://www.youtube.com/watch?v=uisBaTkQAEs")

logan = media.Movie("Logan",
    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
    "https://www.youtube.com/watch?v=RH3OxVFvTeg")

movies = [matrix, avatar, toy_story, fast8, logan]
fresh_tomatoes.open_movies_page(movies)