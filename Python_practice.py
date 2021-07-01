# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for countyKey, countyValue in counties_dict.items():
#     print(f"{countyKey} has {countyValue:,} of voters")
# print(str(countyKey) + " county has " +
#       str(countyValue) + " registered voters")


# voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
#                {"county": "Denver", "registered_voters": 463353},
#                {"county": "Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)


# for county in range(len(voting_data)):
#     print(voting_data[county]['county'])

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# for county_dict in voting_data:
#     print(county_dict['registered_voters'])


voting_data = [{"county": "Arapahoe", "registered_voters": 422829}, {"county": "Denver",
                                                                     "registered_voters": 463353}, {"county": "Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(
        f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters")
    # print(county_dict['registered_voters'])
