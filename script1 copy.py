from googlesearch import search
import requests
from bs4 import BeautifulSoup

# Define the search term
search_term = "palestine"

# Function to get Google search results
def get_google_search(search_term):
    search_results = search(search_term)
    return search_results

# Function to scrape page text from Google search results
def scrape_page_text(search_results):
    texts = []

    for link in search_results:
        page = requests.get(link).text
        soup = BeautifulSoup(page, 'html.parser')

        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.extract()

        page_text = soup.get_text()

        lines = (line.strip() for line in page_text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        page_text = '\n'.join(chunk for chunk in chunks if chunk)

        texts.append(page_text)

    return texts

# Get Google search results
search_results = get_google_search(search_term)

# Scrape page text from the search results
page_texts = scrape_page_text(search_results)

# Print the page text for each result
for text in page_texts:
    print(f"Page Text:\n{text}\n")
