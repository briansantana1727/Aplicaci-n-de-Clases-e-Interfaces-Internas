class Reporte:
    def __init__(self,lista_empleados):
        self._lista_empleados = lista_empleados

class ReporteConta(Reporte):
    def print_reporte(self):
        print(".::::: Reporte de contabilidad :::::.")
        print("=====================================")
        for e in self._lista_empleados:
            print(f'{e.get_nombre_completo()},{e.salario}')

class ReporteEmpleados(Reporte):
    def print_reporte(self):
        print(".::::: Reporte de empleados :::::.")
        print("==================================")
        for e in self._lista_empleados:
            print(f'{e.get_nombre_completo()},{e.puesto}')

class ReporteProgramacion(Reporte):
    def print_reporte(self):
        print(".::::: Reporte de horarios :::::.")
        print("=================================")
        for e in self._lista_empleados:
            print(f'{e.get_nombre_completo()},{e.programacion.get_programacion_info()}')