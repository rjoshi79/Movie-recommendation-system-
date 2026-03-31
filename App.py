import streamlit as st
import pickle
import pandas as pd



def recommend(movie):
     movie_index = movies[movies['title'] == movie].index[0]
     distance = similar[movie_index]
     movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

     recommended_movies=[]



     for i in movie_list:
         movie_id=i[0]
         recommended_movies.append(movies.iloc[i[0]].title)
     return recommended_movies
movie_dic=pickle.load(open('movie_dic.pkl','rb'))

similar = pickle.load(open('similar.pkl','rb'))
movies=pd.DataFrame(movie_dic)
st.title('Cinema Sense')


movie_name = st.selectbox(
     "Select Movie",
     movies['title'].values
 )

if st.button("Recommandation"):
     recommendations = recommend(movie_name)
     for i in recommendations:
         st.write(i)


