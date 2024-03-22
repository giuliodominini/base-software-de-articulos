from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button

floatlayout = FloatLayout()

floatlayout.add_widget(Label(
    text="REGISTRO DE USUARIO",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='30sp',
    size_hint=(1, .1),
    pos_hint={'x': 0, 'y': .80}
))

floatlayout.add_widget(Label(
    text="Nombre de Usuario*:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .65}
))

floatlayout.add_widget(Label(
    text="Permiso de*:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .55}
))

floatlayout.add_widget(Label(
    text="Contrasena*:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .45}
))

floatlayout.add_widget(Label(
    text="Repetir Contrasena*:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .35}
))


floatlayout.add_widget(Label(
    text="Telefono*:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .25}
))

floatlayout.add_widget(Label(
    text="* campos obligatorios",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='15sp',
    size_hint=(0.4, .1),
    pos_hint={'x': .10, 'y': .15}
))


usuario = TextInput(
    size_hint=(0.4, .05),
    multiline=True,
    hint_text="Nombre de usuario",
    pos_hint={'x': .35, 'y': .68},
    input_type='number'
)

permiso = Spinner(
    text="Seleccione uno",
    size_hint=(0.25, .04),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .35, 'y': .58},
    values=["Administrador", "Empleado"]
)

contraseña = TextInput(
    size_hint=(0.4, .05),
    password=True,
    multiline=False,
    hint_text="Contraseña",
    pos_hint={'x': .35, 'y': .48}
)

contraseña1 = TextInput(
    size_hint=(0.4, .05),
    password=True,
    multiline=False,
    hint_text="Repetir Contraseña",
    pos_hint={'x': .35, 'y': .38}

)

telefono = TextInput(
    size_hint=(0.4, .05),
    multiline=False,
    hint_text="Telefono",
    pos_hint={'x': .35, 'y': .28}

)

btn_guardar = Button(
    text="Guardar",
    size_hint=(0.25, .1),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .2, 'y': .05}
)

btn_cancel = Button(
    text="Cancelar",
    size_hint=(0.25, .1),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .55, 'y': .05}
)

floatlayout.add_widget(usuario)
floatlayout.add_widget(permiso)
floatlayout.add_widget(contraseña)
floatlayout.add_widget(contraseña1)
floatlayout.add_widget(telefono)
floatlayout.add_widget(btn_guardar)
floatlayout.add_widget(btn_cancel)
