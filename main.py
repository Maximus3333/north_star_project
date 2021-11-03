def main():
    # Main database stuff here
    name = 'north_star_school_database.db'
    conn, curs = open_db(name)
    #create
    setup_employees(curs, conn)
    populate_employees(curs, conn)
    # select_from(curs)
    # get_info(cursor, id) # May want to consider including this in GUI
    app = guiwindow.QApplication(sys.argv)
    ex = guiwindow.Window(conn, curs)
    # print(sys.argv)
    # print(help(guiwindow))
    sys.exit(app.exec_())

main()