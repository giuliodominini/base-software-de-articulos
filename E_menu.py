from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


boxlayout = BoxLayout(
    orientation="vertical",
    spacing=20,
    padding=50,
)

boxlayout.add_widget(Label(
    text="EL IMAN",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='50sp',
    size_hint=(1, .1),
    pos_hint={'x': 0, 'y': .90}
))


btn_articulos = Button(
    text="Articulos",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
)

btn_rubro = Button(
    text="Rubro y Linea",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
)

btn_provedores = Button(
    text="Provedores",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
)

btn_cliente = Button(
    text="Clientes",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
)

btn_configuracion = Button(
    text="Configuracion",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
)

btn_cerrar = Button(
    text="Cerrar Secion",
    size_hint=(0.25, .05),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .55, 'y': .05}
)

boxlayout.add_widget(btn_articulos)
boxlayout.add_widget(btn_rubro)
boxlayout.add_widget(btn_provedores)
boxlayout.add_widget(btn_cliente)
boxlayout.add_widget(btn_configuracion)
boxlayout.add_widget(btn_cerrar)
