# модуль html


from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view

def create(device = 1):
    stile = 'stile="front-size:22px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    
    html += '    <p {}>Temperature: {} c</p>\n'\
        .format(stile, temperature_view(device))
    
    html += '    <p {}>Wind_speed: {} m/s</p>\n'\
        .format(stile, wind_speed_view(device))
    
    html += '    <p {}>Pressure: {} mmHg</p>\n'\
        .format(stile, pressure_view(device))

    with open('index.html', 'w') as page:
        page.write(html)

    return html