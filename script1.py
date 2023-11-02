from googlesearch import search
import requests
from bs4 import BeautifulSoup

# Function to get Google search results
def get_google_search(search_term):
    results = search(search_term)

    # for link in results:
    #     print(f"Link: {link}")

    return results

# Function to scrape page text from Google search results
def scrape_page_text(search_results):
    texts = []

    for link in search_results:
        page = requests.get(link).text
        soup = BeautifulSoup(page, 'html.parser')

        for script in soup(["script", "style"]):
            script.extract()

        page_text = soup.get_text()

        lines = (line.strip() for line in page_text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        page_text = '\n'.join(chunk for chunk in chunks if chunk)

        texts.append(page_text)

    return texts

search_term = input("Enter the search term: ")

search_results = get_google_search(search_term)

page_texts = scrape_page_text(search_results)


for text in page_texts:
    print(f"Page Text:\n{text}\n")
