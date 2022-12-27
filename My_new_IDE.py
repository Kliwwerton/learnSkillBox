# -*- coding: utf-8 -*-

# import tkinter as tk
#
# window = tk.Tk()
# window.mainloop()

from kivy.app import App
# from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class My_windowApp(App):
    def build(self):
        layout = BoxLayout(padding=10)
        # label = Label(text='Hello kivy', size_hint=(1, 1))
        btn = Button(text='Press Me', background_color=[1, 0, 0, 1], )

        layout.add_widget(btn)
        return layout


if __name__ == '__main__':
    my_window = My_windowApp()
    my_window.run()
