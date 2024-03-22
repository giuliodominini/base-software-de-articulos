"""
Microbits
Eliman
base datos
Dominini Giulio
"""
import sqlite3

# base usuario


def crear_base_usuario():
    try:
        bd = sqlite3.connect("eliman.db")  # conectamos con la base dedato
        cursor = bd.cursor()
        tablas = [  # creamos las tablas
            """
                CREATE TABLE IF NOT EXISTS registro(
                    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                    Nombre VARCHAR (20) NOT NULL,
                    Permiso VARCHAR (20) NOT NULL,
                    Contraseña VARBINARY (50) NOT NULL,
                    tel NUMBER (15) NOT NULL
                );
            """
        ]
        for tabla in tablas:  # si no se crea la base de dato salta un aviso de que no se puede crear la base de dato
            cursor.execute(tabla)
            print("Tablas creadas correctamente")
    except sqlite3.OperationalError as error:  # error al abrir la base de dato
        print("Error al abrir:", error)


def insertar_usuario(nombre, permiso, contra, tel):
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    cursor.execute("INSERT INTO registro(Nombre, Permiso, Contraseña, tel)"
                   "VALUES('" + nombre + "','" + permiso + "', '" + contra + "', '"+tel+"' )")
    print("Guardado correctamente")
    bd.commit()
    bd.close()


def consulta_usuario(usuario, contraseña, permiso):
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    cursor.execute('SELECT * FROM registro WHERE Nombre = ? AND Contraseña = ? AND Permiso = ?',
                   (usuario, contraseña, permiso))
    registros = cursor.fetchall()
    return registros


def eliminar_usuario():

    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    cursor.execute(
        "SELECT Nombre, Permiso, Contraseñal, tel FROM registro WHERE codigo = '" + str(codigo) + "'")

    cursor.execute("DELETE FROM registro WHERE codigo = '" + str(codigo) + "'")
    bd.commit()
    bd.close()


def editar_usuario(codigo, Nombre, Permiso, Contraseña, tel):
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    cursor.execute("UPDATE registro SET Nombre, Permiso, Contraseñal, tel"
                   "VALUES('" + Nombre + "','" + Permiso + "', '" + Contraseña + "', '"+tel+"')")
    bd.commit()
    bd.close()

# base articulo


def crear_base_articulo():
    try:
        bd = sqlite3.connect("eliman.db")
        cursor = bd.cursor()
        tablas = [
            """
                CREATE TABLE IF NOT EXISTS articulo(
                    codigo NUMBER PRIMARY KEY NOT NULL,
                    articulo VARCHAR (20) NOT NULL,
                    rubro VARCHAR (10)NOT NULL,
                    linea VARCHAR(10)NOT NULL,
                    descripcion VARCHAR (50) NOT NULL,
                    proveedores VARCHAR (50) NOT NULL,
                    stock NUMBER NOT NULL,
                    stock_minimo NUMBER NOT NULL,
                    stock_ideal NUMBER NOT NULL,
                    precio NUMBER NOT NULL,
                    precio_compra NUMBER NOT NULL,
                    fecha_ult VARCHAR (8) NOT NULL

                );
            """
        ]
        for tabla in tablas:  # si no se crea la base de dato salta un aviso de que no se puede crear la base de dato
            cursor.execute(tabla)
        print("Tablas creadas correctamente")
    except sqlite3.OperationalError as error:                      # error al abrir la base de dato
        print("Error al abrir:", error)


# agregar articulos a la base de dato

# esta funcion es para agregar articulos a la base de dato
def insertar_art(codigo, articulo, rubro, linea, descripcion, proveedor, stock, stock_min, stock_ideal, precio, precio_com, fecha_ult):
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    cursor.execute("INSERT INTO articulo(codigo, articulo, rubro, linea, descripcion, proveedores, stock, stock_minimo, stock_ideal, precio, precio_compra, fecha_ult)"
                   "VALUES('"+codigo+"','" + articulo + "', '"+rubro+"', '"+linea + "','" + descripcion + "','" + proveedor+"','" + stock+"','" + stock_min+"','" + stock_ideal+"','" + precio+"', '"+precio_com+"', '"+fecha_ult+"')")
    print("Guardado correctamente")
    bd.commit()
    bd.close()


# seleccionamos articulo para editar
def select_editar_articulo(articulo):
    conn = sqlite3.connect("eliman.db")
    cursor = conn.cursor()
    cursor.execute("SELECT codigo, articulo, rubro, linea, descripcion, proveedores, stock, stock_minimo, stock_ideal, precio, precio_compra, fecha_ult FROM articulo WHERE articulo = '" + articulo+"'")
    movimentos = cursor.fetchall()
    return movimentos


# editamos articulo en la base de dato
def edita_articulo(codigo, articulo, rubro, linea, descripcion, proveedor, stock, stock_min, stock_ideal, precio, precio_com, fecha_ult):
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    sentencia = "UPDATE articulo SET articulo=?, rubro=?, linea=?, descripcion=?, proveedores=?, stock=?, stock_minimo=?, stock_ideal=?, precio=?, precio_compra=?, fecha_ult=? WHERE codigo =  '"+codigo+"'"
    cursor.execute(sentencia, [articulo, rubro, linea, descripcion, proveedor,
                   stock, stock_min, stock_ideal, precio, precio_com, fecha_ult])
    bd.commit()
    bd.close()


# eliminamos el articulo
def eliminar_articulo(codigo):
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    cursor.execute("DELETE FROM articulo WHERE codigo = '"+str(codigo)+"'")
    bd.commit()
    bd.close()


# consulta
def consu_movmiento_articulo(pesquisa):
    conn = sqlite3.connect("eliman.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM articulo WHERE articulo = '" + pesquisa + "'")
    movimentos = cursor.fetchall()
    return movimentos


# consulta de lista
def consulta_lista_articulo():
    conn = sqlite3.connect("eliman.db")
    cursor = conn.cursor()
    cursor.execute("SELECT codigo, articulo, rubro, linea, descripcion, proveedores, stock, stock_minimo, stock_ideal, precio, precio_compra, fecha_ult FROM articulo")
    movimentos = cursor.fetchall()
    return movimentos


# consulta de articulo individual
def consulta_articulo():
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    cursor.execute("SELECT codigo, articulo, rubro, linea, descripcion, proveedores, stock, stock_minimo, stock_ideal, precio, precio_compra, fecha_ult FROM articulo")
    clientes = cursor.fetchall()
    return clientes

# base proveedor


def crear_base_proveedor():
    try:
        con = sqlite3.connect("eliman.db")
        cursor = con.cursor()
        tabla = [
            """
                CREATE TABLE IF NOT EXISTS proveedores(
                    ID_prov        INTEGER PRIMARY KEY ,
                    RAZON_SOCIAL    VARCHAR2(35) NOT NULL,
                    DIRECCION       VARCHAR2(30) NOT NULL,
                    TELEFONO        NUMBER(15) NOT NULL,
                    NOM_CONTACTO    VARCHAR2(15) NOT NULL,
                    CEL_CONTACTO    NUMBER(15) NOT NULL,
                    MAIL            VARCHAR2(30) NOT NULL,
                    CUIT            NUMBER(15) NOT NULL,
                    CBU             NUMBER(15) NOT NULL
                ); 
            """
        ]
        for tabla in tabla:
            cursor.execute(tabla)
        print("tablas creadas correctamente")

    except sqlite3.OperationalError as error:
        print("Error al abrir:", error)


def insertar_proveedor(d1, d2, d3, d4, d5, d6, d7, d8, d9):
    con = sqlite3.connect("eliman.db")
    cursor = con.cursor()

    cursor.execute("INSERT INTO proveedores(ID_prov, RAZON_SOCIAL, DIRECCION, TELEFONO, NOM_CONTACTO, CEL_CONTACTO, MAIL, CUIT, CBU)"
                   "VALUES('" + d1 + "','" + d2 + "', '" + d3 + "', '" + d4+"','" + d5 + "', '" + d6 + "','"+d7+"', '" + d8 + "', '" + d9 + "')")
    print("Guardado correctamente")

    con.commit()
    con.close()


def consulta_lista_proveedor():
    con = sqlite3.connect("eliman.db")
    cursor = con.cursor()
    cursor.execute(
        "SELECT ID_prov, RAZON_SOCIAL,DIRECCION, TELEFONO, NOM_CONTACTO, CEL_CONTACTO,MAIL,CUIT,CBU FROM proveedores")
    movimentos = cursor.fetchall()
    return movimentos


def select_editar_proveeddor(razon_social):
    con = sqlite3.connect("eliman.db")
    cursor = con.cursor()
    cursor.execute("SELECT ID_prov, RAZON_SOCIAL,DIRECCION, TELEFONO, NOM_CONTACTO, CEL_CONTACTO,MAIL,CUIT,CBU FROM proveedores WHERE RAZON_SOCIAL = '" + razon_social+"'")
    movimentos = cursor.fetchall()
    return movimentos


def consu_movmiento_proveedor(pesquisa):
    con = sqlite3.connect("eliman.db")
    cursor = con.cursor()
    cursor.execute("SELECT ID_prov, RAZON_SOCIAL,DIRECCION, TELEFONO, NOM_CONTACTO, CEL_CONTACTO,MAIL,CUIT,CBU FROM proveedores WHERE RAZON_SOCIAL = '" + pesquisa + "'")
    movimentos = cursor.fetchall()
    return movimentos


def edita_proveedor(ID_prov, RAZON_SOCIAL, DIRECCION, TELEFONO, NOM_CONTACTO, CEL_CONTACTO, MAIL, CUIT, CBU):
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    sentencia = "UPDATE proveedores SET RAZON_SOCIAL = ?, DIRECCION = ?, TELEFONO = ?, NOM_CONTACTO = ?, CEL_CONTACTO = ?, MAIL = ?, CUIT =?,CBU = ? '" + \
        str(a)+"'"
    cursor.execute(sentencia, [RAZON_SOCIAL, DIRECCION,
                   TELEFONO, NOM_CONTACTO, CEL_CONTACTO, MAIL, CUIT, CBU])
    bd.commit()
    bd.close()


def eliminar_proveedor(ID_prov):
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()

    cursor.execute(
        "DELETE FROM proveedores WHERE  ID_prov = '" + str(ID_prov) + "'")
    bd.commit()
    bd.close()

# base cliente


# se crea la tabla, esta se llama una sola vez para la creacion de la tabla
def crear_base_cliente():
    try:
        bd = sqlite3.connect("eliman.db")  # conectamos con la base dedato
        cursor = bd.cursor()
        tablas = [  # creamos las tablas
            """
                CREATE TABLE IF NOT EXISTS CLIENTE(
                    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                    razon_social VARCHAR (30),
                    direccion VARCHAR(50),
                    telefono NUMBER (15),
                    nombre_contac VARCHAR (30),
                    celular NUMBER (15),
                    mail VARCHAR (59),
                    tipo_clientes VARCHAR (30),
                    CBU_cliente NUMBER (10),
                    Cuit_cliente NUMBER (10)

                );
            """
        ]
        for tabla in tablas:  # si no se crea la base de dato salta un aviso de que no se puede crear la base de dato
            cursor.execute(tabla)
        print("Tablas creadas correctamente")
    except sqlite3.OperationalError as error:  # error al abrir la base de dato
        print("Error al abrir:", error)


def select_editar_cliente(razon_social):
    conn = sqlite3.connect("eliman.db")
    cursor = conn.cursor()
    cursor.execute("SELECT codigo, razon_social, direccion, telefono, nombre_contac, celular, mail, tipo_clientes, CBU_cliente, Cuit_cliente FROM CLIENTE WHERE razon_social = '" + razon_social+"'")
    movimentos = cursor.fetchall()
    return movimentos


def consu_movmiento_cliente(pesquisa):
    conn = sqlite3.connect("eliman.db")
    cursor = conn.cursor()
    cursor.execute("SELECT codigo, razon_social, direccion, telefono, nombre_contac, celular, mail, tipo_clientes, CBU_cliente, Cuit_cliente FROM CLIENTE WHERE razon_social = '" + pesquisa + "'")
    movimentos = cursor.fetchall()
    return movimentos


def consulta_lista_cliente():
    conn = sqlite3.connect("eliman.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT codigo, razon_social, direccion, telefono, nombre_contac, celular, mail, tipo_clientes, CBU_cliente, Cuit_cliente FROM CLIENTE")
    movimentos = cursor.fetchall()
    return movimentos


# esta funcion es para agregar articulos a la base de dato
def insertar_cliente(razon, dire, numero, nombre, celu, mail, tipo_cli, cbu_cli,):

    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()

    cursor.execute("INSERT INTO CLIENTE(razon_social, direccion, telefono, nombre_contac, celular, mail, tipo_clientes, CBU_cliente, Cuit_cliente)"
                   "VALUES('" + razon + "','" + dire + "', '" + numero + "' , '" + nombre + "','" + celu + "', '" + mail + "', '" + tipo_cli + "', '" + cbu_cli + "', '" + cuit_cli + "')")
    print("Guardado correctamente")

    bd.commit()
    bd.close()


def consulta_cliente():
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    cursor.execute(
        "SELECT codigo, razon_social, direccion, telefono, nombre_contac, celular, mail, tipo_clientes, CBU_cliente, Cuit_cliente FROM CLIENTE")
    clientes = cursor.fetchall()
    return clientes


def edita_clientes(codigo, razon, fantasia, tipo, categoria, dire, numero, nombre, celu, mail):
    a = teg.lbl.text
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    sentencia = "UPDATE CLIENTE SET razon_social = ?, nombre_fantasia = ?, tipo_cliente = ?, categoria_fiscal = ?, direccion = ?, telefono = ?, nombre_contac = ?, celular = ?, mail = ? '" + \
        str(a)+"'"
    cursor.execute(sentencia, [razon, fantasia, tipo,
                   categoria, dire, numero, nombre, celu, mail])
    bd.commit()
    bd.close()


def eliminar_cliente(codigo):

    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    cursor.execute("DELETE FROM CLIENTE WHERE codigo = '"+str(codigo)+"'")
    bd.commit()
    bd.close()

# base rubro


def crear_base_rubro():
    try:
        bd = sqlite3.connect("eliman.db")
        cursor = bd.cursor()
        tablas = [
            """
                CREATE TABLE IF NOT EXISTS rubro(
                    rubro VARCHAR (10) PRIMARY KEY,
                    descripcion VARCHAR (30)
                );
            """
        ]
        for tabla in tablas:
            cursor.execute(tabla)
        print("Tablas creadas correctamente")
    except sqlite3.OperationalError as error:
        print("Error al abrir:", error)


def insertar_rubro(rubro, descripcion):
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    cursor.execute("INSERT INTO rubro(rubro,descripcion)"
                   "VALUES('" + rubro + "','" + descripcion + "')")
    print("Guardado correctamente")
    bd.commit()
    bd.close()


def consulta_rubro():
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    cursor.execute("SELECT rubro, descripcion FROM rubro")
    rubros = cursor.fetchall()
    return rubros


def editar_rubro(rubro, descripcion):
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    cursor.execute("UPDATE rubro SET rubro, descripcion"
                   "VALUES('" + rubro + "','" + descripcion + "')")
    bd.commit()
    bd.close()


def eliminar_rubro():
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    cursor.execute(
        "SELECT descripcion FROM rubro WHERE rubro = '" + int(rubro) + "'")
    cursor.execute("DELETE FROM art WHERE rubro = '" + int(rubro) + "'")
    bd.commit()
    bd.close()

# base linea


def crear_base_linea():
    try:
        bd = sqlite3.connect("eliman.db")
        cursor = bd.cursor()
        tablas = [
            """
                CREATE TABLE IF NOT EXISTS lineas(
                    descripcion VARCHAR  (30) NOT NULL,
                    nombre_linea VARCHAR (30) NOT NULL PRIMARY KEY
                );
            """
        ]
        for tabla in tablas:
            cursor.execute(tabla)
        print("Tablas creadas correctamente")
    except sqlite3.OperationalError as error:
        print("Error al abrir:", error)


def agregar_linea(descripcion, nombre_linea):

    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    cursor.execute("INSERT INTO lineas(descripcion,nombre_linea)"
                   "VALUES('" + descripcion + "','"+nombre_linea+"')")
    print("Guardado correctamente")

    bd.commit()
    bd.close()


def consulta_lista_linea():
    con = sqlite3.connect("eliman.db")
    cursor = con.cursor()
    cursor.execute("SELECT descripcion,nombre_linea  FROM lineas")
    movimentos = cursor.fetchall()
    return movimentos


def select_editar_linea(nom_linea):
    con = sqlite3.connect("eliman.db")
    cursor = con.cursor()
    cursor.execute(
        "SELECT descripcion,nombre_linea FROM lineas WHERE codigo = '" + nom_linea+"'")
    movimentos = cursor.fetchall()
    return movimentos


def consu_movmiento_linea(pesquisa):
    con = sqlite3.connect("eliman.db")
    cursor = con.cursor()
    cursor.execute(
        "SELECT descripcion,nombre_linea FROM lineas WHERE nombre_linea = '" + pesquisa + "'")
    movimentos = cursor.fetchall()
    return movimentos


def edita_linea(descripcion, nombre_linea):
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    sentencia = "UPDATE lineas SET descripcion = ?, nombre_linea = ?"
    cursor.execute(sentencia, [descripcion, nombre_linea])
    bd.commit()
    bd.close()


def eliminar_linea(nom_linea):
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()

    cursor.execute(
        "DELETE FROM lineas WHERE  nombre_linea = '" + str(nom_linea) + "'")
    bd.commit()
    bd.close()


# idioma
def idioma():
    try:
        bd = sqlite3.connect("eliman.db")
        cursor = bd.cursor()
        tablas = [
            """
                CREATE TABLE IF NOT EXISTS idioma(
                    idiomas VARCHAR (15)NOT NULL
                );
            """
        ]
        for tabla in tablas:
            cursor.execute(tabla)
        print("Tablas creadas correctamente")
    except sqlite3.OperationalError as error:
        print("Error al abrir:", error)


def agregar_idioma(idi1):

    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    cursor.execute("INSERT INTO idioma(idiomas)"
                   "VALUES('" + idi1 + "')")
    print("Guardado correctamente")

    bd.commit()
    bd.close()


def consulta_idioma(pesquisa):
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    cursor.execute(
        "SELECT idiomas FROM idioma  WHERE idiomas = '" + pesquisa + "'")
    elegido = cursor.fetchall()
    return elegido


def select_editar_idioma(idioma1):
    con = sqlite3.connect("eliman.db")
    cursor = con.cursor()
    cursor.execute(
        "SELECT idiomas FROM idioma WHERE idiomas = '" + idioma1+"'")
    movimentos = cursor.fetchall()
    return movimentos


def edita_idioma(idioma1):
    bd = sqlite3.connect("eliman.db")
    cursor = bd.cursor()
    sentencia = "UPDATE idioma SET idiomas = ?"
    cursor.execute(sentencia, [idioma1])
    bd.commit()
    bd.close()


# crear_base_usuario()
# crear_base_articulo()
# crear_base_proveedor()
# crear_base_cliente()
# crear_base_rubro()
# crear_base_linea()
# idioma()
