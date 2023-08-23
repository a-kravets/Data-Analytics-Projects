# use http://localhost:3000/ for testing locally
# bentoml serve service.py:svc
# json has to be using "" instead of ''

# bentoml will get versions of libs we were using and use the same

# to build bentoml model for deployment, we need bentofile.yaml

import numpy as np

import bentoml
from bentoml.io import JSON

model_ref = bentoml.xgboost.get("credit_risk_model:latest")
dv = model_ref.custom_objects['dictVectorizer']

model_runner = model_ref.to_runner()

svc = bentoml.Service("credit_risk_model", runners=[model_runner])


@svc.api(input=JSON(), output=JSON())
def classify(application_data):
    vector = dv.transform(application_data)
    prediction = model_runner.predict.run(vector)
    print(prediction)
    result = prediction[0]

    if result > 0.5:
        return {
            "status": "DECLINED"
        }
    elif result > 0.25:
        return {
            "status": "MAYBE"
        }
    else:
        return {
            "status": "APPROVED"
        }

# 'bentoml models list' lists all the bento models we saved
# 'bentoml models get credit_risk_model:kwsinikbp6r4di62 (tag)' shows the details of a specific model
# 'bentoml build'
# 'bentoml containerize credit_risk_model:latest (tag created by bentoml build)'
# Once the docker image is built, we can run 'docker run -it --rm -p 3000:3000 containerize credit_risk_classifier:kdelkqsqms4i2b6d'
# to see if everything is working as expected. We are exposing 3000 port to map with the service port which is also 3000
# and this should take us to Swagger UI page again.