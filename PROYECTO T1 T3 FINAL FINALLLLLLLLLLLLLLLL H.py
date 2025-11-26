# ================================
# SISTEMA DE GESTIÓN DE RECURSOS HUMANOS Y PROYECTOS
# ================================


# ================================
# FUNCIONES DEL MENÚ PRINCIPAL
# ================================

def mostrar_menu_principal():
    print("\n" + "=" * 50)
    print("       SISTEMA INTEGRAL DE GESTIÓN DE RRHH")
    print("=" * 50)
    print("1. Registrar nuevo empleado en el sistema")
    print("2. Crear nuevo proyecto empresarial")
    print("3. Asignar proyecto a empleado específico")
    print("4. Validar factibilidad económica de proyecto")
    print("5. Mostrar reporte general del sistema")
    print("6. Mostrar información de cada empleado")
    print("7. SALIR del sistema")
    print("=" * 50)


def crear_nuevo_empleado(lista_empleados):
    print("\n" + "-" * 50)
    print("   REGISTRO DE NUEVO EMPLEADO")
    print("-" * 50)
    
    while True:
        nombre_completo = input("Ingrese nombre y apellido del empleado: ").strip()
        if nombre_completo and len(nombre_completo) >= 3:
            break
        print("Error: El nombre debe tener al menos 3 caracteres")
    
    while True:
        try:
            salario_base = float(input("Ingrese salario base del empleado: "))
            if salario_base > 0:
                break
            print("Error: El salario debe ser un valor positivo")
        except ValueError:
            print("Error: Debe ingresar un valor numérico válido")
    
    print("\nSeleccione el tipo de empleado a registrar:")
    print("1. Desarrollador de software")
    print("2. Diseñador gráfico/UX/UI")
    print("3. Gerente de departamento")
    
    while True:
        tipo_empleado = input("Opción seleccionada (1-3): ").strip()
        if tipo_empleado in ["1", "2", "3"]:
            break
        print("Error: Debe seleccionar una opción entre 1 y 3")
    
    if tipo_empleado == "1":
        lenguajes = input("Ingrese lenguajes de programación (separados por coma): ").split(",")
        nivel_experiencia = input("Nivel de experiencia (Junior/SemiSenior/Senior): ").strip()
        nuevo_empleado = Desarrollador(nombre_completo, salario_base, lenguajes, nivel_experiencia)
        
    elif tipo_empleado == "2":
        herramientas = input("Ingrese herramientas de diseño (separadas por coma): ").split(",")
        especialidad = input("Especialidad (UI/UX/Gráfico): ").strip()
        nuevo_empleado = Diseñador(nombre_completo, salario_base, herramientas, especialidad)
        
    elif tipo_empleado == "3":
        departamento = input("Departamento de gerencia: ").strip()
        nuevo_empleado = Gerente(nombre_completo, salario_base, departamento)
    
    # SIN APPEND - usando concatenación
    lista_empleados = lista_empleados + [nuevo_empleado]
    print("\nEmpleado registrado exitosamente")
    print(f"ID: {nuevo_empleado.obtener_id_empleado()}")
    print(f"Nombre: {nuevo_empleado.obtener_nombre_completo()}")
    print(f"Tipo: {nuevo_empleado.tipo_empleado}")
    return lista_empleados  # Importante: retornar la lista actualizada


def crear_nuevo_proyecto(lista_proyectos):
    print("\n" + "-" * 50)
    print("   CREACIÓN DE NUEVO PROYECTO")
    print("-" * 50)
    
    while True:
        nombre_proyecto = input("Ingrese nombre del proyecto: ").strip()
        if nombre_proyecto and len(nombre_proyecto) >= 2:
            break
        print("Error: El nombre del proyecto debe tener al menos 2 caracteres")
    
    while True:
        try:
            presupuesto_asignado = float(input("Ingrese presupuesto asignado al proyecto: "))
            if presupuesto_asignado > 0:
                break
            print("Error: El presupuesto debe ser un valor positivo")
        except ValueError:
            print("Error: Debe ingresar un valor numérico válido")
    
    nuevo_proyecto = Proyecto(nombre_proyecto, presupuesto_asignado)
    
    # SIN APPEND - usando concatenación
    lista_proyectos = lista_proyectos + [nuevo_proyecto]
    print("\nProyecto creado exitosamente")
    print(f"Nombre: {nuevo_proyecto.nombre_proyecto}")
    print(f"ID: {nuevo_proyecto.id_proyecto}")
    print(f"Presupuesto: ${nuevo_proyecto.presupuesto_asignado:,.2f}")
    return lista_proyectos  # Importante: retornar la lista actualizada


def asignar_proyecto_empleado(lista_empleados, lista_proyectos):
    print("\n" + "-" * 50)
    print("   ASIGNACIÓN DE PROYECTO A EMPLEADO")
    print("-" * 50)
    
    if not lista_empleados:
        print("Error: No hay empleados registrados en el sistema")
        return lista_empleados, lista_proyectos
    
    if not lista_proyectos:
        print("Error: No hay proyectos creados en el sistema")
        return lista_empleados, lista_proyectos
    
    print("\nLISTA DE EMPLEADOS DISPONIBLES")
    for empleado in lista_empleados:
        info_basica = empleado.obtener_informacion_empleado()
        if hasattr(empleado, 'tipo_empleado'):
            info_basica += f", Tipo: {empleado.tipo_empleado}"
        print(info_basica)
    
    while True:
        try:
            id_empleado = int(input("\nIngrese ID del empleado a asignar: "))
            empleado_seleccionado = None
            
            for empleado in lista_empleados:
                if empleado.obtener_id_empleado() == id_empleado:
                    empleado_seleccionado = empleado
                    break
            
            if empleado_seleccionado:
                break
            else:
                print("Error: No existe un empleado con ese ID")
        except ValueError:
            print("Error: Debe ingresar un número válido")
    
    print("\nLISTA DE PROYECTOS DISPONIBLES")
    for indice, proyecto in enumerate(lista_proyectos):
        print(f"{indice + 1}. {proyecto.obtener_informacion_proyecto()}")
    
    while True:
        try:
            seleccion = int(input("\nSeleccione el número del proyecto a asignar: "))
            if 1 <= seleccion <= len(lista_proyectos):
                proyecto_seleccionado = lista_proyectos[seleccion - 1]
                break
            else:
                print(f"Error: Debe seleccionar un número entre 1 y {len(lista_proyectos)}")
        except ValueError:
            print("Error: Debe ingresar un número válido")
    
    try:
        empleado_seleccionado.asignar_proyecto_empleado(proyecto_seleccionado)
        print("Asignación realizada exitosamente")
    except ValueError as error:
        print(f"Error en asignación: {error}")
    
    return lista_empleados, lista_proyectos


def validar_factibilidad_proyecto(lista_proyectos):
    print("\n" + "-" * 50)
    print("   VALIDACIÓN DE FACTIBILIDAD DE PROYECTO")
    print("-" * 50)
    
    if not lista_proyectos:
        print("Error: No hay proyectos creados en el sistema")
        return
    
    print("\nLISTA DE PROYECTOS DISPONIBLES")
    for indice, proyecto in enumerate(lista_proyectos):
        print(f"{indice + 1}. {proyecto.obtener_informacion_proyecto()}")
    
    while True:
        try:
            seleccion = int(input("\nSeleccione el número del proyecto a validar: "))
            if 1 <= seleccion <= len(lista_proyectos):
                proyecto_seleccionado = lista_proyectos[seleccion - 1]
                break
            else:
                print(f"Error: Debe seleccionar un número entre 1 y {len(lista_proyectos)}")
        except ValueError:
            print("Error: Debe ingresar un número válido")
    
    costo_total = proyecto_seleccionado.calcular_costo_total_proyecto()
    es_factible = proyecto_seleccionado.verificar_factibilidad_proyecto()
    
    print("\nRESULTADO DE VALIDACIÓN")
    print(f"Proyecto: {proyecto_seleccionado.nombre_proyecto}")
    print(f"Presupuesto asignado: ${proyecto_seleccionado.presupuesto_asignado:,.2f}")
    print(f"Costo total calculado: ${costo_total:,.2f}")
    print(f"Empleados asignados: {len(proyecto_seleccionado.lista_empleados_asignados)}")
    
    if es_factible:
        margen = proyecto_seleccionado.presupuesto_asignado - costo_total
        print("RESULTADO: El proyecto ES FACTIBLE económicamente")
        print(f"Margen disponible: ${margen:,.2f}")
    else:
        deficit = costo_total - proyecto_seleccionado.presupuesto_asignado
        print("RESULTADO: El proyecto NO ES FACTIBLE económicamente")
        print(f"Deficit presupuestario: ${deficit:,.2f}")


def generar_reporte_general(lista_empleados, lista_proyectos):
    print("\n" + "=" * 60)
    print("           REPORTE GENERAL DEL SISTEMA")
    print("=" * 60)
    
    print("\nESTADÍSTICAS DE EMPLEADOS")
    print(f"Total de empleados registrados: {len(lista_empleados)}")
    
    if lista_empleados:
        desarrolladores = [e for e in lista_empleados if isinstance(e, Desarrollador)]
        diseñadores = [e for e in lista_empleados if isinstance(e, Diseñador)]
        gerentes = [e for e in lista_empleados if isinstance(e, Gerente)]
        
        print(f"  Desarrolladores: {len(desarrolladores)}")
        print(f"  Diseñadores: {len(diseñadores)}")
        print(f"  Gerentes: {len(gerentes)}")
        
        empleados_con_proyectos = [e for e in lista_empleados if e.obtener_cantidad_proyectos() > 0]
        print(f"Empleados con proyectos asignados: {len(empleados_con_proyectos)}")
    
    print("\nESTADÍSTICAS DE PROYECTOS")
    print(f"Total de proyectos creados: {len(lista_proyectos)}")
    
    if lista_proyectos:
        proyectos_factibles = [p for p in lista_proyectos if p.verificar_factibilidad_proyecto()]
        proyectos_no_factibles = [p for p in lista_proyectos if not p.verificar_factibilidad_proyecto()]
        
        print(f"  Proyectos factibles: {len(proyectos_factibles)}")
        print(f"  Proyectos no factibles: {len(proyectos_no_factibles)}")
        
        proyectos_sin_empleados = [p for p in lista_proyectos if len(p.lista_empleados_asignados) == 0]
        print(f"Proyectos sin empleados asignados: {len(proyectos_sin_empleados)}")
    
    print("\n" + "=" * 60)


def mostrar_informacion_empleados(lista_empleados):
    print("\n" + "=" * 60)
    print("       INFORMACIÓN DETALLADA DE EMPLEADOS")
    print("=" * 60)
    
    if not lista_empleados:
        print("No hay empleados registrados en el sistema")
        return
    
    for empleado in lista_empleados:
        print("\n" + "-" * 50)
        print(empleado.obtener_informacion_completa())
        print("-" * 50)


# ================================
# DEFINICIÓN DE CLASES DEL SISTEMA
# ================================

class Empleado:
    contador_id_empleado = 1
    
    def __init__(self, nombre_completo, salario_base):
        self.id_empleado = Empleado.contador_id_empleado
        Empleado.contador_id_empleado += 1
        self.nombre_completo = nombre_completo
        self.salario_base = salario_base
        self.lista_proyectos = []
        self.activo = True
    
    def obtener_id_empleado(self):
        return self.id_empleado
    
    def obtener_nombre_completo(self):
        return self.nombre_completo
    
    def calcular_salario_total(self):
        return self.salario_base
    
    def asignar_proyecto_empleado(self, proyecto):
        for proyecto_existente in self.lista_proyectos:
            if proyecto_existente.nombre_proyecto == proyecto.nombre_proyecto:
                raise ValueError("El empleado ya está asignado a este proyecto")
        
        if len(self.lista_proyectos) >= 3:
            raise ValueError("Límite máximo de 3 proyectos alcanzado")
        
        # SIN APPEND - usando concatenación
        self.lista_proyectos = self.lista_proyectos + [proyecto]
        proyecto.agregar_empleado_proyecto(self)
        print(f"Proyecto '{proyecto.nombre_proyecto}' asignado a {self.nombre_completo}")
    
    def obtener_cantidad_proyectos(self):
        return len(self.lista_proyectos)
    
    def obtener_informacion_empleado(self):
        return (f"ID: {self.id_empleado}, Nombre: {self.nombre_completo}, "
                f"Proyectos: {self.obtener_cantidad_proyectos()}")
    
    def obtener_informacion_completa(self):
        info = f"ID: {self.id_empleado}\n"
        info += f"Nombre completo: {self.nombre_completo}\n"
        info += f"Salario base: ${self.salario_base:,.2f}\n"
        info += f"Salario total: ${self.calcular_salario_total():,.2f}\n"
        info += f"Proyectos asignados: {self.obtener_cantidad_proyectos()}\n"
        
        if self.lista_proyectos:
            info += "Proyectos:\n"
            for proyecto in self.lista_proyectos:
                info += f"  - {proyecto.nombre_proyecto}\n"
        else:
            info += "Proyectos: Ninguno asignado\n"
            
        return info


class Desarrollador(Empleado):
    def __init__(self, nombre_completo, salario_base, lenguajes_programacion, nivel_experiencia):
        super().__init__(nombre_completo, salario_base)
        self.lenguajes_programacion = [lenguaje.strip() for lenguaje in lenguajes_programacion]
        self.nivel_experiencia = nivel_experiencia
        self.tipo_empleado = "Desarrollador"
    
    def calcular_salario_total(self):
        salario_calculado = self.salario_base
        if self.nivel_experiencia.lower() == "senior":
            salario_calculado *= 1.25
        elif self.nivel_experiencia.lower() == "semisenior":
            salario_calculado *= 1.15
        return salario_calculado
    
    def obtener_porcentaje_bonificacion(self):
        if self.nivel_experiencia.lower() == "senior":
            return 25
        elif self.nivel_experiencia.lower() == "semisenior":
            return 15
        return 0
    
    def obtener_informacion_completa(self):
        info = super().obtener_informacion_completa()
        info += f"Tipo de empleado: {self.tipo_empleado}\n"
        info += f"Nivel de experiencia: {self.nivel_experiencia}\n"
        info += f"Lenguajes: {', '.join(self.lenguajes_programacion)}\n"
        info += f"Bonificación aplicada: {self.obtener_porcentaje_bonificacion()}%\n"
        return info


class Diseñador(Empleado):
    def __init__(self, nombre_completo, salario_base, herramientas_diseno, especialidad_diseno):
        super().__init__(nombre_completo, salario_base)
        self.herramientas_diseno = [herramienta.strip() for herramienta in herramientas_diseno]
        self.especialidad_diseno = especialidad_diseno
        self.tipo_empleado = "Diseñador"
    
    def calcular_salario_total(self):
        salario_calculado = self.salario_base
        if self.especialidad_diseno.lower() in ["ui", "ux"]:
            salario_calculado *= 1.20
        return salario_calculado
    
    def obtener_informacion_completa(self):
        info = super().obtener_informacion_completa()
        info += f"Tipo de empleado: {self.tipo_empleado}\n"
        info += f"Especialidad: {self.especialidad_diseno}\n"
        info += f"Herramientas: {', '.join(self.herramientas_diseno)}\n"
        
        if self.especialidad_diseno.lower() in ["ui", "ux"]:
            info += "Bonificación aplicada: 20%\n"
        else:
            info += "Bonificación aplicada: 0%\n"
        return info


class Gerente(Empleado):
    def __init__(self, nombre_completo, salario_base, departamento_gerencia):
        super().__init__(nombre_completo, salario_base)
        self.departamento_gerencia = departamento_gerencia
        self.tipo_empleado = "Gerente"
    
    def calcular_salario_total(self):
        return self.salario_base * 1.35
    
    def obtener_informacion_completa(self):
        info = super().obtener_informacion_completa()
        info += f"Tipo de empleado: {self.tipo_empleado}\n"
        info += f"Departamento: {self.departamento_gerencia}\n"
        info += "Bonificación aplicada: 35%\n"
        return info


class Proyecto:
    contador_id_proyecto = 1
    
    def __init__(self, nombre_proyecto, presupuesto_asignado):
        self.id_proyecto = Proyecto.contador_id_proyecto
        Proyecto.contador_id_proyecto += 1
        self.nombre_proyecto = nombre_proyecto
        self.presupuesto_asignado = presupuesto_asignado
        self.lista_empleados_asignados = []
        self.estado_proyecto = "Planificación"
    
    def agregar_empleado_proyecto(self, empleado):
        # SIN APPEND - usando concatenación
        self.lista_empleados_asignados = self.lista_empleados_asignados + [empleado]
    
    def calcular_costo_total_proyecto(self):
        costo_total = 0
        for empleado in self.lista_empleados_asignados:
            costo_total += empleado.calcular_salario_total()
        return costo_total
    
    def verificar_factibilidad_proyecto(self):
        costo_total = self.calcular_costo_total_proyecto()
        return costo_total <= self.presupuesto_asignado
    
    def obtener_informacion_proyecto(self):
        return (f"ID: {self.id_proyecto}, Nombre: {self.nombre_proyecto}, "
                f"Empleados: {len(self.lista_empleados_asignados)}, "
                f"Presupuesto: ${self.presupuesto_asignado:,.2f}")


# ================================
# PROGRAMA PRINCIPAL
# ================================

def main():
    lista_empleados = []
    lista_proyectos = []
    
    print("BIENVENIDO AL SISTEMA DE GESTIÓN DE RRHH Y PROYECTOS")
    print("Sistema inicializado correctamente")
    
    while True:
        try:
            mostrar_menu_principal()
            opcion = input("Seleccione una opción del menú (1-7): ").strip()
            
            if opcion == "1":
                lista_empleados = crear_nuevo_empleado(lista_empleados)
            elif opcion == "2":
                lista_proyectos = crear_nuevo_proyecto(lista_proyectos)
            elif opcion == "3":
                lista_empleados, lista_proyectos = asignar_proyecto_empleado(lista_empleados, lista_proyectos)
            elif opcion == "4":
                validar_factibilidad_proyecto(lista_proyectos)
            elif opcion == "5":
                generar_reporte_general(lista_empleados, lista_proyectos)
            elif opcion == "6":
                mostrar_informacion_empleados(lista_empleados)
            elif opcion == "7":
                print("\n" + "=" * 50)
                print("   GRACIAS POR USAR EL SISTEMA DE GESTIÓN")
                print("           ¡HASTA PRONTO!")
                print("=" * 50)
                break
            else:
                print("Error: Opción no válida. Seleccione 1-7")
                
        except KeyboardInterrupt:
            print("\nOperación cancelada por el usuario")
            break
        except Exception as error:
            print(f"Error inesperado: {error}")


if __name__ == "__main__":
    main()