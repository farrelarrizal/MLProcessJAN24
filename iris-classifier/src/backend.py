from fastapi import FastAPI, Request
import pickle
import uvicorn


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Your API is UP!"}

# Check model
@app.get('/check-model')
def check_model():
    try:
        with open('model/classifier.pkl', 'rb') as model:
            model = pickle.load(model)
        result = {
            'status': 'OK',
            'message': 'Model is ready to use'
        }
        return result
    except Exception as e:
        result = {
            'status': 'Error',
            'message': str(e)
        }
        return result
    
# Predict
@app.post('/predict')
async def predict(request: Request):
    # get data from request
    data = await request.json()

    # store to variable
    sepal_length = data['sepal_length']
    sepal_width = data['sepal_width']
    petal_length = data['petal_length']
    petal_width = data['petal_width']
    
    # load model
    with open('model/classifier.pkl', 'rb') as model:
        model = pickle.load(model)
    
    # Label
    label = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    
    
    # Predict
    try:
        prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        result = {
            'status': 'OK',
            'message': 'Prediction is ready',
            'prediction': label[prediction[0]]
        }
        return result
    except Exception as e:
        result = {
            'status': 'Error',
            'message': str(e)
        }
        return result
    
# Run API
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)