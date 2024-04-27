import fastapi
import uvicorn
import requests
import pydantic


class CurrentWeather(pydantic.BaseModel):
    temperature: float
    condition: str

    class Meta:
        from_attributes = True


app = fastapi.FastAPI()


@app.get('/current-weather', response_model=CurrentWeather)
def get_current_weather():
    response = requests.get('http://api.weatherapi.com/v1/current.json?'
                            'key=5075db59e18e484aba1151017242704&q=saint-petersburg&aqi=no').json()
    return CurrentWeather(temperature=response['current']['temp_c'],
                          condition=response['current']['condition']['text'])


uvicorn.run(app=app, host='127.0.0.1', port=3000)
