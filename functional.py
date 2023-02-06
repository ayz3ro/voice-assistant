import os
import random
import webbrowser

import pyfiglet

import dict as dict
import voice_recognition.stt as stt
import voice_recognition.tts as tts


def spotify():
    tts.say('Spotify is open now')
    webbrowser.open('https://open.spotify.com/')


def startfunc():
    os.system('cls')
    print(pyfiglet.figlet_format("Voice assistant"))
    print("     ┌────────────────────────────────────────────────────┐")
    print("     │ Author : ayz3ro                                    │")
    print("     │ Tool   : Voice assistant                           │")
    print("     │ GitHub : https://github.com/ayz3ro                 │")
    print("     │ Coder  : ayz3ro                                    │")
    print("     └────────────────────────────────────────────────────┘")
    i = str(random.randint(1, 6))
    tts.say(dict.greetingDictionary[i])


def turnofffunc():
    i = str(random.randint(1, 2))
    tts.say(dict.farewellDictionary[i])
    os.system('cls')
    quit()


def webbrowser_search():
    tts.say('What shoud i search?')
    speach = stt.speach()
    webbrowser.open('https://www.google.com/search?q='+speach)
    tts.say('Done')


def mood():
    i = str(random.randint(1, 3))
    tts.say(dict.moodDictionary[i])


def main():
    startfunc()
    while True:
        speach = stt.speach()
        if speach in dict.spotifyDictionary:
            spotify()
        elif speach in dict.findDictionary:
            webbrowser_search()
        elif speach in dict.moodaskDictionary:
            mood()
        elif speach in dict.turnoffDictionary:
            turnofffunc()
