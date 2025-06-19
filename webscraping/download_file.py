import requests

response = requests.get("https://automatetheboringstuff.com/files/rj.txt")

print(type(response))

print(response.status_code)

print(response.text)



response = requests.get("https://automatetheboringstuff.com/files/rj,txt")
try:
    response.raise_for_status()
except Exception as e:
    print(f'there was a problem: {e}')
