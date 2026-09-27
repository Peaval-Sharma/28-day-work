import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=10)

    # Check HTTP status code
    if response.status_code == 200:

        # Convert JSON response into Python data
        users = response.json()

        print("===== USER INFORMATION =====")

        for user in users:
            print("ID      :", user["id"])
            print("Name    :", user["name"])
            print("Username:", user["username"])
            print("Email   :", user["email"])
            print("City    :", user["address"]["city"])
            print("----------------------------")

    else:
        print("API Error!")
        print("Status Code:", response.status_code)

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet connection.")

except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)