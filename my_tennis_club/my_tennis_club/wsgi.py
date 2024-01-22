from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class WordsApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.word_input = TextInput(hint_text="Enter a word")
        self.definition_box = BoxLayout(orientation='vertical', spacing=10, padding=10, size_hint=(None, None), size=(400, 200))
        self.definition_label = Label(
            text="Definition will appear here",
            markup=True,
            halign="center",
            valign="middle",
        )
        self.definition_box.add_widget(self.definition_label)

        search_button = Button(text="Search", on_release=self.lookup_word)
        history_button = Button(text="History", on_release=self.show_history)

        self.word_history = {}

        layout.add_widget(self.word_input)
        layout.add_widget(search_button)
        layout.add_widget(self.definition_box)
        layout.add_widget(history_button)

        return layout

    def lookup_word(self, instance):
        word = self.word_input.text.lower()

        # Simulated word database
        word_database = {
            'apple': 'A round fruit with red or green skin and sweet flesh.',
            'kivy': 'An open-source Python library for developing multitouch applications.',
            'python': 'A high-level programming language known for its readability.',
        }

        word_info = word_database.get(word, None)
        if word_info:
            self.definition_label.text = f'[b]Definition:[/b]\n{word_info}'
            self.word_history[word] = word_info

    def show_history(self, instance):
        history_text = "\n\n".join(f"[b]{word}[/b]: {definition}" for word, definition in self.word_history.items())
        if not history_text:
            history_text = "No history available."
        self.definition_label.text = history_text

if __name__ == '__main__':
    WordsApp().run()
