import streamlit as st
import pandas as pd
import numpy as np
import json
from datetime import datetime
import os

path=r'/storage/0000-0000/Memmento-v3/newfoldertosync/'
#path=r'C:\Users\zack`\Desktop\tOOTH\'
###path=r'C:\Users\dianne\Documents\dental\\'

###ff=open(path+'Names.json')

#path=r'C:\Users\dianne\Documents\dental\usb_streamlit\\'
#ff=open(path+'Namezzz.json')
ff=open('Namezzz.json')
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
            
st.title("Cases by Due Date")           
for index,row in df2.iterrows():   ##...>>or change to df.iterrows():
    print('df4')
                #print(df)
    nowtime=pd.Timestamp.now()
    time_left=row['date-due']-nowtime
    print('Due in:',time_left)
    ff=pd.to_datetime(row['date-due'])
    day=ff.day
    month=ff.month
    year=ff.year
    print('day left:',day)
    print('month left:',month)
    print('year left:',year)
   # nw=(nowtime-ff)/ pd.timedelta64(1, 'D')
  #  print('nw:',nw)
    nw1=(ff-nowtime).days
    print('nw1:',nw1)
    print('ct:',row['sub-c'])
    if 1>nw1:
        print("small")
        st.warning("WARNING: CASE OVER DUE: " +str(nw1)+ " days  by "+ str(month)+'/'+str(day)+'/'+str(year) )
    else:
        print('bigg')
    
        st.warning("CASE DUE IN: " +str(nw1)+ " days  by "+ str(month)+'/'+str(day)+'/'+str(year) )
    print(index,row['case#'],row['patient'],row['date-due'])
   # st.write(">>",index,row['case#'],row['patient'],row['date-due'])
    
    with st.expander(":: "+row['case#']+' '+row['patient']+"  --  "+row['description']+'--'+'#'+row['tooth#']+'  --  '+row['shade']+' -- '+row['quads']+'-------->'+ row['status']+
                                              "\n\n"+"   -------------------------------   "+row['description2']+" -- "+row['quads2']):
    #with st.expander("Details"):
        col1,col2,col3=st.columns(3)
        with col1:
            col1.write('Period-'+row['billing-period'])
            st.write('Office:',row['Dental Office'])
        
        
        with col2:
            st.write('Ph:3474943356')
            st.write('cont:',row['sub-c'])
            
        
        st.write('cont:',row['sub-c'])
        col3.write('picked:'+row['date-picked-up'])
        col3.write('delivery:'+row['drop-off-date'])
        
        #st.write(str('delvrd:',row['drop-off-date']))
        st.write('cont:',row['sub-c'])
        
        st.write('Dentist:' ,row['dentist'])
        st.write(row['prescription_pic'])
        print(str(row['prescription_pic']))
        print(str('delvrd:'+row['drop-off-date']))
def  now():   
	now1=datetime.now()  #<---NOOOW
	print('now:',now1)
now()

now1=datetime.now() 
date2=now1.strftime("%x %X")  
print('today:',date2)

#with st.expander("Details"):
#        st.write('Dentist:', row['dentist'])

st.sidebar.title("Todays date")
st.sidebar.button('search')
st.write("Main Page")