# En vista de la crisis mundial que estamos viviendo debido a la la pandemia generada por el Covid-19, se está
# produciendo una cantidad de información sin precedente alguno. Por tal razón, se necesita crear un programa que
# permita llevar su control. En este sentido, se requiere: Permitir el registro de los datos básicos
# (nombre, apellido, fecha de nacimiento, país de residencia, género) de las personas que representan casos sospechosos.
# -Proporcionar la opción de cambiar el estatus de la persona de sospechoso a activo (en caso de tener el virus)
# o inactivo (en caso de ser una falsa sospecha).
# Además, se podrá indicar cuáles casos activos se han recuperado y cuáles lamentablemente han fallecido.
# -Proporcionar la opción de ver cuántos casos sospechosos, confirmados, descartados, recuperados y fallecidos hay
# hasta el momento, por país, en todo el mundo, por género y por edad (niños, adultos y ancianos).
# -Proporcionar la opción de saber los datos de la persona de mayor y menor edad en condición de sospechoso, confirmado,
# descartado, recuperado y fallecido.
# Nota: Para cambiar el estatus de sospechoso a activo o inactivo, se tendrán que ir indicando los síntomas que presenta
# y basado en ello el programa determinará si lo posee o no. En caso de que el resultado sea negativo,
# le indicará la condición que realmente tiene. (Simularán esto tomando como referencia la información que
# se maneja sobre la diferencia entre los síntomas de un resfriado común, una alergia y el virus en cuestión)


class Usuario:
    def __init__(self, nombre, apellido, fecha, pais, genero):
        self.informe = {
            "condition": True,  # True = Vivo / False = Fallecido
            "status": False,  # Todo es falso hasta que se demuestre lo contario (En Analisis = false)
            "virus": False  # No es portador del virus
        }
        self.nombre = nombre
        self.apellido = apellido
        self.fecha = fecha
        self.pais = pais
        self.genero = genero

    def mostrar_atributos(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Fecha de Nacimiento: {self.fecha}")
        print(f"Pais: {self.pais}")
        print(f"Sexo: {self.genero}")
        print(f"Informe:"
              f"\tCondicion: {self.informe['condition']}"
              f"\tStatus: {self.informe['status']}"
              f"\tVirus: {self.informe['virus']}"
              )

    def virus_status(self):
        if self.informe["status"]:
            if self.informe["virus"]:
                return "Virus Activo"
            else:
                return "Virus Inactivo"
        else:
            return "En Analisis"

    def get_condition(self):
        return "Vivo" if self.informe["condition"] else "Fallecido"


def registrar_usuario():
    datos = [
        input("Nombre: ").strip(),
        input("Apellido: ").strip(),
        input("Fecha de Nacimiento: ").strip(),
        input("Pais de Residencia: ").strip(),
        input("Sexo: ").strip()
    ]
    nuevo_usuario = Usuario(datos[0], datos[1], datos[2], datos[3], datos[4])
    return nuevo_usuario


def mostrar_menu():
    opcion_valida = False
    while not opcion_valida:
        print(" 1. Registrar Caso Sospechoso.")
        print(" 2. Modificar Casos Registrados.")
        print(" 3. Mostrar Casos Registrados.")
        print(" 4. Salir.")
        try:
            opcion = int(input("Opcion: "))
        except ValueError:
            print("\"Escoja una opcion valida\"")
        else:
            if 1 <= opcion <= 3:
                opcion_valida = True
            elif opcion == 4:
                exit("Gracias por usar el registro de casos Covid-19")  # Finalizar Programa
            else:
                print("\"Escoja una opcion valida\"")
    return opcion


def chequear_estado_paciente(usuario):
    if usuario.informe["condition"]:  # Si esta vivo
        if usuario.informe["status"]:  # Ya tiene resultado de los analisis
            if (usuario in registros["contagiados"]) and not usuario.informe["virus"]:  # No es portador del virus
                registros["contagiados"].remove(usuario)
                registros["recuperados"].append(usuario)
                print("El paciente esta curado.")
        else:
            print("Esperando Resultado de los Analisis")
    else:  # Si ha fallecido
        if usuario in registros["sospechosos"]:
            registros["sospechosos"].remove(usuario)
        if usuario in registros["contagiados"]:
            registros["sospechosos"].remove(usuario)
        if usuario in registros["recuperados"]:
            registros["sospechosos"].remove(usuario)
        registros["fallecidos"].append(usuario)
        print("El paciente ha fallecido.")


def volver_al_menu_msg():
    while True:
        volver = input("Desea volver al Menu Principal? (Y/N): ").lower()
        if volver == "y":
            return True
        elif volver == "n":
            return False


registros = {
    "sospechosos": [],
    "contagiados": [],
    "recuperados": [],
    "fallecidos": [],
    "sintomas": {
        "covid19": ["secreciones nasales", "dolor de garganta", "tos", "fiebre", "dificultad para respirar"],
        ""
    }
}

print(end="\n\n")
print("Bienvenido al registro de Covid-19")
while True:
    opcion_seleccionada = mostrar_menu()
    if opcion_seleccionada == 1:  # Registrar Usuario Sospechoso
        desea_continuar = True
        while desea_continuar:
            try:
                registros["sospechosos"].append(registrar_usuario())
            except:
                print("Hubo un error al registrar el usuario por favor intentelo de nuevo")
            else:
                print("\t Se ha registrado el usuario exitosamente en la lista de sospechosos.", end="\n\n")
                desea_continuar = volver_al_menu_msg()
    elif opcion_seleccionada == 2:  # Modificar Casos

    else:  # Mostrar Registros
        pass
