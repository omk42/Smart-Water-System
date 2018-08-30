import pyowm
import time

API = "04ea3b5a85a13541d2852b5d752618bc"

class Weather:
    def __init__(self):
        self._owm = pyowm.OWM(API)
        self._observation = self._owm.weather_at_coords(33.653460, -117.820650)
        self._weather = self._observation.get_weather()

    def temperature(self):
        return self._weather.get_temperature('celsius')["temp"]

    def humidity(self):
        return self._weather.get_humidity()

    def time(self):
        return self._weather.get_reference_time('iso')

    def weather_code(self):
        return self._weather.get_weather_code()

    def clouds(self):
        return self._weather.get_clouds()

    def rain(self):
        rain_dict = self._weather.get_rain()
        if len(rain_dict) == 0:
            return 0
        else:
            return rain_dict

    def city(self):
        return self._observation.get_location().get_name()


    def current(self):
        ret_dict = dict(temperature=0, weather_code=0, humidity=0, cloud_percent=0, rain=0, city=0)
        try:
            ret_dict["temperature"] = self.temperature()
            ret_dict["humidity"] = self.humidity()
            ret_dict["weather_code"] = self.weather_code()
            ret_dict["cloud_percent"] = self.clouds()
            ret_dict["rain"] = self.rain()
            ret_dict["city"] = self.city()
        except:
            pass
        finally:
            return ret_dict

if __name__ == "__main__":
    w = Weather()

    print(w.temperature())
    print(w.humidity())
    print(w.weather_code())
    print(w.clouds())
    print(w.rain())
    print(w.city())

    print (w.current())