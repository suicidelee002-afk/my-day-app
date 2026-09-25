from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp


class MyDayApp(App):

    def build(self):
        self.tasks = []

        root = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(12)
        )

        title = Label(
            text="MY DAY",
            font_size=dp(30),
            size_hint_y=None,
            height=dp(60)
        )
        root.add_widget(title)

        self.task_input = TextInput(
            hint_text="What do you need to do?",
            multiline=False,
            size_hint_y=None,
            height=dp(55)
        )
        root.add_widget(self.task_input)

        self.time_input = TextInput(
            hint_text="How many minutes?",
            input_filter="int",
            multiline=False,
            size_hint_y=None,
            height=dp(55)
        )
        root.add_widget(self.time_input)

        add_button = Button(
            text="ADD TASK",
            size_hint_y=None,
            height=dp(55)
        )
        add_button.bind(on_press=self.add_task)
        root.add_widget(add_button)

        self.schedule = BoxLayout(
            orientation="vertical",
            spacing=dp(8),
            size_hint_y=None
        )
        self.schedule.bind(minimum_height=self.schedule.setter("height"))

        scroll = ScrollView()
        scroll.add_widget(self.schedule)
        root.add_widget(scroll)

        self.message = Label(
            text="Your schedule will appear here",
            size_hint_y=None,
            height=dp(50)
        )
        root.add_widget(self.message)

        return root

    def add_task(self, instance):
        task = self.task_input.text.strip()
        minutes = self.time_input.text.strip()

        if not task or not minutes:
            self.message.text = "Please enter a task and time."
            return

        minutes = int(minutes)

        self.tasks.append((task, minutes))

        label = Label(
            text=f"• {task} — {minutes} minutes",
            size_hint_y=None,
            height=dp(45),
            halign="left"
        )
        label.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", (instance.width, None))
        )

        self.schedule.add_widget(label)

        total = sum(time for _, time in self.tasks)
        self.message.text = f"Total planned time: {total} minutes"

        self.task_input.text = ""
        self.time_input.text = ""


if __name__ == "__main__":
    MyDayApp().run()