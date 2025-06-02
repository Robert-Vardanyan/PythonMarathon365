import requests
from bs4 import BeautifulSoup

def basic_web_scraper(url):
    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # raise error if bad status

        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract headings (h1, h2, h3)
        headings = []
        for level in ['h1', 'h2', 'h3']:
            for heading in soup.find_all(level):
                headings.append((level.upper(), heading.get_text(strip=True)))

        # Extract paragraphs
        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p') if p.get_text(strip=True)]

        # Extract links
        links = []
        for a in soup.find_all('a', href=True):
            text = a.get_text(strip=True)
            href = a['href']
            links.append((text, href))

        # Print results
        print(f"Headings on {url}:")
        for level, text in headings:
            print(f"{level}: {text}")

        print("\nParagraphs:")
        for para in paragraphs[:5]:  # show only first 5 paragraphs to keep output short
            print(f"- {para}")

        print("\nLinks:")
        for text, href in links[:5]:  # show only first 5 links
            print(f"- {text} -> {href}")

    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ").strip()
    basic_web_scraper(url)
