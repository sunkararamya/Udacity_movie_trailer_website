import fresh_tomatoes
import film_media

def main():
    """Creates six Movie objects, initialising these objects with title, storyline,
    poster image link, video trailer link and release date."""
    In_the_Loop = film_media.Film("In the Loop",
                          "A political satire about a group of skeptica American and British operatives attempting to prevent a war between two countries.",
                          "https://cover.box3.net/newsimg/dvdmov/max1355591424-inlay-cover.jpg",
                          "https://www.youtube.com/watch?v=yJU2qRg5zLI",
                          "October 2, 2009")

    get_out = film_media.Film("Get Out","A young African-American vis its his white girlfriend parents for the weekend, where his simmering uneasiness abouttheir reception of him eventually reaches a boiling point.",
                          "https://upload.wikimedia.org/wikipedia/en/a/a3/Get_Out_poster.png",
                          "https://www.youtube.com/watch?v=sRfnevzM9kQ",
                          "July 11,2016")

  

   Mission_Impossible = film_media.Film("Mission: Impossible - Fallout",
                                        '''a devil movie on titanic''',
                         "https://images-na.ssl-images-amazon.com/images/I/814V1XJaoAL._SY445_.jpg",
                         "https://www.youtube.com/watch?v=wb49-oV0F78",
                         "Feb 5, 2018")

    Annihilation = film_media.Film("Annihilation",
                           '''A biologist signs up for a dangerous, secret expedition
                           "into a mysterious zone where the laws of nature don't apply.''',
                           "https://upload.wikimedia.org/wikipedia/en/f/f6/Annihilation_%28film%29.png",
                           "https://www.youtube.com/watch?v=89OP78l9oF0",
                           "October 19, 2018")

    Fantastic_Beasts= film_media.Film("Fantastic_Beasts",
                          "The latest James Bond movie",
                          "https://upload.wikimedia.org/wikipedia/en/c/c3/Spectre_poster.jpg",
                          "https://www.youtube.com/watch?v=vBnGxAkdh_k",
                          "October 26, 2015")

    # Store the Movie objects in a list.
    films = [In_the_Loop, get_out, thats_my_boy, Mission_Impossible, Annihilation,Fantastic_Beasts]

    # Open the movie website in the user's browser, featuring the films above.
    fresh_tomatoes.open_films_page(films)

if __name__ == '__main__':
    main()
