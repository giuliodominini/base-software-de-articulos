"""
Giulio Dominini
Microbits
Eliman

"""
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button



floatlayout = FloatLayout()


floatlayout.add_widget(Label(
    text="Registro de Articulos",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='30sp',
    size_hint=(1, .1),
    pos_hint={'x': 0, 'y': .90}
))


floatlayout.add_widget(Label(
    text="Codigo :",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .77}

))

floatlayout.add_widget(Label(
    text="Articulo :",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .69}

))

floatlayout.add_widget(Label(
    text="Rubro:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': -0.05, 'y': .47}

))


floatlayout.add_widget(Label(
    text="Linea:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0.40, 'y': .47}

))

floatlayout.add_widget(Label(
    text="Descripcion:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .61}
))


floatlayout.add_widget(Label(
    text="Proveedor:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .54}
))


floatlayout.add_widget(Label(
    text="Stock:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': -0.15, 'y': .37}
))

floatlayout.add_widget(Label(
    text="Stock ideal:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0.15, 'y': .37}
))


floatlayout.add_widget(Label(
    text="Stock minimo:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0.5, 'y': .37}
))

floatlayout.add_widget(Label(
    text="Precio de compra:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': -0.05 ,'y': .26}
))

floatlayout.add_widget(Label(
    text="Precio de venta:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0.38, 'y': .26}
))

floatlayout.add_widget(Label(
    text="Fecha de la ultima compra:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .15}
))


codigo = TextInput(
    size_hint=(0.5, .05),
    multiline=False,
    hint_text="Articulo",
    pos_hint={'x': .35, 'y': .80}
)

articulo = TextInput(
    size_hint=(0.5, .05),
    multiline=False,
    hint_text="Articulo",
    pos_hint={'x': .35, 'y': .72}
)

Rubro = Spinner(
    text="Seleccione uno",
    size_hint=(0.25, .04),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .20, 'y': .50}
)

Linea = Spinner(
    text="Seleccione uno",
    size_hint=(0.25, .04),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .65, 'y': .50},

)

Descripcion = TextInput(
    size_hint=(0.5, .05),
    multiline=False,
    hint_text="Descripcion",
    pos_hint={'x': .35, 'y': .64},
    input_type='number'
)



Proveedor = Spinner(
    text="Seleccione uno",
    size_hint=(0.25, .04),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .35, 'y': .57},
)

Stock = TextInput(
    size_hint=(0.2, .05),
    multiline=False,
    hint_text="Stock disponible",
    pos_hint={'x': .09, 'y': .40},
    input_type='number'
)



Stock_ideal = TextInput(
    size_hint=(0.2, .05),
    multiline=False,
    hint_text="Stock ideal ",
    pos_hint={'x': .42, 'y': .40},
    input_type='number'
)


Stock_minimo = TextInput(
    size_hint=(0.2, .05),
    multiline=False,
    hint_text="Stock minimo ",
    pos_hint={'x': .77, 'y': .40},
    input_type='number'
)

Pre_compra = TextInput(
    size_hint=(0.2, .05),
    multiline=False,
    hint_text="precio de compra",
    pos_hint={'x': .25, 'y': .29},
    input_type='number'
)

Pre_venta = TextInput(
    size_hint=(0.2, .05),
    multiline=False,
    hint_text="Precio de venta",
    pos_hint={'x': .68, 'y': .29},
    input_type='number'
)

Fech_ult_comp = TextInput(
    size_hint=(0.5, .05),
    multiline=False,
    hint_text="DD/MM/YYYY",
    pos_hint={'x': .35, 'y': .17}
)

btn = Button(
    text="Agregar",
    size_hint=(0.15, .05),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .2, 'y': .05}
)

btn1 = Button(
    text="Volver",
    size_hint=(0.15, .05),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .55, 'y': .05}
)

floatlayout.add_widget(codigo)
floatlayout.add_widget(articulo)
floatlayout.add_widget(Rubro)
floatlayout.add_widget(Linea)
floatlayout.add_widget(Descripcion)
floatlayout.add_widget(Proveedor)
floatlayout.add_widget(Stock)
floatlayout.add_widget(Stock_ideal)
floatlayout.add_widget(Stock_minimo)
floatlayout.add_widget(Pre_compra)
floatlayout.add_widget(Pre_venta)
floatlayout.add_widget(Fech_ult_comp)
floatlayout.add_widget(btn)
floatlayout.add_widget(btn1)
