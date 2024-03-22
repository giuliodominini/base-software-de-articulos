from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


floatlayout = FloatLayout()

floatlayout.add_widget(Label(
	text="Register Supplier",
	color=(1, 1, 1, 1),
	#font_name="minha_fonte.ttf",
	font_size='30sp',
	size_hint=(1, .1),
	pos_hint={'x': 0, 'y': .90}
))

floatlayout.add_widget(Label(
	text="ID_Proveedor:",
	color=(1, 1, 1, 1),
	#font_name="minha_fonte.ttf",
	font_size='20sp',
	size_hint=(0.4, .1),
	pos_hint={'x': 0, 'y': .80}
))

floatlayout.add_widget(Label(
	text="business name:",
	color=(1, 1, 1, 1),
	#font_name="minha_fonte.ttf",
	font_size='20sp',
	size_hint=(0.4, .1),
	pos_hint={'x': 0, 'y': .70}
))
floatlayout.add_widget(Label(
	text="Address:",
	color=(1, 1, 1, 1),
	#font_name="minha_fonte.ttf",
	font_size='20sp',
	size_hint=(0.4, .1),
	pos_hint={'x': 0, 'y': .60}
))
floatlayout.add_widget(Label(
	text="Tel:",
	color=(1, 1, 1, 1),
	#font_name="minha_fonte.ttf",
	font_size='20sp',
	size_hint=(0.4, .1),
	pos_hint={'x': 0, 'y': .50}
))
floatlayout.add_widget(Label(
	text="Nombre_Contac:",
	color=(1, 1, 1, 1),
	#font_name="minha_fonte.ttf",
	font_size='20sp',
	size_hint=(0.4, .1),
	pos_hint={'x': 0, 'y': .40}
))
floatlayout.add_widget(Label(
	text="Celular_Contac:",
	color=(1, 1, 1, 1),
	#font_name="minha_fonte.ttf",
	font_size='20sp',
	size_hint=(0.4, .1),
	pos_hint={'x': 0, 'y': .30}
))
floatlayout.add_widget(Label(
	text="Email:",
	color=(1, 1, 1, 1),
	#font_name="minha_fonte.ttf",
	font_size='20sp',
	size_hint=(0.4, .1),
	pos_hint={'x': 0, 'y': .20}
))
floatlayout.add_widget(Label(
	text="CUIT:",
	color=(1, 1, 1, 1),
	#font_name="minha_fonte.ttf",
	font_size='20sp',
	size_hint=(0.4, .1),
	pos_hint={'x': 0, 'y': .10}
))
floatlayout.add_widget(Label(
	text="CBU:",
	color=(1, 1, 1, 1),
	#font_name="minha_fonte.ttf",
	font_size='20sp',
	size_hint=(0.4, .1),
	pos_hint={'x': .40, 'y': .10}
))
txt_codigo = TextInput(
	size_hint=(0.4,.05),
	multiline=False,
	hint_text="Codigo",
	pos_hint={'x': .30, 'y': .83}
)
txt_razon = TextInput(
	size_hint=(0.4,.05),
	multiline=False,
	hint_text="Razon Social",
	pos_hint={'x': .30, 'y': .73}
)
txt_direccion = TextInput(
	size_hint=(0.4,.05),
	multiline=False,
	hint_text="Direccion",
	pos_hint={'x': .30, 'y': .63}
)
txt_telefono= TextInput(
	size_hint=(0.4,.05),
	multiline=False,
	hint_text="Telefono",
	pos_hint={'x': .30, 'y': .53}
)
txt_nombre_contac = TextInput(
	size_hint=(0.4,.05),
	multiline=False,
	hint_text="Nombre_Contac",
	pos_hint={'x': .30, 'y': .43}
)
txt_celular_contac = TextInput(
	size_hint=(0.4,.05),
	multiline=False,
	hint_text="Celular_Contac",
	pos_hint={'x': .30, 'y': .33}
)
txt_email= TextInput(
	size_hint=(0.4,.05),
	multiline=False,
	hint_text="Email",
	pos_hint={'x': .30, 'y': .23}
)
txt_cuit= TextInput(
	size_hint=(0.20,.05),
	multiline=False,
	hint_text="cuit",
	pos_hint={'x': .25, 'y': .13}
)
txt_cbu= TextInput(
	size_hint=(0.20,.05),
	multiline=False,
	hint_text="cbu",
	pos_hint={'x': .65, 'y': .13}
)
btn_agregar= Button(
	text="Agregar",
	size_hint=(0.15, .05),
	background_color=(.5, 1.6, 3, .8),
	pos_hint={'x': .2, 'y': .02}
)
btn_volver= Button(
	text="Volver",
	size_hint=(0.15, .05),
	background_color=(.5, 1.6, 3, .8),
	pos_hint={'x': .55, 'y': .02}
)


floatlayout.add_widget(txt_codigo)
floatlayout.add_widget(txt_razon)
floatlayout.add_widget(txt_direccion)
floatlayout.add_widget(txt_telefono)
floatlayout.add_widget(txt_nombre_contac)
floatlayout.add_widget(txt_celular_contac)
floatlayout.add_widget(txt_email)
floatlayout.add_widget(txt_cuit)
floatlayout.add_widget(txt_cbu)
floatlayout.add_widget(btn_agregar)
floatlayout.add_widget(btn_volver)