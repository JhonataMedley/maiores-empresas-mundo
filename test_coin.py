import requests
import json


url = "https://v6.exchangerate-api.com/v6/e31352a229eabff366b77b76/latest/USD"

valorempresa = 6676644102144

response = requests.get(url)
data = response.json()

taxa = data["conversion_rates"]["SAR"]

valor_USD = valorempresa / taxa

print(valor_USD)

#print(json.dumps(data, indent=4))
