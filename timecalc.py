import re
import sys
import datetime

print("How long to do 1 [thing]?")
tsflag = True
while tsflag:
    timestr = input("> ")
    tm_st_splt = re.split(r'^(\d+)(\.\d+)?', timestr)
    if(tm_st_splt[3]):
        tmbase = tm_st_splt[3].lower()
        tsflag = False
    else:
        print("Time Unit Please!")

print("How many [thing]s?")
try:
    multip = input("> ")
    mulval = float(multip)
except:
    sys.exit(1)

if(tm_st_splt[2]):
    tmexstr = tm_st_splt[1] + tm_st_splt[2]
    tmval = float(tmexstr)
else:
    tmval = float(tm_st_splt[1])

st = datetime.datetime.now()
if(tmbase[0] == 's'):
    et = st + datetime.timedelta(seconds=mulval * tmval)
if(tmbase[0] == 'm'):
    et = st + datetime.timedelta(minutes=mulval * tmval)
if(tmbase[0] == 'h'):
    et = st + datetime.timedelta(hours=mulval * tmval)


print("Now:\n", st.ctime())
print("ETC:\n", et.ctime(), end='\n\n')
