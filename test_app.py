from fastapi.testclient import TestClient
from main import app

# test to check the correct functioning of the /ping route
def test_ping():
    with TestClient(app) as client:
        response = client.get("/ping")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"ping": "pong"}


# test to check if good risk is classified correctly
def test_pred_good_risk():
    # defining a sample payload for the testcase
    # test values are changed
    payload = {
        "status_of_existing_checking_account": 'A11',   
        "duration_in_month": 6,
        "credit_history":	'A34',
        "purpose": 'A43',
        "credit_amount": 1169,
        "savings_account_bonds": 'A65',
      }
    with TestClient(app) as client:
        response = client.post("/predict_credit", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        #assert response.json() == {"credit_status ": "Good Risk"}
        assert response.json()["credit_status"]== 1
        #assert response.json()["timstamp"] != ''


# test to check if Bad Risk is classified correctly
def test_pred_bad_risk():
    # defining a sample payload for the testcase
    # test values are changed
    payload = {

        "status_of_existing_checking_account": 'A12',
        "duration_in_month": 48,
        "credit_history":	'A32',
        "purpose": 'A43',
        "credit_amount": 5951,
        "savings_account_bonds": 'A61',
      }

    with TestClient(app) as client:
        response = client.post("/predict_credit", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        #assert response.json() == {"credit_status": "Bad Risk"}
        assert response.json()["credit_status"]== 2
        #assert response.json()["timstamp"] != ''
