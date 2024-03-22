"""
Giulio Dominini
Microbits
El iman

"""
import os
# paquetes
import sqlite3
from functools import partial       

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup, PopupException
from kivy.uix.screenmanager import (FadeTransition, RiseInTransition, Screen,
                                    ScreenManager, TransitionBase,
                                    WipeTransition)

# modulos
import base_dato as bd
import E_articulo_consulta as eac
import E_articulo_editar as eae
import E_articulo_insertar as eai
import E_articulo_lista as eal
import E_articulo_menu as eam
import E_cliente_consultar as ecc
import E_cliente_editar as ece
import E_cliente_insertar as eci
import E_cliente_lista as ecl
import E_cliente_menu as ecm
import E_configuracion_menu as eco
import E_inicio_sesion as eis
import E_linea_consultar as elc
import E_linea_editar as ele
import E_linea_lista as ell
import E_linea_menu as elm
import E_linea_registro as elr
import E_menu as em
import E_proveedor_consultar as epc
import E_proveedor_editar as epe
import E_proveedor_insertar as epi
import E_proveedor_lista as epl
import E_proveedor_menu as epm
import E_registro as er
import E_rubro_consulta as erc
import E_rubro_editar as ere
import E_rubro_insertar as eri
import E_rubro_linea as eryl
import E_rubro_lista as erl
import E_rubro_menu as erm
import E_seleccion_idioma as edi
import E_terminosycondiciones as etyc
import I_articulo_consulta as iac
import I_articulo_editar as iae
import I_articulo_insertar as iai
import I_articulo_lista as ial
import I_articulo_menu as iam
import I_cliente_consultar as icc
import I_cliente_editar as ice
import I_cliente_insertar as ici
import I_cliente_lista as icl
import I_cliente_menu as icm
import I_configuracion_menu as ico
import I_inicio_sesion as iis
import I_linea_consultar as ilc
import I_linea_lista as ill
import I_linea_menu as ilm
import I_linea_modificar as ile
import I_linea_registro as ilr
import I_menu as im
import I_proveedor_consultar as ipc
import I_proveedor_insertar as ipi
import I_proveedor_lista as ipl
import I_proveedor_menu as ipm
import I_proveedor_modificar as ipe
import I_registro as ir
import I_rubro_consulta as irc
import I_rubro_insertar as iri
import I_rubro_linea as iryl
import I_rubro_lista as irl
import I_rubro_menu as irm
import I_rubro_modificar as ire
import I_seleccion_idioma as idi
import I_terminosycondiciones as ityc

# declaracion de variables
sm = ScreenManager()

# ventanas emergente español
popup_verificacion = Popup(title="Error", content=Label(
    text='Acepte los terminos y condiciones!'), size_hint=(0.5, 0.2))

# ventanas emergente ingles
popup_verificacion1 = Popup(title="Error", content=Label(
    text='Accept the terms and conditions!'), size_hint=(0.5, 0.2))

# ventana emergente idioma
popup_idioma = Popup(title="Error", content=Label(
    text='Selecciones un idioma'), size_hint=(0.5, 0.2))

# ventana emergente registro español
pupup_blanco = Popup(title="Error", content=Label(
    text="Algun campo esta en blanco"), size_hint=(0.5, 0.2))
popup_contra_desigual = Popup(title="Error", content=Label(
    text="Contraseñas no coinciden"), size_hint=(0.5, 0.2))
popup_telefono = Popup(title="Error", content=Label(
    text="Telefono solo numero y sin espacio "), size_hint=(0.5, 0.2))
popup_registro_exito = Popup(title="Error", content=Label(
    text="Registrado con exito"), size_hint=(0.5, 0.2))

# ventana emergente registro ingles
pupup_blancoi = Popup(title="Error", content=Label(
    text="Some field is blank"), size_hint=(0.5, 0.2))
popup_contra_desiguali = Popup(title="Error", content=Label(
    text="Passwords do not match"), size_hint=(0.5, 0.2))
popup_telefonoi = Popup(title="Error", content=Label(
    text="Phone only number and without space "), size_hint=(0.5, 0.2))
popup_registro_exitoi = Popup(title="Error", content=Label(
    text="Successfully registered"), size_hint=(0.5, 0.2))

# ventana emergente de inicio español
popup_inicio_incorrectoe = Popup(title="Error", content=Label(
    text="Usuario incorrecto"), size_hint=(0.5, 0.2))

# ventana emergente de inicio ingles
popup_inicio_incorrectoi = Popup(title="Error", content=Label(
    text="incorrect user"), size_hint=(0.5, 0.2))

# ventana emergente solo numero español
popup_numero = Popup(title="Error", content=Label(
    text="Solo numeros en stock y precios"), size_hint=(0.5, 0.2))
# ventana emergente agregdo exitodamente
popup_agregado = Popup(title="Error", content=Label(
    text="Agregado exitosamente "), size_hint=(0.5, 0.2))
# ventana emregente  exitente
popup_articulo_exitente = Popup(title="Error", content=Label(
    text="Articulo ya existente "), size_hint=(0.5, 0.2))
popup_linea_exitente = Popup(title="Error", content=Label(
    text="Linea ya existente "), size_hint=(0.5, 0.2))
# ventana emergente eliminado
popup_elimina = Popup(title="Error", content=Label(
    text="Eliminado con exito "), size_hint=(0.5, 0.2))


# -------------------------Interfaces--------------------------------------------

# idioma


def cargar_idioma(self):
    global idi1
    idi1 = idi.spn_idioma.text
    if idi1 == "Español":
        terminos_español1(self)
    elif idi1 == "Ingles":
        terminos_ingles1(self)
    else:
        popup_idioma.open()


def idioma_elegido():
    elegido = str("Español")
    elegido = bd.consulta_idioma(elegido)
    if elegido == []:
        sm.add_widget(inicio_sesion_ingles)
    else:
        sm.add_widget(inicio_sesion_español)


pantalla_idioma1 = Screen(name="pantalla_idioma1")
pantalla_idioma1.add_widget(idi.floatlayout)
idi.btn_ok.bind(on_press=cargar_idioma)


# idioma 2
def idiomas(self):
    sm.switch_to(pantalla_idioma)


def editar_idioma(self):
    elegido = edi.spn_idioma.text
    idioma1 = edi.spn_idioma.text
    elegido = bd.consulta_idioma(elegido)
    bd.edita_idioma(idioma1)
    if idioma1 == "Ingles":
        sm.switch_to(menu_principal_ingles)
    else:
        sm.switch_to(menu_principal_español)


pantalla_idioma = Screen(name="pantalla_idioma")
pantalla_idioma.add_widget(edi.floatlayout)

# terminos y condiciones español


def verificacion(self):
    condiciones = etyc.desp_fix.active
    if condiciones == True:
        bd.idioma()
        bd.crear_base_usuario()
        bd.crear_base_articulo()
        bd.crear_base_proveedor()
        bd.crear_base_cliente()
        bd.crear_base_rubro()
        bd.crear_base_linea()
        bd.agregar_idioma(idi1)
        inicio_secion_e(self)
    else:
        popup_verificacion.open()


def terminos_español1(self):
    sm.switch_to(terminos_español, transition=FadeTransition())


terminos_español = Screen(name="terminos_español")
terminos_español.add_widget(etyc.floatlayout)


# terminos y condiciones ingles
def verificacion1(self):
    condiciones = ityc.desp_fix.active
    if condiciones == True:
        bd.idioma()
        bd.crear_base_usuario()
        bd.crear_base_articulo()
        bd.crear_base_proveedor()
        bd.crear_base_cliente()
        bd.crear_base_rubro()
        bd.crear_base_linea()
        bd.agregar_idioma(idi1)
        inicio_secion_i(self)
    else:
        popup_verificacion1.open()


def terminos_ingles1(self):
    sm.switch_to(terminos_ingles, transition=FadeTransition())


terminos_ingles = Screen(name="terminos_ingles")
terminos_ingles.add_widget(ityc.floatlayout)


# inicio de sesion español
def inicio_secion_e(self):
    sm.switch_to(inicio_sesion_español, direction="left")


def verificacion_registro_e(self):
    usuario = eis.usuario.text
    permiso = eis.permiso.text
    contra = eis.contraseña.text
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    cursor.execute(
        'SELECT * FROM registro WHERE Nombre = ? AND Contraseña = ? AND Permiso = ?', (usuario, contra, permiso))
    if usuario == "" or permiso == "Seleccione uno" or contra == "":
        pupup_blanco.open()
    elif cursor.fetchall():
        menu_principale(self)
    else:
        popup_inicio_incorrectoe.open()


inicio_sesion_español = Screen(name="inicio_sesion_español")
inicio_sesion_español.add_widget(eis.floatlayout)


# inicio de sesion ingles
def inicio_secion_i(self):
    sm.switch_to(inicio_sesion_ingles)


def verificacion_registro_i(self):
    usuario = iis.usuario.text
    permiso = iis.permiso.text
    contra = iis.contraseña.text
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    cursor.execute(
        'SELECT * FROM registro WHERE Nombre = ? AND Contraseña = ? AND Permiso = ?', (usuario, contra, permiso))
    if usuario == "" or permiso == "Select one" or contra == "":
        pupup_blanco.open()
    elif cursor.fetchall():
        menu_principali(self)
    else:
        popup_inicio_incorrectoi.open()


inicio_sesion_ingles = Screen(name="inicio_sesion_ingles")
inicio_sesion_ingles.add_widget(iis.floatlayout)

# registro español


def registro_español1(self):
    sm.switch_to(registro_español)


def registro(self):
    nombre = er.usuario.text
    permiso = er.permiso.text
    contra = er.contraseña.text
    contra1 = er.contraseña1.text
    telefono = er.telefono.text
    tel = telefono.isdigit()
    if nombre == "" or permiso == "Seleccione uno" or contra == "" or contra1 == "" or telefono == "":
        pupup_blanco.open()
    elif contra != contra1:
        popup_contra_desigual.open()
    elif tel == False:
        popup_telefono.open()
    else:
        bd.insertar_usuario(str(nombre), str(permiso),
                            str(contra), str(telefono))
        popup_registro_exito.open()


registro_español = Screen(name="registro_españo")
registro_español.add_widget(er.floatlayout)

# registro ingles


def registro_ingles1(self):
    sm.switch_to(registro_ingles, direction="left")


def registroi(self):
    nombre = ir.usuario.text
    permiso = ir.permiso.text
    contra = ir.contraseña.text
    contra1 = ir.contraseña1.text
    telefono = ir.telefono.text
    tel = telefono.isdigit()
    if nombre == "" or permiso == "Select one" or contra == "" or contra1 == "" or telefono == "":
        pupup_blancoi.open()
    elif contra != contra1:
        popup_contra_desiguali.open()
    elif tel == False:
        popup_telefonoi.open()
    else:
        bd.insertar_usuario(str(nombre), str(permiso),
                            str(contra), str(telefono))
        popup_registro_exitoi.open()


registro_ingles = Screen(name="registro_ingles")
registro_ingles.add_widget(ir.floatlayout)


# menu principal español
def menu_principale(self):
    sm.switch_to(menu_principal_español)


menu_principal_español = Screen(name="menu_principal_español")
menu_principal_español.add_widget(em.boxlayout)


# menu principal ingles
def menu_principali(self):
    sm.switch_to(menu_principal_ingles)


menu_principal_ingles = Screen(name="menu_principal_ingles")
menu_principal_ingles.add_widget(im.boxlayout)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Articulo~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Menu articulo español
def menu_art_e(self):
    sm.switch_to(menu_articulo_español)


menu_articulo_español = Screen(name="menu_articulo_español")
menu_articulo_español.add_widget(eam.boxlayout)


# menu articulo ingles
def menu_art_i(self):
    sm.switch_to(menu_articulo_ingles)


menu_articulo_ingles = Screen(name="menu_articulo_ingles")
menu_articulo_ingles.add_widget(iam.boxlayout)


# agrgar articulo español
def agrgar_articulo_e(self):
    sm.switch_to(agregar_articulo_español)


def funcion_agregar_art_e(self):
    codigo = eai.codigo.text
    articulo = eai.articulo.text
    rubro = eai.Rubro.text
    linea = eai.Linea.text
    descripcion = eai.Descripcion.text
    proveedor = eai.Proveedor.text
    stock = eai.Stock.text
    stock_min = eai.Stock_minimo.text
    stock_ideal = eai.Stock_ideal.text
    precio = eai.Pre_venta.text
    precio_com = eai.Pre_compra.text
    fecha_ult = eai.Fech_ult_comp.text
    stocke = stock.isdigit()
    stock_ide = stock_ideal.isdigit()
    stock_mi = stock_min.isdigit()
    precio_comp = precio_com.isdigit()
    pre = precio.isdigit()
    if codigo == "" or articulo == "" or rubro == "Seleccione unoq" or linea == "Seleccione unoq" or descripcion == "" or proveedor == "Selqeccione uno" or stocke == "" or stock_min == "" or stock_ideal == "" or precio == "" or precio_com == "" or fecha_ult == "":
        pupup_blanco.open()
    elif stocke == False or stock_ide == False or stock_mi == False or precio_comp == False or pre == False:
        popup_numero.open()
    else:
        bd.insertar_art(str(codigo), str(articulo), str(rubro), str(linea), str(descripcion), str(
            proveedor), str(stock), str(stock_min), str(stock_ideal), str(precio), str(precio_com), str(fecha_ult))
        popup_agregado.open()


agregar_articulo_español = Screen(name="agregar_articulo_español")
agregar_articulo_español.add_widget(eai.floatlayout)

# agrear articulo ingles


def agregar_articulo_i(self):
    sm.switch_to(agregar_articulo_ingles)


agregar_articulo_ingles = Screen(name="agregar_articulo_ingles")
agregar_articulo_ingles.add_widget(iai.floatlayout)


def funcion_agregar_art_i(self):
    codigo = iai.codigo.text
    articulo = iai.articulo.text
    rubro = iai.Rubro.text
    linea = iai.Linea.text
    descripcion = iai.Descripcion.text
    proveedor = iai.Proveedor.text
    stock = iai.Stock.text
    stock_min = iai.Stock_minimo.text
    stock_ideal = iai.Stock_ideal.text
    precio = iai.Pre_venta.text
    precio_com = iai.Pre_compra.text
    fecha_ult = iai.Fech_ult_comp.text
    stck = stock.isdigit()
    stock_ide = stock_ideal.isdigit()
    stock_mi = stock_min.isdigit()
    precio_comp = precio_com.isdigit()
    pre = precio.isdigit()
    try:
        bd.insertar_art(str(codigo), str(articulo), str(rubro), str(linea), str(descripcion), str(
            proveedor), str(stock), str(stock_mi), str(stock_ideal), str(precio), str(precio_com), str(fecha_ult))
        popup_agregado.open()

    except Exception as e:
        mensaje = popup_articulo_exitente.open()
        if codigo == "" or articulo == "" or rubro == "Seleccione unoq" or linea == "Seleccione unoq" or descripcion == "" or proveedor == "Selqeccione uno" or stock == "" or stock_min == "" or stock_ideal == "" or precio == "" or precio_com == "" or fecha_ult == "":
            pupup_blanco.open()
        elif stck == False or stock_ide == False or stock_min == False or precio_comp == False or pre == False:
            popup_numero.open()
        else:
            mensaje = str(e)


# consulta de articulo español
def consu_art_e(self):
    sm.switch_to(consu_arte)


def consulta_art_el(self):
    j = eac.txt_busqueda.text

    eac.gridlayout.clear_widgets()
    movimentos = str(eac.txt_busqueda.text)
    movimentos = bd.consu_movmiento_articulo(movimentos)
    if movimentos == []:
        eac.gridlayout.add_widget(Label(text="No existe el articulo!", font_size="20sp",
                                        color=(1, 1, 1, 1), size_hint_y=None, height=25))
    else:
        buttons = []

        for j in movimentos:

            buttons.append(
                Button(text="Articulo: "+str(j[1]) + "\n" + "Precio de venta :"+str(j[10]) + "\n"
                            + "Descripcion: "+str(j[4])+"\n" + "Codigo"+str(j[0]), background_color=(0, 1, 0, 1), size_hint_y=None, height=200))
        buttons[movimentos.index(j)].bind(
            on_press=partial(preenche_form_edita, j))
        eac.gridlayout.add_widget(buttons[movimentos.index(j)])
        eac.gridlayout.add_widget(Label(text="\n", size_hint_y=None, height=1))


def editar_art_e(self):
    sm.switch_to(editar_arte)


editar_arte = Screen(name="editar_arte")
editar_arte.add_widget(eae.floatlayout)

consu_arte = Screen(name="consu_arte")
consu_arte.add_widget(eac.floatlayout)


def preenche_form_edita(self, j):
    j = j.text

    editar_art_e(self)
    j = j.split('\n')
    j = j[0].split(": ")
    j = j[1]
    j = bd.select_editar_articulo(j)
    j = j[0]
    eae.codigo.text = str(j[0])
    eae.articulo.text = str(j[1])
    eae.Rubro.text = str(j[2])
    eae.Linea.text = str(j[3])
    eae.Descripcion.text = str(j[4])
    eae.Proveedor.text = str(j[5])
    eae.Stock.text = str(j[6])
    eae.Stock_ideal.text = str(j[7])
    eae.Stock_minimo.text = str(j[8])
    eae.Pre_compra.text = str(j[9])
    eae.Pre_venta.text = str(j[10])
    eae.Fech_ult_comp.text = str(j[11])


def funcion_editar_art_e(self):
    codigo = eae.codigo.text
    articulo = eae.articulo.text
    rubro = eae.Rubro.text
    linea = eae.Linea.text
    descripcion = eae.Descripcion.text
    proveedor = eae.Proveedor.text
    stock = eae.Stock.text
    stock_min = eae.Stock_minimo.text
    stock_ideal = eae.Stock_ideal.text
    precio = eae.Pre_venta.text
    precio_com = eae.Pre_compra.text
    fecha_ult = eae.Fech_ult_comp.text
    stocke = stock.isdigit()
    stock_ide = stock_ideal.isdigit()
    stock_mi = stock_min.isdigit()
    precio_comp = precio_com.isdigit()
    pre = precio.isdigit()
    if codigo == "" or articulo == "" or rubro == "Seleccione unoq" or linea == "Seleccione unoq" or descripcion == "" or proveedor == "Selqeccione uno" or stocke == "" or stock_min == "" or stock_ideal == "" or precio == "" or precio_com == "" or fecha_ult == "":
        pupup_blanco.open()
    elif stocke == False or stock_ide == False or stock_mi == False or precio_comp == False or pre == False:
        popup_numero.open()
    else:
        bd.edita_articulo(str(codigo), str(articulo), str(rubro), str(linea), str(descripcion), str(
            proveedor), str(stock), str(stock_mi), str(stock_ideal), str(precio), str(precio_com), str(fecha_ult))
        popup_agregado.open()


# eliminar articulo
def eliminar_articuloe(self):
    codigo = eae.codigo.text and iae.codigo.text
    bd.eliminar_articulo(codigo)
    popup_elimina.open()


def eliminar_articuloi(self):
    codigo = iae.codigo.text
    bd.eliminar_articulo(codigo)
    popup_elimina.open()


# consulta ingles
def consu_art_i(self):
    sm.switch_to(consu_arti)


def consulta_art_il(self):
    j = iac.txt_busqueda.text

    iac.gridlayout.clear_widgets()
    movimentos = str(iac.txt_busqueda.text)
    movimentos = bd.consu_movmiento_articulo(movimentos)
    if movimentos == []:
        iac.gridlayout.add_widget(Label(text="No existe el articulo!", font_size="20sp",
                                        color=(1, 1, 1, 1), size_hint_y=None, height=25))
    else:
        buttons = []

        for j in movimentos:

            buttons.append(
                Button(text="Articulo: "+str(j[1]) + "\n" + "Precio de venta :"+str(j[10]) + "\n"
                            + "Descripcion: "+str(j[4])+"\n" + "Codigo"+str(j[0]), background_color=(0, 1, 0, 1), size_hint_y=None, height=200))
        buttons[movimentos.index(j)].bind(
            on_press=partial(preenche_form_editai, j))
        iac.gridlayout.add_widget(buttons[movimentos.index(j)])
        iac.gridlayout.add_widget(Label(text="\n", size_hint_y=None, height=1))


def editar_art_i(self):
    sm.switch_to(editar_arti)


editar_arti = Screen(name="editar_arti")
editar_arti.add_widget(iae.floatlayout)

consu_arti = Screen(name="consu_arti")
consu_arti.add_widget(iac.floatlayout)


def preenche_form_editai(self, j):
    j = j.text

    editar_art_i(self)
    j = j.split('\n')
    j = j[0].split(": ")
    j = j[1]
    j = bd.select_editar_articulo(j)
    j = j[0]
    iae.codigo.text = str(j[0])
    iae.articulo.text = str(j[1])
    iae.Rubro.text = str(j[2])
    iae.Linea.text = str(j[3])
    iae.Descripcion.text = str(j[4])
    iae.Proveedor.text = str(j[5])
    iae.Stock.text = str(j[6])
    iae.Stock_ideal.text = str(j[7])
    iae.Stock_minimo.text = str(j[8])
    iae.Pre_compra.text = str(j[9])
    iae.Pre_venta.text = str(j[10])
    iae.Fech_ult_comp.text = str(j[11])

# listado articulo español


def lista_articulo_e(self):
    sm.switch_to(lista_arte)
    consulta_lista_articulo(self)


def consulta_lista_articulo(self):

    eal.gridlayout.clear_widgets()
    movimentos = bd.consulta_lista_articulo()
    if movimentos == []:
        eal.gridlayout.add_widget(Label(text="No hay articulo!", font_size="20sp",
                                        color=(1, 1, 1, 1), size_hint_y=None, height=25))
    else:
        buttons = []

        for j in movimentos:

            if j != 0:
                buttons.append(
                    Button(text="Articulo: "+str(j[1]) + "\n" + "Precio de venta :"+str(j[2]) + "\n"
                           + "Descripcion: "+str(j[3])+"\n"+"Codigo: " + str(j[6]), background_color=(0, 1, 0, 1), size_hint_y=None, height=200))

            buttons[movimentos.index(j)]
            eal.gridlayout.add_widget(buttons[movimentos.index(j)])
            eal.gridlayout.add_widget(
                Label(text="\n", size_hint_y=None, height=1))


lista_arte = Screen(name="lista_arte")
lista_arte.add_widget(eal.floatlayout)

# listado articulo ingles


def lista_articulo_i(self):
    sm.switch_to(lista_articuloi)
    consulta_lista_articuloi(self)


def consulta_lista_articuloi(self):

    ial.gridlayout.clear_widgets()
    movimentos = bd.consulta_lista_articulo()
    if movimentos == []:
        ial.gridlayout.add_widget(Label(text="No hay articulo!", font_size="20sp",
                                        color=(1, 1, 1, 1), size_hint_y=None, height=25))
    else:
        buttons = []

        for j in movimentos:

            if j != 0:
                buttons.append(
                    Button(text="Article: "+str(j[1]) + "\n" + "Precio de venta :"+str(j[2]) + "\n"
                           + "Descripcion: "+str(j[3])+"\n"+"Codigo: " + str(j[6]), background_color=(0, 1, 0, 1), size_hint_y=None, height=200))

            buttons[movimentos.index(j)]
            ial.gridlayout.add_widget(buttons[movimentos.index(j)])
            ial.gridlayout.add_widget(
                Label(text="\n", size_hint_y=None, height=1))


lista_articuloi = Screen(name="lista_articuloi")
lista_articuloi.add_widget(ial.floatlayout)


# ------------------------------------------ Rubro y linea -------------------------------------------------------------------------

def menu_rub_lin_e(self):
    sm.switch_to(menu_rubro_lineae)


menu_rubro_lineae = Screen(name="menu_rubro_lineae")
menu_rubro_lineae.add_widget(eryl.boxlayout)


def menu_rub_lin_i(self):
    sm.switch_to(menu_rub_lini)


menu_rub_lini = Screen(name="menu_rub_lini")
menu_rub_lini.add_widget(iryl.boxlayout)


# linea
def menu_linea_e(self):
    sm.switch_to(menu_lineae)


menu_lineae = Screen(name="menu_lineae")
menu_lineae.add_widget(elm.boxlayout)


def menu_linea_i(self):
    sm.switch_to(menu_lineai)


menu_lineai = Screen(name="menu_lineai")
menu_lineai.add_widget(ilm.boxlayout)


def carga_linea_e(self):
    sm.switch_to(carga_lineae)


def insert_linea_e(self):
    descripcion = elr.Descripcion.text
    nombre_linea = elr.nombre.text
    descrip = str(descripcion).isspace()
    nom_lin = str(nombre_linea).isspace()
    if descrip == True or nom_lin == True:
        pupup_blanco.open()

    else:
        try:
            bd.agregar_linea(descripcion, nombre_linea)
            popup_agregado.open()
        except Exception as e:
            mensaje = popup_linea_exitente.open()
            mensaje = str(e)


carga_lineae = Screen(name="carga_lineae")
carga_lineae.add_widget(elr.floatlayout)


def carga_linea_i(self):
    sm.switch_to(carga_lineai)


def insert_linea_i(self):
    descripcion = ilr.Descripcion.text
    nombre_linea = ilr.nombre.text
    descrip = str(descripcion).isspace()
    nom_lin = str(nombre_linea).isspace()
    if descrip == True or nom_lin == True:
        pupup_blanco.open()

    else:
        try:
            bd.agregar_linea(descripcion, nombre_linea)
            popup_agregado.open()
        except Exception as e:
            mensaje = popup_linea_exitente.open()
            mensaje = str(e)


carga_lineai = Screen(name="carga_lineai")
carga_lineai.add_widget(ilr.floatlayout)

# consullta linea


def consulta_linea_e(self):
    sm.switch_to(consulta_lineae)


def consulta_linea_es(self):
    j = elc.txt_busqueda.text

    elc.gridlayout.clear_widgets()
    movimentos = str(elc.txt_busqueda.text)
    movimentos = bd.consu_movmiento_linea(movimentos)
    if movimentos == []:
        elc.gridlayout.add_widget(Label(text="No existe el linea!", font_size="20sp",
                                        color=(1, 1, 1, 1), size_hint_y=None, height=25))
    else:
        buttons = []

        for j in movimentos:

            buttons.append(
                Button(text="Descripcion: "+str(j[0]) + "\n" + "Nombre de Linea :"+str(j[1]), background_color=(0, 1, 0, 1), size_hint_y=None, height=200))
        buttons[movimentos.index(j)].bind(
            on_press=partial(preenche_form_editl, j))
        elc.gridlayout.add_widget(buttons[movimentos.index(j)])
        elc.gridlayout.add_widget(Label(text="\n", size_hint_y=None, height=1))


def preenche_form_editl(self, j):
    j = j.text

    # editar(self)

    j = j.split('\n')
    j = j[0].split(": ")
    j = j[1]
    j = bd.select_editar(j)
    j = j[0]
    ele.Descripcion.text = str(j[0])
    ele.nombre.text = str(j[1])


consulta_lineae = Screen(name="consulta_lineae")
consulta_lineae.add_widget(elc.floatlayout)


def consulta_linea_i(self):
    sm.switch_to(consulta_lineai)


consulta_lineai = Screen(name="consulta_lineai")
consulta_lineai.add_widget(ilc.floatlayout)


def lista_linea_e(self):
    sm.switch_to(lista_lineae)


lista_lineae = Screen(name="lista_lineae")
lista_lineae.add_widget(ell.floatlayout)


def lista_linea_i(self):
    sm.switch_to(lista_lineai)


lista_lineai = Screen(name="lista_lineai")
lista_lineai.add_widget(ill.floatlayout)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~rubro~~~~~~~~~~~~~~~~+~+~~~~~~~~~~~~~~~~~~~~~~~~~

def rubro_menu_e(self):
    sm.switch_to(rubro_menue)


rubro_menue = Screen(name="rubro_menue")
rubro_menue.add_widget(erm.boxlayout)


def rubro_menu_i(self):
    sm.switch_to(rubro_menui)


rubro_menui = Screen(name="rubro_menui")
rubro_menui.add_widget(irm.boxlayout)


def rubro_registro_e(self):
    sm.switch_to(rubro_registroe)


rubro_registroe = Screen(name="rubro_registroe")
rubro_registroe.add_widget(eri.floatlayout)


def rubro_registro_i(self):
    sm.switch_to(rubro_registroi)


rubro_registroi = Screen(name="rubro_registroi")
rubro_registroi.add_widget(iri.floatlayout)


def rubro_consulta_e(self):
    sm.switch_to(rubro_consultae)


rubro_consultae = Screen(name="rubro_consultae")
rubro_consultae.add_widget(erc.floatlayout)


def rubro_consulta_e(self):
    sm.switch_to(rubro_consultai)


rubro_consultai = Screen(name="rubro_consultai")
rubro_consultai.add_widget(irc.floatlayout)


def rubro_lista_e(self):
    sm.switch_to(rubro_listae)


rubro_listae = Screen(name="rubro_listae")
rubro_listae.add_widget(erl.floatlayout)


def rubro_lista_i(self):
    sm.switch_to(rubro_listai)


rubro_listai = Screen(name="rubro_listai")
rubro_listai.add_widget(irl.floatlayout)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Proveedores ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def proveedores_menu_e(slef):
    sm.switch_to(proveedores_menue)


proveedores_menue = Screen(name="proveedores_menue")
proveedores_menue.add_widget(epm.boxlayout)


def proveedores_menu_i(slef):
    sm.switch_to(proveedores_menui)


proveedores_menui = Screen(name="proveedores_menui")
proveedores_menui.add_widget(ipm.boxlayout)


def proveedores_ingresar_e(self):
    sm.switch_to(proveedores_ingresare)


proveedores_ingresare = Screen(name="proveedores_ingresare")
proveedores_ingresare.add_widget(epi.floatlayout)


def proveedores_ingresar_i(self):
    sm.switch_to(proveedores_ingresari)


proveedores_ingresari = Screen(name="proveedores_ingresari")
proveedores_ingresari.add_widget(ipi.floatlayout)


def proveedores_consulta_e(self):
    sm.switch_to(proveedores_consultae)


proveedores_consultae = Screen(name="proveedores_consultae")
proveedores_consultae.add_widget(epc.floatlayout)


def proveedores_consulta_e(self):
    sm.switch_to(proveedores_consultai)


proveedores_consultai = Screen(name="proveedores_consultai")
proveedores_consultai.add_widget(ipc.floatlayout)


def proveedores_lista_e(self):
    sm.switch_to(proveedores_listae)


proveedores_listae = Screen(name="proveedores_listae")
proveedores_listae.add_widget(epl.floatlayout)


def proveedores_lista_i(self):
    sm.switch_to(proveedores_listai)


proveedores_listai = Screen(name="proveedores_listai")
proveedores_listai.add_widget(ipl.floatlayout)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~cliente~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def cliente_menu_e(self):
    sm.switch_to(cliente_menue)


cliente_menue = Screen(name="cliente_menue")
cliente_menue.add_widget(ecm.boxlayout)


def cliente_menu_i(self):
    sm.switch_to(cliente_menui)


cliente_menui = Screen(name="cliente_menui")
cliente_menui.add_widget(icm.boxlayout)


def cliente_insertar_e(self):
    sm.switch_to(cliente_insertare)


cliente_insertare = Screen(name="cliente_insertare")
cliente_insertare.add_widget(eci.floatlayout)


def cliente_insertar_i(self):
    sm.switch_to(cliente_insertari)


cliente_insertari = Screen(name="cliente_insertari")
cliente_insertari.add_widget(ici.floatlayout)


def consultar_cliente_e(self):
    sm.switch_to(cliente_consultare)


cliente_consultare = Screen(name="cliente_consultare")
cliente_consultare.add_widget(ecc.floatlayout)


def consultar_cliente_i(self):
    sm.switch_to(cliente_consultari)


cliente_consultari = Screen(name="cliente_consultari")
cliente_consultari.add_widget(icc.floatlayout)


def lista_cliente_e(self):
    sm.switch_to(cliente_listae)


cliente_listae = Screen(name="cliente_listae")
cliente_listae.add_widget(ecl.floatlayout)


def lista_cliente_i(self):
    sm.switch_to(cliente_listai)


cliente_listai = Screen(name="cliente_listai")
cliente_listai.add_widget(icl.floatlayout)


# configuracion español
def configuracion_e(self):
    sm.switch_to(configuracion_español)


configuracion_español = Screen(name="configuracion_español")
configuracion_español.add_widget(eco.boxlayout)

# configuracion ingles


def configuracion_i(self):
    sm.switch_to(configuracion_ingles)


configuracion_ingles = Screen(name="configuracion_ingles")
configuracion_ingles.add_widget(ico.boxlayout)


# botones
# botones terminos y condiciones español
etyc.btn_siguiente.bind(on_press=verificacion)

# botones terminos y condiciones ingles
ityc.btn_siguiente.bind(on_press=verificacion1)

# botones inicio de secion español
eis.btn_registro.bind(on_press=registro_español1)
eis.btn_ingresar.bind(on_press=verificacion_registro_e)

# botones inicio de secion ingles
iis.btn_registro.bind(on_press=registro_ingles1)
iis.btn_ingresar.bind(on_press=verificacion_registro_i)

# botones registro español
er.btn_cancel.bind(on_press=inicio_secion_e)
er.btn_guardar.bind(on_press=registro)

# botones registro ingles
ir.btn_cancel.bind(on_press=inicio_secion_i)
ir.btn_guardar.bind(on_press=registroi)

# boton menu español
em.btn_configuracion.bind(on_press=configuracion_e)
em.btn_articulos.bind(on_press=menu_art_e)
em.btn_rubro.bind(on_press=menu_rub_lin_e)
em.btn_provedores.bind(on_press=proveedores_menu_e)
em.btn_cliente.bind(on_press=cliente_menu_e)

# botn menu ingles
im.btn_articulos.bind(on_press=menu_art_i)
im.btn_configuracion.bind(on_press=configuracion_i)
im.btn_rubro.bind(on_press=menu_rub_lin_i)
im.btn_provedores.bind(on_press=proveedores_menu_i)
im.btn_cliente.bind(on_press=cliente_menu_i)

# boton configuracion español
eco.btn_idioma.bind(on_press=idiomas)

# boton configuracion español
ico.btn_idioma.bind(on_press=idiomas)

# boton cambio de idioma
edi.btn_ok.bind(on_press=editar_idioma)

# botones menu articulo español
eam.btn_nuevo_articulo.bind(on_press=agrgar_articulo_e)
eam.btn_eliminar.bind(on_press=consu_art_e)
eam.btn_listas.bind(on_press=lista_articulo_e)
eam.btn_volver1.bind(on_press=menu_principale)

# botones menu articulo ingles
iam.btn_nuevo_articulo.bind(on_press=agregar_articulo_i)
iam.btn_volver1.bind(on_press=menu_principali)
iam.btn_eliminar.bind(on_press=consu_art_i)
iam.btn_listas.bind(on_press=lista_articulo_i)

# botones nuevo articulos
eai.btn.bind(on_press=funcion_agregar_art_e)
eai.btn1.bind(on_press=menu_art_e)

# boton nuevo articlo iongles
iai.btn.bind(on_press=funcion_agregar_art_i)
iai.btn1.bind(on_press=menu_art_i)

# botones cnsulta articulo
eac.btn_busqueda.bind(on_press=consulta_art_el)
eae.btn.bind(on_press=funcion_editar_art_e)
iac.btn_busqueda.bind(on_press=consulta_art_il)

# botones volver lista articulo
ial.btn_volver.bind(on_press=menu_art_i)
eal.btn_volver.bind(on_press=menu_art_e)

# botones volver consuta articulo
eac.btn_volver.bind(on_press=menu_art_e)
iac.btn_volver.bind(on_press=menu_art_i)

# botones volver editar articulo
eae.btn1.bind(on_press=consu_art_e)
iae.btn1.bind(on_press=consu_art_i)

# boton eliminar articulo
eae.btn2.bind(on_press=eliminar_articuloe)
iae.btn2.bind(on_press=eliminar_articuloi)

# boton rubro y linea
eryl.btn_linea.bind(on_press=menu_linea_e)
iryl.btn_linea.bind(on_press=menu_linea_i)
eryl.btn_rubro.bind(on_press=rubro_menu_e)
iryl.btn_rubro.bind(on_press=rubro_menu_i)

# Botones linea
elm.btn_nuevo_linea.bind(on_press=carga_linea_e)
ilm.btn_nuevo_linea.bind(on_press=carga_linea_i)
elm.btn_consultar.bind(on_press=consulta_linea_e)
# Boton agregar linea
elr.btn.bind(on_press=insert_linea_e)
elr.btn1.bind(on_press=menu_linea_e)
ilr.btn.bind(on_press=insert_linea_i)
ilr.btn1.bind(on_press=menu_linea_i)
# boron consultar linea
elc.btn_busqueda.bind(on_press=consulta_linea_es)
# creacion de base de dato
if os.path.exists("eliman.db") is False:
    sm.add_widget(pantalla_idioma1)
else:
    idioma_elegido()


class Microbits(App):
    def build(self):
        Window.clearcolor = (0, 0, 0.8, .5)
        Window.size = (1000, 750)
        return sm


if __name__ == '__main__':
    Microbits().run()
