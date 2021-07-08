""""
Test Streamlit app used for lab meeting on 2021-07-08
"""
import streamlit as st
import pandas as pd
import numpy as np


# Page config
st.set_page_config(
    page_title='Lab Meeting 2021-07-08',
    layout='wide',
    page_icon='https://streamlit.io/images/brand/streamlit-mark-color.png',
    initial_sidebar_state='expanded'
)

# Individual Page Functions
def title():
    st.image('https://streamlit.io/images/brand/streamlit-logo-primary-colormark-lighttext.png')


def streamlit_intro():
    st.header('What is Streamlit?')
    st.markdown("""
        - [Streamlit](https://streamlit.io/) is an open source Python library
        - Create a complete web app with __only__ Python
        - Fast way to create data share apps
    """)

    with st.beta_expander('Uber Example'):
        uber_example()



def uber_example():
    col1, col2 = st.beta_columns(2)
    with col1:
        st.title('Uber pickups in NYC')

        DATE_COLUMN = 'date/time'
        DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
                    'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

        @st.cache
        def load_data(nrows):
            data = pd.read_csv(DATA_URL, nrows=nrows)
            lowercase = lambda x: str(x).lower()
            data.rename(lowercase, axis='columns', inplace=True)
            data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
            return data

        data_load_state = st.text('Loading data...')
        data = load_data(10000)
        data_load_state.text("Done! (using st.cache)")

        if st.checkbox('Show raw data'):
            st.subheader('Raw data')
            st.write(data)

        st.subheader('Number of pickups by hour')
        hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
        st.bar_chart(hist_values)

        # Some number in the range 0-23
        hour_to_filter = st.slider('hour', 0, 23, 17)
        filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

        st.subheader('Map of all pickups at %s:00' % hour_to_filter)
        st.map(filtered_data)

    with col2:
        st.markdown("""
            ### See full tutorial in [Streamlit docs](https://docs.streamlit.io/en/stable/tutorial/create_a_data_explorer_app.html)
        """)
        st.markdown("""
            ```python
            st.title('Uber pickups in NYC')

            DATE_COLUMN = 'date/time'
            DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
                        'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

            @st.cache
            def load_data(nrows):
                data = pd.read_csv(DATA_URL, nrows=nrows)
                lowercase = lambda x: str(x).lower()
                data.rename(lowercase, axis='columns', inplace=True)
                data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
                return data

            data_load_state = st.text('Loading data...')
            data = load_data(10000)
            data_load_state.text("Done! (using st.cache)")

            if st.checkbox('Show raw data'):
                st.subheader('Raw data')
                st.write(data)

            st.subheader('Number of pickups by hour')
            hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
            st.bar_chart(hist_values)

            # Some number in the range 0-23
            hour_to_filter = st.slider('hour', 0, 23, 17)
            filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

            st.subheader('Map of all pickups at %s:00' % hour_to_filter)
            st.map(filtered_data)
            ```
        """)


def streamlit_apps():
    st.title("Deploy apps to Streamlit")
    st.markdown("""
        - Request invite to [Streamlit sharing](https://streamlit.io/sharing)
        - Add your app to a public GitHub repo
        - Connect GitHub account to Streamlit sharing account
        - Create new app and deploy!
        - Deployed app can be found at `https://share.streamlit.io/[user name]/[repo name]/[branch name]/[app path]`
    """)

    st.header("Examples")
    st.markdown("""
        - [Python Data Visualization Tour](https://share.streamlit.io/discdiver/data-viz-streamlit/main/app.py)
        - [GECO (Gene Expression Clustering Optimization)](https://share.streamlit.io/starstorms9/geco/master/geco_app.py/)
        - [The evolution, evolvability and engineering of gene regulatory DNA](https://share.streamlit.io/1edv/evolution/app/app.py)
    """)


def github_copilot():
    st.header('GitHub Copilot')
    st.subheader('The AI Pair Programmer')

    st.markdown("""
        - Remember OpenAI's GPT-3?
        - OpenAI's Codex trained on public code on GitHub
        - Revealed GitHub Copilot on June 29, 2021
        - Limited preview available as a Visual Studio Code extension
    """)

    st.image('https://copilot.github.com/diagram.png',
        caption='Photo: https://copilot.github.com/diagram.png')


def copilot_example():
    st.title('Copilot Demo')
    st.video('https://www.youtube.com/watch?v=edSZh-tpTIk&ab_channel=Catalin%27sTech')


# Main App Execution
pages = {
    'Title': title,
    'Streamlit Intro': streamlit_intro,
    'Streamlit Apps': streamlit_apps,
    'GitHub Copilot': github_copilot,
    'Copilot Example': copilot_example,
}

st.sidebar.title('Lab Meeting')
st.sidebar.header('2021-07-08')
current_page = st.sidebar.radio('', list(pages.keys()), index=0)
pages[current_page]()
