#!/usr/bin/env python
# coding: utf-8

# # weather API

# This code serves as a practical example of retrieving and displaying weather information through user interaction and API integration

# In[1]:


import requests


# In[2]:


while True:
    def weather_in_cities():
        API_key="88c8dabab7e73a8742990f6704fe6040"
        city_name=input("enter city name : ")
        url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name,API_key)

        response=requests.get(url)
        if response.status_code !=200:
            print("city is not found\n")
        else:
            data=response.json()
            kelvin_temp=data['main']['temp']
            celsius_temp = kelvin_temp - 273.15
            print("weather in %s is %.0f C\n"%(city_name,celsius_temp))

    weather_in_cities()
    key=input('press any key to continue or "E" for Exit \t')
    if key.lower() =="e":
        print("Exit")
        break
    else:
        continue


# In[ ]:





# In[ ]:




