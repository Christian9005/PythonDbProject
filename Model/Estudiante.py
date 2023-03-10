from Services.DataBase import Connection_DB

def Validation_User(name):
    valid = True
    connection = Connection_DB()
    my_DB = connection.cursor()
    my_DB.execute("SELECT cedula FROM estudiantes")
    total_users = my_DB.fetchall()
    for user in total_users:
        if user[0] == name:
            valid = False
            return valid
    return valid

class Student:
    def __init__(self, cedula, nombre = "", apellido = "", correo = "", celular = ""):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.celular = celular

    def Login_Student(self):
        connection = Connection_DB()
        mydb = connection.cursor()
        valid = Validation_User(self.cedula)
        if valid:
            sql = "INSERT INTO estudiantes (cedula, nombre, apellido, correo, celular) VALUES (%s, %s, %s, %s, %s)"
            val = (self.cedula, self.nombre, self.apellido, self.correo, self.celular)
            mydb.execute(sql, val)
            connection.commit()
            print(f"El Estudiante: {self.nombre} con CI: {self.cedula} creado exitosamente")
        else:
            print("Error Estudiante duplicado")

    def Search_Student(self):
        valid = Validation_User(self.cedula)
        if not valid:
            print("Estudiante Encontrado")
            connection = Connection_DB()
            my_DB = connection.cursor()
            name = (f"{self.cedula}",)
            sql = "SELECT * FROM estudiantes WHERE cedula= %s"
            my_DB.execute(sql, name)
            names_users = my_DB.fetchall()
            for user in names_users:
                print("Id     Cedula   Nombre   Apellido  Correo      Celular")
                print(f"{user[0]}      {user[1]}       {user[2]}     {user[3]}     {user[4]}     {user[5]}")
        else:
            print("Estudiante no registrado!!!")

    def Modifity_Student(self):
        valid = Validation_User(self.cedula)
        if not valid:
            print("Estudiante Encontrado")
            print("Ingrese las credenciales del estudiante a modificar")
            cedula = input("Cedula: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            celular = input("Celular: ")
            confirmation = input("Confirme la actualizacion del estudiante (S/N): ")
            if confirmation == "S" or confirmation == "s":
                connection = Connection_DB()
                my_DB = connection.cursor()
                student_update = (f"{cedula}", f"{nombre}", f"{apellido}", f"{correo}", f"{celular}", f"{self.cedula}")
                sql = "UPDATE estudiantes set cedula= %s, nombre= %s, apellido= %s, correo= %s, celular= %s WHERE cedula= %s"
                my_DB.execute(sql, student_update)
                connection.commit()
                print("Estudiante modificado exitosamente")
            elif confirmation == "N" or confirmation == "n":
                print("Estudiante no modificado")
            else:
                print("Opcion no valida")
        else:
            print("Estudiante no registrado!!!")

    def Delete_Student(self):
        valid = Validation_User(self.cedula)
        if not valid:
            print("Estudiante Encontrado")
            confirmation = input("Confirme la eliminacion del estudiante (S/N): ")
            if confirmation == "S" or confirmation == "s":
                connection = Connection_DB()
                my_DB = connection.cursor()
                cedula = (f"{self.cedula}",)
                sql = "DELETE FROM estudiantes WHERE cedula= %s"
                my_DB.execute(sql, cedula)
                connection.commit()
                print("Usuario eliminado exitosamente")
            elif confirmation == "N" or confirmation == "n":
                print("Estudiante no eliminado")
            else:
                print("Opcion no valida")
        else:
            print("Estudiante no registrado!!!")