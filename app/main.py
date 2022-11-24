import utils

keys, values = utils.get_population()
print(keys, values)

data = [
    {
        'Country': 'Colombia',
        'Population': 300
    },
    {
        'Country': 'Argentina',
        'Population': 400
    }
]

country = input('Type Country => ')

result = utils.population_by_country(data, country)
print(result)