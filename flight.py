import cx_Oracle

cx_Oracle.init_oracle_client(
    lib_dir=r"C:\Users\fjwu\Downloads\instantclient-basic-nt-19.11.0.0.0dbru\instantclient_19_11")

try:
    con = cx_Oracle.connect('scott/tiger@localhost:1521/scottt')


    print(" \t\t***********************************************************************************************")
    print("                                                            ")
    print("             \t\t\t\t\t\t\t\t\tWELCOME                      ")
    print("                \t\t\t\t\t\t\t\t  TO                        ")
    print("         \t\t\t\t\t\t\t\t FLIGHT SYSTEM MANAGMENT           ")
    print("                                                            ")
    print(" \t\t***********************************************************************************************")

except cx_Oracle.DatabaseError as er:
    print('There is an error in the Oracle database:', er)

else:
    try:
        cur = con.cursor()

        # fetchall() is used to fetch all records from result set
        print("       \t\t\t\t\t\t\t\t\t * BOARDING_DETAIL *                    ")
        cur.execute('select * from BOARDING_DETAIL')
        rows = cur.fetchall()
        for i in rows:
            print('BID=', i[0] ,'FID=', i[1],'PID=', i[2],'TID=', i[3],'PASS_ID=', i[4],'GATE=', i[5],'BAGGAGE=', i[6],'MEAL=', i[7])





        # fetchall() is used to fetch all records from result set
        print("       \t\t\t\t\t\t\t\t\t * FLIGHT_DETAIL *                    ")
        cur.execute('select * from FLIGHT_DETAIL')
        rows = cur.fetchall()
        for i in rows:
            print('FID=', i[0] ,'PID=', i[1],'DEP_DATE=', i[2],'DEP_TIME=', i[3],'ARRV_DATE=', i[4],'ARRV_TIME=', i[5],'TAKE_OFF=', i[6],'LANDING=', i[7])



        # fetchall() is used to fetch all records from result set
        print("       \t\t\t\t\t\t\t\t\t * PILOT_DETAIL *                    ")
        cur.execute('select * from PILOT_DETAIL')
        rows = cur.fetchall()
        for i in rows:
            print('PID=', i[0] ,'F_NAME=', i[1],'L_NAME=', i[2],'CONT_NO=', i[3],'PILOY_LTS=', i[4])



        # fetchall() is used to fetch all records from result set
        print("       \t\t\t\t\t\t\t\t\t * TICKET_DETAIL *                    ")
        cur.execute('select * from TICKET_DETAIL')
        rows = cur.fetchall()
        for i in rows:
            print('TID=', i[0] ,'PASS_ID=', i[1],'FID=', i[2],'PID=', i[3],'DEP_AIRPORT=', i[4],'ARR_AIRPORT=', i[5],'FARE=', i[6])




        # fetchall() is used to fetch all records from result set
        print("       \t\t\t\t\t\t\t\t\t * PASSENGER_DETAIL *                    ")
        cur.execute('select * from PASSENGER_DETAIL')
        rows = cur.fetchall()
        for i in rows:
            print('PASS_ID=', i[0] ,'FIRST_NAME=', i[1],'LAST_NAME=', i[2],'EMAIL=', i[3],'P_NO=', i[4])



    except cx_Oracle.DatabaseError as er:
        print('There is an error in the Oracle database:', er)

    except Exception as er:
        print('Error:' + str(er))

    finally:
        if cur:
            cur.close()

finally:
    if con:
        con.close()