import requests

class RequestCalculations:
    url = 'https://odds1project.appspot.com/_ah/api/odds1projectEndpoint/v1/loadStarupInfo'
    x = requests.post(url)
    