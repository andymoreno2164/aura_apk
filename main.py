from kivy.app import App
from kivy.uix.textinput import TextInput

class AuraApp(App):

    def build(self):
        terminal = TextInput(
            text="💫 AURA iniciada\n> ",
            multiline=True
        )
        return terminal

AuraApp().run()
