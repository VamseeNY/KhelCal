import streamlit as st 


st.set_page_config(layout="wide",page_title="KhelCalc")


d={'Cycling-light(10-11.9mph)': 1.234853445,
 'Cycling-moderate(12-13.9mph)': 1.647825266,
 'Cycling-vigorous(14-15.9mph)': 2.059443081,
 'Running-slow(5mph) ': 1.647825266,
 'Running-moderate(7mph)': 2.368156442,
 'Running-vigorous(10mph)': 3.294973528,
 'Track and field(shotput/discus)': 0.82323563,
 'Track and field(high jump/pole vault)': 1.234853445,
 'Track and field(hurdles)': 2.059443081,
 'Badminton': 0.92749409,
 'Basketball-competitive': 1.647825266,
 'Basketball-casual': 1.234853445,
 'Cricket': 1.02972154,
 'Handball': 2.471060896,
 'Handball-team': 1.647825266,
 'Hockey(Field)': 1.647825266,
 'Skipping rope-fast': 2.471060896,
 'Skipping rope-moderate': 2.059443081,
 'Skipping rope-slow': 1.647825266,
 'Soccer-competitive': 2.059443081,
 'Soccer-casual': 1.441339355,
 'Squash': 2.471060896,
 'Table tennis': 0.82323563,
 'Tennis-doubles': 1.234853445,
 'Tennis-singles': 1.647825266,
 'Volleyball-competitive': 1.647825266,
 'Volleyball-casual': 0.617426722,
 'Backpacking/Hiking with pack': 1.441339355,
 'Hiking/cross country': 1.234853445,
 'Walking-moderate(3.0 mph)': 0.679710997,
 'Walking-brisk pace(3.5 mph)': 0.782615451,
 'Walking-very brisk (4.0 mph)': 1.02972154,
 'Swimming-freestyle': 1.441339355,
 'Swimming-leisurely': 1.234853445}

def calc(targ,sp,w,tm):
  ans=[]
  for i in sp:
    ckg=d[i]
    ckg*=w
    fin=float(targ/ckg)
    fin=round(fin,3)

    min=int((fin-int(fin))*60)
    if tm<fin:
        s="Insufficient time for sport: "+i
    else:
        s="Indulge in "+i+" for "+str(int(fin))+" hours and "+str(min+1)+" minutes"
    ans.append(s)
  
  return ans


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
        for i in calc(calcount,list(pref),weight*2.205,time):
            st.text(i)    
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