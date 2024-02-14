import requests

# inthis file will be check the request response get the terminal

end_point = "http://192.168.0.35:70/check"

modelinstance = "http://192.168.0.35:70/modelinstance"

get_modelresponse = requests.get(modelinstance)

print(get_modelresponse.json())
print(get_modelresponse.headers)


# get_resp = requests.get(end_point)

# print(get_resp.text)
# print("the status code is :", get_resp.status_code)
