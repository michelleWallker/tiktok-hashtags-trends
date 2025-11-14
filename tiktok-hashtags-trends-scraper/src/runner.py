thonimport json
import logging
from extractors.tiktok_hashtags import fetch_trending_hashtags
from config.settings import load_settings

def run_scraper():
    settings = load_settings()
    hashtags = fetch_trending_hashtags(settings['country_code'], settings['proxy'])
    with open('data/sample_output.json', 'w') as outfile:
        json.dump(hashtags, outfile, indent=4)
    logging.info("Scraping complete. Data saved to 'data/sample_output.json'.")

if __name__ == "__main__":
    run_scraper()