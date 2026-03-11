import streamlit as st
import streamlit_option_menu
from processing import preprocess
from processing.display import Main

st.set_page_config(layout="wide")

displayed = []

if 'movie_number' not in st.session_state:
    st.session_state['movie_number'] = 0

if 'selected_movie_name' not in st.session_state:
    st.session_state['selected_movie_name'] = ""

if 'user_menu' not in st.session_state:
    st.session_state['user_menu'] = ""


def main():

    def initial_options():

        st.session_state.user_menu = streamlit_option_menu.option_menu(
            menu_title='What are you looking for? 👀',
            options=['Recommend me a similar movie', 'Describe me a movie', 'Check all Movies'],
            icons=['film', 'film', 'film'],
            menu_icon='list',
            orientation="horizontal",
        )

        if st.session_state.user_menu == 'Recommend me a similar movie':
            recommend_display()

        elif st.session_state.user_menu == 'Describe me a movie':
            display_movie_details()

        elif st.session_state.user_menu == 'Check all Movies':
            paging_movies()

    def recommend_display():

        st.title('Movie Recommender System')

        selected_movie_name = st.selectbox(
            'Select a Movie...', new_df['title'].values
        )

        rec_button = st.button('Recommend')

        if rec_button:
            st.session_state.selected_movie_name = selected_movie_name

            recommendation_tags(new_df, selected_movie_name, r'Files/similarity_tags_tags.pkl', "are")
            recommendation_tags(new_df, selected_movie_name, r'Files/similarity_tags_genres.pkl', "on the basis of genres are")
            recommendation_tags(new_df, selected_movie_name, r'Files/similarity_tags_tprduction_comp.pkl', "from the same production company are")
            recommendation_tags(new_df, selected_movie_name, r'Files/similarity_tags_keywords.pkl', "on the basis of keywords are")
            recommendation_tags(new_df, selected_movie_name, r'Files/similarity_tags_tcast.pkl', "on the basis of cast are")

    def recommendation_tags(new_df, selected_movie_name, pickle_file_path, text):

        movies, posters = preprocess.recommend(new_df, selected_movie_name, pickle_file_path)

        st.subheader(f'Best Recommendations {text}...')

        rec_movies = []
        rec_posters = []

        cnt = 0

        for i, j in enumerate(movies):

            if cnt == 5:
                break

            if j not in displayed:
                rec_movies.append(j)
                rec_posters.append(posters[i])
                displayed.append(j)
                cnt += 1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.text(rec_movies[0])
            st.image(rec_posters[0])

        with col2:
            st.text(rec_movies[1])
            st.image(rec_posters[1])

        with col3:
            st.text(rec_movies[2])
            st.image(rec_posters[2])

        with col4:
            st.text(rec_movies[3])
            st.image(rec_posters[3])

        with col5:
            st.text(rec_movies[4])
            st.image(rec_posters[4])

    def display_movie_details():

        selected_movie_name = st.session_state.selected_movie_name

        if not selected_movie_name:
            st.warning("Please select a movie from the 'Recommend' section first!")
            return

        info = preprocess.get_details(selected_movie_name)

        if info is None:
            st.error("Movie details not found. Please try another movie.")
            return

        with st.container():

            image_col, text_col = st.columns((1, 2))

            with image_col:
                st.image(info[0])

            with text_col:

                st.title(selected_movie_name)

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.text("Rating")
                    st.write(info[8])

                with col2:
                    st.text("No. of ratings")
                    st.write(info[9])

                with col3:
                    st.text("Runtime")
                    st.write(info[6])

                st.write("Overview")
                st.write(info[3])

        st.header('Cast')

        cnt = 0
        urls = []
        bio = []

        for i in info[14]:

            if cnt == 5:
                break

            url, biography = preprocess.fetch_person_details(i)

            urls.append(url)
            bio.append(biography)

            cnt += 1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.image(urls[0])
            with st.expander("Show More"):
                st.write(bio[0])

        with col2:
            st.image(urls[1])
            with st.expander("Show More"):
                st.write(bio[1])

        with col3:
            st.image(urls[2])
            with st.expander("Show More"):
                st.write(bio[2])

        with col4:
            st.image(urls[3])
            with st.expander("Show More"):
                st.write(bio[3])

        with col5:
            st.image(urls[4])
            with st.expander("Show More"):
                st.write(bio[4])

    def paging_movies():

        max_pages = movies.shape[0] // 10

        col1, col2, col3 = st.columns([1, 9, 1])

        with col1:
            if st.button("Prev"):
                if st.session_state['movie_number'] >= 10:
                    st.session_state['movie_number'] -= 10

        with col2:
            new_page = st.slider("Jump to page", 0, max_pages, st.session_state['movie_number'] // 10)
            st.session_state['movie_number'] = new_page * 10

        with col3:
            if st.button("Next"):
                if st.session_state['movie_number'] + 10 < len(movies):
                    st.session_state['movie_number'] += 10

        display_all_movies(st.session_state['movie_number'])

    def display_all_movies(start):

        i = start

        for _ in range(2):

            with st.container():

                cols = st.columns(5)

                for col in cols:

                    if i >= len(movies):
                        break

                    id = movies.iloc[i]['movie_id']
                    link = preprocess.fetch_posters(id)

                    with col:
                        st.image(link, caption=movies['title'][i])

                    i += 1

    with Main() as bot:

        bot.main_()

        new_df, movies, movies2 = bot.getter()

        initial_options()


if __name__ == '__main__':
    main()
