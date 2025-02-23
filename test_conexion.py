from models.conexion_db_posproy import ConexionPosProyectosDb


DML_CONSULTA = """SELECT employee_id, first_name, last_name, salary 
                FROM employees ORDER BY employee_id DESC"""


db = ConexionPosProyectosDb()
db.mostrar_resultado(DML_CONSULTA)
