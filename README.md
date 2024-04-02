# Movie Recommender System

This repository offers the code for a content-based movie recommender system. The system leverages the TMDB 5000 dataset. By focusing on movie attributes like genres, descriptions, and cast, it personalizes recommendations based on a user's past preferences. To achieve this, the system employs vectorization techniques to convert textual movie data into a numerical format suitable for machine learning algorithms. Subsequently, similarity measures like cosine similarity are used to identify movies with profiles most closely resembling those previously enjoyed by the user. Finally, the system filters or selects a predefined number of these most similar movies, generating a personalized recommendation list for the user.

## Files Included

- `Notebook.ipynb`: Jupyter Notebook containing the initial exploration, data preprocessing, and algorithm development.
- `functions.py`: Python script containing necessary functions for the movie recommender system.
- `main.py`: Python script for Streamlit deployment of the recommender system.

## Usage

To use the movie recommender system:

1. Clone the repository to your local machine.
2. Ensure you have Python installed on your machine.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Download the ZIP archive containing the required files. Extract the contents of the downloaded ZIP archive into the main directory of your project or where you plan to use the movie recommender system.
    [https://drive.google.com/file/d/17u3cgVbYQSaVhyehTel1kPoTr1YHidwC/view?usp=sharing](https://drive.google.com/file/d/17u3cgVbYQSaVhyehTel1kPoTr1YHidwC/view?usp=sharing)
    This link will take you to the Google Drive file containing the movie recommender system files.
6. Run the `main.py` file to deploy the recommender system using Streamlit.

## Credits

This movie recommender system was developed by Subarno Maji.

If you have any questions or suggestions, feel free to contact me at [subarnomaji@gmail.com]. Thank you for using the movie recommender system!
