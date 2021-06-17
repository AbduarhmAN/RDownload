from mysql import connector
class Quiries:
    # Dont change these Variables
    # -------------------------------------
    __d_name = "sql3419536"
    __d_table = "download"
    __d_host = "sql3.freemysqlhosting.net"
    __d_port = "3306"
    __d_user_name = "sql3419536"
    __d_password = "KtLLMC5IHi"
    # --------------------------------------
    __cursore = None

    main_table_columns={"id":"file_id","url":"file_url","status":"file_status"}

    def setName(self,name : str):
        self.__d_name = name

    def setTable(self,table : str):
        self.__d_table = table

    def setHost(self,host : str):
        self.__d_host = host

    def setPort(self,port : int):
        self.__d_port = port

    def setUsername(self,user_name : str):
        self.__d_user_name = user_name

    def setPassword(self,password : str):
        self.__d_password = password


    def connect(self):
        try:
            sql = connector.connect(
            host=self.__d_host,
            user=self.__d_user_name,
            password=self.__d_password,
            database=self.__d_name
            )
            self.__cursore = sql.cursor()
            print("CONNECTED SECCESSFULLY")
        except Exception as err:
            print("ERROR HaPpEnD !")
            print(err)

def main():
    test = Quiries()
    test.connect()

if __name__ == '__main__':
    main()
    