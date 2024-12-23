# Declare an empty list
list_empty = []


# Declare a list with more than 5 items
cellphones_brands = ["Huawei", "Apple", "Samsung", "Xiaomi", "Realme", "Oppo", "Motorola"] 


# Find the length of your list
print(len(cellphones_brands))

# Get the first item, the middle item and the last item of the list
print(cellphones_brands[0], cellphones_brands[3], cellphones_brands[-1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Eliezer", 25, 1.73, "Married", "Cancún"]
print(mixed_data_types)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]


# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0], it_companies[3], it_companies[-1])

# Print the list after modifying one of the companies
it_companies[5] = "HP"
print(it_companies)

# Add an IT company to it_companies
it_companies.append("Asus")
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(4, "Lenovo")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[-1] = it_companies[-1].upper()
print(it_companies)

# Join the it_companies with a string '#;'
joined_string = '#;'.join(it_companies)
print(joined_string)

# Check if a certain company exists in the it_companies list.
print("GitHub" in it_companies)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[0:3])

# Slice out the last 3 companies from the list
print(it_companies[-3:])

# Slice out the middle IT company or companies from the list
middle = len(it_companies) // 2
print(it_companies[middle])

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies.pop(4)
print(it_companies)

# Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)

# Remove all IT companies from the list
del it_companies[0:]
print(it_companies)

# Destroy the IT companies list
del it_companies

"""
Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
"""
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_list = front_end + back_end

""" 
After joining the lists in question 26. 
Copy the joined list and assign it 
to a variable full_stack, then insert Python and SQL after Redux.
"""
full_stack = joined_list.copy()
full_stack.insert(4, "Python")
full_stack.insert(5, "SQL")
print(full_stack)

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
min_ages = min(ages)
max_ages = max(ages)
print(f"Min ages: {min_ages}\nMax ages: {max_ages}")

# Add the min age and the max age again to the list
ages.append(min_ages)
ages.append(max_ages)
print(ages)

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
middle_left = ages[len(ages) // 2 - 1]
middle_right = ages[len(ages) // 2]
median_age = (middle_left + middle_right) / 2

print(median_age)


# Find the average age (sum of all items divided by their number)
average_ages = sum(ages) / len(ages)
print(average_ages)

# Find the range of the ages (max minus min)
range_ages = max_ages - min_ages
print(range_ages)

# Compare the value of (min - average) and (max - average), use abs() method
print(abs(min_ages - average_ages))
print(abs(max_ages - average_ages))

# Find the middle country(ies) in the countries list
countries = [
'Afghanistan',
'Albania',
'Algeria',
'Andorra',
'Angola',
'Antigua and Barbuda',
'Argentina',
'Armenia',
'Australia',
'Austria',
'Azerbaijan',
'Bahamas',
'Bahrain',
'Bangladesh',
'Barbados',
'Belarus',
'Belgium',
'Belize',
'Benin',
'Bhutan',
'Bolivia',
'Bosnia and Herzegovina',
'Botswana',
'Brazil',
'Brunei',
'Bulgaria',
'Burkina Faso',
'Burundi',
'Cambodia',
'Cameroon',
'Canada',
'Cape Verde',
'Central African Republic',
'Chad',
'Chile',
'China',
'Colombi',
'Comoros',
'Congo (Brazzaville)',
'Congo',
'Costa Rica',
"Cote d'Ivoire",
'Croatia',
'Cuba',
'Cyprus',
'Czech Republic',
'Denmark',
'Djibouti',
'Dominica',
'Dominican Republic',
'East Timor (Timor Timur)',
'Ecuador',
'Egypt',
'El Salvador',
'Equatorial Guinea',
'Eritrea',
'Estonia',
'Ethiopia',
'Fiji',
'Finland',
'France',
'Gabon',
'Gambia, The',
'Georgia',
'Germany',
'Ghana',
'Greece',
'Grenada',
'Guatemala',
'Guinea',
'Guinea-Bissau',
'Guyana',
'Haiti',
'Honduras',
'Hungary',
'Iceland',
'India',
'Indonesia',
'Iran',
'Iraq',
'Ireland',
'Israel',
'Italy',
'Jamaica',
'Japan',
'Jordan',
'Kazakhstan',
'Kenya',
'Kiribati',
'Korea, North',
'Korea, South',
'Kuwait',
'Kyrgyzstan',
'Laos',
'Latvia',
'Lebanon',
'Lesotho',
'Liberia',
'Libya',
'Liechtenstein',
'Lithuania',
'Luxembourg',
'Macedonia',
'Madagascar',
'Malawi',
'Malaysia',
'Maldives',
'Mali',
'Malta',
'Marshall Islands',
'Mauritania',
'Mauritius',
'Mexico',
'Micronesia',
'Moldova',
'Monaco',
'Mongolia',
'Morocco',
'Mozambique',
'Myanmar',
'Namibia',
'Nauru',
'Nepal',
'Netherlands',
'New Zealand',
'Nicaragua',
'Niger',
'Nigeria',
'Norway',
'Oman',
'Pakistan',
'Palau',
'Panama',
'Papua New Guinea',
'Paraguay',
'Peru',
'Philippines',
'Poland',
'Portugal',
'Qatar',
'Romania',
'Russia',
'Rwanda',
'Saint Kitts and Nevis',
'Saint Lucia',
'Saint Vincent',
'Samoa',
'San Marino',
'Sao Tome and Principe',
'Saudi Arabia',
'Senegal',
'Serbia and Montenegro',
'Seychelles',
'Sierra Leone',
'Singapore',
'Slovakia',
'Slovenia',
'Solomon Islands',
'Somalia',
'South Africa',
'Spain',
'Sri Lanka',
'Sudan',
'Suriname',
'Swaziland',
'Sweden',
'Switzerland',
'Syria',
'Taiwan',
'Tajikistan',
'Tanzania',
'Thailand',
'Togo',
'Tonga',
'Trinidad and Tobago',
'Tunisia',
'Turkey',
'Turkmenistan',
'Tuvalu',
'Uganda',
'Ukraine',
'United Arab Emirates',
'United Kingdom',
'United States',
'Uruguay',
'Uzbekistan',
'Vanuatu',
'Vatican City',
'Venezuela',
'Vietnam',
'Yemen',
'Zambia',
'Zimbabwe',
];

print(countries[len(countries) // 2])


# Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_countries = countries[0: len(countries) // 2 + 1 ]
second_countries = countries[len(countries) // 2 + 1 :]
print(first_countries)
print(second_countries)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *scandic_countries = countries
print(first_country)
print(second_country)
print(third_country)
print(scandic_countries)