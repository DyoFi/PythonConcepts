from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation = "vertical")
        text = TextInput(readonly = False, halign = "left", font_size = 40, hint_text = "Enter weight in kg")
        text2 = TextInput(readonly = False, halign = "left", font_size = 40, hint_text = "Enter height in cm")
        button = Button(text = "Calculate BMI")
        label = Label(
            text = "BMI:",
            font_size = 24,
            color = (1,1,1,1),
            size_hint = (1,0.2)
        )
        layout.add_widget(text)
        layout.add_widget(text2)
        layout.add_widget(button)
        layout.add_widget(label)
        return layout
    

if __name__ == "__main__":
    MyApp().run()