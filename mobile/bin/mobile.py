import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.togglebutton import ToggleButton

kivy.require('1.11.1')

class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical')

        self.info_label = Label(
            text="Created by PyGeniusGithub. Kivy framework used for development. Still in alpha tests!",
            opacity=0,
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.info_label)

        self.new_file_button = Button(
            text="Create New File",
            size_hint=(0.5, 0.1)
        )
        self.new_file_button.bind(on_press=self.create_new_file)
        self.layout.add_widget(self.new_file_button)

        self.add_widget(self.layout)

        # Show the info label with animation
        self.show_info_label()

    def show_info_label(self):
        self.animation = Animation(opacity=1, duration=1.5)
        self.animation.bind(on_complete=lambda *args: self.hide_info_label())
        self.animation.start(self.info_label)

    def hide_info_label(self):
        Clock.schedule_once(self.create_new_file, 5)
        Animation(opacity=0, duration=1.5).start(self.info_label)

    def create_new_file(self, *args):
        self.manager.current = 'text_editor'
        self.manager.get_screen('text_editor').load_text('')

class TextEditor(Screen):
    def __init__(self, **kwargs):
        super(TextEditor, self).__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical')
        self.text_input = TextInput(
            multiline=True,
            font_name='Arial',  # Example font name
            font_size=16,  # Example font size
        )
        self.layout.add_widget(self.text_input)

        self.format_bold_button = ToggleButton(
            text='Bold',
            group='formatting',
            size_hint=(None, None),
            size=(100, 50)
        )
        self.format_bold_button.bind(on_press=self.toggle_bold)
        self.layout.add_widget(self.format_bold_button)

        self.format_italic_button = ToggleButton(
            text='Italic',
            group='formatting',
            size_hint=(None, None),
            size=(100, 50)
        )
        self.format_italic_button.bind(on_press=self.toggle_italic)
        self.layout.add_widget(self.format_italic_button)

        self.save_button = Button(
            text="Save",
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.5}
        )
        self.save_button.bind(on_press=self.save_file)
        self.layout.add_widget(self.save_button)

        self.main_menu_button = Button(
            text="Main Menu",
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.5}
        )
        self.main_menu_button.bind(on_press=self.main_menu)
        self.layout.add_widget(self.main_menu_button)

        self.add_widget(self.layout)

    def load_text(self, content):
        self.text_input.text = content

    def toggle_bold(self, instance):
        if instance.state == 'down':
            self.text_input.bold = True
        else:
            self.text_input.bold = False

    def toggle_italic(self, instance):
        if instance.state == 'down':
            self.text_input.italic = True
        else:
            self.text_input.italic = False

    def save_file(self, instance):
        content = self.text_input.text
        # You can add saving logic here

    def main_menu(self, instance):
        self.manager.current = 'main_menu'

class TextEditorApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainMenu(name='main_menu'))
        screen_manager.add_widget(TextEditor(name='text_editor'))
        return screen_manager

if __name__ == '__main__':
    TextEditorApp().run()
