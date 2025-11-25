# ---------------------- SISTEMA DE GESTIÓN DE RECURSOS HUMANOS Y PROYECTOS ----------------------
# Sistema desarrollado para la gestión integral de empleados y proyectos empresariales
# Permite crear empleados, proyectos, asignaciones y validaciones de factibilidad

# ---------------------- DEFINICIÓN DE CLASES DEL SISTEMA ----------------------

class Empleado:
    # Contador para generar IDs únicos para cada empleado
    contadorIdEmpleado = 1
    
    def __init__(self, nombreCompleto, salarioBase):
        # Asignación de ID único y autoincremental
        self.idEmpleado = Empleado.contadorIdEmpleado
        Empleado.contadorIdEmpleado += 1
        self.nombreCompleto = nombreCompleto
        self.salarioBase = salarioBase
        self.listaProyectos = []  # Lista para almacenar proyectos asignados
        self.activo = True  # Estado del empleado
    
    def obtenerIdEmpleado(self):
        # Retorna el ID único del empleado
        return self.idEmpleado
    
    def obtenerNombreCompleto(self):
        # Retorna el nombre completo del empleado
        return self.nombreCompleto
    
    def calcularSalarioTotal(self):
        # Método base para cálculo de salario, será sobreescrito por clases hijas
        return self.salarioBase
    
    def asignarProyectoEmpleado(self, proyecto):
        # Valida que el empleado no esté ya asignado al proyecto
        for proyectoExistente in self.listaProyectos:
            if proyectoExistente.nombreProyecto == proyecto.nombreProyecto:
                raise ValueError("Error: El empleado ya se encuentra asignado a este proyecto específico")
        
        # Valida que el empleado no exceda el límite de 3 proyectos
        if len(self.listaProyectos) >= 3:
            raise ValueError("Error: Límite máximo de proyectos alcanzado. Un empleado no puede tener más de 3 proyectos asignados simultáneamente")
        
        # Asigna el proyecto al empleado y registra la asignación bidireccional
        self.listaProyectos.append(proyecto)
        proyecto.agregarEmpleadoProyecto(self)
        print(f"Proyecto '{proyecto.nombreProyecto}' asignado exitosamente al empleado {self.nombreCompleto}")
    
    def obtenerCantidadProyectos(self):
        # Retorna la cantidad de proyectos asignados
        return len(self.listaProyectos)
    
    def obtenerInformacionEmpleado(self):
        # Retorna información completa del empleado
        return f"ID: {self.idEmpleado}, Nombre: {self.nombreCompleto}, Proyectos: {self.obtenerCantidadProyectos()}"
    
    def obtenerInformacionCompleta(self):
        # Retorna información detallada del empleado
        info = f"ID: {self.idEmpleado}\n"
        info += f"Nombre completo: {self.nombreCompleto}\n"
        info += f"Salario base: ${self.salarioBase:,.2f}\n"
        info += f"Salario total: ${self.calcularSalarioTotal():,.2f}\n"
        info += f"Proyectos asignados: {self.obtenerCantidadProyectos()}\n"
        
        if self.listaProyectos:
            info += "Proyectos:\n"
            for proyecto in self.listaProyectos:
                info += f"  - {proyecto.nombreProyecto}\n"
        else:
            info += "Proyectos: Ninguno asignado\n"
            
        return info

class Desarrollador(Empleado):
    def __init__(self, nombreCompleto, salarioBase, lenguajesProgramacion, nivelExperiencia):
        # Inicialización de la clase padre
        super().__init__(nombreCompleto, salarioBase)
        self.lenguajesProgramacion = [lenguaje.strip() for lenguaje in lenguajesProgramacion]
        self.nivelExperiencia = nivelExperiencia
        self.tipoEmpleado = "Desarrollador"
    
    def calcularSalarioTotal(self):
        # Calcula salario con bonificaciones según nivel de experiencia
        salarioCalculado = self.salarioBase
        if self.nivelExperiencia.lower() == "senior":
            salarioCalculado = salarioCalculado * 1.25  # 25% de bonificación para seniors
        elif self.nivelExperiencia.lower() == "semisenior":
            salarioCalculado = salarioCalculado * 1.15  # 15% de bonificación para semi-seniors
        return salarioCalculado
    
    def obtenerInformacionEspecifica(self):
        # Retorna información específica del desarrollador
        return f"Lenguajes: {', '.join(self.lenguajesProgramacion)}, Nivel: {self.nivelExperiencia}"
    
    def obtenerInformacionCompleta(self):
        # Retorna información completa del desarrollador
        info = super().obtenerInformacionCompleta()
        info += f"Tipo de empleado: {self.tipoEmpleado}\n"
        info += f"Nivel de experiencia: {self.nivelExperiencia}\n"
        info += f"Lenguajes de programación: {', '.join(self.lenguajesProgramacion)}\n"
        info += f"Bonificación aplicada: {self.obtenerPorcentajeBonificacion()}%\n"
        return info
    
    def obtenerPorcentajeBonificacion(self):
        # Retorna el porcentaje de bonificación aplicado
        if self.nivelExperiencia.lower() == "senior":
            return 25
        elif self.nivelExperiencia.lower() == "semisenior":
            return 15
        return 0

class Diseñador(Empleado):
    def __init__(self, nombreCompleto, salarioBase, herramientasDiseno, especialidadDiseno):
        # Inicialización de la clase padre
        super().__init__(nombreCompleto, salarioBase)
        self.herramientasDiseno = [herramienta.strip() for herramienta in herramientasDiseno]
        self.especialidadDiseno = especialidadDiseno
        self.tipoEmpleado = "Diseñador"
    
    def calcularSalarioTotal(self):
        # Calcula salario con bonificación para especialidades UI/UX
        salarioCalculado = self.salarioBase
        if self.especialidadDiseno.lower() in ["ui", "ux"]:
            salarioCalculado = salarioCalculado * 1.20  # 20% de bonificación para UI/UX
        return salarioCalculado
    
    def obtenerInformacionEspecifica(self):
        # Retorna información específica del diseñador
        return f"Herramientas: {', '.join(self.herramientasDiseno)}, Especialidad: {self.especialidadDiseno}"
    
    def obtenerInformacionCompleta(self):
        # Retorna información completa del diseñador
        info = super().obtenerInformacionCompleta()
        info += f"Tipo de empleado: {self.tipoEmpleado}\n"
        info += f"Especialidad: {self.especialidadDiseno}\n"
        info += f"Herramientas de diseño: {', '.join(self.herramientasDiseno)}\n"
        if self.especialidadDiseno.lower() in ["ui", "ux"]:
            info += "Bonificación aplicada: 20%\n"
        else:
            info += "Bonificación aplicada: 0%\n"
        return info

class Gerente(Empleado):
    def __init__(self, nombreCompleto, salarioBase, departamentoGerencia):
        # Inicialización de la clase padre
        super().__init__(nombreCompleto, salarioBase)
        self.departamentoGerencia = departamentoGerencia
        self.tipoEmpleado = "Gerente"
    
    def calcularSalarioTotal(self):
        # Calcula salario con bonificación fija para gerentes
        return self.salarioBase * 1.35  # 35% de bonificación para gerentes
    
    def obtenerInformacionEspecifica(self):
        # Retorna información específica del gerente
        return f"Departamento: {self.departamentoGerencia}"
    
    def obtenerInformacionCompleta(self):
        # Retorna información completa del gerente
        info = super().obtenerInformacionCompleta()
        info += f"Tipo de empleado: {self.tipoEmpleado}\n"
        info += f"Departamento: {self.departamentoGerencia}\n"
        info += "Bonificación aplicada: 35%\n"
        return info

class Proyecto:
    # Contador para generar IDs únicos para cada proyecto
    contadorIdProyecto = 1
    
    def __init__(self, nombreProyecto, presupuestoAsignado):
        # Asignación de ID único y autoincremental
        self.idProyecto = Proyecto.contadorIdProyecto
        Proyecto.contadorIdProyecto += 1
        self.nombreProyecto = nombreProyecto
        self.presupuestoAsignado = presupuestoAsignado
        self.listaEmpleadosAsignados = []  # Lista de empleados en el proyecto
        self.estadoProyecto = "Planificación"  # Estado inicial del proyecto
    
    def agregarEmpleadoProyecto(self, empleado):
        # Agrega un empleado a la lista del proyecto
        self.listaEmpleadosAsignados.append(empleado)
    
    def calcularCostoTotalProyecto(self):
        # Calcula el costo total sumando los salarios de todos los empleados asignados
        costoTotalCalculado = 0
        for empleado in self.listaEmpleadosAsignados:
            costoTotalCalculado += empleado.calcularSalarioTotal()
        return costoTotalCalculado
    
    def verificarFactibilidadProyecto(self):
        # Verifica si el proyecto es factible comparando costo total con presupuesto
        costoTotal = self.calcularCostoTotalProyecto()
        return costoTotal <= self.presupuestoAsignado
    
    def obtenerInformacionProyecto(self):
        # Retorna información completa del proyecto
        return f"ID: {self.idProyecto}, Nombre: {self.nombreProyecto}, Empleados: {len(self.listaEmpleadosAsignados)}, Presupuesto: {self.presupuestoAsignado}"

# ---------------------- FUNCIONES DEL MENÚ PRINCIPAL ----------------------

def mostrarMenuPrincipal():
    # Muestra el menú principal del sistema
    print("\n" + "="*50)
    print("       SISTEMA INTEGRAL DE GESTIÓN DE RRHH")
    print("="*50)
    print("1. Registrar nuevo empleado en el sistema")
    print("2. Crear nuevo proyecto empresarial")
    print("3. Asignar proyecto a empleado específico")
    print("4. Validar factibilidad económica de proyecto")
    print("5. Mostrar reporte general del sistema")
    print("6. Mostrar información de cada empleado")
    print("7. SALIR del sistema")
    print("="*50)

def crearNuevoEmpleado(listaEmpleados):
    # Función para crear y registrar un nuevo empleado
    print("\n" + "-"*50)
    print("   REGISTRO DE NUEVO EMPLEADO")
    print("-"*50)
    
    # Validación de entrada de nombre
    while True:
        nombreCompleto = input("Ingrese nombre y apellido del empleado: ").strip()
        if nombreCompleto and len(nombreCompleto) >= 3:
            break
        print("Error: El nombre debe tener al menos 3 caracteres")
    
    # Validación de entrada de salario
    while True:
        try:
            salarioBase = float(input("Ingrese salario base del empleado: "))
            if salarioBase > 0:
                break
            print("Error: El salario debe ser un valor positivo")
        except ValueError:
            print("Error: Debe ingresar un valor numérico válido")
    
    # Selección de tipo de empleado
    print("\nSeleccione el tipo de empleado a registrar:")
    print("1. Desarrollador de software")
    print("2. Diseñador gráfico/UX/UI")
    print("3. Gerente de departamento")
    
    while True:
        tipoEmpleado = input("Opción seleccionada (1-3): ").strip()
        if tipoEmpleado in ["1", "2", "3"]:
            break
        print("Error: Debe seleccionar una opción entre 1 y 3")
    
    # Proceso de creación según tipo de empleado
    if tipoEmpleado == "1":
        lenguajesProgramacion = input("Ingrese lenguajes de programación (separados por coma): ").split(",")
        nivelExperiencia = input("Nivel de experiencia (Junior/SemiSenior/Senior): ").strip()
        nuevoEmpleado = Desarrollador(nombreCompleto, salarioBase, lenguajesProgramacion, nivelExperiencia)
        
    elif tipoEmpleado == "2":
        herramientasDiseno = input("Ingrese herramientas de diseño (separadas por coma): ").split(",")
        especialidadDiseno = input("Especialidad (UI/UX/Gráfico): ").strip()
        nuevoEmpleado = Diseñador(nombreCompleto, salarioBase, herramientasDiseno, especialidadDiseno)
        
    elif tipoEmpleado == "3":
        departamentoGerencia = input("Departamento de gerencia: ").strip()
        nuevoEmpleado = Gerente(nombreCompleto, salarioBase, departamentoGerencia)
    
    # Registro del empleado en el sistema
    listaEmpleados.append(nuevoEmpleado)
    print(f"\nEmpleado registrado exitosamente con ID: {nuevoEmpleado.obtenerIdEmpleado()}")
    print(f"   Nombre: {nuevoEmpleado.obtenerNombreCompleto()}")
    print(f"   Tipo: {nuevoEmpleado.tipoEmpleado}")

def crearNuevoProyecto(listaProyectos):
    # Función para crear un nuevo proyecto
    print("\n" + "-"*50)
    print("   CREACIÓN DE NUEVO PROYECTO")
    print("-"*50)
    
    # Validación de nombre del proyecto
    while True:
        nombreProyecto = input("Ingrese nombre del proyecto: ").strip()
        if nombreProyecto and len(nombreProyecto) >= 2:
            break
        print("Error: El nombre del proyecto debe tener al menos 2 caracteres")
    
    # Validación de presupuesto
    while True:
        try:
            presupuestoAsignado = float(input("Ingrese presupuesto asignado al proyecto: "))
            if presupuestoAsignado > 0:
                break
            print("Error: El presupuesto debe ser un valor positivo")
        except ValueError:
            print("Error: Debe ingresar un valor numérico válido")
    
    # Creación del proyecto
    nuevoProyecto = Proyecto(nombreProyecto, presupuestoAsignado)
    listaProyectos.append(nuevoProyecto)
    print(f"\nProyecto creado exitosamente: {nuevoProyecto.nombreProyecto}")
    print(f"   ID del proyecto: {nuevoProyecto.idProyecto}")
    print(f"   Presupuesto asignado: {nuevoProyecto.presupuestoAsignado}")

def asignarProyectoEmpleado(listaEmpleados, listaProyectos):
    # Función para asignar un proyecto a un empleado
    print("\n" + "-"*50)
    print("   ASIGNACIÓN DE PROYECTO A EMPLEADO")
    print("-"*50)
    
    # Validación de existencia de empleados y proyectos
    if not listaEmpleados:
        print("Error: No hay empleados registrados en el sistema")
        return
    
    if not listaProyectos:
        print("Error: No hay proyectos creados en el sistema")
        return
    
    # Mostrar lista de empleados disponibles
    print("\n--- LISTA DE EMPLEADOS DISPONIBLES ---")
    for empleado in listaEmpleados:
        infoBasica = empleado.obtenerInformacionEmpleado()
        if hasattr(empleado, 'tipoEmpleado'):
            infoBasica += f", Tipo: {empleado.tipoEmpleado}"
        print(infoBasica)
    
    # Selección de empleado
    while True:
        try:
            idEmpleadoSeleccionado = int(input("\nIngrese ID del empleado a asignar: "))
            empleadoSeleccionado = None
            
            for empleado in listaEmpleados:
                if empleado.obtenerIdEmpleado() == idEmpleadoSeleccionado:
                    empleadoSeleccionado = empleado
                    break
            
            if empleadoSeleccionado:
                break
            else:
                print("Error: No existe un empleado con ese ID")
        except ValueError:
            print("Error: Debe ingresar un número válido")
    
    # Mostrar lista de proyectos disponibles
    print("\n--- LISTA DE PROYECTOS DISPONIBLES ---")
    for indice, proyecto in enumerate(listaProyectos):
        print(f"{indice + 1}. {proyecto.obtenerInformacionProyecto()}")
    
    # Selección de proyecto
    while True:
        try:
            seleccionProyecto = int(input("\nSeleccione el número del proyecto a asignar: "))
            if 1 <= seleccionProyecto <= len(listaProyectos):
                proyectoSeleccionado = listaProyectos[seleccionProyecto - 1]
                break
            else:
                print(f"Error: Debe seleccionar un número entre 1 y {len(listaProyectos)}")
        except ValueError:
            print("Error: Debe ingresar un número válido")
    
    # Intentar realizar la asignación
    try:
        empleadoSeleccionado.asignarProyectoEmpleado(proyectoSeleccionado)
        print("Asignación realizada exitosamente")
    except ValueError as error:
        print(f"Error en asignación: {error}")

def validarFactibilidadProyecto(listaProyectos):
    # Función para validar la factibilidad de un proyecto
    print("\n" + "-"*50)
    print("   VALIDACIÓN DE FACTIBILIDAD DE PROYECTO")
    print("-"*50)
    
    # Validación de existencia de proyectos
    if not listaProyectos:
        print("Error: No hay proyectos creados en el sistema")
        return
    
    # Mostrar lista de proyectos
    print("\n--- LISTA DE PROYECTOS DISPONIBLES ---")
    for indice, proyecto in enumerate(listaProyectos):
        print(f"{indice + 1}. {proyecto.obtenerInformacionProyecto()}")
    
    # Selección de proyecto a validar
    while True:
        try:
            seleccionProyecto = int(input("\nSeleccione el número del proyecto a validar: "))
            if 1 <= seleccionProyecto <= len(listaProyectos):
                proyectoSeleccionado = listaProyectos[seleccionProyecto - 1]
                break
            else:
                print(f"Error: Debe seleccionar un número entre 1 y {len(listaProyectos)}")
        except ValueError:
            print("Error: Debe ingresar un número válido")
    
    # Cálculo y validación de factibilidad
    costoTotal = proyectoSeleccionado.calcularCostoTotalProyecto()
    esFactible = proyectoSeleccionado.verificarFactibilidadProyecto()
    
    print("\n--- RESULTADO DE VALIDACIÓN ---")
    print(f"Proyecto: {proyectoSeleccionado.nombreProyecto}")
    print(f"Presupuesto asignado: {proyectoSeleccionado.presupuestoAsignado}")
    print(f"Costo total calculado: {costoTotal}")
    print(f"Empleados asignados: {len(proyectoSeleccionado.listaEmpleadosAsignados)}")
    
    if esFactible:
        print("RESULTADO: El proyecto ES FACTIBLE económicamente")
        print(f"   Margen disponible: {proyectoSeleccionado.presupuestoAsignado - costoTotal}")
    else:
        print("RESULTADO: El proyecto NO ES FACTIBLE económicamente")
        print(f"   Déficit presupuestario: {costoTotal - proyectoSeleccionado.presupuestoAsignado}")

def generarReporteGeneral(listaEmpleados, listaProyectos):
    # Función para generar un reporte general del sistema
    print("\n" + "="*60)
    print("           REPORTE GENERAL DEL SISTEMA")
    print("="*60)
    
    # Estadísticas de empleados
    print("\n--- ESTADÍSTICAS DE EMPLEADOS ---")
    print(f"Total de empleados registrados: {len(listaEmpleados)}")
    
    if listaEmpleados:
        # Contar por tipo de empleado
        desarrolladores = [e for e in listaEmpleados if isinstance(e, Desarrollador)]
        diseñadores = [e for e in listaEmpleados if isinstance(e, Diseñador)]
        gerentes = [e for e in listaEmpleados if isinstance(e, Gerente)]
        
        print(f"  - Desarrolladores: {len(desarrolladores)}")
        print(f"  - Diseñadores: {len(diseñadores)}")
        print(f"  - Gerentes: {len(gerentes)}")
        
        # Empleados con proyectos asignados
        empleadosConProyectos = [e for e in listaEmpleados if e.obtenerCantidadProyectos() > 0]
        print(f"Empleados con proyectos asignados: {len(empleadosConProyectos)}")
    
    # Estadísticas de proyectos
    print("\n--- ESTADÍSTICAS DE PROYECTOS ---")
    print(f"Total de proyectos creados: {len(listaProyectos)}")
    
    if listaProyectos:
        proyectosFactibles = [p for p in listaProyectos if p.verificarFactibilidadProyecto()]
        proyectosNoFactibles = [p for p in listaProyectos if not p.verificarFactibilidadProyecto()]
        
        print(f"  - Proyectos factibles: {len(proyectosFactibles)}")
        print(f"  - Proyectos no factibles: {len(proyectosNoFactibles)}")
        
        # Proyectos sin empleados
        proyectosSinEmpleados = [p for p in listaProyectos if len(p.listaEmpleadosAsignados) == 0]
        print(f"Proyectos sin empleados asignados: {len(proyectosSinEmpleados)}")
    
    print("\n" + "="*60)

def mostrarInformacionEmpleados(listaEmpleados):
    # Función para mostrar información detallada de cada empleado
    print("\n" + "="*60)
    print("       INFORMACIÓN DETALLADA DE EMPLEADOS")
    print("="*60)
    
    if not listaEmpleados:
        print("No hay empleados registrados en el sistema")
        return
    
    for empleado in listaEmpleados:
        print("\n" + "-"*50)
        print(empleado.obtenerInformacionCompleta())
        print("-"*50)

# ---------------------- PROGRAMA PRINCIPAL ----------------------

# Inicialización de listas principales
listaCompletaEmpleados = []
listaCompletaProyectos = []

print("BIENVENIDO AL SISTEMA DE GESTIÓN DE RRHH Y PROYECTOS")
print("Sistema inicializado correctamente")

# Bucle principal del sistema
while True:
    try:
        mostrarMenuPrincipal()
        opcionSeleccionada = input("Seleccione una opción del menú (1-7): ").strip()
        
        if opcionSeleccionada == "1":
            crearNuevoEmpleado(listaCompletaEmpleados)
            
        elif opcionSeleccionada == "2":
            crearNuevoProyecto(listaCompletaProyectos)
            
        elif opcionSeleccionada == "3":
            asignarProyectoEmpleado(listaCompletaEmpleados, listaCompletaProyectos)
            
        elif opcionSeleccionada == "4":
            validarFactibilidadProyecto(listaCompletaProyectos)
            
        elif opcionSeleccionada == "5":
            generarReporteGeneral(listaCompletaEmpleados, listaCompletaProyectos)
            
        elif opcionSeleccionada == "6":
            mostrarInformacionEmpleados(listaCompletaEmpleados)
            
        elif opcionSeleccionada == "7":
            print("\n" + "="*50)
            print("   GRACIAS POR USAR EL SISTEMA DE GESTIÓN")
            print("           ¡HASTA PRONTO!")
            print("="*50)
            break
            
        else:
            print("Error: Opción no válida. Por favor seleccione una opción entre 1 y 7")
            
    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario")
        break
    except Exception as error:
        print(f"\nError inesperado: {error}")
        print("Por favor, contacte al administrador del sistema")