import requests

# Function to retrieve the content of a website based on its URL
def get_website_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to fetch data. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage of the function to retrieve the content of a website
url_to_scrape = "https://www.example.com"
web_content = get_website_content(url_to_scrape)
print(web_content)
