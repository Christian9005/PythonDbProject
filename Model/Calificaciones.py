from Model.Estudiante import Student
from Services.DataBase import Connection_DB

def Validation_Score(a):
    while True:
        n = int(input(f"Ingrese la nota {a}: "))
        if n < 0 or n > 100:
            print("Debes ingresar la nota en el rango.")
            continue
        else:
            return n


def Validation_User(name):
    valid = True
    connection = Connection_DB()
    my_DB = connection.cursor()
    my_DB.execute("SELECT cedula FROM calificaciones")
    total_users = my_DB.fetchall()
    for user in total_users:
        if user[0] == name:
            valid = False
            return valid
    return valid

class Scores(Student):
    def __init__(self, cedula, promedio=0):
        super().__init__(cedula)
        self.promedio = promedio

    def Insert_Scores(self):
        connection = Connection_DB()
        mydb = connection.cursor()
        valid = Validation_User(self.cedula)
        if valid:
            sql = "INSERT INTO calificaciones (cedula, nombre, apellido, correo, celular, promedio) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (self.cedula, self.nombre, self.apellido, self.correo, self.celular, self.promedio)
            mydb.execute(sql, val)
            connection.commit()
            print(f"Notas del Estudiante con CI: {self.cedula} creadas exitosamente")
        else:
            print("Error Estudiante duplicado")

    def List_Scores(self):
        print("Notas de los Estudiantes")
        connection = Connection_DB()
        my_DB = connection.cursor()
        sql = "SELECT * FROM calificaciones"
        my_DB.execute(sql)
        names_users = my_DB.fetchall()
        for user in names_users:
            print("Id     Cedula     Promedio")
            print(f"{user[0]}      {user[1]}       {user[6]}")

    def Search_Student_Scores(self):
        valid = Validation_User(self.cedula)
        if not valid:
            print("Estudiante Encontrado")
            connection = Connection_DB()
            my_DB = connection.cursor()
            name = (f"{self.cedula}",)
            sql = "SELECT * FROM calificaciones WHERE cedula= %s"
            my_DB.execute(sql, name)
            names_users = my_DB.fetchall()
            for user in names_users:
                print("Id     Cedula     Promedio")
                print(f"{user[0]}      {user[1]}       {user[6]}")
        else:
            print("Estudiante no registrado!!!")

    def Modifity_Student_Scores(self):
        valid = Validation_User(self.cedula)
        if not valid:
            print("Estudiante Encontrado")
            print("Ingrese las notas del estudiante a modificar")
            nota1 = Validation_Score(1)
            nota2 = Validation_Score(2)
            nota3 = Validation_Score(3)
            nota4 = Validation_Score(4)
            print(f"Notas {nota1}, {nota2}, {nota3}, {nota4}")
            confirmation = input(f"Confirme las notas ingresado. (S/N): ")
            if confirmation == "S" or confirmation == "s":
                self.promedio = (nota1 + nota2 + nota3 + nota4) // 4
                connection = Connection_DB()
                my_DB = connection.cursor()
                student_update = (f"{self.cedula}", f"{self.promedio}", f"{self.cedula}")
                sql = "UPDATE calificaciones set cedula= %s, promedio= %s WHERE cedula= %s"
                my_DB.execute(sql, student_update)
                connection.commit()
                print("Notas del estudiante modificadas exitosamente")
            elif confirmation == "N" or confirmation == "n":
                print("Notas del estudiante no modificadas")
            else:
                print("Opcion no valida")
        else:
            print("Estudiante no registrado!!!")

    def Delete_Student_Scores(self):
        valid = Validation_User(self.cedula)
        if not valid:
            print("Estudiante Encontrado")
            confirmation = input("Confirme la eliminacion de las notas del estudiante (S/N): ")
            if confirmation == "S" or confirmation == "s":
                connection = Connection_DB()
                my_DB = connection.cursor()
                cedula = (f"{self.cedula}",)
                sql = "DELETE FROM calificaciones WHERE cedula= %s"
                my_DB.execute(sql, cedula)
                connection.commit()
                print("Notas eliminadas exitosamente")
            elif confirmation == "N" or confirmation == "n":
                print("Notas no eliminadas")
            else:
                print("Opcion no valida")
        else:
            print("Estudiante no registrado!!!")
