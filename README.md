# **Fruit Lookup CLI**

A Python script that interacts with the FruityVice API to fetch and display details about fruits. It can be used via the command line or as a library in other Python programs.

**Features**
• Fetches fruit details including:
    • Full name
    • ID number
    • Family (biological classification)
    • Sugar content (g)
    • Carbohydrates content (g)

• Two output formats:
    • Human-readable
    • JSON (machine-readable)

• Handles errors gracefully if a fruit is not found or th API is unavailable.
• Can be used as a command-line tool or imported as a library.

**Installation**

Ensure you have Python installed (version 3.x recommended). Install required dependencies using:
```python
pip install requests
```

**Usage**
**Command Line**

Run the script from the terminal:
```python
python fruit_lookup.py <fruit_name> [--output json]
```

**Examples**
Fetch details for an apple in human-readable format:
```python
python fruit_lookup.py apple
```
Fetch details for a banana in JSON format:
```python
python fruit_lookup.py banana --output json
```

**Import as a Library**

You can also use this script in your own Python programs:
```python
from fruit_lookup import get_fruit_info

fruit_data = get_fruit_info("strawberry")
print(fruit_data)

```

**Error Handling**
• If a fruit is not found, it will return an error message.
• If the API is unavailable, it will notify the user.
• If an unexpected issue occurs, it will provide a relevant error message.

**Future Enhancements**
• Add support for listing all available fruits from the API.
• Improve caching to reduce API calls for repeated requests.

**License**
This project is open-source under the MIT License.
