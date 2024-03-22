from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button



floatlayout = FloatLayout()


floatlayout.add_widget(Label(
    text="Modify",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='30sp',
    size_hint=(1, .1),
    pos_hint={'x': 0, 'y': .90}
))



floatlayout.add_widget(Label(
    text="Bussines name:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .65}

))

floatlayout.add_widget(Label(
    text="Adress:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .55}
))


floatlayout.add_widget(Label(
    text="Tel:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .45}
))


floatlayout.add_widget(Label(
    text="Contact name:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .35}
))

floatlayout.add_widget(Label(
    text="Phone Contact:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .25}
))


floatlayout.add_widget(Label(
    text="Mail:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .15}
))

lbl = Label(
    text="",
    font_size='20sp',
    color=(1, 1, 1, 1),
    size_hint=(0.6, .1),
    pos_hint={'x': 0, 'y': .75}
)



razon_social = TextInput(
    size_hint=(0.5, .05),
    multiline=False,
    hint_text="Bussines name",
    pos_hint={'x': .35, 'y': .68}
)

direccion = TextInput(
    size_hint=(0.4, .05),
    multiline=False,
    hint_text="address",
    pos_hint={'x': .35, 'y': .58},
    input_type='number'
)


numero = TextInput(
    size_hint=(0.4, .05),
    multiline=False,
    hint_text="number",
    pos_hint={'x': .35, 'y': .48}
)


nombre_contac = TextInput(
    size_hint=(0.4, .05),
    multiline=False,
    hint_text="Contact name",
    pos_hint={'x': .35, 'y': .38}
)

txt_celu = TextInput(
    size_hint=(0.4, .05),
    multiline=False,
    hint_text="Phone Contact",
    pos_hint={'x': .35, 'y': .28}

    )

txt_mail1 = TextInput(
    size_hint=(0.4, .05),
    multiline=False,
    hint_text="Mail",
    pos_hint={'x': .35, 'y': .18}

    )


btn_guardar = Button(
    text="Save ",
    size_hint=(0.25, .1),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .2, 'y': .05}
)

btn_cancel = Button(
    text="Cancel",
    size_hint=(0.25, .1),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .55, 'y': .05}
)

btn_eliminar = Button(
    text="Delete",
    size_hint=(0.25, .05),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .40, 'y': .777}
)




floatlayout.add_widget(lbl)
floatlayout.add_widget(razon_social)
floatlayout.add_widget(nombre_contac)
floatlayout.add_widget(direccion)
floatlayout.add_widget(numero)
floatlayout.add_widget(txt_celu)
floatlayout.add_widget(txt_mail1)
floatlayout.add_widget(btn_guardar)
floatlayout.add_widget(btn_cancel)
floatlayout.add_widget(btn_eliminar)



FloatLayout()