from mysqlx import get_session, errors, Session, Schema
import mysqlx
import mysqlx.authentication
from extras_func import binary_question, clear_scr
     

def do_login() -> Session:
    host = 'localhost'
    port = 33060
    user = 'dbadmin'
    password = 'dbadmin'

    sessiondata = {'host': host,
                   'port': port,
                   'user': user,
                   'password': password }
    
    if not session_verify(sessiondata):

        resp = binary_question("Desea volver a intentarlo [s/n]:")

        if resp == 's':
            do_login()
        else:
            print("Ha salido de la aplicación")
            exit(0)

    session = get_session(sessiondata)

    return session

def db_select(db_list: list) -> str:
    dbname = ""
    while dbname not in db_list:
        clear_scr()
        print("+----------------------------------------------------------------------+")
        print("|                      BASE DE DATOS DISPONIBLES                       |")
        print("+----------------------------------------------------------------------+")
        for i in range(0,len(db_list)):
            print(f"| <{i+1}> {db_list[i]:<64} |")
        
        print("+----------------------------------------------------------------------+")

        dbname = input("Seleccione una base de datos o si quiere salir escriba [exit]\n")
        if dbname.lower() == "exit":
            exit(0)

    return dbname



def session_verify(sessiondata:Session):
    try:

        get_session(sessiondata)
        return True
    
    except errors.InterfaceError as err:
        print(err)
        return False
    
def connect_db():
    session = do_login()
    while session.is_open():

        db_list = session.get_schemas()
        db_name = db_select(db_list)


        print(database)
        session.close()





connect_db()