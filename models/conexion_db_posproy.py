import oracledb
from tabulate import tabulate


class ConexionPosProyectosDb:
    # Constructor
    def __init__(self):
        self.usuario = "HR"
        self.contrasenia = "hr"
        self.host = "localhost"
        self.puerto = 1521

    # Abre conexion

    def crea_conexion(self):

        try:
            conexion = oracledb.connect(
                user=self.__usuario, password=self.__contrasenia, port=self.__puerto, dsn=self.__dns)
            print("Conexión establecida")
            return conexion

        except Exception as e:
            print(f"Error al conectar con la base de datos: {e}")
            return None

    # Obtiene consulta
    def genera_consulta(self, DML_CONSULTA):
        conexion = self.crea_conexion()
        if conexion is None:
            return None
        try:
            # Crear un cursor y ejecutar la consulta
            cursor = conexion.cursor()
            cursor.execute(DML_CONSULTA)
            resultado = cursor.fetchall()

            cursor.close()
            return resultado

        except oracledb.DatabaseError as e:
            print(f"Error al ejecutar la consulta: {e}")

        finally:
            conexion.close()

    def mostrar_resultado(self, DML_CONSULTA):
        resultado = self.genera_consulta(DML_CONSULTA)
        if resultado:

            headers = ["Id Empleado", "Nombre", "Apellido", "Salario"]
            print(tabulate(resultado, headers, tablefmt="rounded_grid"))
        else:
            print("No se obtuvieron resultados.")
