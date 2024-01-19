from django.shortcuts import render

def home(request):
    import json
    import requests
    from geopy.geocoders import Nominatim
    city="lucknow"
    
    if request.method=="POST":
        
        city=request.POST['city']
  
        # return render(request,'home.html',{'city':city})
        geolocator = Nominatim(user_agent="MyApp")
        location = geolocator.geocode(city,addressdetails=True)
        
        api_request=requests.get("https://api.openweathermap.org/data/2.5/weather?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&appid=4b9d5d7f629bce44d965bd8262877c11")
        try:
            api=json.loads(api_request.content)
        except Exception as e:
            api="error"
        return render(request,'home.html',{'api':api})
    
    else:
    
        
        geolocator = Nominatim(user_agent="MyApp")
        location = geolocator.geocode(city)
        
        api_request=requests.get("https://api.openweathermap.org/data/2.5/weather?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&appid=4b9d5d7f629bce44d965bd8262877c11")
        try:
            api=json.loads(api_request.content)
        except Exception as e:
            api="error"
        return render(request,'home.html',{'api':api})
# Create your views here.

def about(request):
    return render(request,'about.html',{})