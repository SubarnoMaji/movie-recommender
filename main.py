import streamlit as st
import pickle
from functions import *

def display_main(recommended_movie_posters,recommended_movie_names,recommended_id):
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
    
def display_cast(recommended_movie_names,recommended_movie_posters,recommended_id):
        st.markdown(f"""
                # <div > <span style="color:#d9d9d9;font-size:35px">More from the Star Cast :sparkles: </span></div>
               
               """, 
               unsafe_allow_html=True)
        
        col4, col5, col6= st.columns(3)
    
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
    
def display_director(recommended_movie_names,recommended_movie_posters,recommended_id):
    
    st.markdown(f"""
                # <div > <span style="color:#d9d9d9;font-size:35px">More from the Director :mega: </span></div>
               
               """, 
               unsafe_allow_html=True)

    col4, col5, col6= st.columns(3)
    
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



movies = pickle.load(open('pickles/movie_list.pkl','rb'))


st.markdown(f"""
                # <div align= "center"> <span style="color:#d9d9d9;"> Movie Recommender :movie_camera: </span></div>
               
               """, 
               unsafe_allow_html=True)


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Similar movies",
    movie_list
)


if st.button('Show Recommendation'):  
    st.markdown(f"""
                # <div > <span style="color:#d9d9d9;font-size:35px"> Top Recommendations :boom: </span></div>
               
               """, 
               unsafe_allow_html=True)

    recommended_movie_names,recommended_movie_posters,recommended_id = recommend(selected_movie)
    recommended_movie_names_cast,recommended_movie_posters_cast,recommended_id_cast = recommend_cast(selected_movie)
    recommended_movie_names_director,recommended_movie_posters_director,recommended_id_director = recommend_director(selected_movie)    
    
    
    display_main(recommended_movie_posters,recommended_movie_names,recommended_id)
    display_cast(recommended_movie_names_cast,recommended_movie_posters_cast,recommended_id_cast)
    display_director(recommended_movie_names_director,recommended_movie_posters_director,recommended_id_director)
   
            
search_query = st.text_input("Search for a movie with plot", "Type here...") 

if st.button("Search"):
        recommended_id = search_text(search_query)
        recommended_movie_names,recommended_movie_posters = fetch_by_id(recommended_id)
        
        display_main(recommended_movie_posters,recommended_movie_names,recommended_id)