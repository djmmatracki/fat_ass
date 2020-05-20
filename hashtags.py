import random
from kivy.uix.videoplayer import VideoPlayer
import os
from kivy.uix.carousel import Carousel
from kivy.properties import ObjectProperty
from playsound import playsound
import AWSStreaming


class Hash():
    hash = ObjectProperty(None)
    carousel = ObjectProperty(None)
    def __init__(self):
        self.vide = []

    def vid_rand(self):

        if self.carousel.current_slide == (self.vide[-1] or self.vide[-2] or self.vide[-3]):
            pass