from msilib.schema import CheckBox
import kivy
from genericpath import isfile
import kivy.utils
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
import os
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
import json


class DataBase:
    def __init__(self):
        self.ingredients = None
        self.load()
        pass

    def load(self):
        with open('ingredients.json', 'r') as openfile:
            # Reading from json file
            self.ingredients = json.load(openfile)
            
        pass

    def add_ingredient(self, ingredient):
        if ingredient.strip() not in self.ingredients:
            self.ingredients.append(ingredient.strip())
            self.save()
            return 1
        else:
            print("Ingredient exists already")
            return -1
        pass

    def save(self):
        with open("ingredients.json", "w") as outfile:
            json.dump(self.ingredients, outfile)
        pass


class MainWindow(Screen):
    def checkbox_click(self, instance, value):
        if value:
            pass
        else:
            pass

    def populateList():
        if os.path.exists("ingredients.json") and os.path.isfile("ingredients.json"):
            with open('ingredients.json', 'r') as openfile:
                # Reading from json file
                ingredients = json.load(openfile)
                layout = GridLayout(cols=3, spacing=10, size_hint_y=None)
                for i in range(len(ingredients)):
                    checkbox = CheckBox(active=False)
                    label = Label(text=str(ingredients), font_size=32, font_name="Royalacid.ttf", color=[.00, .00, .00, 1])
                    button = Button(text="patata",background_normal="trash-can.png")
                    
                    layout.add_widget(checkbox)
                    layout.add_widget(label)
                    layout.add_widget(button)
                #self.ids.scroll_ingredients.add_widget(layout)
    pass


class SecondWindow(Screen):
    ingredient_name = ObjectProperty(None)

    def submit(self):
        if self.ingredient_name.text != "":
            if self.ingredient_name.text not in dt.ingredients:
                dt.add_ingredient(self.ingredient_name.text)
                self.reset()
            else:
                self.reset()
                print("ingredient already in")
        else:
            print("no text")
            #invalidForm()
    pass

    def reset(self):
        self.ingredient_name.text = ""
    pass


class ThirdWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("interface.kv")
if os.path.exists("ingredients.json") and os.path.isfile("ingredients.json"):
    with open("ingredients.json") as datafile:
        db = datafile
else:
    open("ingredients.json", "w")
    with open("ingredients.json") as datafile:
        db = datafile
        x = []
        with open("ingredients.json", "w") as outfile:
            json.dump(x, outfile)

dt = DataBase()
MainWindow.populateList()

class KitchenInTheFridgeApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    KitchenInTheFridgeApp().run()