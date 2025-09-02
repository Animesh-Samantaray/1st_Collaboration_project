import requests

url = "http://127.0.0.1:8000/predict"
headers = {"x-api-key": "mysecretkey123"}
data = {
    "age": 30,
    "sex": "male",
    "bmi": 25.5,
    "children": 2,
    "smoker": "no",
    "region": "northwest"
}

response = requests.post(url, json=data, headers=headers)
print(response.json())
