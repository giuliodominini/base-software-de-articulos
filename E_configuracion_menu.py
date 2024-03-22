#from kivy.logger import ColoredFormatter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button



boxlayout = BoxLayout(
    orientation="vertical",
    spacing=20,
    padding=50,
    )

boxlayout.add_widget(Label(
    text="CONFIGURACION",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='50sp',
    size_hint=(1, .1),
    pos_hint={'x': 0, 'y': .90}
))



btn_idioma = Button(
    text="Idioma",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
    )

btn_2 = Button(
    text="Null",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
    )


btn_3 = Button(
    text="Null",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
    )
btn_volver = Button(
    text="Volver",
    size_hint=(0.15, .05),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .55, 'y': .05}
)




boxlayout.add_widget(btn_idioma)
boxlayout.add_widget(btn_2)
boxlayout.add_widget(btn_3)
boxlayout.add_widget(btn_volver)
