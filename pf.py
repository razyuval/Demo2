import json

with open('students.JSON') as f:
    data = json.load(f)
ageTotal = 0
numOfEntries = (len(data['students']))
for student in data['students']:
   ageTotal += int(student['age'])
   if int(student['age']) > 18:
      student['member'] = True
   else:
      student['member'] = False

print(format("average age is %s years old" % str(ageTotal/numOfEntries) ))
print(str(data['students']))


with open('students_updates.JSON', 'w') as f:
   json.dump(data, f, indent=2)