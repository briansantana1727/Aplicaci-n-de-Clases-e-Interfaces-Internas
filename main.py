from empleado import *
from reportes import *
from programacion import *

empleados = [
    Gerente("Roberto","Perez","$20,000.00", Matutino()),
    Gestora("Alejandra","Juarez","$8,000.00", Matutino()),
    Gestora("Selene","Gonzalez","$8,000.00", Matutino()),
    Tecnico("Artemio","Jose","$9,000.00", Vespertino()),
    Tecnico("Salvador","Perez","$9,000.00", Vespertino()),
    Tecnico("Rolando","Santana","$9,000.00", Matutino()),
    Administrador("Marco","Marquez","$15,000.00", Matutino())
]
reportes =[
    ReporteConta(empleados),
    ReporteEmpleados(empleados),
    ReporteProgramacion(empleados)
]
for r in reportes:
    r.print_reporte()