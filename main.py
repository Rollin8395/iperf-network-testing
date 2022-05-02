import os
import pandas as pd
import socket
import pypyodbc as odbc
hostname=socket.gethostname()
client=socket.gethostbyname(hostname)
# print(IP)
server = 'localhost'
run= "iperf3.exe -c{} -t6 -T %time% ".format(server)
v=os.popen(run)
TS=[]
Ban=[]
Int=[]
direction=[]
# sTS=[]
# sBan=[]
# sInt=[]
# sender=[]
with v as out:
    for line in out:
        if 'sec' in line:
            if 'sender'  in line:
                sTs,sc,sID,sinter,ssec,stransvalue,sMB,sBandwidth,sunit,swho= line.split()
                Bans=str(sBandwidth)+str(sunit)
                # sBan.append(Ban)
                # sInt.append(sinter)
                # sender.append(swho)
                TS.append(sTs)
                Ban.append(Bans)
                Int.append(sinter)




            elif 'receiver' in line:
                rTs,rc,rID,rinter,rsec,rtransvalue,rMB,rBandwidth,runit,rwho= line.split()
                Banr = str(rBandwidth) + str(runit)
                # rBan.append(Banr)
                # rTS.append(rTs)
                # rInt.append(rinter)
                # receiver.append(rwho)
                TS.append(rTs)
                Ban.append(Banr)
                Int.append(rinter)


            # else:
            #     print()
            #     # Ts,c,ID,inter,sec,transvalue,MB,Bandwidth,unit=line.split()
            #     # rTS.append(Ts)
            #     # # rBan.append(Bandwidth)
            #     # # runit.append(unit)
            #     # Ban=str(Bandwidth) + str(unit)
            #     # rBan.append(Ban)




# print(TS)
# print(Ban)
# print(Int)

StR=str(swho)+' to '+str(rwho) +'('+str(client)+' to '+str(server)+')'
RtS=str(rwho)+' to '+str(swho) + '('+str(server)+' to '+str(client)+')'
direction.append(StR)
direction.append(RtS)


df1=pd.DataFrame(TS,columns=['Time Stamp'])
df2=pd.DataFrame(direction,columns=['Direction'])
df3=pd.DataFrame(Ban,columns=['Bandwidth'])
df4=pd.DataFrame(Int,columns=['Interval'])
pd. set_option('display.max_columns', 6)

res=pd.concat([df1, df2,df4,df3], axis=1)
# res['From']=server
# res['To']= IP
print(res)
# # records=res.values.tolist()
























#---------------SQL----------------
# DRIVER = 'SQL Server'
# SERVER_NAME = 'ROLLIN\SQLEXPRESS'
# DATABASE_NAME = 'networkiperf'
#
#
# def connection_string(driver, server_name, database_name):
#     conn_string = f"""
#              DRIVER={{{driver}}};
#              SERVER={server_name};
#              DATABASE={database_name};
#            """
#     return conn_string
#
#
# """Create database connection instance"""
#
# try:
#     conn = odbc.connect(connection_string(DRIVER, SERVER_NAME, DATABASE_NAME))
# except odbc.DatabaseError as e:
#     print('Database Error:')
#     print(str(e.value[1]))
# except odbc.Error as e:
#     print('Connection Error:')
#     print(str(e.value[1]))
#
# """
# Create a cursor connection
# """
# sql_insert = '''
#              INSERT INTO  New_database_table
#              VALUES(?,?,?,?)
#        '''
#
#
# try:
#     cursor = conn.cursor()
#     cursor.executemany(sql_insert, records)
#     cursor.commit();
# except Exception as e:
#     cursor.rollback()
#     print(str(e[1]))
# finally:
#     print('DONE')
#     cursor.close()
#     conn.close()

