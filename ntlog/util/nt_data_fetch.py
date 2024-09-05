import requests, json

def get_nt_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        # titles = [item['title'] for item in json_data['pagedMultiMatch']['results']]
        # return titles
        return json_data
    else:
        print("Failed to fetch the JSON data.")
        return []

if __name__ == "__main__":
    url = 'https://www.nationaltrust.org.uk/api/search/places?query=&placeSort=alphabetical&lat=52.561928&lon=-1.464854&milesRadius=1000&pageStartIndex=0&pageSize=656&lang=en&publicationChannel=NATIONAL_TRUST_ORG_UK&maxPlaceResults=1000&maxLocationPageResults=0'

    json_data = get_nt_data(url)
    with open('../resources/nt_data.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)

    # for idx, title in enumerate(place_titles, start=1):
        # print(f"{idx}. {title}")
