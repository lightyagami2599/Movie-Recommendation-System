# 🎬 Movie Recommender System

Welcome to my Movie Recommender System! I built this project to help movie lovers (like myself) find their next favorite film without the endless scrolling. Using Natural Language Processing (NLP) and a sleek Streamlit interface, this app analyzes movie metadata to find the perfect matches for you.

## 🚀 What can this app do?

*   **Smart Recommendations**: Get suggestions based on what you like. The app looks at tags, genres, cast, and even keywords to suggest similar movies.
*   **Deep Dives**: Want to know more about a movie? Head to the "Describe me a movie" section to see the overview, rating, budget, revenue, and more.
*   **Meet the Cast**: I've integrated the TMDB API to pull in real-time poster images and cast biographies, so you can see who's behind the characters.
*   **Explore Everything**: A dedicated "Check all Movies" section with smooth paging to browse through the entire TMDB 5000 dataset.

## 🛠️ How I Built It (Tech Stack)

*   **Python**: The backbone of the project.
*   **Streamlit**: For that clean, interactive web interface.
*   **Pandas**: For all the heavy lifting with data manipulation.
*   **Scikit-learn**: Used `CountVectorizer` and `Cosine Similarity` to calculate how "close" two movies are based on their tags (Bag of Words model).
*   **NLTK**: For text preprocessing and stemming to ensure the engine understands movie themes correctly.
*   **TMDB API**: To fetch high-quality posters and up-to-date actor information.

## 📺 Live Demo
Check out the deployed app: [**Streamlit App Link**](https://movie-recommendation-system-ek42mzvwcnd4uimekasuzd.streamlit.app/)

## ⚙️ Running it Locally

If you want to play around with the code yourself:

1.  **Clone the repo**:
    ```bash
    git clone https://(https://github.com/lightyagami2599/Movie-Recommendation-System)
    ```
2.  **Install the requirements**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Launch the app**:
    ```bash
    streamlit run main.py
    ```

---
*Developed with ❤️ by [Vibhu Vishwakarma](https://github.com/lightyagami2599/Movie-Recommendation-System)*
