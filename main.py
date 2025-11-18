from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput


class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        name_layout = GridLayout(cols=2, size_hint=(1, 1))
        name_layout.add_widget(Label(text="Name:"))
        self.name_input = TextInput(multiline=False)
        name_layout.add_widget(self.name_input)
        self.layout.add_widget(name_layout)

        self.layout.add_widget(Label(text="1. What is the capital of France?"))
        self.q1_options = []
        q1_answers = ["Berlin", "Madrid", "Paris"]

        for ans in q1_answers:
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

        for ans in q2_answers:
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

        for ans in q3_answers:
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

        # RESULT / ERROR LABEL
        self.result_label = Label(text="Score:")
        self.layout.add_widget(self.result_label)

        return self.layout

    def submit_quiz(self, instance):
        name = self.name_input.text.strip()
        self.score = 0

        if self.q1_options[2].active and not self.q1_options[0].active and not self.q1_options[1].active:
            self.score += 1

        if self.q2_options[1].active and not self.q2_options[0].active and not self.q2_options[2].active:
            self.score += 1

        if self.q3_options[1].active and not self.q3_options[0].active and not self.q3_options[2].active:
            self.score += 1

        any_answer_selected = any(chk.active for chk in self.q1_options + self.q2_options + self.q3_options)

        if name == "":
            self.result_label.text = "[ERROR] Please enter a name."
            return

        if not any_answer_selected:
            self.result_label.text = "[ERROR] You must answer at least one question."
            return

        try:
            with open("results.txt", "a") as file:
                file.write(f"{name} - Score: {self.score}/3\n")
        except Exception as e:
            self.result_label.text = f"[ERROR] Could not save file: {e}"
            return

        self.result_label.text = f"Saved! Score: {self.score}/3"

        self.name_input.text = ""

        for chk in self.q1_options + self.q2_options + self.q3_options:
            chk.active = False


if __name__ == "__main__":
    MyApp().run()