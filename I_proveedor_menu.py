from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

############################################################
#######################    interfaz de entrada #############
boxlayout = BoxLayout(
    orientation="vertical",
    spacing=20,
    padding=50
    )

boxlayout.add_widget(Label(
    text="SUPPLIER",
    color=(1, 1, 1, 1),
    font_size='50sp',
    size_hint=(1, .1),
    pos_hint={'x': 0, 'y': .70}
))


btn_cargar_prov=Button(
    text="Register Supplier ",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
    )


btn_eliminar_prov = Button(
    text="Modify, delete or Query",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
    )
btn_lista_prov = Button(
    text="list ",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
    )

btn_volver = Button(
    text="Back",
    size_hint=(0.15, .05),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .55, 'y': .05}
	)


boxlayout.add_widget(btn_cargar_prov)
boxlayout.add_widget(btn_eliminar_prov)
boxlayout.add_widget(btn_lista_prov)
boxlayout.add_widget(btn_volver)

########################------------------------------------############