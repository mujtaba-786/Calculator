import math
import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.gridlayout import GridLayout

class CalGridLayo(GridLayout):

    Builder.load_file(r'C:\Users\Mohd  Mujtaba\AppData\Roaming\JetBrains\PyCharm2020.2\scratches\main.kv')

    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = 'Error'
class MyfirstApp(App):

    def build(self):

        return CalGridLayo()





if __name__=='__main__':
    MyfirstApp().run()




