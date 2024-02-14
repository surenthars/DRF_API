import requests


end_point = "http://localhost:1754/ONE"

get_resp = requests.get(end_point)

print(get_resp.text)
print("the status code is :", get_resp.status_code)
