import requests
import sys



def loop():
    url = f"http://{ip_address}/api"
    for word in sys.stdin:
        response = requests.get(url=url)
        if response.status_code == 404:
            loop(ip_address)
        else:
            data = response.json()
            print(data)
            print(response.status_code)
            print(word)
        

def main():
    ip_address = input("Enter an IP address")
    loop(ip_address)


if __name__ == "__main__":
    main()
