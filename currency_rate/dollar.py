import fastapi
import uvicorn
import requests
import pydantic


class CurrencyRate(pydantic.BaseModel):
    dollar: float

    class Meta:
        from_attributes = True


app = fastapi.FastAPI()


@app.get('/currency-rate', response_model=CurrencyRate)
def get_current_weather():
    response = requests.get('https://api.freecurrencyapi.com/v1/latest?apikey='
                            'fca_live_X8yNCic3Nn1oKMx2ihAIokfNQYkY2qpZz8n9umQP&currencies=RUB').json()
    return CurrencyRate(dollar=response['data']['RUB'])


uvicorn.run(app=app, host='127.0.0.1', port=4000)
