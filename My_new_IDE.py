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


def on_press_button_2(instance):
    print('Вы нажали на кнопку 2!')


class My_windowApp(App):
    def build(self):
        layout = BoxLayout(padding=50)
        label = Label(text='Привет Китти',
                      size_hint=(0.2, 0.2),
                      pos_hint={'center_x': 0.1, 'center_y': 0.5})

        btn = Button(text='Press Me',
                     size_hint=(0.2, 0.25),
                     pos_hint={'center_x': 0.5, 'center_y': 0.5},
                     background_color=[0.5, 1, 1, 1])
        btn_2 = Button(text='Press my too',
                       size_hint=(0.2, 0.25),
                       pos_hint={'center_x': 0.7, 'center_y': 0.7},
                       background_color=[0.5, 1, 0.5, 1])

        layout.add_widget(label)
        layout.add_widget(btn)
        layout.add_widget(btn_2)
        btn.bind(on_press=on_press_button)
        btn_2.bind(on_press=on_press_button_2)

        return layout


if __name__ == '__main__':
    my_window = My_windowApp()
    my_window.run()
