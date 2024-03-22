from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button

floatlayout = FloatLayout()

floatlayout.add_widget(Label(
    text="Seleccione Idioma",
    font_name="minha_fonte.ttf",
    color=(0, 0, 0, 1),
    font_size='30sp',
    size_hint=(1, .1),
    pos_hint={'x': 0, 'y': .85}
))

spn_idioma = Spinner(
    text="Idioma",
    size_hint=(0.25, .1),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .36, 'y': .53},
    values=["Español", "Ingles"]
)

btn_ok = Button(
    text="Siguiente",
    size_hint=(0.25, .1),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .36, 'y': .05}
)

floatlayout.add_widget(spn_idioma)
floatlayout.add_widget(btn_ok)
