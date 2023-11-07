import requests
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux and macOS

def search_oda(query):
    # Define the API endpoint URL
    api_url = f"https://oda.com/_next/data/5850647b769e3a3105c03311722d85e0d44a1a3e/no/search/products.json?q={query}&site=no"

    # Send a GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        product_list = data['pageProps']['dehydratedState']['queries'][0]['state']['data']['items']

        # Check if there are any results
        if not product_list:
            print(f"{Fore.RED}No results found.{Style.RESET_ALL}")
            return

        # Iterate through the products and extract and display relevant information
        for product in product_list:
            print(f"{Fore.LIGHTYELLOW_EX}Product ID: {Fore.WHITE}{product['id']}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTYELLOW_EX}Product Name: {Fore.WHITE}{product['attributes']['fullName']}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTYELLOW_EX}Brand: {Fore.WHITE}{product['attributes']['brand']}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTYELLOW_EX}Description: {Fore.WHITE}{product['attributes']['name']} {product['attributes']['nameExtra']}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTYELLOW_EX}Price: {Fore.WHITE}{product['attributes']['grossPrice']} NOK{Style.RESET_ALL}")
            print(f"{Fore.LIGHTYELLOW_EX}Unit Price: {Fore.WHITE}{product['attributes']['grossUnitPrice']} NOK per {product['attributes']['unitPriceQuantityName']}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTYELLOW_EX}Availability: {Fore.WHITE}{product['attributes']['availability']['description']}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTYELLOW_EX}Promotion: {Fore.WHITE}{product['attributes']['promotion']['title'] if product['attributes']['promotion'] else 'N/A'}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTYELLOW_EX}Product URL: {Fore.BLUE}https://oda.com{product['attributes']['absoluteUrl']}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTYELLOW_EX}Image URL: {Fore.BLUE}{product['attributes']['images'][0]['large']['url']}{Style.RESET_ALL}")
            print()

    else:
        print(f"{Fore.RED}Failed to retrieve product data. Status code: {response.status_code}{Style.RESET_ALL}")

if __name__ == "__main__":
    while True:
        user_input = input("Enter a search query, 'clear' to clear the screen, or 'q' to quit: ")
        
        if user_input.lower() == 'q':
            break
        elif user_input.lower() == 'clear':
            clear_screen()
        else:
            search_oda(user_input)
