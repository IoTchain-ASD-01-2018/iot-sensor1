import requests
import json

sensor_id = "sensor 1"
url_transacao_iot = "http://localhost:8081/transacao"
body = {
    "origem": sensor_id
}
response = requests.post(url_transacao_iot,
                        json.JSONEncoder().encode(body)).json()
print(response['hash'], response['data_insercao'])