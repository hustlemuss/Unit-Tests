def longest_film(film_1: str, film_2: str, film_3: str) -> str:
    longest_film = [film_1, film_2, film_3]
    list_film = sorted(longest_film, key=len, reverse=True)
    sorted_list = list_film[0]
    return sorted_list