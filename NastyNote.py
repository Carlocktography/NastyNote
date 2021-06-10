#! /usr/bin/env python3

#Import modules needed for Python version check, date/time, timer, file/folder exists, sqlite, truncate number to non-fractional digits, OS/host check
import sys, datetime, time, os.path, sqlite3, math, platform, shutil
#from tkinter import *
#from tkinter import ttk
#window = Tk()
#window.title('NastyNote')
#window.mainloop()

#Define a function to scale b/Kb/Mb/Gb/Tb/Pb/Eb/Zb/Yb/WTFb and return it rounded to two decimal places
def dataunits(x):
    try:
        #def bytes(x):
            if len(str(math.trunc(x))) <4 and len(str(math.trunc(x))) >= 1:
                return str(round(x,2)) + 'B'
        #def kilobytes(x):
            elif len(str(math.trunc(x))) < 7 and len(str(math.trunc(x))) >= 4:
                return str(round(x/1000,2)) + 'KB'
        #def megabytes(x):
            elif len(str(math.trunc(x))) < 10 and len(str(math.trunc(x))) >=7: 
                return str(round(x/1000000,2)) + 'MB'
        #def gigabytes(x):
            elif len(str(math.trunc(x))) < 13 and len(str(math.trunc(x))) >=10:
                return str(round(x/1000000000,2)) + 'GB'
        #def terabytes(x):
            elif len(str(math.trunc(x))) < 16 and len(str(math.trunc(x))) >=13:
                return str(round(x/1000000000000,2)) + 'TB'
        #def petabytes(x):
            elif len(str(math.trunc(x))) < 19 and len(str(math.trunc(x))) >=16:
                return str(round(x/1000000000000000,2)) + 'PB'
        #def exabytes(x):
            elif len(str(math.trunc(x))) < 22 and len(str(math.trunc(x))) >=19:
                return str(round(x/1000000000000000000,2)) + 'EB'
        #def zettabytes(x):
            elif len(str(math.trunc(x))) < 25 and len(str(math.trunc(x))) >=22:
                return str(round(x/1000000000000000000000,2)) + 'ZB'
        #def yottabytes(x):
            elif len(str(math.trunc(x))) < 28 and len(str(math.trunc(x))) >=25:
                return str(round(x/1000000000000000000000000,2)) + 'YB'
        #def whatthefuckabytes(x):
            elif len(str(math.trunc(x))) >= 28:
                return str(round(x/1000000000000000000000000000,2)) + 'WTFB'
            else:
                return 'NaN'
    except SyntaxError:
        return 'NaN'
    except NameError:
        return 'NaN'
    except TypeError:
        return 'NaN'

#Establish 'now' variable to store current date/time
now = str(datetime.datetime.now())

#Establish 'header' variable to add newlines and 80-char break lines
header = '\n--------------------------------------------------------------------------------\n'
header_one = '\n--------------------------------------------------------------------------------'

#Establish 'footer' variable to add newline and 80-char break line
footer = '\n================================================================================\n'
footer_one = '\n================================================================================'

#Establish NastyNote version.
nn_v = 'NastyNote v2.0 | Compiled: 2016-04-19 21:07:03'

#Store results of version check
python_version = sys.version

#Print version of Nastynote & Python Version
print(python_version+'\n'+nn_v+footer_one, sep='')

#Establish Lin/Mac/Win Path variables
lin_path = os.path.expanduser('~/Public/Documents/NastyNote/nastynote.db')
mac_path = os.path.expandvars('/Users/Shared/Documents/NastyNote/nastynote.db')
win_path = os.path.expandvars('%PUBLIC%\\Documents\\NastyNote\\nastynote.db')

#Establish SQLite3 query for the new database to initialize it
db_establish = 'CREATE TABLE notes (id INTEGER NOT NULL UNIQUE PRIMARY KEY ASC AUTOINCREMENT, author TEXT, author_initials TEXT, note TEXT, datetime INTEGER (26, 0), time_read INTEGER, time_write INTEGER, bytes INTEGER, nn_v INTEGER (50, 0))'

#Establish SQLite3 query and variables to populate a starter entry in a fresh db
author_populate = "Brett Edmond Carlock"
author_initials_populate = "B.E.C"
note_populate = "Welcome to NastyNote!"
datetime_populate = "2016-04-19 21:07:03.704029"
bytes_populate = "21"
nn_v_populate = nn_v
db_populate = 'INSERT INTO notes (author, author_initials, note, datetime, bytes, nn_v) VALUES (?,?,?,?,?,?)',[author_populate,author_initials_populate,note_populate,datetime_populate,bytes_populate,nn_v_populate]    

#Check for existing file 'nastynote.db' under Documents/NastyNote and create file/folder structure if False
if platform.system() == 'Linux':
        if os.path.isfile(lin_path) == False:   
                mkdir_path = os.path.expanduser('~//Public//Documents//NastyNote')
                if os.path.isdir(mkdir_path) == True:
                        pass
                elif os.path.isdir(mkdir_path) == False:
                        try:
                                os.makedirs(mkdir_path)
                        except OSError:
                                pass
                con_lin = sqlite3.connect(lin_path)
                con_lin.execute(db_establish) 
                print('Establishing a new ', lin_path, '.', sep='')
                cur = con_lin.cursor()
                cur.execute(db_populate)
        elif os.path.isfile(lin_path) == True:
                print('Existing ', lin_path, ' found.\nPrevious entry: ', sep='')
        nn_path = lin_path
        platform = platform.system()
        
elif platform.system() == 'Mac':
        if os.path.isfile(mac_path) == False:
                mkdir_path = os.path.expandvars('//Users//Shared//Documents//NastyNote')
                if os.path.isdir(mkdir_path) == True:
                        pass
                elif os.path.isdir(mkdir_path) == False:
                        try:
                                os.makedirs(mkdir_path)
                        except OSError:
                                pass
                con_mac = sqlite3.connect(mac_path)
                con_mac.execute(db_establish)
                print('Establishing a new ', mac_path, '.', sep='')
                cur = con_mac.cursor()
                cur.execute(db_populate)
        elif os.path.isfile(mac_path) == True:
                print('Existing ', mac_path, ' found.\nPrevious entry: ', sep='')
        nn_path = mac_path
        platform = platform.system()
        
elif platform.system() == 'Windows':
        if os.path.isfile(win_path) == False:
                mkdir_path = os.path.expandvars('%PUBLIC%\\Documents\\NastyNote')
                if os.path.isdir(mkdir_path) == True:
                        pass
                elif os.path.isdir(mkdir_path) == False:       
                        try:
                                os.makedirs(mkdir_path)
                        except OSError:
                                pass
                con_win = sqlite3.connect(win_path)
                con_win.execute(db_establish) 
                print('Establishing a new ', win_path, '.', sep='')
                cur = con.win.cursor()
                cur.execute(db_populate)
        elif os.path.isfile(win_path) == True:
                print('Existing ', win_path,' found.\nPrevious entry: ', sep='')
        nn_path = win_path
        platform = platform.system()

#Start the read timer
start_read = time.perf_counter()

#Open 'nastynote.db' using With
with sqlite3.connect(nn_path) as con:
    #Establish a cursor object
    cur = con.cursor()

    #Establish variables to hold memebers of each column in table for reading
    note_id = str(cur.execute('SELECT id FROM notes ORDER BY id DESC').fetchone()[0])
    note_author = str(cur.execute('SELECT author FROM notes ORDER BY id DESC').fetchone()[0])
    note_author_initials = str(cur.execute('SELECT author_initials FROM notes ORDER BY id DESC').fetchone()[0])
    note_content = str(cur.execute('SELECT note FROM notes ORDER BY id DESC').fetchone()[0])
    note_datetime = str(cur.execute('SELECT datetime FROM notes ORDER BY id DESC').fetchone()[0])
    note_bytes_written = int(cur.execute('SELECT bytes FROM notes ORDER BY id DESC').fetchone()[0])
    note_nn_v = str(cur.execute('SELECT nn_v FROM notes ORDER BY id DESC').fetchone()[0])
    print(header,'Note #: ',note_id,'\n','Author: ',note_author,' : ',note_author_initials,'\n','Date: ',note_datetime,header,note_content,footer,'Version: ',note_nn_v,' | ','Size: ',dataunits(note_bytes_written),footer, sep='')
 
    #Get file size
    bytes_read = len(note_id+note_author+note_author_initials+note_datetime+note_content+str(note_bytes_written)+note_nn_v)

#End the read timer
end_read = time.perf_counter()

#Get the file read time elapsed
time_read = round(end_read - start_read, 2)

#Tell the user how big the file has grown and how long it took to load
print(dataunits(bytes_read), ' of data read in ',time_read,' seconds. ', dataunits(bytes_read/time_read),'/s.',sep='')

#Inform the user that they'll be appending to the notes file
print('\nAppend a new entry by answering the prompts.')

#Initialize a variable with user-specified value
input_author = input('Author: ')
input_author_initials = input('Initials: ')
input_content = input('Note: ')
input_datetime = now
input_bytes_written = len(input_content)
input_nn_v = nn_v

#Start the write timer
start_write = time.perf_counter()

#Re-open 'nastynote.db' using With
with sqlite3.connect(nn_path) as con:
    #Establish a cursor object
    cur = con.cursor()
    #Establish variables to hold memebers of each column in table for reading
    cur.execute('INSERT INTO notes (author, author_initials, note, datetime, bytes, nn_v, time_read) VALUES (?,?,?,?,?,?,?)',[input_author,input_author_initials,input_content,input_datetime,input_bytes_written,input_nn_v,time_read])
    print(header,'Note #: ',int(note_id)+1,'\n','Author: ',input_author,' : ',input_author_initials,'\n','Date: ',input_datetime,header,input_content,footer,'Version: ',input_nn_v,' | ','Size: ',dataunits(input_bytes_written),footer, sep='')

#End the write timer
end_write = time.perf_counter()

#Get the file write time elapsed
time_write = round(end_write - start_write, 2)

#Print the file write status
print(dataunits(input_bytes_written),' of data written in ',time_write,' seconds. ',dataunits(input_bytes_written/time_write),'/s.', sep='')

#Re-open 'nastynote.db' using With to store IOPerf information
with sqlite3.connect(nn_path) as con:
    #Establish a cursor object
    cur = con.cursor()
    #Establish variables to hold memebers of each column in table for reading
    cur.execute('UPDATE notes SET time_write = (?) WHERE id = (?)',[time_write, int(note_id)+1])

#Ask the user to quit
quit=input('Type something to exit: ')