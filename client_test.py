import requests

payload={"message": "Explain AI models simply."}
response=requests.post("http://localhost:8000/chat",json=payload)

print("Status:",response.status_code)
print("Response:", response.json())