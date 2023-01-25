# -*- coding: utf-8 -*-

# import tkinter as tk
#
# window = tk.Tk()
# window.mainloop()

from kivy.app import App
from kivy import Config
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

Config.set('graphics', 'width', 1000)
Config.set('graphics', 'height', 800)


class My_popup(Popup):
    size_hint = 0.8, 0.2

    content = BoxLayout()
    # button = Button(text='Закрой меня!',
    #                  size_hint=(0.5, 0.3),
    #                  pos_hint={'x': 0.5, 'y': 0.2})
    # content.add_widget(button)


def on_press_button(a):
    new_window = My_popup(title='Расчёт давления прессования')
    button = Button(text='Hello', size_hint=(0.5, 0.2))
    new_window.content.add_widget(button)
    button.bind(on_release=new_window.dismiss)

    # new_window.size_hint = 0.6, 0.2
    # new_window.button = Button(text="Hello", size_hint=(0.5, 0.1), pos_hint={'x': 0.5, 'y': 0.1})

    # new_window.add_widget(new_window.button)
    new_window.open()
    print('Вы нажали на кнопку! РАСЧЁТ ДАВЛЕНИЯ ПРЕССОВАНИЯ')


def on_press_button_2(a):
    print('Вы нажали на кнопку 2!')


def on_press_button_3(a):
    print('Вы нажали "СПРАВОЧНИКИ"!')


def on_press_button_4(a):
    print('Вы нажали на кнопку "Нормативы"!')


class My_windowApp(App):
    def build(self):
        layout = BoxLayout(padding=50, orientation='vertical')
        label = Label(text='Привет Юный ИНЖЕНЕР!', font_size=55,
                      size_hint=(0.2, 0.1),
                      pos_hint={'center_x': 0.5, 'center_y': 1})

        btn = Button( font_size=25,
                     size_hint=(0.6, 0.1),
                     pos_hint={'center_x': 0.5, 'center_y': 0.5},
                     background_color=[0.5, 1, 1, 1],
                     text=f'{"Расчёт давления прессования"}')
        btn_2 = Button(text='Расчёт химического состава',
                       size_hint=(0.6, 0.1),
                       pos_hint={'center_x': 0.5, 'center_y': 0.5},
                       background_color=[0.5, 1, 0.5, 1])
        btn_3 = Button(text='Справочник\n(ГОСТы, Классы шамота',
                       size_hint=(0.6, 0.1), font_size=25,
                       pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btn_4 = Button(text='Нормативы брака (по переделам)',
                       font_size=25,
                       size_hint=(0.6, 0.1),
                       pos_hint={'center_x': 0.5, 'center_y': 0.5})

        layout.add_widget(label)
        layout.add_widget(btn)
        layout.add_widget(btn_2)
        layout.add_widget(btn_3)
        layout.add_widget(btn_4)
        btn.bind(on_press=on_press_button)
        btn_2.bind(on_press=on_press_button_2)
        btn_3.bind(on_press=on_press_button_3)
        btn_4.bind(on_press=on_press_button_4)


        return layout


if __name__ == '__main__':
    my_window = My_windowApp(title='Я ИНЖЕНЕР!')
    my_window.run()
