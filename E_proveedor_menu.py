from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


boxlayout = BoxLayout(
    orientation="vertical",
    spacing=20,
    padding=50
    )

boxlayout.add_widget(Label(
    text="PROVEEDOR",
    color=(1, 1, 1, 1),
    font_size='50sp',
    size_hint=(1, .1),
    pos_hint={'x': 0, 'y': .70}
))


btn_cargar_prov=Button(
    text="Cargar Proveedor ",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
    )


btn_eliminar_prov = Button(
    text="Modifica, Eliminar",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
    )
btn_lista_prov = Button(
    text="listas ",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
    )

btn_volver = Button(
    text="Volver",
    size_hint=(0.15, .05),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .55, 'y': .05}
	)


boxlayout.add_widget(btn_cargar_prov)
boxlayout.add_widget(btn_eliminar_prov)
boxlayout.add_widget(btn_lista_prov)
boxlayout.add_widget(btn_volver)
