from models.conexion_db_posproy import ConexionPosProyectosDb

buscar_rrn = input("Ingresa RRN: ")
DML_CONSULTA = f"""
                SELECT * FROM (
                    SELECT TRL_ORIGIN_IAP_NAME IAP_ORIGEN, 
                    TRL_DEST_IAP_NAME IAP_DESTINO,
                    TRL_CARD_ACPT_TERMINAL_IDENT Dispatcher,
                    TO_CHAR(TRL_SYSTEM_TIMESTAMP,'YYYY-MM-DD HH24:MI:SS.FF3' )Fecha_Hora,
                    TRL_ID,
                    TRL_MESSAGE_TYPE MTI,
                    SUBSTR(Trl_additional_response_data,94,6) PROC_CODE, -- PC para 4.5
                    TRL_CARD_ACPT_IDENT_CODE AFILIACION,
                    substr(Trl_additional_response_data,100,3) PEM,
                    TRL_AMT_TXN IMPORTE,
                    TRL_PAN TRACK_II, 
                    trl_rrn,
                    TRL_APPROVAL_CODE NUM_AUTH
                    from RPOS_OWNER.transaction_log
                    WHERE trl_rrn = '{buscar_rrn}'
                    Order By Trl_System_Timestamp DESC
                ) WHERE ROWNUM <= 100
    """


db = ConexionPosProyectosDb()
db.mostrar_resultado(DML_CONSULTA)
