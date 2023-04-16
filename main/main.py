import streamlit as st 
import pandas as pd
import pyrebase
st.set_page_config(layout="wide",page_title="KhelCalc")


d=ast.literal_eval(st.secrets["d"])


firebaseConfig=ast.literal_eval(st.secrets["firebaseConfig"])


firebase = pyrebase.initialize_app(firebaseConfig)
db=firebase.database()



def calc(targ,sp,w,tm):
  ans=[]
  for i in sp:
    ckg=d[i]
    ckg*=w
    fin=float(targ/ckg)
    fin=round(fin,3)

    min=int((fin-int(fin))*60)
    if tm<fin:
        s=[0,i]
    else:
        s=[int(fin),min+1,i]
    ans.append(s)
  
  return ans


def push(data):
    datad={'activity':data[1],'time':data[3]}
    db.child(int(data[0])).push(datad) 

def dataview(data):
  stuff=db.child(data[0]).get()
  output=[i.val() for i in stuff.each()]
  frequency = {}
  for item in output:
      for activity in item['activity']:
          if activity in frequency:
              frequency[activity] += 1
          else:
              frequency[activity] = 1
  for i in list(frequency.keys()):
    #frequency[i]=[i for i in range(frequency[i]+1)]
    frequency[i]=[frequency[i]]
  return(frequency)
  


header=st.container()
with header:
    itms, txt = st.columns([1,1])
    with itms:
        st.subheader("KhelCalc")
        st.write("A website that takes in the users body weight, amount od calories to burn, favourite sport and amount of free time to display the amount of time they must spend on that sport to achieve their target.")

        weight=st.number_input("Enter your weight in Kilograms")
        calcount=st.number_input("Enter target calories")
        time=st.number_input("Enter available hours in hours")
        pref=st.multiselect("Enter your preferred sports",d.keys())
        if all([weight,calcount,time,pref])!=0:
          st.text("You could indulge in:")
          for i in calc(calcount,list(pref),weight*2.205,time):
              st.text(str(i[-1])+'for '+str(i[0])+' hours '+'and '+str(i[1])+' minutes')    
          
          push([calcount,list(pref),weight*2.205,time])
          st.write("Users with similar calorie goals also played these sports")
          st.bar_chart(data=dataview([int(calcount)]),use_container_width=True)
          


    with txt:
        st.write("Playing sports is a great way to stay physically active and healthy, but it's important to keep safety in mind to avoid injury. ")
        st.write("Here are some basic safety precautions for playing any sport:")
        st.write("Wear appropriate protective gear: Depending on the sport, wearing appropriate protective gear such as helmets, mouthguards, shin guards, or padding is important to reduce the risk of injury.")
        st.write("Stay hydrated: Drink plenty of water before, during, and after playing sports to stay hydrated and avoid heat-related illnesses.")
        st.write("Warm-up and cool down: Always take the time to warm up and cool down properly to prevent injury and improve performance.")
        st.write("Know the rules: Understanding and following the rules of the sport can help reduce the risk of injury for both yourself and other players.")
        st.write("Listen to your body: If you feel pain or discomfort during play, stop and take a break. Don't push yourself beyond your limits.")
        st.write("Use proper technique: Using proper technique and form can help reduce the risk of injury and improve performance.")
        st.write("Play on safe surfaces: Avoid playing on unsafe surfaces such as concrete or uneven ground that can increase the risk of falls and injuries.")
        st.write("Be aware of weather conditions: Extreme weather conditions such as heat, cold, or rain can increase the risk of injury. Adjust your play accordingly and take breaks as needed.")
        st.write("Remember, taking the necessary precautions before and during sports activities can help keep you safe and healthy while enjoying the game.")
