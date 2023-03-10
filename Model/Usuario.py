from Services.DataBase import Connection_DB

def Validation_User(name):
    valid = True
    connection = Connection_DB()
    my_DB = connection.cursor()
    my_DB.execute("SELECT nombre FROM usuarios")
    total_users = my_DB.fetchall()
    for user in total_users:
        if user[0] == name:
            valid = False
            return valid
    return valid

class User:
    def __init__(self, name, password = ""):
        self.name = name
        self.password = password

    def Login_User(self):
        connection = Connection_DB()
        mydb = connection.cursor()
        valid = Validation_User(self.name)
        if valid:
            sql = "INSERT INTO usuarios (nombre, contrasena) VALUES (%s, %s)"
            val = (self.name, self.password)
            mydb.execute(sql, val)
            connection.commit()
            print(f"Usuario {self.name} creado exitosamente")
        else:
            print("Error Usuario duplicado")

    def Search_User(self):
        valid = Validation_User(self.name)
        if not valid:
            print("Usuario Encontrado")
            connection = Connection_DB()
            my_DB = connection.cursor()
            name = (f"{self.name}",)
            sql = "SELECT * FROM usuarios WHERE nombre= %s"
            my_DB.execute(sql, name)
            names_users = my_DB.fetchall()
            for user in names_users:
                print("Id       Nombre      Contraseña")
                print(f"{user[0]}        {user[1]}       {user[2]}")
        else:
            print("Usuario no registrado!!!")

    def Modifity_User(self):
        valid = Validation_User(self.name)
        if not valid:
            print("Usuario Encontrado")
            print("Ingrese el nombre a modificar")
            name_update = input("Usuario: ")
            pass_update = input("Contraseña: ")
            confirmation = input("Confirme la actualizacion del usuario (S/N): ")
            if confirmation == "S" or confirmation == "s":
                connection = Connection_DB()
                my_DB = connection.cursor()
                user_update = (f"{name_update}", f"{pass_update}", f"{self.name}")
                sql = "UPDATE usuarios set nombre= %s, contrasena= %s WHERE nombre= %s"
                my_DB.execute(sql, user_update)
                connection.commit()
                print("Usuario modificado exitosamente")
            elif confirmation == "N" or confirmation == "n":
                print("Usuario no modificado")
            else:
                print("Opcion no valida")
        else:
            print("Usuario no registrado!!!")

    def Delete_User(self):
        valid = Validation_User(self.name)
        if not valid:
            print("Usuario Encontrado")
            confirmation = input("Confirme la eliminacion del usuario (S/N): ")
            if confirmation == "S" or confirmation == "s":
                connection = Connection_DB()
                my_DB = connection.cursor()
                name = (f"{self.name}",)
                sql = "DELETE FROM usuarios WHERE nombre= %s"
                my_DB.execute(sql, name)
                connection.commit()
                print("Usuario eliminado exitosamente")
            elif confirmation == "N" or confirmation == "n":
                print("Usuario no eliminado")
            else:
                print("Opcion no valida")
        else:
            print("Usuario no registrado!!!")
