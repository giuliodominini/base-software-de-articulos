from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button



floatlayout = FloatLayout()


floatlayout.add_widget(Label(
    text="Registro de Clientes",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='30sp',
    size_hint=(1, .1),
    pos_hint={'x': 0, 'y': .90}
))



floatlayout.add_widget(Label(
    text="Razon Social:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .80}

))

floatlayout.add_widget(Label(
    text="Direccion:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .70}
))


floatlayout.add_widget(Label(
    text="Tel:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .60}
))


floatlayout.add_widget(Label(
    text="Nombre del Contacto:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': -0.05, 'y': .50}
))

floatlayout.add_widget(Label(
    text="Celular del Contacto:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': -0.05, 'y': .40}
))


floatlayout.add_widget(Label(
    text="Mail:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .30}
))

floatlayout.add_widget(Label(
    text="Tipo de cliente:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': .0, 'y': .20}
))


floatlayout.add_widget(Label(
    text="CBU:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': -0.05, 'y': .10}
))

floatlayout.add_widget(Label(
    text="CUIT:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': .35, 'y': .10}
))



razon_social = TextInput(
    size_hint=(0.5, .05),
    multiline=False,
    hint_text="Razon Social",
    pos_hint={'x': .30, 'y': .83}
)

direccion = TextInput(
    size_hint=(0.4, .05),
    multiline=False,
    hint_text="Direccion",
    pos_hint={'x': .30, 'y': .73}
)




numero = TextInput(
    size_hint=(0.4, .05),
    multiline=False,
    hint_text="Numero",
    pos_hint={'x': .30, 'y': .63}
)


nombre_contac = TextInput(
    size_hint=(0.4, .05),
    multiline=False,
    hint_text="Nombre del Contacto",
    pos_hint={'x': .30, 'y': .53}
)

txt_celu = TextInput(
    size_hint=(0.4, .05),
    multiline=False,
    hint_text="Celular",
    pos_hint={'x': .30, 'y': .43}

    )

txt_mail1 = TextInput(
    size_hint=(0.4, .05),
    multiline=False,
    hint_text="Mail",
    pos_hint={'x': .30, 'y': .33}

    )



Tipo_cli = Spinner(
    text="Seleccione uno",
    values = ("Monotributista","Responsable inscripto"),
    size_hint=(0.25, .04),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .35, 'y': .23},

)

CBU_cli = TextInput(
    size_hint=(0.2, .05),
    multiline=False,
    hint_text="CBU",
    pos_hint={'x': .25, 'y': .13},
    input_type='number'
)

Cuit_cli = TextInput(
    size_hint=(0.2, .05),
    multiline=False,
    hint_text="CUIT",
    pos_hint={'x': .65, 'y': .13},
    input_type='number'
)

btn = Button(
    text="Agregar",
    size_hint=(0.15, .05),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .2, 'y': .05}
)

btn1 = Button(
    text="Volver",
    size_hint=(0.15, .05),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .55, 'y': .05}
)



floatlayout.add_widget(razon_social)
floatlayout.add_widget(nombre_contac)
floatlayout.add_widget(direccion)
floatlayout.add_widget(numero)
floatlayout.add_widget(txt_celu)
floatlayout.add_widget(txt_mail1)
floatlayout.add_widget(Tipo_cli)
floatlayout.add_widget(CBU_cli)
floatlayout.add_widget(Cuit_cli)
floatlayout.add_widget(btn)
floatlayout.add_widget(btn1)
