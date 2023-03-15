import re

from Model.Calificaciones import Scores
from Model.Estudiante import Student
from Model.Usuario import User
from Services.DataBase import Connection_DB

def Login(name, password):
    index = None
    i_db = 0
    user_validate = False
    connection = Connection_DB()
    my_DB = connection.cursor()
    my_DB.execute("SELECT nombre FROM usuarios")
    names_users = my_DB.fetchall()

    for user in names_users:
        if user[0] == name:
            user_validate = True
            break

    if user_validate:
        for user in names_users:
            if user[0] == name:
                index = names_users[i_db].index(name)
                break
            i_db += 1

        my_DB.execute("SELECT contrasena FROM usuarios")
        passwords_users = my_DB.fetchall()

        if passwords_users[i_db][index] == password:
            print(f"\nIngreso exitoso, {name}")
            return True
        else:
            print("\nContraseña incorrecta")
            return False

    else:
        print("Usuario no encontrado")
        print("Vuelva a intentar")
        return False


def Total_User():
    connection = Connection_DB()
    my_DB = connection.cursor()
    my_DB.execute("SELECT nombre FROM usuarios")
    total_users = my_DB.fetchall()
    return len(total_users)

def Validation_Score(a):
    while True:
        n = int(input(f"Ingrese la nota {a}: "))
        if n < 0 or n > 100:
            print("Debes ingresar la nota en el rango.")
            continue
        else:
            return n

def Validation_Response():
    while True:
        n = input("Confirme los datos a guardar (S/N): ")
        if n.upper() == "S":
            return n
        elif n.upper() == "N":
            return n
        else:
            continue

def Validation_Email():
    while True:
        email = input("Correo: ")
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',email.lower()):
            return email
        else:
            continue
def Menu_star():
    while True:
        print("\n-----Bienvenido-----")
        print("Para acceder al menu debe ingresar sesion")
        user = input("Usuario: ")
        password = input("Contraseña: ")
        status_login = Login(user, password)

        if status_login:
            while(True):
                print("\n-----Menu-----")
                print("a. Usuarios")
                print("b. Estudiantes")
                print("c. Calificaciones")
                print("d. Cerrar Sesión")
                print("e. Salir del programa")
                option = input("Opcion: ")

                if option == "a":
                    while(True):
                        print("\n---Usuarios---")
                        print("a. Ingresar usuario")
                        print("b. Listar usuarios")
                        print("c. Consultar un usuario")
                        print("d. Modificar usuario")
                        print("e. Eliminar usuario")
                        print("f. Salir al Menu Principal")
                        op_user = input("Opcion: ")

                        if op_user == "a":
                            while(True):
                                print("\nIngresando nuevo usuario")
                                user = input("Usuario: ")
                                password = input("Contraseña: ")
                                confirmed = Validation_Response()

                                if confirmed.upper() == "S":
                                    user_dto = User(user, password)
                                    user_dto.Login_User()
                                    validate = input("\nDesea seguir registrando usuarios (S/N): ")
                                    if validate.upper() == "N":
                                        break
                                    elif validate.upper() == "S":
                                        print("Vuela a registrar")
                                    else:
                                        print("Opcion invalida")

                                elif confirmed.upper() == "N":
                                    print("Usuario no registrado")
                                    validate = input("\nDesea seguir registrando usuarios (S/N): ")
                                    if validate.upper() == "N":
                                        break
                                    elif validate.upper() == "S":
                                        print("Vuela a registrar")
                                    else:
                                        print("Opcion invalida")

                                else:
                                    print("Opcion invalida!!")

                        elif op_user == "b":
                            user_dto = User("", "")
                            user_dto.Lists_User()

                        elif op_user == "c":
                            while(True):
                                print("\nConsulta")
                                user = input("Ingrese el usuario a consultar: ")
                                user_dto = User(user)
                                user_dto.Search_User()
                                validate = input("\nDesea seguir consultado usuarios (S/N): ")
                                if validate.upper() == "N":
                                    break
                                elif validate.upper() == "S":
                                    print("\nVuela a consultar")
                                else:
                                    print("Opcion invalida")

                        elif op_user == "d":
                            while(True):
                                print("\nModificar usuario")
                                user = input("Ingrese el usuario a modificar: ")
                                user_dto = User(user)
                                user_dto.Modifity_User()
                                validate = input("\nDesea seguir modificando usuarios (S/N): ")
                                if validate.upper() == "N":
                                    break
                                elif validate.upper() == "S":
                                    print("\nVuela a modificar")
                                else:
                                    print("Opcion invalida")

                        elif op_user == "e":
                            while(True):
                                print("\nEliminacion de usuario")
                                user = input("Ingrese el usuario a eliminar: ")
                                user_dto = User(user)
                                user_dto.Delete_User()
                                validate = input("\nDesea seguir eliminado usuarios (S/N): ")
                                if validate.upper() == "N":
                                    break
                                elif validate.upper() == "S":
                                    print("\nVuela a eliminar")
                                else:
                                    print("Opcion invalida")

                        elif op_user == "f":
                            break

                elif option == "b":
                    while (True):
                        print("\n---Estudiantes---")
                        print("a. Ingresar estudiante")
                        print("b. Consultar un estudiante")
                        print("c. Modificar estudiante")
                        print("d. Eliminar estudiante")
                        print("e. Salir al Menu Principal")
                        op_user = input("Opcion: ")

                        if op_user == "a":
                            while (True):
                                print("\nIngresando nuevo estudiante")
                                cedula = input("Cedula: ")
                                nombre = input("Nombre: ")
                                apellido = input("Apellido: ")
                                correo = Validation_Email()
                                celular = input("Celular: ")
                                confirmed = Validation_Response()

                                if confirmed.upper() == "S":
                                    student_dto = Student(cedula, nombre, apellido, correo, celular)
                                    student_dto.Login_Student()
                                    validate = input("\nDesea seguir registrando estudiantes (S/N): ")
                                    if validate.upper() == "N":
                                        break
                                    elif validate.upper() == "S":
                                        print("Vuela a registrar")
                                    else:
                                        print("Opcion invalida")

                                elif confirmed.upper() == "N":
                                    print("Estudiante no registrado")
                                    validate = input("\nDesea seguir registrando estudiantes (S/N): ")
                                    if validate.upper() == "N":
                                        break
                                    elif validate.upper() == "S":
                                        print("Vuela a registrar")
                                    else:
                                        print("Opcion invalida")

                                else:
                                    print("Opcion invalida!!")

                        elif op_user == "b":
                            while (True):
                                print("\nConsulta")
                                cedula = input("Ingrese la cedula del estudiante a consultar: ")
                                student_dto = Student(cedula)
                                student_dto.Search_Student()
                                validate = input("\nDesea seguir consultado estudiantes (S/N): ")
                                if validate.upper() == "N":
                                    break
                                elif validate.upper() == "S":
                                    print("\nVuela a consultar")
                                else:
                                    print("Opcion invalida")

                        elif op_user == "c":
                            while (True):
                                print("\nModificar Estudiante")
                                cedula = input("Ingrese la cedula del estudiante a modificar: ")
                                student_dto = Student(cedula)
                                student_dto.Modifity_Student()
                                validate = input("\nDesea seguir modificando estudiantes (S/N): ")
                                if validate.upper() == "N":
                                    break
                                elif validate.upper() == "S":
                                    print("\nVuela a modificar")
                                else:
                                    print("Opcion invalida")

                        elif op_user == "d":
                            while (True):
                                print("\nEliminacion de Estudiante")
                                cedula = input("Ingrese la cedula del estudiante a eliminar: ")
                                student_dto = Student(cedula)
                                student_dto.Delete_Student()
                                validate = input("\nDesea seguir eliminado estudiantes (S/N): ")
                                if validate.upper() == "N":
                                    break
                                elif validate.upper() == "S":
                                    print("\nVuela a eliminar")
                                else:
                                    print("Opcion invalida")

                        elif op_user == "e":
                            break

                elif option == "c":
                    while (True):
                        print("\n---Calificaciones---")
                        print("a. Ingresar calificaciones estudiante")
                        print("b. Listar todas las calificaciones de los estudiantes")
                        print("c. Consultar notas de un estudiante")
                        print("d. Modificar notas de un estudiante")
                        print("e. Eliminar notas de un estudiante")
                        print("f. Salir al Menu Principal")
                        op_user = input("Opcion: ")

                        if op_user == "a":
                            while (True):
                                cedula = input("\nIngrese cedula del estudiante: ")
                                print("\nIngresando notas de un estudiante")
                                nota1 = Validation_Score(1)
                                nota2 = Validation_Score(2)
                                nota3 = Validation_Score(3)
                                nota4 = Validation_Score(4)
                                print(f"Notas {nota1}, {nota2}, {nota3}, {nota4}")
                                confirmed = input(f"Confirme las notas ingresado. (S/N): ")
                                if confirmed.upper() == "S":
                                    promedio = (nota1+nota2+nota3+nota4)//4
                                    scores_dto = Scores(cedula, promedio)
                                    scores_dto.Insert_Scores()
                                    validate = input("\nDesea seguir registrando notas de estudiantes (S/N): ")
                                    if validate.upper() == "N":
                                        break
                                    elif validate.upper() == "S":
                                        print("Vuela a registrar")
                                    else:
                                        print("Opcion invalida")

                                elif confirmed.upper() == "N":
                                    print("Notas no registradas")
                                    validate = input("\nDesea seguir registrando estudiantes (S/N): ")
                                    if validate.upper() == "N":
                                        break
                                    elif validate.upper() == "S":
                                        print("Vuela a registrar")
                                    else:
                                        print("Opcion invalida")

                                else:
                                    print("Opcion invalida!!")

                        elif op_user == "b":
                            scores_dto = Scores("")
                            scores_dto.List_Scores()

                        elif op_user == "c":
                            while (True):
                                print("\nConsulta")
                                cedula = input("Ingrese la cedula del estudiante a consultar: ")
                                scores_dto = Scores(cedula)
                                scores_dto.Search_Student_Scores()
                                validate = input("\nDesea seguir consultado notas de estudiantes (S/N): ")
                                if validate.upper() == "N":
                                    break
                                elif validate.upper() == "S":
                                    print("\nVuela a consultar")
                                else:
                                    print("Opcion invalida")

                        elif op_user == "d":
                            while (True):
                                print("\nModificar notas del estudiante")
                                cedula = input("Ingrese la cedula del estudiante a modificar: ")
                                scores_dto = Scores(cedula)
                                scores_dto.Modifity_Student_Scores()
                                validate = input("\nDesea seguir modificando notas de estudiantes (S/N): ")
                                if validate.upper() == "N":
                                    break
                                elif validate.upper() == "S":
                                    print("\nVuela a modificar")
                                else:
                                    print("Opcion invalida")

                        elif op_user == "e":
                            while (True):
                                print("\nEliminacion de notas del estudiante")
                                cedula = input("Ingrese la cedula del estudiante a eliminar: ")
                                scores_dto = Scores(cedula)
                                scores_dto.Delete_Student_Scores()
                                validate = input("\nDesea seguir eliminado notas de estudiantes (S/N): ")
                                if validate.upper() == "N":
                                    break
                                elif validate.upper() == "S":
                                    print("\nVuela a eliminar")
                                else:
                                    print("Opcion invalida")

                        elif op_user == "f":
                            break

                elif option == "d":
                    print("Cerrando Sesión")
                    break
                elif option == "e":
                    print("Saliendo...")
                    exit(0)
                else:
                    print(f"Error opcion invalida {option}")
                    print("Ingrese una opcion valida!!!")


if __name__ == '__main__':
    Menu_star()