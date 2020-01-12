import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=10, orientation="vertical")
        self.header = TextInput(multiline=False)
        self.text = TextInput(multiline=True)
        self.btn = Button(text="Send", background_color=green)
        self.btn.bind(on_press=self.click)
        self.btn2 = Button(text="Display", background_color=purple)
        self.btn2.bind(on_press=self.click_btn2)
        layout.add_widget(self.header)
        layout.add_widget(self.text)
        layout.add_widget(self.btn)
        layout.add_widget(self.btn2)
        return layout
    def click(self, instance):
    	template = '''#{}
    	###current_time
    	{}'''
    	try:
    		with open("README.md", "a") as f:
    			f.write(template.format(self.header.text, self.text.text))
    	except:
    		self.text.text = "No README"
    def click_btn2(self, instance):
    	with open("README.md", "r") as f:
    		content = f.read()
    		self.text.text = content
		

if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()