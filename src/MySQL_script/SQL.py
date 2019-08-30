# MySQL class
# Note causes errors if you try to save again .csv file with same name because moving to archive folder will fail as the file already exists
# Save functions print file name for debug purpose

class SQLConnection:
    from _socket import close
    import mysql.connector
    from datetime import date
    import csv
    from sqlite3.test.factory import MyCursor
    import glob
    import os
    import datetime
    import shutil
    
    #Log in information for MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root"
    )
    
    
    mycursor = mydb.cursor()
    
    # Creates the database name (date + data)
    DatabaseName = date.today().strftime("%d%m%Y") + "data"
    
    # Creates the Database with tables for mir and books
    mycursor.execute("CREATE DATABASE IF NOT EXISTS " + DatabaseName)
    mycursor.execute("USE {}".format(DatabaseName))    
    
    mycursor.execute("CREATE TABLE IF NOT EXISTS mir_data (ID_MIR INT NOT NULL AUTO_INCREMENT, X FLOAT NULL, Y FLOAT NULL, Orientation FLOAT NULL, Time_mir TIMESTAMP NULL, PRIMARY KEY (ID_MIR))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS book_data (ID_BOOK INT NOT NULL AUTO_INCREMENT, Time_books TIMESTAMP NULL, Data VARCHAR(45), RSSI INT NULL, PRIMARY KEY (ID_BOOK))")
    
    
    #Imports folder paths all .csv files to MySQL and then moves them to archive folder in the same path.
    def SaveBookCSV(self,file_path):
        all_files = self.glob.glob(file_path + "*.csv")
        
        #Makes folder for scanned files if not yet created (named archive)
        foldername = file_path + "archive/"
        if not self.os.path.exists(foldername):
            self.os.makedirs(foldername)
        
        #Saves information row by row and skips first 
        for x in all_files:
            print(x)
            open_file = open(x)
            csv_data = self.csv.reader(open_file)
            firstline = True
            
            for row in csv_data:
                if firstline:
                    firstline = False
                    continue
                self.mycursor.execute("INSERT INTO book_data (Time_books, Data, RSSI) VALUES (%s, %s, %s)", row)
                
            open_file.close()
            
            
        self.mydb.commit() 
        
        #Moves scanned files to "archive" folder
        for x in all_files:
            self.shutil.move(x,foldername)
    
    
    #Imports folder paths all .csv files to MySQL and then moves them to archive folder in the same path.       
    def SaveMirCSV(self,file_path):
        all_files = self.glob.glob(file_path + "*.csv")
        
        #Makes folder for scanned files if not yet created (named archive)
        foldername = file_path + "archive/"
        if not self.os.path.exists(foldername):
            self.os.makedirs(foldername)
        
        #Saves information row by row and skips first row 
        for x in all_files:
            print(x)
            open_file = open(x)
            csv_data = self.csv.reader(open_file)
            firstline = True
            
            for row in csv_data:
                if firstline:
                    firstline = False
                    continue
                self.mycursor.execute("INSERT INTO mir_data (X, Y, Orientation, Time_mir) VALUES (%s, %s, %s, %s)", row)
                
            open_file.close()
            
            
        self.mydb.commit() 
        
        #Moves scanned files to "archive" folder
        for x in all_files:
            self.shutil.move(x,foldername)
    
    #Combines MIRData and BookData by timestamp and saves that data to bigbang table
    def CombineTables(self):
        self.mycursor.execute("""
        USE %s;
        DROP TABLE IF EXISTS tmp_bang;
        CREATE TABLE tmp_bang
        SELECT r.*,
            (SELECT c.ID_MIR
            FROM mir_data c
            WHERE c.Time_mir <= r.Time_books
            ORDER BY c.Time_mir DESC
            LIMIT 1
        ) AS ID_MIR
        from book_data r;

        DROP TABLE IF EXISTS bigbang;
        CREATE TABLE bigbang
        SELECT t.ID_BOOK,t.`Data`,t.RSSI,t.Time_books as time_book,
        c.ID_MIR,c.Time_mir as time_mir,
        c.X,c.Y,c.orientation
        FROM tmp_bang t
        JOIN mir_data c
        ON t.ID_MIR = c.ID_MIR;""" % self.DatabaseName)
        
    

#test = SQLConnection()
#test.SaveBookCSV("C:/Test/Desktop/protopaja/csv/")
#test.SaveMirCSV("C:/Test/Desktop/protopaja/csvmir/")
#test.CombineTables2()