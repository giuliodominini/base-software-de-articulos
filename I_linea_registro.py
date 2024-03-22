from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


floatlayout= FloatLayout()


floatlayout.add_widget(Label(
	text="Line registration",
	color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='30sp',
    size_hint=(1, .1),
    pos_hint={'x': 0, 'y': .90}
))


floatlayout.add_widget(Label(
    text="Name:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .55}
))
floatlayout.add_widget(Label(
    text="Description:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .45}
))





Descripcion= TextInput(
    size_hint=(0.4, .2),
    multiline=True,
    hint_text="Description",
    pos_hint={'x': .35, 'y': .32},
    input_type='number'
)
nombre= TextInput(
    size_hint=(0.4, .05),
    multiline=True,
    hint_text="Name",
    pos_hint={'x': .35, 'y': .58},
    input_type='number'
)


btn = Button(
    text="Save",
    size_hint=(0.15, .05),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .2, 'y': .05}
)

btn1 = Button(
    text="Back",
    size_hint=(0.15, .05),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .55, 'y': .05}
)


floatlayout.add_widget(Descripcion)
floatlayout.add_widget(nombre)
floatlayout.add_widget(btn)
floatlayout.add_widget(btn1)