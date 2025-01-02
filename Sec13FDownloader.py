import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
from io import BytesIO

class Sec13FDownloader:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def fetch_zip_links(self):
        """Fetch all links ending with .zip from the SEC webpage."""
        try:
            response = requests.get(self.base_url, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            zip_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith('.zip')]
            return zip_links
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching the webpage: {e}")
            return []

    def download_and_extract_infotable(self, zip_url, extract_to='./'):
        """
        Download a zip file from the given URL and extract INFOTABLE.tsv.

        Parameters:
            zip_url (str): The URL of the zip file to download.
            extract_to (str): Directory to save the extracted INFOTABLE.tsv file.
        """
        try:
            response = requests.get(zip_url, headers=self.headers)
            response.raise_for_status()

            with ZipFile(BytesIO(response.content)) as zip_file:
                if 'INFOTABLE.tsv' in zip_file.namelist():
                    zip_file.extract('INFOTABLE.tsv', path=extract_to)
                    print(f"INFOTABLE.tsv extracted to: {os.path.abspath(extract_to)}")
                else:
                    print("INFOTABLE.tsv not found in the zip file.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while downloading the file: {e}")
        except Exception as e:
            print(f"An error occurred while processing the zip file: {e}")

# Example usage
if __name__ == "__main__":
    base_url = "https://www.sec.gov/data-research/sec-markets-data/form-13f-data-sets"
    downloader = Sec13FDownloader(base_url)

    # Fetch .zip links
    zip_links = downloader.fetch_zip_links()
    print("Links ending with .zip:")
    for link in zip_links:
        print(link)

    # Download and extract INFOTABLE.tsv from the first .zip link
    if zip_links:
        first_zip_url = zip_links[0]
        if not first_zip_url.startswith("http"):
            first_zip_url = f"https://www.sec.gov{first_zip_url}"
        downloader.download_and_extract_infotable(first_zip_url)
