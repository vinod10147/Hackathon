import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from ml_utils import load_model, predict
from typing import List
from datetime import datetime

# defining the main app
app = FastAPI(title="German Credit Predictor", docs_url="/")

# calling the load_model during startup.
# this will train the model and keep it loaded for prediction.
app.add_event_handler("startup", load_model)

# class which is expected in the payload
class QueryIn(BaseModel):
    status_of_existing_checking_account: str
    duration_in_month: int
    credit_history:	str
    purpose: str
    credit_amount: int
    savings_account_bonds:	str


# class which is returned in the response
class QueryOut(BaseModel):
    credit_status: int
    description: str 

# Route definitions
@app.get("/ping")
# Healthcheck route to ensure that the API is up and running
def ping():
    return {"ping": "pong"}


@app.post("/predict_credit", response_model=QueryOut, status_code=200)
# Route to do the prediction using the ML model defined.
# Payload: QueryIn containing the parameters
# Response: QueryOut containing the Credit  predicted (200)
def predict_credit(query_data: QueryIn):
    p=predict(query_data)
    output = {"credit_status": p,"description":"Eligible for loan" if p==1  else "Not Eligible for loan"} 
    print('Output value is : ',output)
    return output

# Main function to start the app when main.py is called
if __name__ == "__main__":
    # Uvicorn is used to run the server and listen for incoming API requests on 0.0.0.0:8888
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
