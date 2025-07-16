
def generate_metadata(title, description, artist, year, image_url):
    return {
        "name": title,
        "description": f"{description} — by {artist} ({year})",
        "image": image_url,
        "attributes": [
            {"trait_type": "Artist", "value": artist},
            {"trait_type": "Year", "value": year}
        ]
    }
