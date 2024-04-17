import requests

def get_poem_by_title(title):
    """ Fetch a poem by its title. """
    url = f"https://poetrydb.org/title/{title}"
    response = requests.get(url)
    return response.json()

def get_poems_by_author(author):
    """ Fetch all poems by a specific author. """
    url = f"https://poetrydb.org/author/{author}"
    response = requests.get(url)
    return response.json()
