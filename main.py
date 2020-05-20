from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import os
import random
import AWS
from hashtags import Hash
from kivy.event import EventDispatcher
from kivy.clock import Clock
from kivy.properties import StringProperty
import AWSStreaming
from kivy.uix.image import AsyncImage
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.uix.switch import Switch


class Logging(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(Logging, self).__init__(**kwargs)


    def log(self):

        Logging.is_logged = AWS.ifAccount(self.email.text, self.password.text)

        if Logging.is_logged == None:
            return False

        elif Logging.is_logged[0] == True:
            self.password.text = ""
            self.email.text = ""
            Logging.Info = AWS.getBasicInfo(Logging.is_logged[1])
            print(Logging.Info["Username"])
            return True

    def show_popup(self):
        show = P()
        popupWindow = Popup(title = "Invalid Email or password", content = show , size_hint = (None, None), size = (300, 300))
        popupWindow.open()

class P(FloatLayout):
    pass

class Main(Screen):

    carousel = ObjectProperty(None)
    launch = ObjectProperty(None)
    hash = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.vide = []
        self.p = play_button(pos_hint={"top": 0.2, "x": 0.45}, size_hint=(0.1, 0.1))
    def initial(self):
        self.vide = []
        number = 5
        x = AWSStreaming.getRandomList(number)
        for i in x:
            videocontent = AWSStreaming.getFile(i)
            self.vide.append(
                [AsyncImage(source = videocontent["ImageURL"]), SoundLoader.load(videocontent["AudioURL"])])
            self.carousel.add_widget(self.vide[-1][0])


    def on_leave(self, *args):
        for i in range(len(self.vide)-1):
            self.vide[i][1].stop()
        self.carousel.clear_widgets()
        self.vide = []


    def on_enter(self, *args):
        self.initial()
        Clock.schedule_interval(self.vid, 0.5)
        self.add_widget(self.p)


    def show_popup(self):
        show = P()
        popupWindow = Popup(title = "Wrong Hashtags", content = show , size_hint = (None, None), size = (300, 300))
        popupWindow.open()


    def vid(self, *args):
        for i in range(len(self.vide)-1):
            if self.carousel.current_slide == self.vide[i][0]:
                if self.p.state == "down":
                    self.vide[i][1].play()
                #elif self.p.state == "normal":
                 #   self.vide[i][1].stop()

class Registration(Screen):

    r_email = ObjectProperty(None)
    r_password = ObjectProperty(None)
    nickname = ObjectProperty(None)

    def regi(self):
        AWS.AddingAccount(self.nickname.text, self.r_email.text, self.r_password.text)
        self.nickname.text = ""
        self.r_email.text = ""
        self.r_password.text = ""



    def proper(self):
        if " " not in self.r_email.text and " " not in self.r_password.text:
            if self.r_email.text != "" and self.r_password.text != "":
                return True
        return False


    def show_popup(self):
        show = P()
        popupWindow = Popup(title = "Invalid Email or password", content = show , size_hint = (None, None), size = (300, 300))
        popupWindow.open()

class play_button(Button):
    def __init__(self, **kwargs):
        super(Button, self).__init__(**kwargs)
        self.pla = False
        #self.background_down = "on_play.png"
        #self.background_normal = "on_pause.png"
    def on_touch_down(self, touch):
        if (touch.x >= self.x and touch.x <= self.x+100) and (touch.y >= self.y and touch.y <= self.y+100):
            if self.state == "normal":
                self.state = "down"
                self.pla = True
            elif self.state == "down":
                self.state = "normal"
                self.pla = False
    def on_touch_up(self, touch):
        if touch.x == self.x and touch.y == self.y:
            if self.pla == True:
                self.state = "down"
            elif self.pla == False:
                self.state = "normal"
class MyProfile(Screen):
    nickname = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MyProfile, self).__init__(**kwargs)

    def on_enter(self, *args):
        self.nickname.text = Logging.Info["Username"]


class WindowManager(ScreenManager):
    pass

class MyMainApp(App):
    def build(self):
        return kv



kv = Builder.load_file("apli.kv")


if __name__ == "__main__":
    MyMainApp().run()