import requests

def get_fruit_info(fruit_name):
    url = f"https://www.fruityvice.com/api/fruit/{fruit_name}"
    response = requests.get(url)

    #fruit_data = response.json()

    # Print the response to debug
    print(response.status_code)  # Check if request was successful (should be 200)
    print(response.json())  # Print the full response data

    return response.json()

#get information about an apple
apple_info = get_fruit_info("apple")

print(apple_info["name"]) #Ouput: "Apple"

# Check if 'nutritions' exists before accessing it
if "nutritions" in apple_info:
    print(apple_info["nutritions"]["carbohydrates"])  # Output: carbohydrate value
else:
    print("Key 'nutritions' not found in API response.")