from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        self.icon = "Logo.png"
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=5)
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55,
        )
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout(spacing=5)
            for label in row:
                if label == "C":
                    button = Button(text=label, font_size=25,
                                    background_color=[80/255, 232/255, 120/255, 0.8],
                                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    )
                    button.bind(on_press=self.on_button_press)
                    h_layout.add_widget(button)
                else:
                    button = Button(text=label, font_size=25,
                                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    )
                    button.bind(on_press=self.on_button_press)
                    h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(text="=",
                               pos_hint={"center_x": 0.5, "center_y": 0.5},
                               background_color=[1,0,0,1],
                               font_size=25,
                )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Очистка виджета с решением
            self.solution.text = ""
        else:
            if current and (
                    self.last_was_operator and button_text in self.operators):
                # Не добавляйте два оператора подряд, рядом друг с другом
                return
            elif current == "" and button_text in self.operators:
                # Первый символ не может быть оператором
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ == "__main__":
    CalculatorApp().run()
