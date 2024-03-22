from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window



floatlayout= FloatLayout()


floatlayout.add_widget(Label(
	text="Supplier a query",
    color=(1, 1, 1, 1),
    font_size='30sp',
    size_hint=(1, .1),
    pos_hint={'x': 0, 'y': .85}
))

txt_busqueda = TextInput(
    multiline=False,
    size_hint=(0.6, .05),
    hint_text="Busque Aqui por Razon Social",
    pos_hint={'x': .15, 'y': .70}
)

btn_busqueda = Button(
    text="OK",
    size_hint=(0.09, .052),
    pos_hint={'x': .80, 'y': .697},
    background_color=(.5, 1.6, 3, .8)
)

btn_volver = Button(
    text="Back",
    size_hint=(0.15, .052),
    pos_hint={'x': .05, 'y': .80},
    background_color=(.5, 1.6, 3, .8)
)

scrollview = ScrollView(size_hint=(1, None), size=(Window.width, Window.height * 0.66))
gridlayout = GridLayout(cols=1, spacing=1, size_hint=(1, None))
gridlayout.bind(minimum_height=gridlayout.setter('height'))

floatlayout.add_widget(btn_volver)
floatlayout.add_widget(btn_busqueda)
floatlayout.add_widget(txt_busqueda)
floatlayout.add_widget(scrollview)
scrollview.add_widget(gridlayout)