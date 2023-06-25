import streamlit as st
import pandas as pd
import numpy as np
import json
from datetime import datetime
import os

#path=r'/storage/0000-0000/Memmento-v3/newfoldertosync/'
#path=r'C:\Users\zack`\Desktop\tOOTH\'
#path=r'C:\Users\dianne\Documents\dental\usb_streamlit\\'
path=r'C:\Users\dianne\Documents\dental\\'
ff=open(path+'Names.json')
deeta=json.load(ff) 







from pandas import json_normalize
            #df = json_normalize(deeta)
df = json_normalize(deeta)
            ##for index,row in df.iterrows():
            ##    print('df')
                #print(df)
             ##   print(row['case#'],row['date-due'])
                ###dfm=(['case#'])+' -'+(['date-due'])
                ###print(dfm)
                ###break
                #>###df.sort_values(['date-due'],ascending=False)
                #>print ('sorted by due date--> ')
                #>print(row['case#'],row['date-due'])
                #>print (df)
            #df2=df.sort_values(['date-due']).reset_index(drop=True)
df['date-due']=pd.to_datetime(df['date-due'])
print(df['date-due'])
            #break
# Sort DataFrame by date column
           ### df.sort_values(by='date-due',ascending = False, inplace = True)
           ## print(";;;;")
            ##print(df['date-due'],df['case#'])

            
df2=df.sort_values(['date-due'],ascending=False)
print(df2['date-due'], df2['patient'])
            
            #break
#for row in df2:
#    print('dff')
#    print(row)
            
st.title("cases due")            
for index,row in df2.iterrows():   ##...>>or change to df.iterrows():
    print('df4')
                #print(df)
    print(index,row['case#'],row['patient'],row['date-due'])
    nowtime=pd.Timestamp.now()
    time_left=row['date-due']-nowtime
    print('Due in:',time_left)
    ff=pd.to_datetime(row['date-due'])
    day=ff.day
    print('day left:',day)
   # nw=(nowtime-ff)/ pd.timedelta64(1, 'D')
  #  print('nw:',nw)
    nw1=(nowtime-ff).days
    print('nw1:',nw1)
    ####Streamlit
    
    
    st.write(":::",index,row['case#'],row['patient'],row['date-due'])
    #st.write('...',nw1)
    
    
st.sidebar.title("Todays date")
st.sidebar.button('search')
st.write("Main Page")    
    
def  now():   
	now1=datetime.now()  #<---NOOOW
	print('now:',now1)
now()

now1=datetime.now() 
date2=now1.strftime("%x %X")  
print('today:',date2)


timestamp = pd.Timestamp(datetime(2021, 10, 10))
print (timestamp)
nowtime=pd.Timestamp.now()
print(nowtime)
