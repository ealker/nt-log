import requests

def get_place_titles(url):
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        titles = [item['title'] for item in json_data['pagedMultiMatch']['results']]
        return titles
    else:
        print("Failed to fetch the JSON data.")
        return []

if __name__ == "__main__":
    url = 'https://www.nationaltrust.org.uk/api/search/places?query=&placeSort=alphabetical&lat=52.561928&lon=-1.464854&milesRadius=1000&pageStartIndex=0&pageSize=656&lang=en&publicationChannel=NATIONAL_TRUST_ORG_UK&maxPlaceResults=1000&maxLocationPageResults=0'

    place_titles = get_place_titles(url)
    for idx, title in enumerate(place_titles, start=1):
        print(f"{idx}. {title}")
