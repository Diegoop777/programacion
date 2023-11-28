import mysql.connector 
from mysql.connector import errorcode
from Model import usuarios
from typing import List 

class DAO:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                user="root",
                password="123456789",
                host="localhost",
                database="basedate"
            )
            self.cursor = self.cnx.cursor()
            
        
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de Usuario o Contraseña")
            elif err.errno == errorcode.ER_BAD_basedate_ERROR:
                print("La base de datos NO existe")
            else:
                print(err)
                
                
                
    def crear_usuario(self, username, password, rol):
        query = "INSERT INTO tbl_usuarios (nombre, password, rol, bloqueado) VALUES (%s, %s, %s, %s)"
        values = (username, password, rol, False)
        self.cursor.execute(query, values)
        self.cnx.commit()           
                
                
                
                
                
    def iniciar_sesion(self, usuario, password):
        try:
            query = "SELECT * FROM tbl_usuario WHERE nombre = %s AND password = %s"
            self.cursor.execute(query, (usuario, password))
            datos_usuario = self.cursor.fetchone()

            if datos_usuario:
                # Si se encuentra el usuario y la contraseña coincide, devolver los datos del usuario
                usuario = {
                    'id_usuario': datos_usuario[0],
                    'nombre': datos_usuario[1],
                    'password': datos_usuario[2],
                    'rol': datos_usuario[3]
                    # Puedes agregar más campos según sea necesario
                }
                return usuario
            else:
                if usuario == "SuperAdministrador":
                    query = "INSERT INTO tbl_usuario (nombre, password, rol) VALUES (%s, %s, %s)"
                    self.cursor.execute(query, ("SuperAdministrador", "123456", "SuperAdministrador"))
                    self.cnx.commit()
                    return {"nombre": "SuperAdministrador", "password": "123456", "rol": "SuperAdministrador"}
                else:
                    return None

        except mysql.connector.Error as err:
            print("Error al ejecutar la consulta:", err)
            return None

    
    def crear_super_admin(self):
        try:
            query = "SELECT * FROM tbl_usuario WHERE nombre = 'SuperAdministrador'"
            self.cursor.execute(query)
            datos_usuario = self.cursor.fetchone()

            if not datos_usuario:
                query = "INSERT INTO tbl_usuario (nombre, password, rol) VALUES (%s, %s, %s)"
                self.cursor.execute(query, ("SuperAdministrador", "123456", "SuperAdministrador"))
                self.cnx.commit()
                return {"nombre": "SuperAdministrador", "password": "123456", "rol": "SuperAdministrador"}
            else:
                return None
    
        except mysql.connector.Error as err:
            
            print("Error al ejecutar la consulta:", err)
            return None


    def bloquear_usuario(self, id_usuario):
        cursor = self.cnx.cursor()
        query = "UPDATE usuarios SET bloqueado = 1 WHERE id = %s"
        cursor.execute(query, (id_usuario,))
        self.cnx.commit()

    def desbloquear_usuario(self, id_usuario):
        cursor = self.cnx.cursor()
        query = "UPDATE usuarios SET bloqueado = 0 WHERE id = %s"
        cursor.execute(query, (id_usuario,))
        self.cnx.commit()

    def cambiar_contraseña(self, id_usuario, nueva_contraseña):
        cursor = self.cnx.cursor()
        query = "UPDATE usuarios SET password = %s WHERE id = %s"
        cursor.execute(query, (nueva_contraseña, id_usuario))
        self.cnx.commit()

    def cambiar_informacion_usuario(self, id_usuario, nuevo_nombre, nuevo_rol):
        cursor = self.cnx.cursor()
        query = "UPDATE usuarios SET nombre = %s, rol = %s WHERE id = %s"
        cursor.execute(query, (nuevo_nombre, nuevo_rol, id_usuario))
        self.cnx.commit()







