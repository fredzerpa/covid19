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
    print()
    datos = [
        input("Nombre: ").strip().capitalize(),
        input("Apellido: ").strip().capitalize(),
        input("Fecha de Nacimiento: ").strip().capitalize(),
        input("Pais de Residencia: ").strip().capitalize(),
        input("Sexo: ").strip().capitalize()
    ]
    nuevo_usuario = Usuario(datos[0], datos[1], datos[2], datos[3], datos[4])
    return nuevo_usuario


def mostrar_menu_principal():
    opcion_valida = False
    print(end="\n\n")
    print("Bienvenido al registro de Covid-19")
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


def mostrar_menu_opciones():
    opcion_valida = False
    print(end="\n\n")
    print("Por favor escoja una opcion para continuar:")
    while not opcion_valida:
        print(" 1. Sospechosos.")
        print(" 2. Descartados.")
        print(" 3. Contagiados.")
        print(" 4. Recuperados.")
        print(" 5. Fallecidos.")
        try:
            opcion = int(input("Opcion: "))
        except ValueError:
            print("\"Escoja una opcion valida\"")
        else:
            if 1 <= opcion <= 5:
                opcion = "sospechosos" if opcion == 1 else "descartados" if opcion == 2 else "contagiados" if opcion == 3 else "recuperados" if opcion == 4 else "fallecidos"
                opcion_valida = True
            else:
                print("\"Escoja una opcion valida\"")
    return opcion


def validar_opciones_validas(max_num_opciones, text_input="Opcion: "):
    while True:
        try:
            opcion_seleccionada = int(input(text_input))
        except ValueError:
            print("\"Escoja una opcion valida\"")
        else:
            if 1 <= opcion_seleccionada <= max_num_opciones:
                return opcion_seleccionada
            else:
                print("\"Escoja una opcion valida\"")


def mostrar_usuarios(registros, opcion):
    print(end="\n\n")
    for usuario in registros[opcion]:
        print(f"Nombre: {usuario.nombre} {usuario.apellido}")
        print(f"Fecha de Nacimiento: {usuario.fecha}")
        print(f"Pais: {usuario.pais}")
        print(f"Sexo: {usuario.genero}")
        print(f"Informe")
        condicion = "Vivo" if usuario.informe["condition"] else "Fallecido"
        print(f"\tCondicion: {condicion}")
        estado = "Resultados Listos" if usuario.informe["status"] else "En Analisis"
        print(f"\tStatus: {estado}")
        virus = "Positivo" if usuario.informe["virus"] else "Negativo"
        print(f"\tVirus: {virus}")
        print()


def editar_usuarios(registros, opcion):
    contador = 0
    print(end="\n\n")
    print("Indique el Numero que desea modificar: ")
    for usuario in registros[opcion]:
        contador += 1
        print(f"{contador}. {usuario.nombre} {usuario.apellido}")
    caso = validar_opciones_validas(contador, "Caso # ")

    print(end="\n\n")
    print(f"\t {registros[opcion][caso - 1].nombre} {registros[opcion][caso - 1].apellido}")
    print(f"Condicion del Usuario:")
    print("1. Vivo")
    print("2. Fallecido")
    condicion_seleccionada = validar_opciones_validas(2)
    registros[opcion][caso - 1].informe["condition"] = True if condicion_seleccionada == 1 else False

    if registros[opcion][caso - 1].informe["condition"]:  # Si esta Vivo
        print()
        print("Estado del Analisis:")
        print("1. En Proceso")
        print("2. Con Resultados")
        status_seleccionado = validar_opciones_validas(2)
        registros[opcion][caso - 1].informe["status"] = False if status_seleccionado == 1 else True

        if registros[opcion][caso - 1].informe["status"]:  # Si posee Covid-19
            print()
            es_covid = chequear_tipo_virus(registros["sintomas"]["covid19"], registros["sintomas"]["resfriado"],
                                           registros["sintomas"]["alergia"])
            registros[opcion][caso - 1].informe["virus"] = es_covid  # False si no es COVID

    print(f"\t Se ha modificado exitosamente ha "
          f"{registros[opcion][caso - 1].nombre} {registros[opcion][caso - 1].apellido}")
    chequear_estado_usuarios(registros[opcion][caso - 1])  # Refresh del usuario editado


def chequear_estado_usuarios(usuario):
    if usuario.informe["condition"]:  # Si esta vivo
        if usuario.informe["status"]:  # Ya tiene resultado de los analisis
            if usuario in registros["contagiados"]:  # Esta Registrado como Portador
                if not usuario.informe["virus"]:  # Ya no es Portador
                    borrar_registros_usuario(usuario)
                    registros["recuperados"].append(usuario)
                    print(f"{usuario.nombre} {usuario.apellido} ha sido registrado en los registros de recuperados.")
            else:  # No es Registrado como Portador
                if usuario.informe["virus"]:  # Es portador del Virus
                    borrar_registros_usuario(usuario)
                    registros["contagiados"].append(usuario)
                    print(f"{usuario.nombre} {usuario.apellido} ha sido registrado en los registros de contagiados.")
                else:  # No es Portador
                    borrar_registros_usuario(usuario)
                    registros["descartados"].append(usuario)
                    print(f"{usuario.nombre} {usuario.apellido} ha sido registrado en los registros de descartados.")

        elif usuario not in registros["sospechosos"]:  # No posee Analisis Y No esta Registrado como Sospechoso
            borrar_registros_usuario(usuario)
            registros["sospechosos"].append(usuario)
            print(f"{usuario.nombre} {usuario.apellido} esta en espera de los resultados de analisis.")

    else:  # Si ha fallecido
        if usuario not in registros["fallecidos"]:  # No esta Registrado como Fallecido
            borrar_registros_usuario(usuario)
            registros["fallecidos"].append(usuario)
            print(f"{usuario.nombre} {usuario.apellido} ha sido registrado en los registros de fallecidos.")


def borrar_registros_usuario(usuario):
    if usuario in registros["sospechosos"]:
        registros["sospechosos"].remove(usuario)
    if usuario in registros["contagiados"]:
        registros["contagiados"].remove(usuario)
    if usuario in registros["recuperados"]:
        registros["recuperados"].remove(usuario)
    if usuario in registros["fallecidos"]:
        registros["fallecidos"].remove(usuario)


def volver_al_menu_msg():
    while True:
        volver = input("Desea volver al Menu Principal? (Y/N): ").lower()
        if volver == "y":
            return True
        elif volver == "n":
            return False


def chequear_tipo_virus(covid19, resfriado, alergia):  # Retorna True por COVID else False
    contador = 0
    print("Registro de Sintomas del Paciente", end="\n\n")
    total_sintomas = covid19 + resfriado + alergia
    for sintoma in total_sintomas:
        contador += 1
        if contador % 5 == 0:
            print(f"{contador}.{sintoma}")
        else:
            print(f"{contador}.{sintoma}", end=", ")
    print(end="\n\n")
    print("Por favor escriba el numero de los sintomas que presenta separados por una coma \",\"")
    while True:
        try:
            sintomas_numeros = input("Sintomas: ")
            lista_sintomas = sintomas_numeros.split(",")
            for i in range(len(lista_sintomas)):
                lista_sintomas[i] = lista_sintomas[i].strip()
                lista_sintomas[i] = total_sintomas[int(lista_sintomas[i]) - 1]
        except:
            print()
            print("\t Hubo un Error al registrar el usuario por favor intentelo de nuevo")
            print()
        else:
            print("En base a los sintomas:", ", ".join(lista_sintomas))
            break

    sintomas_parecidos_covid = list(set(lista_sintomas) & set(covid19))
    sintomas_parecidos_resfriado = list(set(lista_sintomas) & set(resfriado))
    sintomas_parecidos_alergia = list(set(lista_sintomas) & set(alergia))

    # En base a la cantidad de sintomas parecidos a una enfermedad se escoje la enfermedad
    if (len(sintomas_parecidos_covid) >= len(sintomas_parecidos_resfriado)) and \
            (len(sintomas_parecidos_covid) >= len(sintomas_parecidos_alergia)):
        print("El sintoma mas probable es Corona Virus.")
        return True
    elif (len(sintomas_parecidos_resfriado) >= len(sintomas_parecidos_covid)) and \
            (len(sintomas_parecidos_resfriado) >= len(sintomas_parecidos_alergia)):
        print("El sintoma mas probable es Alergia.")
        return False
    else:
        print("El sintoma mas probable es Alergia")
        return False


registros = {
    "sospechosos": [],
    "descartados": [],
    "contagiados": [],
    "recuperados": [],
    "fallecidos": [],
    "sintomas": {
        "covid19": ["Tos Seca", "Fiebre", "Cansancio", "Congestion Nasal", "Secrecion Nasal", "Dolor de Garganta",
                    "Dolor de Cabeza", "Diarrea", "Dificultad para Respirar"],
        "resfriado": ["Tos con Flema", "Fiebre", "Congestion Nasal", "Secrecion Nasal", "Dolor de Garganta",
                      "Dolor de Cabeza", "Dolor Muscular", "Cansancio"],
        "alergia": ["Estornudos", "Congestion Nasal", "Secrecion Nasal", "Picazon", "Irritacion Ocular"]
    }
}

while True:

    opcion_seleccionada = mostrar_menu_principal()

    if opcion_seleccionada == 1:  # Registrar Usuario Sospechoso
        volver_al_menu = False
        while not volver_al_menu:
            try:
                registros["sospechosos"].append(registrar_usuario())
            except:
                print(end="\n\n")
                print("\t Hubo un Error al registrar el usuario por favor intentelo de nuevo")
                print(end="\n\n")
            else:
                print("\t Se ha registrado el usuario exitosamente en la lista de Sospechosos.", end="\n\n")
                volver_al_menu = volver_al_menu_msg()

    elif opcion_seleccionada == 2:  # Modificar Casos
        opcion_modificar = mostrar_menu_opciones()
        editar_usuarios(registros, opcion_modificar)

    else:  # Mostrar Registros
        opcion_mostrar = mostrar_menu_opciones()
        mostrar_usuarios(registros, opcion_mostrar)
