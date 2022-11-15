from bs4 import BeautifulSoup
import requests as req



def get_page_links(page, zip_code):
    base_url = f"https://www.zillow.com/professionals/real-estate-agent-reviews/{zip_code}/?page={page}"

    HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',  
    'referer': 'https://www.zillow.com/',
    }

    response = req.get(url=base_url, headers=HEADERS)
    print(response.status_code)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)

    tags = soup.find_all("div", class_="Flex-c11n-8-50-1__sc-n94bjd-0 Summary__StyledFlex-sc-130ry7i-0 hREGHr dRCSGX")
    for tag in tags:
        url = tag.find("a")['href']
        print(url)

def extract_info():
    pass

def save_CSV():
    pass

def main():
    zip_code = input("enter zip_code: ")
    page_number = int(input("How many page do you want to scrape?:"))
    for x in range (1, page_number):
        print(f"getting_page {x}")
        print(get_page_links(x, zip_code))
        
if __name__ == "__main__":
    main()