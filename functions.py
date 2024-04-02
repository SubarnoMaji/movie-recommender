import pickle
import requests
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

movies = pickle.load(open('pickles/movie_list.pkl','rb'))
similarity = pickle.load(open('pickles/similarity.pkl','rb'))
similarity_cast = pickle.load(open('pickles/similarity_cast.pkl','rb'))
similarity_director = pickle.load(open('pickles/similarity_director.pkl','rb'))


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

def fetch_by_id(movie_ids):

        
    recommended_movie_posters =[]
    recommended_movie_names =[]
    
    for movie_id in movie_ids:
       
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies[movies.movie_id == 57825].title)


    return recommended_movie_names,recommended_movie_posters

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

def calculate_similarity(text1, text2):

    vectorizer = TfidfVectorizer()

    
    tfidf_matrix = vectorizer.fit_transform([text1, text2])

  
    similarity_score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

    return similarity_score[0][0]

def search_text(text):
    sim=[]
    y = []
    l = []
    ps = PorterStemmer()
    
    for i in text.split():
        y.append(ps.stem(i))
        
    text1 = " ".join(y)

    for i in movies.index:
        
        similarity = calculate_similarity(text1, movies.tags[i])
        sim.append(similarity)
        
    sim=sorted(list(enumerate(sim)),reverse=True,key = lambda x: x[1])
    
    for i in sim[0:4]:
        l.append(movies.iloc[i[0]].id)

    return l