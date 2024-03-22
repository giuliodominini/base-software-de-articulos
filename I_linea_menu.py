from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

boxlayout = BoxLayout(
    orientation="vertical",
    spacing=20,
    padding=50,
)

boxlayout.add_widget(Label(
    text="LINE",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='50sp',
    size_hint=(1, .1),
    pos_hint={'x': 0, 'y': .90}
))


btn_nuevo_linea = Button(
    text="line registre",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
)

btn_eliminar = Button(
    text="Modify, delete or Query",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
)


btn_listas = Button(
    text="list",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
)
btn_volver1 = Button(
    text="back",  # volver
    size_hint=(0.15, .05),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .55, 'y': .05}
)


boxlayout.add_widget(btn_nuevo_linea)
boxlayout.add_widget(btn_eliminar)
boxlayout.add_widget(btn_listas)
boxlayout.add_widget(btn_volver1)
