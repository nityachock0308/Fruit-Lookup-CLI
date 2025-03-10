import requests
import json
import argparse

def fetch_fruit_data(fruit_name):
    """Fetches fruit details from the FruityVice API."""
    url = f"https://www.fruityvice.com/api/fruit/{fruit_name}"

    try:
        response = requests.get(url)
        if response.status_code == 404:
            print(f"Error: Fruit '{fruit_name}' not found. Check spelling and try again.")
            return None
        response.raise_for_status() # Raises an error for HTTP failures (4xx, 5xx)
        return response.json()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to FruityVice API. Check your internet connection.")
        return None
    except requests.exceptions.HTTPError:
        print("Error: The FruityVice API is currently unavailable. Please try again later.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Unexpected error fetching data: {e}")
        return None
    
def get_fruit_info(fruit_name):
    """Returns fruit details as a dictionary (for programmitc use)."""
    data = fetch_fruit_data(fruit_name)

    if not data:
        return None
    
    # Extract relevant fields
    fruit_info = {
        "Name": data.get("name", "N/A"),
        "ID": data.get("id", "N/A"),
        "Family": data.get("family", "N/A"),
    }

        # Ensure "nutritions" exists before accessing it
    nutritions = data.get("nutritions", {})
    if nutritions:
        fruit_info.update({
            "Sugar (g)": nutritions.get("sugar", "N/A"),
            "Carbohydrates (g)": nutritions.get("carbohydrates", "N/A"),
        })

        return fruit_info
    
def  display_fruit_info(fruit_name, output_format = "human"):
    """Fetches and displays fruit data in human-readable or JSON format."""
    fruit_info = get_fruit_info(fruit_name)

    if not fruit_info :
        print("Error: Could not retrieve data.")
        return
    
    if output_format == "human":
        print("\nFruit Information:")
        for key, value in fruit_info.items():
            print(f"{key}: {value}")
    elif output_format == "json":
        print(json.dumps(fruit_info, indent = 4))

def main():
    """Main function to handle CLI interactions."""
    parser = argparse.ArgumentParser(description = "Fetch fruit details from the FruityVice API.")
    parser.add_argument("fruit", type=str, help="Name of the fruit to look up")
    parser.add_argument("--output", choices = ["human", "json"], default = "human",
                        help = "Choose output format (human-readable or JSON)")
    
    args = parser.parse_args()
    display_fruit_info(args.fruit, args.output)

if __name__ == "__main__":
    main()