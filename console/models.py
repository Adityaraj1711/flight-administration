from django.db import models
from django.utils import timezone


class PhoneList(models.Model):
    name = models.CharField(max_length=100, default='')
    number = models.IntegerField(max_length=12)

    def __str__(self):
        return self.name


class QRData(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField()
    number = models.IntegerField()
    building = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class PhoneDetail(models.Model):
    device_id = models.CharField(default='', max_length=100)
    device_name = models.CharField(default='', max_length=100)
    center_lat = models.FloatField(default=0)
    center_lon = models.FloatField(default=0)
    device_lat = models.FloatField(default=0)
    device_lon = models.FloatField(default=0)
    inrange = models.BooleanField(default=False)

    def __str__(self):
        return str(self.device_lat) + ' ' + str(self.device_lon)

# # #

class Citizen(models.Model):
    name = models.CharField(default='', max_length=50)
    age = models.IntegerField()
    passport_number = models.IntegerField()


class Airport(models.Model):
    name = models.CharField(max_length=100, default='')
    longitude = models.IntegerField()
    latitude = models.IntegerField()


class Plane(models.Model):
    company = models.CharField(default='', max_length=50)
    plane_id = models.IntegerField()


class Flight(models.Model):
    flight_from = models.ForeignKey(Airport, related_name='flight_from', on_delete=models.CASCADE)
    flight_to = models.ForeignKey(Airport, related_name='flight_to', on_delete=models.CASCADE)
    plane_id = models.ForeignKey(Plane, on_delete=models.CASCADE)
    time_of_arrival = models.DateTimeField(default=timezone.now)
    time_of_boarding = models.DateTimeField(default=timezone.now)
    stay_time = models.DurationField()
    cost = models.IntegerField()
    business_capacity = models.IntegerField()
    economy_capacity = models.IntegerField()
    buisness_vacant = models.IntegerField()
    economy_vacant = models.IntegerField()


class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    STATES = [(0, 'NA'), (1, 'FINISHED'), (2, 'INTRANSIT'), (3, 'CANCELLED'), (4, 'FUTURE')]
    state = models.IntegerField(choices=STATES, default=0)


class Luggage(models.Model):
    weight = models.IntegerField()
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)


class Promotion(models.Model):
    name = models.CharField(default='', max_length=50)
    discount_code = models.IntegerField()
    discount_percent = models.IntegerField()
    valid = models.BooleanField(default=False)


class Transaction(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
