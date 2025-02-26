import oracledb
from tabulate import tabulate


'''
Instalar librerias:
oracledb
tabulate
'''

usuario = "RPOS_USER"
contrasenia = "rp0sUser12"
puerto = 1525
host = "172.29.40.64"


# QUERY
DML_CONSULTA = """SELECT employee_id, first_name, last_name, salary 
                FROM employees ORDER BY employee_id DESC"""
# Insertar
DML_INSERT = """
           INSERT INTO hr.employees (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL, HIRE_DATE, JOB_ID, SALARY, MANAGER_ID, DEPARTMENT_ID) 
           VALUES (212, 'Angelica', 'Regaños', 'areganos@correo.com', TO_DATE('2025-02-19 00:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'IT_PROG', 17000, 103, 60) 
    """

# Update
DML_UPDATE = """
                UPDATE hr.employees SET SALARY = 9000 WHERE EMPLOYEE_ID = 230
    """

# Delete
DML_DELETE = """
                DELETE FROM hr.employees WHERE employee_id = 211
    """

# Abrir conexion
with oracledb.connect(user=usuario, password=contrasenia, port=puerto, dsn="172.29.40.64/QAPNPOS") as conexion:
    # Crear Cursor
    with conexion.cursor() as consulta:
        # Ejecutar query
        consulta.execute(DML_CONSULTA)
        # Obtener consulta como lista
        resultado = consulta.fetchall()

    # Iteracion con for
    # for filas in resultado:
    #     print(filas)
    #     print("------------------------------------------------------------------------------------------------------\n")

# Creacion de headers para tabla
headers = ["Id Empleado", "Nombre", "Apellido", "Email", "Contratacio", "Id Puesto",
           "Salario", "Id Manager", "Id Departamento"]
# Uso de tabulate para construir tabla
print(tabulate(resultado, headers, tablefmt="rounded_grid"))
