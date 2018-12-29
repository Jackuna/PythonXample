# ----------------------------------------------------------------------------------------------  #
# PyISSFinder : International Space Station finder will show where it's currently over earth
#
# This script takes no input, one can change the latitude and longitude to find the date/time
# when the ISS will be head over it.
# ----------------------------------------------------------------------------------------------  #


import urllib.request
import json
import turtle
import time


def iss_finder():

    url_01 = 'http://api.open-notify.org/astros.json'
    call_url_01 = urllib.request.urlopen(url_01)
    json_result_01 = json.loads(call_url_01.read())

    total_person_in_ISS = json_result_01['number']
    people = json_result_01['people']


    url_02 = 'http://api.open-notify.org/iss-now.json'
    call_url_02 = urllib.request.urlopen(url_02)

    json_result_02 =  json.loads(call_url_02.read())

    lat = float(json_result_02['iss_position']['latitude'])
    lon = float(json_result_02['iss_position']['longitude'])


    screen=turtle.Screen()
    screen.title('ISS Location Detector')
    screen.setup(730,370)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgcolor('blue')
    screen.bgpic('map.gif')
    screen.register_shape('iss2.gif')

    astronouts = turtle.Turtle()
    astronouts.penup()
    astronouts.color('red')
    astronouts.goto(-170, -10)
    astronouts.write('Astronauts in space')
    astronouts.color('yellow')

    var_list=list(range(total_person_in_ISS))
    y_cord = 0

    for new_val in var_list:
        astronouts.goto(-170, (-50+y_cord))
        astronouts.write(people[new_val]['name'])
        y_cord = y_cord + 10
    astronouts.hideturtle()
       
    iss=turtle.Turtle()
    iss.shape('iss2.gif')
    iss.setheading(90)
    iss.penup()
    iss.goto(lon,lat)

def iss_over_mycity():

    '''  Function to get the next time/date slot when ISS will
         be heading over my city.  
         I have set it to Noida
    '''
    
    mylat = float(28.609170)
    mylong = float(77.352800)

    my_location = turtle.Turtle()
    my_location.penup()
    my_location.color('cyan')
    my_location.goto(mylong, mylat)
    my_location.dot(7)
    my_location.hideturtle()


    url_03 =  'http://api.open-notify.org/iss-pass.json?'+'lat='+str(mylat)+'&lon='+str(mylong)
    call_url_03 = urllib.request.urlopen(url_03)

    json_result_03 = json.loads(call_url_03.read())

    risetime = json_result_03['response'][0]['risetime']

    style = ('Arial', 10, 'normal')

    my_location.write( time.ctime(risetime), font=style)


iss_finder()
iss_over_mycity()


