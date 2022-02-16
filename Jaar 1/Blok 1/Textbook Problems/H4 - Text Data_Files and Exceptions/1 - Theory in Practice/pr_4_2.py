# Assuming that variable forecast has been assigned string 'It will be a sunny day today'
forecast = 'It will be a sunny day today'

# write Python statements corresponding to these assignments:
# (a) To variable count, the number of occurrences of string 'day' in string forecast.
print(forecast.count('day'))

# (b) To variable weather, the index where substring 'sunny' starts.
print(forecast.find('sunny'))


# (c) To variable change, a copy of forecast in which every occurrence of substring 'sunny' is replaced by 'cloudy'.
forecast = forecast.replace('sunny', 'cloudy')
print(forecast)
