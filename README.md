# PoetryDB API Test Suite

This repository contains the test suite for the PoetryDB API, which provides access to a wide collection of poetry data. This suite is designed to validate the functionality and accuracy of the API endpoints using Python and the `requests` library.

## Repository Structure

- `src/`
  - **`test_poetrydb.py`**: Contains the unittest test cases for the API.
  - **`api_helper.py`**: Helper functions that handle API requests to the PoetryDB API.
- `requirements.txt`: Lists all the necessary Python packages required to run the tests.

## Test Cases

The following table outlines the test cases included in this test suite:

| Test Case ID | Description | Endpoint | Expected Result | Validation Method |
|--------------|-------------|----------|-----------------|-------------------|
| 1 | Retrieve a specific poem by its title | `/title/Ozymandias` | The API returns the poem "Ozymandias" by Percy Bysshe Shelley, including the correct lines of the poem. | Check that the `title`, `author`, and `lines` keys in the response JSON match the expected values. |
| 2 | Search poems by author | `/author/Emily Dickinson` | The API returns a list of poems by Emily Dickinson, each including a title and lines. | Ensure each poem in the response has `author` as "Emily Dickinson" and that the `title` and `lines` are present and correct. |

## Validation Description

### Why Validation is Important

Validation ensures that the API responds with the correct data and behaves as expected. This is crucial not only for verifying the functionality but also for maintaining the reliability of the API over time, especially after updates or changes to the API.

### How Validation is Implemented

- **Accuracy of Content**: By checking specific JSON keys (`title`, `author`, `lines`), we ensure the content not only exists but is also accurate compared to known data (e.g., the correct poem and author).
- **Consistency and Completeness**: For lists of poems (e.g., when searching by author), validations confirm that all entries adhere to expected data structures and that no incomplete data is returned.

These validations help identify issues early, reducing the risk of deploying malfunctioning updates to production environments where they could impact users.

## Setup and Running Tests

To set up and run the tests, follow these steps:

1. Clone the repository:
git clone https://github.com/CtrlArtDel/PoetryDB_API_Test_Suite.git
2. Navigate to the cloned directory:
cd PoetryDB_API_Test_Suite
3. Install required packages:
pip install -r requirements.txt
4. Run the tests:
python -m unittest src/test_poetrydb.py


## Contributing

Contributions to this test suite are welcome. Please ensure to update tests as appropriate when making changes to the API, and follow the existing testing patterns established in this suite.

