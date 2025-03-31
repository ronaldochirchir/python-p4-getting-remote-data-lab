import requests
import json

class GetRequester:
    """
    A class to handle GET requests and JSON responses from a specified URL.
    """
    
    def __init__(self, url):
        """
        Initialize the GetRequester with a URL.
        
        Args:
            url (str): The URL to send GET requests to
        """
        self.url = url
    
    def get_response_body(self):
        """
        Send a GET request to the URL and return the response body as bytes.
        
        Returns:
            bytes: The raw response content
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Error making GET request: {e}")
            return None
    
    def load_json(self):
        """
        Get the response body and parse it as JSON.
        
        Returns:
            list or dict: The parsed JSON data
        """
        response_body = self.get_response_body()
        if response_body:
            try:
                return json.loads(response_body.decode('utf-8'))
            except (json.JSONDecodeError, UnicodeDecodeError) as e:
                print(f"Error parsing JSON: {e}")
                return None
        return None