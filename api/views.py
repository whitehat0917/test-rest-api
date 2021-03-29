from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import requests

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def users(request, format=None):
    id = request.GET['id']
    url = 'http://dummy.restapiexample.com/api/v1/employee/%s' % id
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    }
    proxyDict = {
        'http': 'http://ogyrnnc:sjtrZi7dhN0mOwTA_country-Netherlands@resi.tokeproxies.io:31112',
        'https': 'https://ogyrnnc:sjtrZi7dhN0mOwTA_country-Netherlands@resi.tokeproxies.io:31112'
    }
    response = requests.get(url, headers=headers, proxies=proxyDict)
    print(response.text)
    user = response.json()
    content = {
        'data': user
    }
    return Response(content)
