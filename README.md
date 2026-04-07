# BingeAI

A Streamlit-based movie recommendation app that suggests 10 similar movies based on a selected title and displays posters from TMDB when available.

## Features

- Pick a movie from the dropdown
- Get 10 recommended movies
- Show posters for recommended titles
- Handle poster API failures gracefully

## Project Files

- `app.py` - Streamlit application
- `movie_recommender.pkl` - processed movie data and similarity matrix
- `Untitled6.ipynb` - notebook used during development

## Requirements

- Python 3.10+
- Streamlit
- pandas
- requests
- scikit-learn
- numpy

Install dependencies with:

```bash
pip install streamlit pandas requests scikit-learn numpy
```

## Run Locally

1. Clone the repository.
2. Make sure `movie_recommender.pkl` is present in the project folder.
3. Install the required packages.
4. Start the app:

```bash
streamlit run app.py
```

## Important Note About `movie_recommender.pkl`

The app depends on `movie_recommender.pkl` to load the movie dataset and similarity matrix. This file is not included in the GitHub repository, so you must place it manually in the project root before running or deploying the app.

## TMDB API

Movie posters are fetched from TMDB. The app currently expects a TMDB API key in the code. For production deployment, it is better to move the API key into environment variables or Streamlit secrets instead of hardcoding it.

## Deployment

To deploy on Streamlit Community Cloud:

1. Push the repository to GitHub.
2. Make sure the deployment environment can access `movie_recommender.pkl`.
3. Add your TMDB API key securely using Streamlit secrets.
4. Deploy `app.py` as the main file.

## Notes

- If a poster cannot be fetched, the app shows `Poster unavailable`.
- If `movie_recommender.pkl` is missing, the app will not start.
