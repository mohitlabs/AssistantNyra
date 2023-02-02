from gtts import gTTS
import speech_recognition as sr
import os
import sys
import signal
import datetime
import wikipedia
import webbrowser
import sys

class Nyra:
	def __init__(self):
		self.username = "Mohit"
		self.filepath = "audio/"
		self.filename = "Voice.mp3"
	
	def listen(self):
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("Listening...\n")
			r.pause_threshold = 1
			audio = r.listen(source)
		try:
			print("Recognizing...\n")
			query = r.recognize_google(audio, language="en-in").lower()
			print(f"You said: {query}\n")
			self.respond(query)
		except Exception as e:
			print(e)
			self.speak("Sorry, I can't get it. Please, can you say that again?")
			print("Say that again please...\n")
			return "None"
	
	def respond(self, query):
		if "shut up" in query:
			self.speak(f"I'm quitting myself. Have a nice time {self.username}. Good Bye!")
			exit()
#		elif "stop" in query:
#			devnull = open("/dev/null", 'w')
#			p = subprocess.Popen(["./main"], stdout=devnull, shell=False)
#			pid = p.pid
#			os.kill(pid, signal.SIGINT)
#			if not p.poll():
#				print("Process correctly halted.")
		elif "wikipedia" in query:
			self.speak("Searching wikipedia")
			query = query.replace("wikipedia", "")
			try:
				results = wikipedia.summary(query, sentences=2)
				print(results)
				self.speak("According to wikipedia, "+results)
			except Exception as e:
				print(e)
				self.speak("Nothing found. Please try again.")
		elif "google" in query:
			self.speak("Opening Google for you. Just wait.")
			webbrowser.open("https://google.com")
		elif "gmail" in query:
			self.speak("Opening your Gmail. Just wait.")
			webbrowser.open("https://gmail.com")
		elif "youtube" in query:
			self.speak("Opening Youtube for you. Just wait.")
			webbrowser.open("https://youtube.com")
		elif "github" in query:
			self.speak("Opening Github for you. Just wait.")
			webbrowser.open("https://github.com")
		elif "stackoverflow" in query:
			self.speak("Opening Stack Overflow for you. Just wait.")
			webbrowser.open("https://stackoverflow.com")
		elif "play some music" in query:
			music_dir = "/home/pi/Music"
			songs = os.listdir(music_dir)
			print(songs)
			opener = "open" if sys.platform == "darwin" else "xdg-open"
			subprocess.call([opener, os.path.join(music_dir, songs[randint(0, 100)])])
		elif "psychedelic music" in query:
			music_dir = "/home/pi/Downloads"
			songs = os.listdir(music_dir)
			print(songs)
			opener = "open" if sys.platform == "darwin" else "xdg-open"
			subprocess.call([opener, os.path.join(music_dir, songs[0])])
		elif "current time" in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			self.speak("It's "+strTime)
		self.speak("Anything else?")
	
	def speak(self, text):
		try:
			tts = gTTS(text=text, lang="en")
			tts.save(self.filepath+self.filename)
			os.system(f"mpg321 {self.filepath+self.filename}")
		except Exception as e:
			print(e)
			os.system(f"mpg321 {self.filepath}NetworkError.mp3")
	
	def wish_me(self):
		hour = int(datetime.datetime.now().hour)
		if hour >=0 and hour < 12:
			self.speak(f"Good morning {self.username}!")
		elif hour >= 12 and hour < 16:
			self.speak(f"Good afternoon {self.username}!")
		elif hour >= 16 and hour < 20:
			self.speak(f"Good evening {self.username}!")
		else:
			self.speak(f"Good night {self.username}!")
		self.speak("I am Nyra. Your virtual assistant. Tell me, how may I help you?")
