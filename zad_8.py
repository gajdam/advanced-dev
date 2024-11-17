from typing import Optional
import argparse
import requests

class Brewery:
    def __init__(self, id: str, name: str, brewery_type: str, address_1: str, address_2: str, address_3: str, city: str,
                 state_province: str, postal_code: str, country: str, longitude: str, latitude: str, phone: str,
                 website_url: str, state: str, street: str):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street

    def __str__(self):
        return (
            f"Brewery ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Type: {self.brewery_type}\n"
            f"Address: {self.address_1}, {self.address_2}, {self.address_3}, {self.street}, {self.city}, {self.state_province}, {self.state}, {self.postal_code}, {self.country}\n"
            f"Longitude and latitude: {self.longitude}, {self.latitude}\n"
            f"Phone: {self.phone}\n"
            f"Website: {self.website_url}\n"
        )


def fetch_breweries(api_url: str, city: Optional[str] = None, limit: int = 20) -> list[Brewery]:
    params = {"per_page": limit}
    if city:
        params["by_city"] = city

    response = requests.get(api_url, params=params)
    response.raise_for_status()
    breweries_data = response.json()

    breweries = []
    for data in breweries_data:
        brewery = Brewery(
            id=data.get('id'),
            name=data.get('name'),
            brewery_type=data.get('brewery_type'),
            address_1=data.get('address_1'),
            address_2=data.get('address_2'),
            address_3=data.get('address_3'),
            city=data.get('city'),
            state_province=data.get('state_province'),
            postal_code=data.get('postal_code'),
            country=data.get('country'),
            longitude=data.get('longitude'),
            latitude=data.get('latitude'),
            phone=data.get('phone'),
            website_url=data.get('website_url'),
            state=data.get('state'),
            street=data.get('street')
        )
        breweries.append(brewery)

    return breweries


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--city",
        type=str,
        help="City to search for breweries",
        default=None
    )
    args = parser.parse_args()

    API_URL = 'https://api.openbrewerydb.org/v1/breweries'

    try:
        breweries = fetch_breweries(API_URL, city=args.city)
        for brewery in breweries:
            print(brewery)
            print('=' * 20)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")