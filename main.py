import ru_local as ru

print(ru.TASK)
print(ru.INPUT)

# distance from sond to sun in miles
dst_miles = 16_637_000_000
# sond speed in miles per hour
spd_sond = 38241
# speed of radio waves in miles per hour
spd_waves = 299_792_458 * 2.24
# number of days since September 25, 2009

days = int(input())
dst_miles += days * 24 * spd_sond
# distance from sond to sun in kilometers
dst_km = dst_miles * 1.61
# distance from sond to sun in astoronomical units
dst_au = dst_km / 149600000
# wireless delay in hours
delay = dst_miles / spd_waves


print(ru.DST_MILES, dst_miles)
print(ru.DST_KM, dst_km)
print(ru.DST_AU, dst_au)
print(ru.DELAY, delay)
