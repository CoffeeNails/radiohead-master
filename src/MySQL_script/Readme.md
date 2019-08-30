1. Install MySQL server
2. Install MySQL python connector
3. Then open the SQL.py and change login information and ip if needed
4. SQL.py has 3 functions 
	-SaveBookCSV Imports folder paths all .csv files to MySQL and then moves them to archive folder in the same path. 
	-SaveMirCSV Imports folder paths all .csv files to MySQL and then moves them to archive folder in the same path.
	-CombineTables Combines MIRData and BookData by timestamp and saves that data to bigbang table
