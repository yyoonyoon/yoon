import requests

APP_ID = "f2f48eb2"
API_KEY = "e4120647b18a21bba1620f670df613b3"

# sign_up_endpoint = "https://trackapi.nutritionix.com/v2/auth/signup"
# sign_in_endpoint = "https://trackapi.nutritionix.com/v2/auth/signin"
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# sign_up_body = {
#     "password": "password",
#     "email": "email id",
#     "first_name": "Yeom",
# }
# sign_in_body = {
#     "password": "password",
#     "email": "email id"
# }
header = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
    "x-remote-user-id" : "0",
    "Content-Type" : "json"
}
parameters = {
    "query":"ran 3 miles",
    "gender":"male",
    "weight_kg":71,
    "height_cm":175,
    "age":22
}
# # response = requests.post(url= sign_up_endpoint, json= sign_up_body)   #sign in nutritionix api
# response = requests.post(url= sign_in_endpoint, json= sign_in_body)   #sign up nutritionix api
# # response = requests.get(url= nutritionix_endpoint, json= put_data_body, headers= header).json
response = requests.get(url= nutritionix_endpoint, json= parameters, headers= header).json
print(response)