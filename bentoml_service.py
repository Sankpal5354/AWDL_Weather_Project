import bentoml
from bentoml.io import Text

svc = bentoml.Service("weather_service")

@svc.api(input=Text(), output=Text())
def predict(city):
    return f"Weather prediction service running for {city}"