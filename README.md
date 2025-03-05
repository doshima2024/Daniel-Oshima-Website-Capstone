# Daniel Oshima's Music Website:

This project is a solution to the problems that Daniel Oshima wanted both a website to represent himself as a musical artist 
and showcase his music, while simultaneously practicing the skills he learned and developed over the first four phases
of his learning in Flatiron school. It as a full stack web application that allows user get to know Daniel as an artist, leave Guestbook entries on the home page, peruse selected tracks fetched from the backend and embedded in a Spotify player
and comment on them, and use Spotify's API for searching through his entire catalogue on Spotify.

# Technology Used:

Frontend:
React, Javascript and JSX with Vite
Bootstrap for Styling

Backend:
Flask 
Python
SQLalchemy
PostgreSQL

API:
Spotify's API, utilizing Client Credentials Flow for search functionality

# Features:



# Installation and Setup Guide:

Backend:

pipenv --python 3.8
pipenv install
pipenv shell
cd server
flask run

Frontend:
from root directory: 
npm install
npm run dev

The backend should now be running on http://127.0.0.1:5000 and you can visit http://localhost:5173/ at the frontend to view the site.

# Features:

1. Home page with a picture, bio and Guestbook where users can check in and leave their thoughts
2. Songs page that displays selected songs from Daniel's catalogue in an embedded spotify player
3. Songs page allows users to leave a comment on each song displayed
4. Search functionality within Daniel's entire catalogue via Spotify's API
5. Contact page
6. Nav bar and error page when visiting frontend routes that don't exist

# Challenges and New Learning:

1. PostgreSQL implementation for Database
2. Understanding Spotify API and authentication implementation
3. Explored using cards and new color schemes with Bootstrap

# Areas for Further Development

1. Ability for user's to register and login (user authentication) for a personalized experience
2. Building off of user authentication, a way for the user to create a custome mixtape of their favorite songs
3. An email list signup feature
4. An integrated shop or store

# Acknowledgments:

I'd like to thank Flatiron School for the curriculum, learning materials and support throughout my time in
the Software Engineering Bootcamp, with special thanks to my instructor Sakib Rasul for the fun and informative 
lectures, learning and tremendous support throughout my time in the program. I'd also like to acknowledge AskAda
and OpenAI for help with project structuring and debugging.
