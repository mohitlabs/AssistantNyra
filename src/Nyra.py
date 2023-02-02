from gtts import gTTS
import speech_recognition as sr
import os
import sys
import subprocess
#import signal
import datetime
import wikipedia
import webbrowser
import random

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
		if "stop yourself" in query:
			self.speak(f"I'm quitting myself. Have a nice time {self.username}. Good Bye!")
			exit()
#		elif "stop" in query:
#			devnull = open("/dev/null", 'w')
#			p = subprocess.Popen(["./main"], stdout=devnull, shell=False)
#			pid = p.pid
#			os.kill(pid, signal.SIGINT)
#			if not p.poll():
#				print("Process correctly halted.")
		elif "current time" in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			self.speak("It's "+strTime)
#		elif "open the terminal" in query:
#			self.speak("Opening the terminal for you.")
#			os.system("gnome-terminal")
#		elif "close the terminal" in query:
#			self.speak("Closing the terminal.")
#			os.system("exit")
		elif "status" in query:
			self.speak("Showing the current status of git of this local repository on your screen.")
			os.system("git status")
		elif "logs" in query:
			self.speak("Showing the current git logs of this local repository on your screen.")
			os.system("git status")
		elif "add these changes" in query:
			self.speak("Adding your current changes in the staging area.")
			os.system("git add .")
		elif "make a commit" in query:
			self.speak("Commiting your changes.")
			os.system("git commit -m \"Commit By AssistantNyra\"")
		elif "push these changes" in query:
			self.speak("Pushing your current changes into the master branch of the origin.")
			os.system("git push -u origin master")
		elif "play some music" in query:
			self.speak(f"OK {self.username}. Playing some random music from your favourite library.")
			music_dir = "/home/pi/Music"
			songs = os.listdir(music_dir)
			opener = "open" if sys.platform == "darwin" else "xdg-open"
			subprocess.call([opener, os.path.join(music_dir, songs[random.randint(0, 100)])])
		elif "psychedelic music" in query:
			self.speak(f"OK {self.username}. Playing your favourite psychedelic hardcore party music.")
			music_dir = "/home/pi/Downloads"
			songs = os.listdir(music_dir)
			opener = "open" if sys.platform == "darwin" else "xdg-open"
			subprocess.call([opener, os.path.join(music_dir, songs[0])])
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
		elif "open google" in query:
			self.speak("Opening Google for you. Just wait.")
			webbrowser.open("https://google.com")
		elif "open gmail" in query:
			self.speak("Opening your Gmail. Just wait.")
			webbrowser.open("https://gmail.com")
		elif "open youtube" in query:
			self.speak("Opening Youtube for you. Just wait.")
			webbrowser.open("https://youtube.com")
		elif "open github" in query:
			self.speak("Opening your Github. Just wait.")
			webbrowser.open("https://github.com")
		elif "open stackoverflow" in query:
			self.speak("Opening Stack Overflow for you. Just wait.")
			webbrowser.open("https://stackoverflow.com")
		else:
			self.speak(f"{self.username}, your query didn't match with my database. Try something else.")
			return
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
