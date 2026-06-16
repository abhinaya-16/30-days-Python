countries = [
    "Finland",
    "Canada",
    "Thailand",
    "Japan",
    "Poland",
    "Brazil",
    "Iceland",
    "India",
    "New Zealand",
    "Mexico"
]
print(countries)

for i in countries:
    if('land' in i):
        print(i)
print()
#-----------------------------------

fruits=['banana', 'orange', 'mango', 'lemon'] 
length=len(fruits)
reverse_fruits=[]
for i in range(length-1,-1,-1):
    reverse_fruits.append(fruits[i])
print(reverse_fruits)

print()
#-----------------------------------

countries = [
    {
        'name': 'China',
        'population': 1412600000,
        'languages': ['Chinese']
    },
    {
        'name': 'India',
        'population': 1438000000,
        'languages': ['Hindi', 'English']
    },
    {
        'name': 'United States',
        'population': 341000000,
        'languages': ['English']
    },
    {
        'name': 'Canada',
        'population': 41000000,
        'languages': ['English', 'French']
    },
    {
        'name': 'Switzerland',
        'population': 8900000,
        'languages': ['German', 'French', 'Italian']
    },
    {
        'name': 'Brazil',
        'population': 212000000,
        'languages': ['Portuguese']
    },
    {
        'name': 'Nigeria',
        'population': 237000000,
        'languages': ['English']
    },
    {
        'name': 'Japan',
        'population': 124000000,
        'languages': ['Japanese']
    },
    {
        'name': 'Germany',
        'population': 84000000,
        'languages': ['German']
    },
    {
        'name': 'Mexico',
        'population': 131000000,
        'languages': ['Spanish']
    }
]

all_languages = set()
for country in countries:
    all_languages.update(country['languages'])
print(len(all_languages))

language_count = {}
for country in countries:
    for language in country['languages']:
        language_count[language] = language_count.get(language, 0) + 1
top_languages = sorted(
    language_count.items(),
    key=lambda x: x[1],
    reverse=True
)
print(top_languages[:10])

top_populated = sorted(
    countries,
    key=lambda country: country['population'],
    reverse=True
)
for country in top_populated:
    print(country['name'], country['population'])