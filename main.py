import requests

target_input = input("Enter your target website: ")

with open("subdomainfind.txt","r") as subdomain_find:
    for word in subdomain_find:
        word = word.strip()
        url = "http://" + word + "." + target_input
        try:
            response = requests.get(url)
            print(f"Subdomain found: {url}")
        except requests.exceptions.RequestException:
            pass
