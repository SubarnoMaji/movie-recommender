import streamlit as st
import pickle
import numpy as np
import sklearn 
import requests


with st.sidebar:
    st.markdown(f"""
                <div style="text-align: center;">
                
                ##  <span style="color:#d9d9d9; ">Explore Subarno Maji's Projects </span>:chart_with_upwards_trend:
             
                <br>              
                <div>
                """, 
               unsafe_allow_html=True)
    st.markdown(f"""
                <div style="text-align: center;  height: 300px; overflow-y: auto;">
              <button style="background-color:#990033; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 10px; cursor: pointer; border-radius: 4px;width: 250px;">
               <a href="https://www.example1.com" style="color: white; text-decoration: none;"><b>Laptop Price Predictor</b> </a>
                </button> 
                <br>
                
            <button style="background-color: #990033; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 10px; cursor: pointer; border-radius: 4px;width: 250px;">
                <a href="https://www.example2.com" style="color: white; text-decoration: none;"><b>Salary Predictor</b></a>
             </button>
                

            <button style="background-color: #990033; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 10px; cursor: pointer; border-radius: 4px;width: 250px;">
            <a href="https://www.example2.com" style="color: white; text-decoration: none;"><b>Movie Recommender</b></a>
             </button>
                
            </div>
                <hr>
                """, 
               unsafe_allow_html=True)
    st.markdown(f"""
                <div style="text-align: center;">
                
                ##  <span style="color:#d9d9d9; "> Connect with me  </span> :smile:
             
                <br>              
                <div>
                """, 
               unsafe_allow_html=True)
    st.markdown("""



   
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.2/css/all.min.css" integrity="sha512-1sCRPdkRXhBV2PBLUdRb4tMg1w2YPf37qatUFeS7zlBy7jJI8Lf4VHwWfZZfpXtYSLy85pkm9GaYVYMfw5BC1A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

<link rel="stylesheet" href="Style.css">

<div align="center" class="icons" style="display:"flex"; justify-content:"space-between";" >

<a href="mailto:subarnomaji@gmail.com"><i class="fa-solid fa-envelope" style="font-size: 30px; color: #ff4d4d;padding-right: 10px;"></i></a>
<a href="https://www.facebook.com/profile.php?id=100083622261232"><i class="fa-brands fa-facebook" style="font-size: 30px; color:#3b5998;padding-right: 10px;"></i></a>
<a href="#"><i class="fa-brands fa-whatsapp" style="font-size: 30px; color: #075E54;padding-right: 10px;"></i></a>
<a href="https://www.linkedin.com/in/subarno-maji-6076a425b/"><i class="fa-brands fa-linkedin" style="font-size: 30px; color:#3399ff;padding-right: 10px;"></i></a>
<a href="https://github.com/SubarnoMaji"><i class="fa-brands fa-github" style="font-size: 30px; color: white;padding-right: 10px;"></i></a>


   
   </div>
   
   """,unsafe_allow_html=True
       


   )


movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
similarity_cast = pickle.load(open('similarity_cast.pkl','rb'))
similarity_director = pickle.load(open('similarity_director.pkl','rb'))

def get_rating(vote_average):
     if vote_average < 2 :
          return 1 
     elif vote_average < 4:
           return 2 
     elif vote_average < 6:
           return 3 
     elif vote_average < 8:
           return 4
     elif vote_average < 10:
           return 5

def fetch_details(id):
    indx = movies[movies['id'] == id].index[0]
    vote_average = movies['vote_average'][indx]
    runtime= movies['runtime'][indx]  
    popularity=movies['popularity'][indx]  
    overview=movies['overview_original'][indx]  
    rating= get_rating(vote_average)  
    original_language=movies['original_language'][indx]  
    genres=movies['genres'][indx]  
    path = "Rating/{}.png".format(rating)
    year= movies['year'][indx]


    return vote_average,runtime,popularity,overview,path,genres,original_language,year
    
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=def73fa5f4f622c3b3fcafc2e35fe13a&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()

    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def fetch_trailer(movie_id):
    movie_id = movies[movies.title ==movie_id ].movie_id 
    url = "http://api.themoviedb.org/3/movie/{}/videos?api_key=def73fa5f4f622c3b3fcafc2e35fe13a".format(movie_id)
    data = requests.get(url)
    response = requests.get(url)
    data = response.json()
    key = data["results"][0]["key"]
    Y_url = "https://www.youtube.com/embed/" + key
    return Y_url

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters=[]
    recommended_id = []
    for i in distances[1:4]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_id.append(movies.iloc[i[0]].id)
    return recommended_movie_names,recommended_movie_posters,recommended_id

def recommend_cast(movie):
    index = movies[movies['title'] == movie].index[0]

    recommended_movie_names1,recommended_movie_posters1,recommended_id1=recommend(movie)
    
    distances = sorted(list(enumerate(similarity_cast[index])), reverse=True, key=lambda x: x[1])
     
    
    recommended_movie_names = []
    recommended_movie_posters=[]
    recommended_id = []
    
    for i in distances[1:7]:
        
            if i[1]>0.3 :
                movie_id = movies.iloc[i[0]].movie_id
                recommended_movie_posters.append(fetch_poster(movie_id))
                recommended_movie_names.append(movies.iloc[i[0]].title)
                recommended_id.append(movies.iloc[i[0]].id)
  
    
    for j in range(5):
        
        try:
             if recommended_id[0] == recommended_id1[j] :
               recommended_movie_posters.pop(0)
               recommended_movie_names.pop(0)
               recommended_id.pop(0)
        except:
             pass
    return recommended_movie_names,recommended_movie_posters,recommended_id

def recommend_director(movie):
    index = movies[movies['title'] == movie].index[0]

    recommended_movie_names1,recommended_movie_posters1,recommended_id1=recommend(movie)
    recommended_movie_names2,recommended_movie_posters2,recommended_id2=recommend_cast(movie)

    distances = sorted(list(enumerate(similarity_director[index])), reverse=True, key=lambda x: x[1])
     
    
    recommended_movie_names = []
    recommended_movie_posters=[]
    recommended_id = []
    
    for i in distances[1:12]:
        
            if i[1]>0.9 :
                movie_id = movies.iloc[i[0]].movie_id
                recommended_movie_posters.append(fetch_poster(movie_id))
                recommended_movie_names.append(movies.iloc[i[0]].title)
                recommended_id.append(movies.iloc[i[0]].id)
  
    
    for j in range(3):
        
        try:
             if recommended_id[0] == recommended_id2[j] :
               recommended_movie_posters.pop(0)
               recommended_movie_names.pop(0)
               recommended_id.pop(0)
        except:
             pass
        
    for i in range(3):   

        try:
             if recommended_id[0] == recommended_id1[i] :
               recommended_movie_posters.pop(0)
               recommended_movie_names.pop(0)
               recommended_id.pop(0)
        except:
             pass
    
    return recommended_movie_names,recommended_movie_posters,recommended_id




st.markdown(f"""
                # <div align= "center"> <span style="color:#d9d9d9;"> Movie Recommender :movie_camera: </span></div>
               
               """, 
               unsafe_allow_html=True)




movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Movie Search",
    movie_list
)


if st.button('Show Recommendation'):  
    st.markdown(f"""
                # <div > <span style="color:#d9d9d9;font-size:35px"> Top Recommendations :boom: </span></div>
               
               """, 
               unsafe_allow_html=True)

    recommended_movie_names,recommended_movie_posters,recommended_id = recommend(selected_movie)
    
    
    
    col1, col2, col3 = st.columns(3)

    
    with col1:

            st.image(recommended_movie_posters[0])
            

            
             
    with col2:
        vote_average,runtime,popularity,overview,path,genres,original_language,year = fetch_details(recommended_id[0])
        st.markdown(f"""
                <span style="color:#cccccc;"><b><i>
                {overview}
                </b></i></span>
               """, 
               unsafe_allow_html=True)
                
        st.markdown(f"""
                <br>
               """, 
               unsafe_allow_html=True)
                
                

    with col3:
        st.image(path) 
        st.markdown(f"""
                    Release Year  : <span style="color:#00cc00;"><b>{year}</b></span><br>
                    Language   : <span style="color:#00cc00;"><b>{original_language}</b></span><br>
                    Runtime    : <span style="color:#00cc00;"><b>{runtime}</b></span><br>
                    TMDB Votes : <span style="color:#00cc00;"><b>{vote_average}</b></span><br>
                """, 
               unsafe_allow_html=True)
       
         
    
    col8, col9, col10 = st.columns(3)
    
    with col8:

            st.image(recommended_movie_posters[1])
            

          
    with col9:
        vote_average,runtime,popularity,overview,path,genres,original_language,year = fetch_details(recommended_id[1])
        st.markdown(f"""
                <span style="color:#cccccc;"><b><i>
                {overview}
                </b></i></span>
               """, 
               unsafe_allow_html=True)
                
        st.markdown(f"""
                <br>
               """, 
               unsafe_allow_html=True)
                
                


           
    with col10:
        st.image(path) 
        st.markdown(f"""
                    Release Year  : <span style="color:#00cc00;"><b>{year}</b></span><br>
                    Language   : <span style="color:#00cc00;"><b>{original_language}</b></span><br>
                    Runtime    : <span style="color:#00cc00;"><b>{runtime}</b></span><br>
                    TMDB Votes : <span style="color:#00cc00;"><b>{vote_average}</b></span><br>
                """, 
               unsafe_allow_html=True)
    
    
    col11, col12, col13 = st.columns(3)
    with col11:

            st.image(recommended_movie_posters[2])
            

    
    with col12:

        vote_average,runtime,popularity,overview,path,genres,original_language,year = fetch_details(recommended_id[2])
        st.markdown(f"""

                <span style="color:#cccccc;"><b><i>
               
                {overview}
                </b></i></span>
               """, 
               unsafe_allow_html=True)
                
        st.markdown(f"""
                <br>
               """, 
               unsafe_allow_html=True)
                
                

     
               
        
    with col13:
           st.image(path)
           st.markdown(f"""
                    Release Year  : <span style="color:#00cc00;"><b>{year}</b></span><br>
                    Language   : <span style="color:#00cc00;"><b>{original_language}</b></span><br>
                    Runtime    : <span style="color:#00cc00;"><b>{runtime}</b></span><br>
                    TMDB Votes : <span style="color:#00cc00;"><b>{vote_average}</b></span><br>
                """, 
               unsafe_allow_html=True)
           
    st.markdown(f"""
                <br>
               """, 
               unsafe_allow_html=True)
    
    st.markdown(f"""
                # <div > <span style="color:#d9d9d9;font-size:35px">More from the Star Cast :sparkles: </span></div>
               
               """, 
               unsafe_allow_html=True)
   
    col4, col5, col6= st.columns(3)
    recommended_movie_names,recommended_movie_posters,recommended_id = recommend_cast(selected_movie)
    


    
    with col4:
                try:
                    st.image(recommended_movie_posters[0])
                    

                    with st.expander(recommended_movie_names[0]):
                        
                        vote_average,runtime,popularity,overview,path,genres,original_language,year = fetch_details(recommended_id[0])
                    
            
                            
                        st.markdown(f"""
                        <br>
                    """, 
                    unsafe_allow_html=True)
                        
                        

                        st.markdown(f"""
                            Release Year  : <span style="color:#00cc00;"><b>{year}</b></span><br>
                            Language   : <span style="color:#00cc00;"><b>{original_language}</b></span><br>
                            Runtime    : <span style="color:#00cc00;"><b>{runtime}</b></span><br>
                            TMDB Votes : <span style="color:#00cc00;"><b>{vote_average}</b></span><br>
                        """, 
                    unsafe_allow_html=True)
                    
                        st.image(path)
                except:
                     pass        
    with col5:
                try:
                     
                    st.image(recommended_movie_posters[1])
                    

                    with st.expander(recommended_movie_names[1]):
                    
                        vote_average,runtime,popularity,overview,path,genres,original_language,year = fetch_details(recommended_id[1])
                
                        st.markdown(f"""
                        <br>
                    """, 
                    unsafe_allow_html=True)
                        
                        st.markdown(f"""
                            Release Year  : <span style="color:#00cc00;"><b>{year}</b></span><br>
                            Language   : <span style="color:#00cc00;"><b>{original_language}</b></span><br>
                            Runtime    : <span style="color:#00cc00;"><b>{runtime}</b></span><br>
                            TMDB Votes : <span style="color:#00cc00;"><b>{vote_average}</b></span><br>
                        """, 
                    unsafe_allow_html=True)
                    
                        st.image(path)
                except:
                     pass
                
    with col6:
            
            try:
                st.image(recommended_movie_posters[2])
                    

                with st.expander(recommended_movie_names[2]):
                    
                        vote_average,runtime,popularity,overview,path,genres,original_language,year = fetch_details(recommended_id[2])
                
                        st.markdown(f"""
                        <br>
                    """, 
                    unsafe_allow_html=True)
                        
                        st.markdown(f"""
                            Release Year  : <span style="color:#00cc00;"><b>{year}</b></span><br>
                            Language   : <span style="color:#00cc00;"><b>{original_language}</b></span><br>
                            Runtime    : <span style="color:#00cc00;"><b>{runtime}</b></span><br>
                            TMDB Votes : <span style="color:#00cc00;"><b>{vote_average}</b></span><br>
                        """, 
                    unsafe_allow_html=True)
                    
                        st.image(path)
            except: 
                 pass
    
    
    st.markdown(f"""
                <br>
               """, 
               unsafe_allow_html=True)
    
    st.markdown(f"""
                # <div > <span style="color:#d9d9d9;font-size:35px">More from the Director :mega: </span></div>
               
               """, 
               unsafe_allow_html=True)
    col4, col5, col6= st.columns(3)
    recommended_movie_names,recommended_movie_posters,recommended_id = recommend_director(selected_movie)    


    with col4:
                try:
                    st.image(recommended_movie_posters[0])
                    

                    with st.expander(recommended_movie_names[0]):
                        
                        vote_average,runtime,popularity,overview,path,genres,original_language,year = fetch_details(recommended_id[0])
                    
            
                            
                        st.markdown(f"""
                        <br>
                    """, 
                    unsafe_allow_html=True)
                        
                        

                        st.markdown(f"""
                            Release Year  : <span style="color:#00cc00;"><b>{year}</b></span><br>
                            Language   : <span style="color:#00cc00;"><b>{original_language}</b></span><br>
                            Runtime    : <span style="color:#00cc00;"><b>{runtime}</b></span><br>
                            TMDB Votes : <span style="color:#00cc00;"><b>{vote_average}</b></span><br>
                        """, 
                    unsafe_allow_html=True)
                    
                        st.image(path)
                except:
                     pass        
    with col5:
                try:
                     
                    st.image(recommended_movie_posters[1])
                    

                    with st.expander(recommended_movie_names[1]):
                    
                        vote_average,runtime,popularity,overview,path,genres,original_language,year = fetch_details(recommended_id[1])
                
                        st.markdown(f"""
                        <br>
                    """, 
                    unsafe_allow_html=True)
                        
                        st.markdown(f"""
                            Release Year  : <span style="color:#00cc00;"><b>{year}</b></span><br>
                            Language   : <span style="color:#00cc00;"><b>{original_language}</b></span><br>
                            Runtime    : <span style="color:#00cc00;"><b>{runtime}</b></span><br>
                            TMDB Votes : <span style="color:#00cc00;"><b>{vote_average}</b></span><br>
                        """, 
                    unsafe_allow_html=True)
                    
                        st.image(path)
                except:
                     pass
                
    with col6:
            
            try:
                st.image(recommended_movie_posters[2])
                    

                with st.expander(recommended_movie_names[2]):
                    
                        vote_average,runtime,popularity,overview,path,genres,original_language,year = fetch_details(recommended_id[2])
                
                        st.markdown(f"""
                        <br>
                    """, 
                    unsafe_allow_html=True)
                        
                        st.markdown(f"""
                            Release Year  : <span style="color:#00cc00;"><b>{year}</b></span><br>
                            Language   : <span style="color:#00cc00;"><b>{original_language}</b></span><br>
                            Runtime    : <span style="color:#00cc00;"><b>{runtime}</b></span><br>
                            TMDB Votes : <span style="color:#00cc00;"><b>{vote_average}</b></span><br>
                        """, 
                    unsafe_allow_html=True)
                    
                        st.image(path)
            except: 
                 pass
    
    