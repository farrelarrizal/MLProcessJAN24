from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post('/predict')
def predict():
    return {"Predicted": "Virginica Iris"}

@app.get('/greetings/{name}')
def greetings(name: str):
    return {"Greetings": name}

# greetings?name=Farrel
@app.get('/greetings')
def greetings(request: Request):
    name = request.query_params.get('name', 'Farrel')
    return {"Greetings": name}


    