x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def update_values(x, students, sports, z):
    x[1][0] = 15
    students[0]['last_name'] = "Bryant"
    sports['soccer'][0] = 'Andres'
    z[0]['y'] = 30

update_values(x, students, sports_directory, z)



print('==============================================================================')

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(some_list):
    for x in range(len(some_list)):
        print(f"first_name - {some_list[x]['first_name']}, last_name - {some_list[x]['last_name']}")


iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

def iterateDictionary2(key_name, some_list):
    for x in range(len(some_list)):
        print(some_list[x][key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    location_length = len(dojo["locations"])
    print(f"{location_length} LOCATIONS")
    for i in range(len(dojo["locations"])):
        print(dojo["locations"][i])

    instructors_amount = len(dojo["instructors"])
    print(f"{instructors_amount} INSTRUCTORS")
    for x in range(len(dojo["instructors"])):
        print(dojo["instructors"][x])
    
printInfo(dojo)


# SECOND WAY
keys = dojo.keys()
def printInfo2(some_dict):
    for k in keys:
        values = dojo[k]
        value_length = len(values)
        print(f"{value_length} {k}")
        for place in values:
            print(place)

printInfo2(dojo)