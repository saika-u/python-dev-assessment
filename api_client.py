import requests


def fetch_and_display_users(num_users):
    url = " https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print("Error: Could not fetch data from the API.")
            return None

       
        users = response.json()

        
        for user in users[:num_users]:
            try:
                print("Name :", user["name"])
                print("Email:", user["email"])
                print("City :", user["address"]["city"])
                print("-" * 30)

            except KeyError:
                print("Error: Some user information is missing.")
                return None

    except requests.exceptions.RequestException as e:
        print("Network Error:", e)
        return None

    except ValueError:
        print("Error: Invalid JSON data.")
        return None


# Example calls
fetch_and_display_users(4)

print("\nFetching more users...\n")

fetch_and_display_users(16)