from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the saved model


@app.route('/predict', methods=['POST'])
def predict():
    # Parse input JSON
    data = request.get_json()
    input1 = data.get("input1")
    input2 = data.get("input2")

    with open('xgb_model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    with open("scaler.pkl", 'rb') as file:
        scaler = pickle.load(file)
    with open("merged_movie_data.pkl", 'rb') as file:
        df = pickle.load(file)
    with open("avg_user.pkl", 'rb') as file:
        user = pickle.load(file)


    # Validate inputs
    if input1 is None or input2 is None:
        return jsonify({"error": "Missing input1 or input2"}), 400
    # Prepare data for prediction
    filtered_row = df[df['ItemID'] == int(input2)]
    array = filtered_row.to_numpy()
    array = np.insert(array , 0 ,int(input1) , axis = 1  )
    array = np.insert(array , 3 ,1988 , axis = 1  )
    array = np.insert(array , 5 ,user[int(input1)] , axis = 1  )
    df = pd.DataFrame(array,columns = ['UserID', 'ItemID','Release_Year','Rated_Year', 
        'average_movie_rating','average_user_rating','PCA_Binary_1',
       'PCA_Binary_2', 'PCA_Binary_3', 'PCA_Binary_4', 'PCA_Binary_5'])
    result = scaler.transform(df)
    prediction = model.predict(result)

    # Make prediction
    try:
        prediction =  prediction[0]+1

        
        return jsonify({"prediction": int(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

