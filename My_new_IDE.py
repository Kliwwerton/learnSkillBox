# -*- coding: utf-8 -*-

# import tkinter as tk
#
# window = tk.Tk()
# window.mainloop()

from kivy.app import App
from kivy.uix.label import Label


class My_windowApp(App):
    def build(self):
        label = Label(text='Hello kivy')
        return label


my_window = My_windowApp()

my_window.run()
