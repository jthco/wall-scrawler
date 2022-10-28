"""
Deep AI Python interface

Created by Johan Thornton
 2022-09-02
"""
import webbrowser, requests, json, cv2, pytesseract
#from googletrans import Translator, constants

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#translator = Translator()

keepText = ""

class DeepAI:
	def __init__(self):
		self.ApiKey = ""

	def text2Url(self, text):
		print("--- generating AI image ---", keepText)
		r = requests.post(
			"https://api.deepai.org/api/text2img",
			data={
				'text': text,
			},
			headers={'api-key': self.ApiKey}
		)
		return r.json()['output_url']

	def getAiImage(self, url):
		webbrowser.open(url, new=0, autoraise=True)

class WebCam:
	def __init__(self):
		self.deepAi = DeepAI()

	def show_webcam(self):
		cam = cv2.VideoCapture(0)
		while True:
			ret_val, img = cam.read()
			img, text = self.addWordBoxes(img)
			cv2.imshow('"Art Me, Computer!"', img)
			if self.onlyCaps(text):
				#print("Translating", text)
				print(text)

				#text = translator.translate(text)
				#print("to", text)
				keepText = text
			key = cv2.waitKey(1)
			if key == 27: # esc to quit
				break
			if key == 32: # space to generate image
				url = self.deepAi.text2Url(keepText)
				self.deepAi.getAiImage(url)
		cv2.destroyAllWindows()

	def addWordBoxes(self, img):
		def stripSpaces(text):
			return " ".join(text.split())
		h, w, c = img.shape
		d = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
		n_boxes = len(d['text'])
		for i in range(n_boxes):
			if int(d['conf'][i]) > 60:
				(x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
				img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
		sentence = ''.join(word + " " for word in d['text'])
		return img, stripSpaces(sentence)

	def onlyCaps(self, text):
		hasLetters = False
		for letter in text:
			if letter.islower():
				return False
			if letter.isupper():
				hasLetters = True
			if not letter.isupper() and letter != ' ':
				return False
		return hasLetters

if __name__ == '__main__':
	webCam = WebCam()
	webCam.show_webcam()


