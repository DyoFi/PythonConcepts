from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.layout.add_widget(Label(text="1. What is the capital of France?"))
        self.q1_options = []
        q1_answers = ["Berlin", "Madrid", "Paris"]
        for i, ans in enumerate(q1_answers):
            row = BoxLayout(orientation='horizontal', spacing=10)
            chk = CheckBox()
            lbl = Label(text=ans)
            row.add_widget(chk)
            row.add_widget(lbl)
            self.layout.add_widget(row)
            self.q1_options.append(chk)
        self.layout.add_widget(Label(text="2. Which planet is known as the Red Planet?"))
        self.q2_options = []
        q2_answers = ["Venus", "Mars", "Jupiter"]
        for i, ans in enumerate(q2_answers):
            row = BoxLayout(orientation='horizontal', spacing=10)
            chk = CheckBox()
            lbl = Label(text=ans)
            row.add_widget(chk)
            row.add_widget(lbl)
            self.layout.add_widget(row)
            self.q2_options.append(chk)
        self.layout.add_widget(Label(text="3. Who wrote 'Romeo and Juliet'?"))
        self.q3_options = []
        q3_answers = ["Charles Dickens", "William Shakespeare", "Mark Twain"]
        for i, ans in enumerate(q3_answers):
            row = BoxLayout(orientation='horizontal', spacing=10)
            chk = CheckBox()
            lbl = Label(text=ans)
            row.add_widget(chk)
            row.add_widget(lbl)
            self.layout.add_widget(row)
            self.q3_options.append(chk)
        submit_btn = Button(text="Submit", size_hint=(1, 0.2))
        submit_btn.bind(on_press=self.submit_quiz)
        self.layout.add_widget(submit_btn)
        self.result_label = Label(text="Score:")
        self.layout.add_widget(self.result_label)
        return self.layout
    
    def submit_quiz(self, instance):
        self.score = 0

        if not self.q1_options[0].active and not self.q1_options[1].active and self.q1_options[2].active:
            self.score += 1
        if not self.q2_options[0].active and self.q2_options[1].active and not self.q2_options[2].active:
            self.score += 1
        if not self.q3_options[0].active and self.q3_options[1].active and not self.q3_options[2].active:
            self.score += 1

        self.result_label.text = f"Score: {self.score}/3"

if __name__ == "__main__":
    MyApp().run()