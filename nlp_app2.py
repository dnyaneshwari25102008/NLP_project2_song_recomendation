import streamlit as st
import pandas as pd
import pickle
import numpy as np
import random

similarity=pickle.load(open("similarity.pkl","rb"))
df=pd.read_csv("song_data.csv")


st.title("🎵 TuneFinder")

st.sidebar.write("🎵 More listened song of the month")
st.sidebar.image("https://i.pinimg.com/236x/bb/51/9f/bb519fcc8ae45fb38d7aa352eeff24e4.jpg")

mood = st.sidebar.selectbox("",["😊 Happy", "😌 Relaxed", "🤩 Excited", "😱 Thrilled"])
st.sidebar.write("🎧 select Mood")
st.sidebar.write("")
#st.sidebar.write("🎵 click on below button to see best song of the week")
if st.sidebar.button("❤️Click here to see best song of the week "):
    st.sidebar.success(random.choice(df["track_name"].tolist()))

def get_name_from_index(i):
    if i<len(df) and i>0:
        return df.loc[i,'track_name']
    else:
        return''
    
def get_index_from_name(name):
    clean_song=name.lower().strip().replace(" ","").replace("-","")
    match=df[df['track_name'].str.strip().str.replace(" ",'').str.replace("-","")==clean_song]
    if not match.empty:
        return match.index[0]
    return -1


tab1,tab2,tab3=st.tabs(['🏠 Home','❤️ Recommendations','🔥 Trending'])

st.markdown(
    """
    <style>
    .stApp 
    {  
        background-color:#0B1320;
    }
    </style>
    """,unsafe_allow_html=True)

st.markdown(
    """
    <style>
       h1,h2,h3,p,label,span{
           color:white !important;
       } 
    </style>
    """,unsafe_allow_html=True
)


st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #0B1320;
}
</style>
""", unsafe_allow_html=True)


st.markdown(
    """
    <style>
    .stButton button {
        background-color:#1C2541 !important;
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] .stButton button {
        background-color: #1C2541 !important;
        color: white !important;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)



with tab1:
    st.button("🏠 Home")
    col1,col2=st.columns(2)
    with col1:
        img,text=st.columns([1,3])
        with img:
            st.image("https://i1.sndcdn.com/artworks-4Lu85Xrs7UjJ4wVq-vuI2zg-t500x500.jpg",width=100)
        with text:
            st.write("Liked songs")

        img1,text1=st.columns([1,3])
        with img1:
            st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1NtFOhMspkAB-YbZP5C74i358u6GgiUCIkPSnfV2ZHgB7CkkInCdtdVo&s=10",width=100)
        with text1:
            st.write("Talwinder")

        img2,text2=st.columns([1,3])
        with img2:
            st.image("https://i.pinimg.com/736x/dd/d1/e4/ddd1e499a601d0b942ba81130daae7e1.jpg",width=100)
        with text2:
            st.write("Arijit singh")

        
        img3,text3=st.columns([1,3])
        with img3:
            st.image("https://m.media-amazon.com/images/I/71LEFnH3H8L._USNaN_BL10_BG34,34,34_CLa%7CNaN,NaN%7C71LEFnH3H8L.jpg,91jt4vk78fL.jpg,91Fr15xsXQL.jpg,81RuEDQFrcL.jpg%7C0,0,NaN,NaN+0,0,NaN,NaN+NaN,0,NaN,NaN+0,NaN,NaN,NaN+NaN,NaN,NaN,NaN.jpg",width=100)
        with text3:
            st.write("Marathi song")


    with col2:
        img4,text4=st.columns([1,3])
        with img4:
            st.image("https://c.saavncdn.com/731/P-Square-Vol-1-English-2017-20170816133320-500x500.jpg",width=100)
        with text4:
            st.write("Trending songs")

        img5,text5=st.columns([1,3])
        with img5:
            st.image("https://a10.gaanacdn.com/gn_img/albums/MmqK5EKwRO/qK5pLzA1bw/size_m.jpg",width=100)
        with text5:
            st.write("English songs")

        img6,text6=st.columns([1,3])
        with img6:
            st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsRvWVV5dk_7FCFl7BW5iBZALrV_FLRJe7HQqhcYIehoHO2yd7bnF3ll0&s=10",width=100)
        with text6:
            st.write("Shreya ghoshal")

        
        img7,text7=st.columns([1,3])
        with img7:
            st.image("https://i.pinimg.com/236x/67/10/12/67101296c65a1f170d192a17950861ac.jpg",width=100)
        with text7:
            st.write("Korean song")

    st.subheader("🎵 Hit songs")
    col5,col6,col7,col8=st.columns(4)
    with col5:
        st.image("https://c.saavncdn.com/238/Bairan-Unknown-2026-20260223182954-500x500.jpg",width=190)
        st.write("Bairan")
    with col6:
        st.image("https://i.scdn.co/image/ab67616d0000b2739364ca9219b56d781f4e4f5d",width=190)
        st.write("Sheesha")
    with col7:
        st.image("https://i.scdn.co/image/ab67616d0000b273d38cece89af120be49a06024",width=190)
        st.write("Tu chahiye")
    with col8:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgzIwHuSu594Oj2Kxz-zvPMvXZE8WrI_DuYCgBEN70C-nB6AIWghAzu_DE&s=10",width=190)
        st.write("Ratoyaan")
    
    st.subheader("❤️ Singers")
    col9,col11,col12,col13=st.columns(4)
    with col9:
        st.image("https://m.media-amazon.com/images/I/51A7Gka2VfL._AC_UF894,1000_QL80_.jpg",width=190)
        st.write("Jennie")
    with col11:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSC6bnZ9MOrvIfEzjRbVaOinEB0Kb8diyq59uZL_77l44bxmEhDuKRNELtO&s=10",width=190)
        st.write("Arijit singh")
    with col12:
        st.image("https://i.pinimg.com/736x/26/a4/cf/26a4cf509b38fe9305ac4aef8e1b5e37.jpg",width=190)
        st.write("Jubin nitiyal")
    with col13:
        st.image("https://scontent.fklh3-1.fna.fbcdn.net/v/t39.30808-6/487401344_122206167770171926_8874349447753234424_n.jpg?stp=dst-jpg_tt6&cstp=mx1080x1350&ctp=s1080x1350&_nc_cat=103&ccb=1-7&_nc_sid=833d8c&_nc_ohc=5enEBkii0dkQ7kNvwHAc9cU&_nc_oc=AdoPc8HRz2n8TSNfzVaFpPwgghpcikym1WQMgqn4qbcFeZjeM75ND5_mvtwFNxsjMlbkYLjKt9p245dwklL4-V97&_nc_zt=23&_nc_ht=scontent.fklh3-1.fna&_nc_gid=Oy_dMXari-ga0DpQiTy5Bg&_nc_ss=7b289&oh=00_AQDnJCjtLjVv4_Laj3nHhy00l-yZJSRLpP1aIPnwevfaVw&oe=6A58841D",width=190)
        st.write("Shreya ghoshal")

with tab2:
    st.button("❤️ Recommendations")
    name=st.selectbox("** 🎧 Enter song name you listened **",df['track_name'].tolist())
    if st.button("Click to recomend"):
        index=get_index_from_name(name)
        if index!=-1:
            similarity_index=list(enumerate(similarity[index]))
            similarity_index=sorted(similarity_index,key=lambda x:x[1],reverse=True)
            st.write(" 🎵 You are listened :",df.loc[index,'track_name'])
        
            st.info(" ❤️ You must listen following song")
   
            for i in range(1, 6):
                song_idn = similarity_index[i][0]

                song_name = get_name_from_index(song_idn)
                image_url = df.iloc[song_idn]['artwork_url']

                col1, col2 = st.columns([1, 3])

                with col1:
                    st.image(image_url, width=100)
                with col2:
                    st.markdown(
                        f"<h5 style='color:white;'>{i}. {song_name}</h5>",
                        unsafe_allow_html=True
                    )
        else:
            st.write("song not found!")
with tab3:
    st.button("🔥 Trending")
    col10,col20=st.columns(2)
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzV-LwsYlggkxaxZ9kq-78_QJxKoG70x9bWrz0-JykA1BrsUDkIV2e3h4&s=10",width=190)
        st.write("Pal Pal(Talwinder)")
    with col2:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjuYczg_Dx0iTrVYCxcJ45jhSKtlfzs-bwsJqEhWhNb2TEkfzwGI11kcw&s=10",width=190)
        st.write("Lamborghini")
    with col3:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSs_ACcFnhIUYfekXxdU8Zw1Owyz-_J3XObwghrsKaaUKgerJ7k3I4ygqs&s=10",width=190)
        st.write("Like jennie")
    with col4:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCsHinoExOEcUXheqrnKOrutnZnFJpK0mdcf4jYb3-m9Rib59vjsdc-LM&s=10",width=190)
        st.write("BlueEyes")
    st.subheader("🎵 Hit songs")
    col5,col6,col7,col8=st.columns(4)
    with col5:
        st.image("https://c.saavncdn.com/238/Bairan-Unknown-2026-20260223182954-500x500.jpg",width=190)
        st.write("Bairan")
    with col6:
        st.image("https://i.scdn.co/image/ab67616d0000b2739364ca9219b56d781f4e4f5d",width=190)
        st.write("Sheesha")
    with col7:
        st.image("https://i.scdn.co/image/ab67616d0000b273d38cece89af120be49a06024",width=190)
        st.write("Tu chahiye")
    with col8:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgzIwHuSu594Oj2Kxz-zvPMvXZE8WrI_DuYCgBEN70C-nB6AIWghAzu_DE&s=10",width=190)
        st.write("Ratoyaan")






   
    
        
        
        
