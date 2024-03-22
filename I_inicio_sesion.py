from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button

floatlayout = FloatLayout()
floatlayout.add_widget(Label(
    text="Log in",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='30sp',
    size_hint=(1, .1),
    pos_hint={'x': 0, 'y': .80}
))

floatlayout.add_widget(Label(
    text="User name:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .55}
))

floatlayout.add_widget(Label(
    text="Permission of:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .45}
))

floatlayout.add_widget(Label(
    text="Password:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .35}
))


usuario = TextInput(
    size_hint=(0.4, .05),
    multiline=True,
    hint_text="User name",
    pos_hint={'x': .35, 'y': .58},
    input_type='number'
)

permiso = Spinner(
    text="select one",
    size_hint=(0.25, .04),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .35, 'y': .48},
    values=["Administrador", "Empleado"]
)

contraseña = TextInput(
    size_hint=(0.4, .05),
    password=True,
    multiline=False,
    hint_text="Password",
    pos_hint={'x': .35, 'y': .38}
)

btn_ingresar = Button(
    text="Enter",
    size_hint=(0.25, .1),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .2, 'y': .05}
)

btn_registro = Button(
    text="Sign",
    size_hint=(0.25, .1),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .55, 'y': .05}
)

floatlayout.add_widget(usuario)
floatlayout.add_widget(permiso)
floatlayout.add_widget(contraseña)
floatlayout.add_widget(btn_ingresar)
floatlayout.add_widget(btn_registro)
