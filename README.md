# wall-scrawler
An AI art generator that reads hand-written text in any language. (Languages are currently disabled.)

### Installation
You need to install Tesseract-OCR from https://github.com/tesseract-ocr/tesseract.

Then you pip install requests, opencv-python, and pytesseract.

You will need an API key from deepai.org.

### Instructions
Using only upper case letters, show your webcam the text of your desired, and press the space bar when it prints exactly what you wrote. Four images will open in your default browser. Press escape or Q to exit.

### Teaching moment

This was an idea I had, and I did it in Python, because in Python it's often trivially easy to link different modules together to accomplish new things. So here I took a webcam library, an OCR library, a translation library and an AI art generation library, and put them together in two hours and around 70 lines of code. Most of that was found example code, and only a small amount is my glue code.
This is an art installation consisting of a whiteboard where you write a description by hand in one of 37 languages, and then AI projects new art onto that whiteboard. Two hours and 70 lines of code. I love you Python.
