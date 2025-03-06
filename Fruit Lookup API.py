import requests
import json
import argparse

def fetch_fruit_data(fruit_name):
    """"Fetches fruit details from the FruityVice API."""
    url = f"https://www.fruityvice.com/api/fruit/{fruit_name}"

    try:
        response = requests.get(url)
        response.raise_for_status() # Raises an error for HTTP failures (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    
def  display_fruit_info(fruit_name, output_format = "human"):
    """Feches and displays fruit data in human-readable or machine-readable format."""
    data = fetch_fruit_data(fruit_name)

    if not data:
        print("Error: Could not retrieve data. The fruit may not exist or the API is down")
        return
    
    # Extract relevabt fields
    fruit_info = {
        "Name": data.get("name"),
        "ID": data.get("id"),
        "Family": data.get("family"),
        "Sugar (g)": data["nutritions"]["sugar"],
        "Carbohydrates (g)": data["nutrients"]["carbohydrates"]
    }

    # Display the output in the chosen format
    if output_format == "human":
        print("\nFruit Information:")
        for key, value in fruit_info.items():
            print(f"{key}: {value}")
    elif output_format == "json":
        print(json.dumps(fruit_info, indent = 4))

def main():
    """"Main function to handle CLI interactions."""
    parser = argparse.ArgumentParser(description = "Fetch fruit details from the FruityVice API.")
    parser.add_argument("fruit", type=str, help="Name of the fruit to look up")
    parser.add_argument("--output", choices = ["human", "json"], default = "human",
                        help = "Choose output format (human-readable or JSON)")
    
    args = parser.parse_args()
    display_fruit_info(arg.fruit, args.output)

if _name_ == "_main_":
    main()