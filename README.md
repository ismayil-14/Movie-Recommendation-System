# Movie Recommendation System
 
## Introduction
### Overview of the Project
This project aims to develop a personalized movie recommendation system that predicts a user’s rating for a given movie based on historical rating data. The solution leverages machine learning techniques to provide accurate predictions and enhance the user's experience with tailored recommendations.
### Purpose and Scope
The primary objective is to build a scalable and reliable recommendation engine that can be deployed in a production environment. The project follows MLOps principles to ensure seamless integration, deployment, and maintenance of the model.

## Prerequisites
### Required Software, Tools, and Versions
Python: 3.8 or later
### Libraries:
Pandas
NumPy
Scikit-learn
XG Boost
Flask 
Pickle
Docker
### Development Tools:
Git
VS Code orJupyter Notebook
### Containerization:
Docker Desktop
### CI/CD:
GitHub Actions
### Cloud:
AWS Cloud

## Data Overview
### Description of the Dataset
The MovieLens dataset contains ratings provided by users for different movies. It includes fields such as user ID, movie ID, gender, rating, genres, release date, and timestamp.  
Preprocessing Steps
### Handling Missing Values:
There is no Missing value but Some noisy data like Timestamp before Release date has been removed. 
### Splitting Data:
The dataset was divided into training and testing subsets using an 80:20 ratio to ensure fair model evaluation.
Stratified sampling was applied to maintain distribution consistency across subsets.
## Model Development
Training Process and Validation Approach
### Preprocessing and PCA:
Movie genres were transformed using PCA to reduce the dimensionality while retaining critical variance.
The PCA components were integrated with user and movie metadata to form the final feature set.
### Training:
XGBoost was trained to classify user ratings into discrete categories. 
### Validation:
A stratified train-test split ensured consistent class distribution across subsets.
Cross-validation was used to evaluate model performance on unseen data.

## Metrics to Evaluate Model Performance
Accuracy: Measures the proportion of correctly predicted ratings.
Precision, Recall, and F1-Score: Provide a more granular understanding of performance across classes.
Confusion Matrix: Offers insights into class-specific misclassifications.
Model Serialization
Explanation of How the Model Was Saved
Once the XGBoost classification model was trained and validated, it was serialized for reuse in deployment. The Pickle library was used for its efficiency in handling large numpy arrays and objects, which is ideal for XGBoost models. Along with scalar, PCA model and user data. 

## API Implementation
### Overview
The project includes two APIs:
Flask API : Handles predictions using a trained XGBoost model and additional metadata like user ratings and movie genres.
Key Endpoint:
POST /predict: Accepts inputs (user_id, movie_id) and returns a predicted rating after preprocessing and passing through the model.
Error Handling: Ensures inputs are validated and provides detailed error responses.
Streamlit App (s_app.py): Provides a user-friendly interface to interact with the Flask API.
Users can input user_id and movie_id to fetch predictions.

### Testing the API Locally
Run Flask (app.py) and Streamlit (s_app.py) simultaneously in separate terminals.
Access the Streamlit interface at http://localhost:8501.
## Docker Containerization
### Overview
The Docker setup supports running both the Flask API (on port 5000) and the Streamlit app (on port 8501) concurrently.
Key Highlights
Ports:
Flask: 5000
Streamlit: 8501
Command: Starts both services:

CMD ["sh", "-c", "flask run --port=5000 & streamlit run s_app.py --server.port 8501"]

##  Steps to Run:
Build the Docker image:

docker build -t movie-recommender-system .

Run the container:

docker run -p 5000:5000 -p 8501:8501 movie-recommender-system
