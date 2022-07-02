import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_name = "yoon"
user_token = "abs1b41iuyuibh312u3"

user_params = {
    "token" : user_token,
    "username" : user_name,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}
# response = requests.post(url=PIXELA_ENDPOINT, json= user_params) #create my profile in pixela.

graph_config = {
    "id" : "graph1",
    "name" : "Study time",
    "unit" : "hours",
    "type" : "float",
    "color" : "ajisai",
}

headers = {
    "X-USER-TOKEN" : user_token
}

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{user_name}/graphs"
# response = requests.post(url= GRAPH_ENDPOINT, json= graph_config, headers= headers)

PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/graph1"

pixel_config = {
    "date" : "20220702",
    "quantity" : "1.5"
}

response = requests.post(url= PIXEL_ENDPOINT, json= pixel_config, headers= headers)
print(response.text)