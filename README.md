# BingeAI

A Streamlit-based movie recommendation app that suggests 10 similar movies based on a selected title and displays posters from TMDB when available.

## Features

- Pick a movie from the dropdown
- Get 10 recommended movies
- Show posters for recommended titles
- Download the recommendation dataset from Hugging Face
- Handle poster API failures gracefully

## Project Files

- `app.py` - Streamlit application
- `requirements.txt` - Python dependencies for local setup and deployment
- `.streamlit/secrets.toml.example` - example secrets file for local development
- `Untitled6.ipynb` - notebook used during development

## Requirements

- Python 3.10+
- The packages listed in `requirements.txt`

## Run Locally

1. Clone the repository.
2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Create `.streamlit/secrets.toml` from `.streamlit/secrets.toml.example`.
4. Fill in your Hugging Face repo details and TMDB API key.
5. Start the app:

```bash
streamlit run app.py
```

## Hugging Face Dataset

The app downloads `movie_recommender.pkl` from a Hugging Face dataset repository at startup. The file is not stored in this GitHub repository.

If your dataset is private, provide an `HF_TOKEN` in Streamlit secrets. If it is public, the token is optional.

## Secrets

Store deployment values in Streamlit secrets or environment variables:

- `HF_REPO_ID`
- `HF_REPO_TYPE`
- `HF_FILENAME`
- `HF_TOKEN` (optional for public datasets)
- `TMDB_API_KEY`

## Deployment

To deploy on Streamlit Community Cloud:

1. Push the repository to GitHub.
2. Make sure your Hugging Face dataset repo contains `movie_recommender.pkl`.
3. Add the required secrets in Streamlit Community Cloud.
4. Deploy `app.py` as the main file.

## Notes

- If a poster cannot be fetched, the app shows `Poster unavailable`.
- If the Hugging Face dataset cannot be reached, the app will stop with a setup error message.
