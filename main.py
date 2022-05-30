# 1. Library Imports
import pickle

import uvicorn
from fastapi import FastAPI

from app.Iris import Iris
from typing import List

# 2. Create the app object
app = FastAPI()

# 3. Load models
with open('app/models/random_forest.pkl', 'rb') as fi:
    random_forest_model = pickle.load(fi)

with open('app/models/standard_scaler.pkl', 'rb') as si:
    scaler_model = pickle.load(si)


# 4. API Endpoints and methods
@app.get("/")
def home():
    return {"message": "Technical test for Platanomelon."}


@app.post("/predict")
def predict_species(data: List[Iris]):
    predictions = []
    # As the data is a list of objects, we need to iterate through it
    for item in data:
        # Scale the data -- needs to be reordered to match the model
        scaled_data = scaler_model.transform([[item.Area, item.Perimeter, item.Compactness, item.length_of_kernel,
                                               item.width_of_kernel, item.asymmetry_coefficient,
                                               item.length_kernel_groove]])
        # Predict the species
        prediction = random_forest_model.predict(scaled_data)
        # Add prediction to list of predictions
        predictions.append(str(prediction[0]))
    # Generate json from list of predictions
    return {"predictions": predictions}


def start_server():
    "Launch the server with poetry run start at root level"
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    start_server()
