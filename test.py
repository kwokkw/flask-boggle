# Imports the `TestCase` class that contains test methods from the `unittest` module for creating unit tests.
from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

app.config["TESTING"] = True
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]


# Access to different test methods by inheriting from the `TestCase` class.
class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def setUp(self):
        print("inside set up")

    def test_homepage(self):

        # Simulating user interactions with the Flask application during unit tests.
        # Ensures that the created client object (the test client) is properly cleaned up and closed after the code within the block (`with ...`) has finished executing.
        with app.test_client() as client:

            # To see what we have access to
            # import pdb

            # pdb.set_trace()

            res = client.get("/")

            # The following three lines achieve the same result.
            # Extracting and checking the content from a response object (response)
            # in a Flask test, but they differ in how they handle the data and what they verify:

            # Retrieves the raw response body (payload) as a decoded string (likely UTF-8),
            # useful when you want to examine the ACTUAL HUMAN-READABLE HTML content of the response.
            html = res.get_data(as_text=True)

            # use `self.assertIn` (with a string argument) to check for specific text or elements within the HTML.
            self.assertIn("<h1>Welcome To The Boggle Game</h1>", html)

            # directly checks for the presence of the string WITHOUT DECODING it.
            # uses `b"..."` to create a bytestring literal.
            # searches for the exact bytes "<h1>Welcome To The Boggle Game</h1>"
            self.assertIn(b"<h1>Welcome To The Boggle Game</h1>", res.data)

            self.assertEqual(res.status_code, 200)
            print("homepage - testing set up")

    def test_submit_guess(self):
        with app.test_client() as client:
            res = client.post("/submit-guess", json={"keyword": "guessing"})
            self.assertEqual(res.status_code, 200)

            self.assertIn(b"<p>Make a guess</p>", res.data)

    def test_post_score(self):
        with app.test_client() as client:
            res = client.post("/post-score", json={"score": 1})
            self.assertEqual(res.status_code, 200)
            self.assertIn(b"gamePlayed", res.data)


""" To execute the test

$ python -m unittest test.py - runs all test cases

 """
