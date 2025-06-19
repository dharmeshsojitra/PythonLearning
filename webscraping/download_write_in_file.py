import requests, logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
response = requests.get("https://automatetheboringstuff.com/files/rj.txt")
try:
    response.raise_for_status()

    with open('RomeoAndJuliet.txt', 'wb') as f:
        for chunk in response.iter_content(10000):
            logging.info(chunk)
            f.write(chunk)
except Exception as e:
    logging.error(f'there was a problem: {e}')