import json
import requests

# search?status={statusQuery}&page={n}
def avgRotorSpeed(statusQuery, parentId):
    url = 'https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}'
    response = requests.get(url).json()
    #devices = [device for device in response['data']]
    #for device in devices:
    #    print(device)
    return response

print(avgRotorSpeed('RUNNING', 1))
