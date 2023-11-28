
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
            cursor = conexion.cursor()
        
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de Usuario o Contraseña")
            elif err.errno == errorcode.ER_BAD_basedate_ERROR:
                print("La base de datos NO existe")
            else:
                print(err)
