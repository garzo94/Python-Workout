## my solution

def get_rainfall():
    report = {}

    while True:
        city = input('enter a city')
        amount = input('how much rain?')
        if not city or not amount:
            for key in report:
                print(f'{key}: {report[key]}')
        if city != '' and city in report:
            report[city] += int(amount)
        elif city != '' :
            report[city] = int(amount)

get_rainfall()

# book solution
def get_rainfall():
    rainfall = {}
    while True:
        city_name = input('Enter city name: ')
        if not city_name:
            break
        mm_rain = input('Enter mm rain: ')
        rainfall[city_name] = rainfall.get(city_name,0) + int(mm_rain)
    for city, rain in rainfall.items():
        print(f'{city}: {rain}')

get_rainfall()
