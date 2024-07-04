import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
from requests import RequestException

stack = []

def visit_site():
    while True:
        # print(stack)
        input_url = input("Enter the URL, 'exit' to end, or 'back' to navigate to previous page: ")
        if input_url.lower() == 'exit':
            print("Thank you!")
            print()
            exit()

        elif input_url.lower() == 'back':
            if len(stack) > 1:
                stack.pop()
                print(f"Going back to: {stack[-1]}")
                input_url = stack[-1]
                site_display(input_url)
                stack.pop()
            else:
                print("No previous URL present.")
                print()

        elif input_url.lower() != 'exit':
            if not input_url.startswith('https://'):
                input_url = 'https://' + input_url
                site_display(input_url)
            else:
                input_url = input_url
                site_display(input_url)

def site_display(input_url):
    # input_url = input()
    try:
        response = requests.get(input_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for item in soup.find_all(['p', 'a']):
            if item.name == 'p':
                print(Fore.BLACK + item.get_text())
            elif item.name == 'a':
                print(Fore.BLUE + str(item.get('href')) + Style.RESET_ALL)
        stack.append(input_url)
        print()

    except RequestException as e:
        print(f"Error: {e}")
        print("Invalid URL or connection issue. Please try again.")
        print()

    finally:
        print(Style.RESET_ALL)



visit_site()



