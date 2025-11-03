from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation = "vertical")
        self.weight_input = TextInput(readonly = False, halign = "left", font_size = 40, hint_text = "Enter weight in kg")
        self.height_input = TextInput(readonly = False, halign = "left", font_size = 40, hint_text = "Enter height in cm")
        button = Button(text = "Calculate BMI")
        button.bind(on_press=self.calculate_BMI)
        self.result_label = Label(
            text = "BMI:",
            font_size = 24,
            color = (1,1,1,1),
            size_hint = (1,0.2)
        )
        layout.add_widget(self.weight_input)
        layout.add_widget(self.height_input)
        layout.add_widget(button)
        layout.add_widget(self.result_label)
        return layout
    def calculate_BMI(self, instance):
        weight = float(self.weight_input.text)
        height = float(self.height_input.text)
        height = height/100
        bmi = weight / (height ** 2)
        self.result_label.text = f"BMI: {bmi:.2f}"

if __name__ == "__main__":
    MyApp().run()