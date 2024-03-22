"""
Microbits

Líam Jara 5/06/21 20:30 hasta 22:30
Codigo de la interfaz de rubros



"""


from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


floatlayout = FloatLayout()


floatlayout.add_widget(Label(
    text="Registro de rubros",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='30sp',
    size_hint=(1, .1),
    pos_hint={'x': 0, 'y': .90}
))



floatlayout.add_widget(Label(
    text="Rubro:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .65}

))

floatlayout.add_widget(Label(
    text="Descripcion:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .55}
))







Rubro = TextInput(
    size_hint=(0.5, .05),
    multiline=False,
    hint_text="Rubro",
    pos_hint={'x': .35, 'y': .68}
)

Descripcion = TextInput(
    size_hint=(0.4, .35),
    multiline=True,
    hint_text="Descripcion",
    pos_hint={'x': .35, 'y': .28},
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

btn2 = Button(
    text="Eliminar",
    size_hint=(0.15, .05),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .55, 'y': .05}
)

floatlayout.add_widget(Rubro)
floatlayout.add_widget(Descripcion)
floatlayout.add_widget(btn)
floatlayout.add_widget(btn1)
