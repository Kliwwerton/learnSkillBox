# -*- coding: utf-8 -*-

# import tkinter as tk
#
# window = tk.Tk()
# window.mainloop()

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


def on_press_button(instance):
    print('Вы нажали на кнопку!')


class My_windowApp(App):
    def build(self):
        layout = BoxLayout(padding=20)
        label = Label(text='Привет Китти',
                      size_hint=(0.2, 0.2),
                      pos_hint={'center_x': 0.1, 'center_y': 0.5})

        btn = Button(text='Press Me',
                     size_hint=(0.2, 1),
                     pos_hint={'center_x': 0.5, 'center_y': 0.5},
                     background_color=[1, 0, 0, 1])

        layout.add_widget(label)
        layout.add_widget(btn)
        btn.bind(on_press=on_press_button)

        return layout


if __name__ == '__main__':
    my_window = My_windowApp()
    my_window.run()
