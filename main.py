from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner

from Admin.admin import AdminWindow
from Signin.signin import SigninWindow
from Operator.operators import OperatorWindow

class MainWindow(BoxLayout):

    admin_widget = AdminWindow()
    signin_widget = SigninWindow()
    operator_widget = OperatorWindow()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.scrn_si.add_widget(self.signin_widget)
        self.ids.scrn_admin.add_widget(self.admin_widget)
        self.ids.scrn_op.add_widget(self.operator_widget)

class MainApp(App):
    def build(self):

        return MainWindow()

if __name__=='__main__':
    MainApp().run()