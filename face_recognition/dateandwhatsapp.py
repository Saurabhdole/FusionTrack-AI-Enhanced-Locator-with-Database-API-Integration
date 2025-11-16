import requests

def sendmessage(number, name, adhaar, location):
    city = location['city']
    region = location['region']
    country = location['country']
    latitude = location['latitude']
    longitude = location['longitude']
    
    message = (
        f"Your dear one with name {name}, bearing Aadhaar number {adhaar}, "
        f"has been found at a location:\n"
        f"Country: {country}\n"
        f"Region: {region}\n"
        f"City: {city}\n"
        f"Latitude: {latitude}\n"
        f"Longitude: {longitude}\n\n"
        "Regards,\nFusion Track."
    )

    url = "https://api.ultramsg.com/instance125832/messages/chat"
    payload = (
        f"token=cmr06gt3us8os1qu&to=+91{number}"
        f"&body={message}&priority=1&referenceId="
    )
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, data=payload, headers=headers)
    print(response.text)
