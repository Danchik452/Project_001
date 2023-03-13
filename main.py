import ru_local as ru

print(ru.TASK)
print(ru.INPUT)

dst_miles = 16637000000  # distance from sond to sun in miles
spd_sond = 38241  # sond speed in miles per hour
spd_waves = 299792458 * 2.24  # speed of radio waves in miles per hour

days = int(input())  # number of days since September 25, 2009

dst_miles += days * 24 * spd_sond
dst_km = dst_miles * 1.61  # distance from sond to sun in kilometers
dst_au = dst_km / 149600000  # distance from sond to sun in astoronomical units

delay = dst_miles / spd_waves  # wireless delay in hours


print(ru.DST_MILES, dst_miles)
print(ru.DST_KM, dst_km)
print(ru.DST_AU, dst_au)
print(ru.DELAY, delay)
