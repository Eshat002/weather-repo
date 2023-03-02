from django.utils.html import strip_tags
from urllib.parse import quote
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render 
# import json to load json data to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request 
  
  
def index(request): 

    if request.method == 'POST': 
        city = quote(request.POST['city'] )
        print('city',city)
        ''' api key might be expired use your own api_key 
            place api_key in place of appid ="your_api_key_here "  '''
  
        # source contain JSON data from API 
        try:
            source = urllib.request.urlopen( 
                'http://api.openweathermap.org/data/2.5/weather?q=' 
                        + city + '&appid=bb2290bea4b4d12aad0784abf8951c16').read() 


            # converting JSON data to a dictionary 
            list_of_data = json.loads(source) 


        except Exception as e:
        # handle the exception and return an error response
            # response_data = {'success': False, 'error': str(e)}
            # return HttpResponse(status=500, content_type='application/json', content=json.dumps(response_data))
            return HttpResponse("<h2>Please enter a valid city name")

         # data for variable list_of_data 
        data = { 
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']-273) + 'c', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        } 
        print(data) 
    

    else:
        data={}
    
    
    

    return render(request, "index.html", data) 