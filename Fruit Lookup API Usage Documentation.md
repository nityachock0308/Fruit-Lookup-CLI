# **Fruit Lookup CLI – Quick Usage Guide**

## **1. Installation**

Ensure you have Python installed and install the required dependencies:
```python
pip install requests
```

## **2. Running the Script**

Fetch fruit details from the command line:
```python
python "Fruit Lookup API.py" <fruit_name> [--output json]
```

## **3. Example Commands**

Get details for an apple in human-readable format:
```python
 python "Fruit Lookup API.py" apple
```
Get details for a banana in JSON format:
```python
python "Fruit Lookup API.py" banana --output json
```

## **4. Using as a Library**

You can also use the script in a Python program:
```python
from Fruit_Lookup_API import get_fruit_info

fruit_data = get_fruit_info("strawberry")
print(fruit_data)
```

## **5. Error Handling**

• If the fruit name is incorrect:

Example: ```python
python "Fruit Lookup API.py" bannanna
```

Output: ```python
"Error: Fruit 'bannanna' not found. Check spelling and try again."
```


• If the API is down:

Output: ```python
"Error: The FruityVice API is currently unavailable. Please try again later."
```