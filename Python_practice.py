counties = ["Arapahoe","Denver","Jefferson"]
counties_dict = {"Arapahoe": 422829, "Denver": 463352, "Jefferson": 432438}
voting_data = [{'county':'Arapahoe', 'registered_voters':422829}, 
                {'county':'Denver','registered_voters':463352},
                {'county':'Jefferson','registered_voters':432438}]
#if counties[1] == "Denver":
#    print(counties[1])

#if 'Arapahoe' in counties:
#    print('True')
#else:
#    print('False')


#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso is not in the list of counties.")

#for county in counties:
#    print(county)

#for num in range(5):
#    print(num)

for i in range(len(counties)):
    print(counties[i])

for county in counties_dict.keys():
    print(county)

#To get the values of a dictionary, we iterate over the dictionary 
# using the values() method, just like we used the keys() method.
for voters in counties_dict.values():
    print(voters)
#You can also use the format dictionary_name[key] to get the value 
# for the key
for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

#print the key-value pair of the dictionary
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

#iterating over a list of dictionaries
for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters. ")
    
