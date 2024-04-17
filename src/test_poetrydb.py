import unittest
import logging
from api_helper import get_poem_by_title, get_poems_by_author

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestPoetryDBAPI(unittest.TestCase):

    def test_retrieve_poem_by_title(self):
        """Test retrieving a specific poem by its title."""
        poem = get_poem_by_title("Ozymandias")[0]  # Assuming the first result is correct
        self.assertEqual(poem['title'], "Ozymandias")
        self.assertEqual(poem['author'], "Percy Bysshe Shelley")
        self.assertTrue("I met a traveller from an antique land" in poem['lines'])
        logging.info("Test for retrieving poem by title passed successfully.")

    def test_search_poems_by_author(self):
        """Test searching poems by an author."""
        poems = get_poems_by_author("Emily Dickinson")
        self.assertTrue(all(poem['author'] == "Emily Dickinson" for poem in poems))
        self.assertTrue(len(poems) > 0)
        logging.info("Test for searching poems by author passed successfully.")



if __name__ == '__main__':
    unittest.main()
