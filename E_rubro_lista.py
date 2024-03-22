"""
Giulio Dominini
Microbits
Eliman
Codigo general
"""
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

floatlayout=FloatLayout()



floatlayout.add_widget(Label(
	text= "Listas de Rubro",
	color=(1, 1, 1, 1),
	font_size='30sp',
	size_hint=(1, .1),
	pos_hint={'x': 0, 'y': .85}
))
btn_volver = Button(
    text="Volver",
    size_hint=(0.15, .05),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .70, 'y': .80}
)

scrollview = ScrollView(size_hint=(1, None),pos_hint={'x': 0, 'y': .05}, size=(Window.width, Window.height * 0.66))
gridlayout = GridLayout(cols=1, spacing=1, size_hint=(1,None))
gridlayout.bind(minimum_height=gridlayout.setter('height'))

floatlayout.add_widget(btn_volver)
floatlayout.add_widget(scrollview)
scrollview.add_widget(gridlayout)