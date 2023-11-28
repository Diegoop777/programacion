import os
import mysql.connector
from Conexion_baseDatos import DAO







def ingresar_credenciales():
    nombre_usuario = input('Ingrese su nombre de usuario: ')
    contraseña = input('Ingrese su contraseña: ')
    return nombre_usuario ,contraseña


def validar_roles(usuario):
    if usuario:
        if usuario['rol'] in ["SuperAdministrador", "Administrador"]:
            mostrar_menu(usuario)
        else:
            print("Usuario no tiene permisos para realizar estas acciones")

while True:
    print("\nOpciones:")
    print("1. Crear nuevo usuario")
    print("2. Eliminar usuario")
    print("3. Bloquear usuario")
    print("4. Desbloquear usuario")
    print("5. Cambiar Contraseña de Usuario Existentes")
    print("6. Cambiar Informacion o Datos de Usuario Existentes")
    print("7. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':  # Crear nuevo usuario
        username = input("Ingrese el nombre de usuario: ")
        password = input("Ingrese la contraseña: ")
        rol = input("Ingrese el rol (Administrador/Asistente/Vendedor): ")
        if rol not in ['Administrador', 'Asistente', 'Vendedor']:
            print("Rol inválido.")
        #else:
            #query = "INSERT INTO Usuarios (username, password, rol, bloqueado) VALUES (%s, %s, %s, %s)"
            #cursor.execute(query, (username, password, rol, False))
            #mydb.commit()
            #print("Nuevo usuario creado correctamente.")

    elif opcion == '2':  # Eliminar usuario
        id_usuario = input("Ingrese el ID del usuario que desea eliminar: ")
        query = "DELETE FROM Usuarios WHERE id = %s AND rol != 'SuperAdministrador'"
        cursor.execute(query, (id_usuario,))
        if cursor.rowcount > 0:
            mydb.commit()
            print("Usuario eliminado correctamente.")
        else:
            print("No se pudo eliminar el usuario o es el SuperAdministrador.")

    elif opcion == '3':  # Bloquear usuario
        id_usuario = input("Ingrese el ID del usuario que desea bloquear: ")
        query = "UPDATE Usuarios SET bloqueado = True WHERE id = %s AND rol != 'SuperAdministrador'"
        cursor.execute(query, (id_usuario,))
        if cursor.rowcount > 0:
            mydb.commit()
            print("Usuario bloqueado correctamente.")
        else:
            print("No se pudo bloquear el usuario o es el SuperAdministrador.")

    elif opcion == '4':  # Desbloquear usuario
        id_usuario = input("Ingrese el ID del usuario que desea desbloquear: ")
        query = "UPDATE Usuarios SET bloqueado = False WHERE id = %s"
        cursor.execute(query, (id_usuario,))
        if cursor.rowcount > 0:
            mydb.commit()
            print("Usuario desbloqueado correctamente.")
        else:
            print("No se pudo desbloquear el usuario.")

    elif opcion == '7':  # Salir
        print("Saliendo.")
        break

    else:
        print("Opción inválida. Intente de nuevo.")

    if opcion == '5':
        id_usuario = input("Ingrese el ID del usuario: ")
        nueva_contraseña = input("Ingrese la nueva contraseña: ")
        query = "UPDATE Usuarios SET password = %s WHERE id = %s AND rol != 'SuperAdministrador'"
        cursor.execute(query, (nueva_contraseña, id_usuario))
        if cursor.rowcount > 0:
            mydb.commit()
            print("Contraseña actualizada correctamente.")
        else:
            print("No se pudo actualizar la contraseña o es el SuperAdministrador.")
    elif opcion == '6':
        id_usuario = input("Ingrese el ID del usuario: ")
        nuevo_username = input("Ingrese el nuevo nombre de usuario: ")
        nuevo_password = input("Ingrese la nueva contraseña: ")
        nuevo_rol = input("Ingrese el nuevo rol: ")
        query = "UPDATE Usuarios SET username = %s, password = %s, rol = %s WHERE id = %s AND rol != 'SuperAdministrador'"
        cursor.execute(query, (nuevo_username, nuevo_password, nuevo_rol, id_usuario))
        if cursor.rowcount > 0:
            mydb.commit()
            print("Información de usuario actualizada correctamente.")
        else:
            print("No se pudo actualizar la información del usuario o es el SuperAdministrador.")
    elif opcion == '7':
        print("Saliendo.")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
