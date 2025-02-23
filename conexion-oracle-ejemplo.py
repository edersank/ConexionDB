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


DML_QUERY = """
                SELECT * FROM (
                    SELECT TRL_ORIGIN_IAP_NAME IAP_ORIGEN, 
                    TRL_DEST_IAP_NAME IAP_DESTINO,
                    TRL_CARD_ACPT_TERMINAL_IDENT Dispatcher,
                    TO_CHAR(TRL_SYSTEM_TIMESTAMP,'YYYY-MM-DD HH24:MI:SS.FF3' )Fecha_Hora,
                    TRL_ID,
                    TRL_MESSAGE_TYPE MTI,
                    SUBSTR(Trl_additional_response_data,94,6) PROC_CODE,---PC para 4.5
                    TRL_CARD_ACPT_IDENT_CODE AFILIACION,
                    substr(Trl_additional_response_data,100,3) PEM,
                    TRL_AMT_TXN IMPORTE,
                    TRL_PAN TRACK_II, 
                    trl_rrn,
                    TRL_APPROVAL_CODE NUM_AUTH
                    from RPOS_OWNER.transaction_log
                    Order By Trl_System_Timestamp DESC
                ) WHERE ROWNUM <= 20"""


with oracledb.connect(user=usuario, password=contrasenia, port=puerto, dsn="172.29.40.64/QAPNPOS") as conexion:
    with conexion.cursor() as consulta:
        consulta.execute(DML_QUERY)
        resultado = consulta.fetchall()

    # for filas in resultado:
    #     print(filas)
    #     print("------------------------------------------------------------------------------------------------------\n")

headers = ["IAP_ORIGEN", "IAP_DESTINO", "DISPATCHER", "TIME STAMP", "TRL_ID",
           "MTI", "P CODE", "AFILIACION", "PEM", "IMPORTE", "TRACK II", "RRN", "NO. AUTH."]
print(tabulate(resultado, headers, tablefmt="rounded_grid"))
