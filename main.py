from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView




class MyApp(App):
    def build(self):


        self.tabs = TabbedPanel(do_default_tab=False)


        quiz_tab = TabbedPanelItem(text="Quiz")
        quiz_tab.add_widget(self.build_quiz_layout())
        self.tabs.add_widget(quiz_tab)


        results_tab = TabbedPanelItem(text="View results")
        results_tab.add_widget(self.build_results_layout())
        self.tabs.add_widget(results_tab)


        return self.tabs


    def build_quiz_layout(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)


        name_layout = GridLayout(cols=2, size_hint=(1, 1.5))
        name_layout.add_widget(Label(text="Name:"))
        self.name_input = TextInput(multiline=False)
        name_layout.add_widget(self.name_input)
        layout.add_widget(name_layout)


        layout.add_widget(Label(text="1. What is the capital of France?"))
        self.q1_options = []
        for ans in ["Berlin", "Madrid", "Paris"]:
            row = BoxLayout(orientation='horizontal')
            chk = CheckBox()
            row.add_widget(chk)
            row.add_widget(Label(text=ans))
            layout.add_widget(row)
            self.q1_options.append(chk)


        layout.add_widget(Label(text="2. Which planet is known as the Red Planet?"))
        self.q2_options = []
        for ans in ["Venus", "Mars", "Jupiter"]:
            row = BoxLayout(orientation='horizontal')
            chk = CheckBox()
            row.add_widget(chk)
            row.add_widget(Label(text=ans))
            layout.add_widget(row)
            self.q2_options.append(chk)


        layout.add_widget(Label(text="3. Who wrote 'Romeo and Juliet'?"))
        self.q3_options = []
        for ans in ["Charles Dickens", "William Shakespeare", "Mark Twain"]:
            row = BoxLayout(orientation='horizontal')
            chk = CheckBox()
            row.add_widget(chk)
            row.add_widget(Label(text=ans))
            layout.add_widget(row)
            self.q3_options.append(chk)


        submit_btn = Button(text="Submit", size_hint=(1, 0.2))
        submit_btn.bind(on_press=self.submit_quiz)
        layout.add_widget(submit_btn)


        self.result_label = Label(text="Score:")
        layout.add_widget(self.result_label)


        return layout


    def build_results_layout(self):


        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)


        refresh_btn = Button(text="Refresh student list", size_hint=(1, 0.15))
        refresh_btn.bind(on_press=self.load_students)
        main_layout.add_widget(refresh_btn)


        scroll = ScrollView(size_hint=(1, 1))
        self.student_list = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        self.student_list.bind(minimum_height=self.student_list.setter('height'))
        scroll.add_widget(self.student_list)


        main_layout.add_widget(scroll)


        return main_layout


    def submit_quiz(self, instance):
        name = self.name_input.text.strip()
        self.score = 0


        if self.q1_options[2].active and not self.q1_options[0].active and not self.q1_options[1].active:
            self.score += 1


        if self.q2_options[1].active and not self.q2_options[0].active and not self.q2_options[2].active:
            self.score += 1


        if self.q3_options[1].active and not self.q3_options[0].active and not self.q3_options[2].active:
            self.score += 1


        if name == "":
            self.result_label.text = "Please enter a name."
            return
       
        any_answer = any(chk.active for chk in self.q1_options + self.q2_options + self.q3_options)
        if not any_answer:
            self.result_label.text = "Please answer at least one question."
            return


        try:
            with open("results.txt", "a") as f:
                f.write(f"{name}, {self.score}/3\n")
        except:
            self.result_label.text = "Could not save file."
            return


        self.result_label.text = f"Saved! Score: {self.score}/3"


        self.name_input.text = ""
        for chk in self.q1_options + self.q2_options + self.q3_options:
            chk.active = False


    def load_students(self, instance):


        self.student_list.clear_widgets()


        try:
            with open("results.txt", "r") as f:
                lines = f.readlines()


        except:


            self.student_list.add_widget(Label(text="No students found."))
            return


        if not lines:
            self.student_list.add_widget(Label(text="No students found."))
            return


        for line in lines:


            try:
                name, score = line.strip().split(",")
            except:
                continue


            card = BoxLayout(orientation='horizontal', size_hint_y=None, height=40, padding=10)


            card.add_widget(Label(text=name, size_hint_x=0.6))
            card.add_widget(Label(text=score, size_hint_x=0.4))


            self.student_list.add_widget(card)




if __name__ == "__main__":
    MyApp().run()

