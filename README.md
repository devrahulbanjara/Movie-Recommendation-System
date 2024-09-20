# Movie Recommendation System

This project is a **Movie Recommendation System** that provides personalized movie suggestions using the OMDB dataset from Kaggle. It processes and analyzes movie data to recommend movies based on user preferences or movie similarities. The system utilizes various recommendation algorithms such as content-based filtering, enhancing users' movie-watching experience by suggesting relevant titles.

## Features

- Data cleaning and feature extraction from the movie dataset
- Generation of a similarity matrix for movies based on keywords, genres, cast, and crew
- A Streamlit app to interact with users and provide real-time movie recommendations

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/devrahulbanjara/Movie-Recommendation-System.git
cd Movie-Recommendation-System 
```
### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Generate the similarity.pkl file
  - You need to generate the similarity.pkl file, which is used to find similar movies. To do so:
    1) Run the script to generate the similarity matrix:
    ```bash
    pip install -r requirements.txt
    ```
    2) Once the script completes, it will generate a similarity.pkl file.
    ```bash
    mv similarity.pkl models/
    ```
### 5. Run the Streamlit App
  Now that everything is set up, run the Streamlit app to get movie recommendations:
```bash
streamlit run src/app.py
```

