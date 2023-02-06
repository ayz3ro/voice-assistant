import pyttsx3

"""Iinititalization pytts3 library"""
engine = pyttsx3.init()

""" RATE"""
engine.setProperty('rate', 170)


def say(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()
