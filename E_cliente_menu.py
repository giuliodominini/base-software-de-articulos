from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button



boxlayout = BoxLayout(
    orientation="vertical",
    spacing=20,
    padding=50,
    )

boxlayout.add_widget(Label(
    text="CLIENTE",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='50sp',
    size_hint=(1, .1),
    pos_hint={'x': 0, 'y': .90}
))



btn_nuevo_cliente = Button(
    text="Cargar Cliente",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
    )

btn_eliminar = Button(
    text="Modifica, Eliminar o Consultar",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
    )


btn_listas = Button(
    text="Listas",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
    )
btn_volver1 = Button(
    text="Volver",
    size_hint=(0.15, .05),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .55, 'y': .05}
)




boxlayout.add_widget(btn_nuevo_cliente)
boxlayout.add_widget(btn_eliminar)
boxlayout.add_widget(btn_listas)
boxlayout.add_widget(btn_volver1)
