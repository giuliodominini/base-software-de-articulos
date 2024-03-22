from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

floatlayout = FloatLayout()
floatlayout.add_widget(Label(
    text="Terminos y Condiciones",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='30sp',
    size_hint=(1, .1),
    pos_hint={'x': 0, 'y': .90}
))

terminos_condiciones = TextInput(
	text="""AL INSTALAR, COPIAR O, EN CUALQUIER CASO, UTILIZAR EL SOFTWARE SE CONSIDERA QUE USTED ESTÁ DE ACUERDO CON LOS TÉRMINOS Y CONDICIONES DE ESTE DOCUMENTO.
		El usuario adquiere solamente el derecho a usarlo libremente en su sistema informático, con las únicaslimitaciones que se detallan a continuación en este documento:
		En ningún caso esta licencia implica la cesión del derecho de propiedad sobre el software, por lo que el usuario no podrá proceder a su redistribución, venta, o modificación del código interno del programa mediante ingeniería inversa o por cualquier otro procedimiento, sin la autorización expresa y por escrito del autor.
		La licencia es exclusiva y no transferible a terceros, es indefinida en el tiempo, y da derecho a instalar el programa en un único ordenador, o en un único grupo de ordenadores interconectados entre sí en una red de área local y compartiendo necesariamente los datos de usuario cuando la versión ofrecida contemple esta función.
		La instalación del Software en otro equipo o en otra red local siempre es posible a condición de que se siga el proceso completo de desinstalación, empezando por el panel de control de Windows, sección «Agregar o quitar programas», en el ordenador u ordenadores de red donde hubiera estado instalado anteriormente, y eliminando después físicamente del disco todos los ficheros del programa.
		La licencia es efectiva hasta su cancelación. La cancelación se producirá automáticamente sin recibir notificación expresa de Microbits en el caso de no cumplirse alguna de las condiciones previstas en esta licencia.  En ningún caso se realizará devolución de montos pagados cuando el número de serie de habilitación haya sido expedido.  A los fines de evitar malos entendidos, Microbits ofrece la posibilidad de probar el software antes de solicitar el número de serie de habilitación.
		Microbits garantiza el buen funcionamiento del sistema ofrecido.
		Ante la imposibilidad material de poner a prueba el programa en la gran variedad de ordenadores existente, con todos los sistemas operativos y sus diferentes versiones y actualizaciones en circulación, y en interacción con las múltiples configuraciones particulares y de red local que en la práctica pueden hallarse, Microbits considera que es el propio usuario quien – en todo caso – debe cerciorarse previamente, mediante el uso o la prueba a fondo antes de la compra, de la completa idoneidad del software a las circunstancias específicas de su equipo informático, de su red, y de su empresa, y que, en un supuesto afirmativo, el cliente acepta el programa TAL CUAL, sin derecho a exigir ningún tipo de modificación que no haya sido pactada con anterioridad.
		DATOS DE REGISTRO PARA EMISIÓN DE LICENCIA DE HABILITACIÓN
		Microbits solicitará datos de registro para poder emitir la Licencia de Habilitación Definitiva del software.  Es EXCLUSIVA RESPONSABILIDAD DEL USUARIO informar datos comerciales correspondientes a su actividad, tomando en cuenta que ciertos datos como teléfono, correo electrónico o razón social podrán ser asignados automáticamente en reportes o comprobantes fiscales.   Los datos de registro enviados para solicitar el número de serie de habilitación NO PODRÁN SER MODIFICADOS en caso de errores u omisiones una vez emitido el serial, razón por la cual el Usuario deberá prestar especial atención antes de realizar el envío.  Para CORRECCIONES POSTERIORES A LA EMISIÓN DE LA LICENCIA DE USO, se deberá abonar nuevamente por la misma ya que se generará una nueva licencia.
		RESPONSABILIDAD ANTE FALLAS
		En caso de contener la aplicación algún error, Microbits se compromete a resolverlo a la mayor brevedad de tiempo posible, pero no se responsabilizará de los daños directos o indirectos, consecuencia de la utilización o imposibilidad de utilización de la aplicación, incluida la pérdida de datos que eventualmente pudiera producirse con ocasión de, o en relación con, el uso del software autorizado.   La posibilidad ofrecida al Usuario de PROBAR ANTES DE COMPRAR, minimiza los riesgos de encontrarse con fallas que pudieran complicar la puesta en marcha.
		RESPONSABILIDAD SOBRE LOS DATOS
		La integridad y conservación de los ficheros de datos corre por cuenta exclusiva del usuario, quien deberá obtener y mantener una copia de seguridad por lo menos una vez al día.  Para facilitar la realización de copias se seguridad, el software centraliza todos los datos en una única carpeta.
		El Usuario deberá mantener a resguardo el correo electrónico recibido con el número de serie de habilitación del software, para aquellos casos en que, por roturas o cambios de equipo, se deba volver a reinstalar.
		Microbits mantendrá los datos a resguardo durante un año calendario y podrán ser solicitados enviando un correo electrónico «exclusivamente» desde la dirección de correo registrada.   Cualquier solicitud enviada desde otra casilla de correo electrónico que no sea la registrada, será desestimada.
		En caso que se solicite el reenvío de datos de registro, pasado el año calendario, se deberá abonar una nueva licencia para obtenerlos.
		ALCANCES DE LA RESPONSABILIDAD DE MICROBITS
		La responsabilidad de Microbits estará limitada a la substitución del programa defectuoso o , como máximo, la implementación de una nueva versión sin cargo, siempre en un plazo de 30 días a partir de la fecha de compra. Esta garantía limitada será nula si el defecto del software es resultado de accidente, abuso o utilización incorrecta.
		DERECHO DEL USUARIO DE PROBAR ANTES DE COMPRAR
		Para una mayor seguridad acerca de la aplicación, el Usuario cuenta con la posibilidad de descargar el software en modo DEMOSTRACIÓN sin que sea necesario abonar nada por este servicio. Microbits recomienda que el Usuario haga uso de este derecho, para evitar malos entendidos y realizar la compra estando plenamente seguro.
		REINTEGROS DE DINERO POR INCONFORMIDAD DEL USUARIO
		Contando el Usuario con la posibilidad de PROBAR ANTES DE COMPRAR y de realizar todas las consultas que estime necesarias, se considera inviable la posibilidad de reintegros de dinero por disconformidad, errores de interpretación o por diversos motivos que lleven al Usuario a no utilizar la aplicación. Bajo ninguna circunstancia se realizarán reintegros de dinero por Licencias abonadas cuando el número de serie de habilitación haya sido expedido.
		En aquellos casos que se solicite devolución de dinero por Compras Abonadas sin que el número de serie de habilitación haya sido expedido, las devoluciones de generarán dentro de los 60 días de solicitadas por un monto equivalente al importe de la compra menos un 20% (veinte por ciento) en concepto de gastos de pasarela de pagos.
		SOPORTE TÉCNICO POST VENTA
		El Soporte al Usuario se realizará ingresando al área exclusiva de CLIENTES, para lo cual el Usuario deberá registrarse en el sitio para obtener su Usuario y Password de acceso. 
		Las respuestas a Tickets de asistencia serán respondidas según su plan de Asistencia, dentro de las 48 horas hábiles, 24 horas hábiles o 24 horas (hábiles o no). 
		ATENCIÓN PERSONALIZADA
		La atención a Usuarios por DUDAS o CONSULTAS SIMPLES previas a la compra, se podrá realizar por correo electrónico (ovandogiulio.00@gmail.com) de lunes a viernes de 9:00 a 12:00 Hs.  Microbits ofrece comunicación telefónica al 351-6966161.
		Las consultas por Correo Electrónico que no impliquen asistencia técnica, se responderán sólo cuando los tiempos lo permitan dentro del horario de atención.  Las consultas relacionadas con asistencia técnicas se derivarán al Servicio de Asistencia.
		""",
    size_hint=(.90, .79),
    multiline=True,
    pos_hint={'x': .05, 'y': .13},
    readonly= True,
   

)


floatlayout.add_widget(Label(
    text="Acepta Terminos y Condiciones:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .05}
))




desp_fix = CheckBox(
    size_hint=(0.27, .04),
    pos_hint={'x': .35, 'y': .08}
)



btn_siguiente = Button(
    text="Siguiente",
    size_hint=(0.15, .05),
    background_color=("9ACD32"),
    pos_hint={'x': .85, 'y': .03}
)



floatlayout.add_widget(terminos_condiciones)
floatlayout.add_widget(desp_fix)

floatlayout.add_widget(btn_siguiente)