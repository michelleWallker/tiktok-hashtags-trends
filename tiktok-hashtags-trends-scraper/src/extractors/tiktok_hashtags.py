thonimport requests
import logging

def fetch_trending_hashtags(country_code, proxy):
    url = f"https://api.tiktok.com/trending/{country_code}"
    try:
        response = requests.get(url, proxies={'http': proxy, 'https': proxy})
        response.raise_for_status()
        hashtags = response.json()
        return hashtags
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        return []