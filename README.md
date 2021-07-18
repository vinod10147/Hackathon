## CredScore Application

Dataset –German Credit Dataset (https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/)
Keywords – API, MLOps, Usage of rule-based and ML models, Visualization, Explainability


## How to run this assigment?


## Running Instructions

- Create a fork of the repo using the `fork` button.
- Clone your fork using `git clone https://www.github.com/vinod10147/Hackathon`
- Install dependencies using `pip3 install -r requirements.txt`
- Run application using `python3 main.py`
- Run tests using `pytest test_app.py`
- Run as interactive application `python ui.py` or check `ui.ipynb` file


# API

After running the application, open http://localhost:8080/
You will be able to check and execute apis (ping and predict_credit) on swagger.
```
sample_payload = {
        "status_of_existing_checking_account": 'A11',   
        "duration_in_month": 6,
        "credit_history":	'A34',
        "purpose": 'A43',
        "credit_amount": 1169,
        "savings_account_bonds": 'A65',
      }
```

# Model And Variable Selection


We have used the h2o module to compare different models on the basis of different evaluation metrics. Accordingly we have selected GBM model for our application.
We have only selected top 6 features according to their variable-importance.
You can check implementation in `Model_Selection.ipynb` file.

# MLOPS(CI-CD)

On push and pull actions ci-cd will execute the yaml file. yaml file first install the dependencies and then executes the testcases.

# Explainability

Based on the features importance model is deciding whether the person is eligible or not.
Feature Importance we have calculated using h20 module.
     

## Further Improvements

We can create bitmap for paths, that will decrease the memory usage further and also increase the performance as it can perform faster union operation.

