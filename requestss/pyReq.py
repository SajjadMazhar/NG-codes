import requests

api_url = "https://saral.navgurukul.org/api/courses"
myData = requests.get(api_url).json()


IDs = []
courseNames = []
for obj in myData['availableCourses']:
    IDs.append(obj['id'])
    courseNames.append(obj['name'])

for i in range(len(IDs)):
    print(f"{IDs[i]} - {courseNames[i]}")
userInput = int(input("Enter the course ID: "))
courseAPI = f"http://saral.navgurukul.org/api/courses/{userInput}/exercises"
courseData = requests.get(courseAPI).json()
slugs = []
slugId = []
for index, exercise in enumerate(courseData['data']):
    print(f"{index+1}. {exercise['name']}")
    slugId.append(exercise['id'])
    slugs.append(exercise['slug'])

courseLinks = []
childEx = []
for index, data in enumerate(courseData['data']):
    courseLink = f"http://saral.navgurukul.org/api/courses/{data['id']}/exercise/getBySlug?slug={data['slug']}"
    courseLinks.append(courseLink)
    if data['childExercises']:
        for i, cData in data['childExercises']:
            courseLink1 = f"http://saral.navgurukul.org/api/courses/{cData['id']}/exercise/getBySlug?slug={cData['slug']}"
            indexing = f"{index}.{i} - {cData['name']}"
    else:
        indexing = f"{index} - {data['name']}"
    # requestedData = requests.get(courseLinks[0]).json()
    # with open(f'{fileName}', 'a') as f:
    #     f.write(str(requestedData))


print(courseLinks)