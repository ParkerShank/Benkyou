# Benkyou
Benkyou | Flashcard Study App
Benkyou is a Python desktop application built with Tkinter for creating, organizing, and studying flashcards including support for text, image, and audio cards. The app uses a JSON file to manage sets and cards, and provides an intuitive graphical interface for navigation and learning.

Features
Multiple Flashcard Sets
Create, view, and manage multiple flashcard sets, each with its own cards.

Text, Image, & Audio Cards
Add flashcards with text questions/answers, images (.jpeg), or audio files (.mp3/.mp4).

Randomized Study Mode
Study cards in randomized order with forward/backward navigation.

Delete Cards or Sets
Easily remove unwanted cards or entire sets.

Custom Theming
Styled with a clean, modern UI using consistent background and accent colors.

Setup & Installation
Requirements
Python 3.x

Dependencies:
pip install pillow playsound

Folder Structure
├── benkyou.py         # Main app file
├── test.json          # JSON file for flashcard sets
├── images/            # Folder for image cards (JPEGs)
├── audio/             # Folder for audio cards (MP3/MP4)
Run the App

python benkyou.py
Make sure test.json is initialized with:

json

{
  "default": ""
}

How It Works
Set Management
Create Set: Go to “View Sets” → “Create Set” to add a new set.

Delete Set: Inside a set, click “Delete Set” to remove it permanently.

Adding Cards
Text Card: Enter a question and answer, then submit.

Image Card: Place a .jpeg file in the images/ folder, enter its name as the question.

Audio Card: Place an .mp3 or .mp4 file in audio/, enter its name as the question.

Studying
Click “Study Cards” inside a set.

Navigate with Back, Next, Show Answer, or Exit.

File Structure
All flashcard data is saved in a JSON file. Here's a basic structure:

{
  "Biology": {
    "Question 1": ["What is the powerhouse of the cell?", "Mitochondria"],
    "count": 2
  }
}

Image/audio questions simply use the filename instead of a question string.

Code Structure
Class benkyou: Main application class handling UI, logic, and data.

Methods:

makeFrames(): Initializes all screens.

createSet(), submit_data(): For adding sets/cards.

study_cards(): Launches random study mode.

displayFrame(): Switches between screens.

del_set(), del_card(), del_cards(): Deletion utilities.

To-Do / Ideas
Support .wav or .ogg files.

switch to a new sound module

Study statistics (accuracy, streaks).

Export/import sets as files.

Preview audio/image before adding.

Authors:
Parker Shanklin, Amaar Sharif
A creative, hands-on developer passionate about interactive educational tools.