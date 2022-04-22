cohort_10 = {'name': 'Segun',
             'age': '12',
             'sex': 'male',
             'passion': ['python', 'Java'],
             'is_wife_beater': False
             }
print(cohort_10)
print()
print(len(cohort_10))
print()
print(cohort_10['passion'])
print()
for key in cohort_10:
    print(key)
print()
for key in cohort_10:
    print(key, '---->', cohort_10[key])
print()
for key in cohort_10.keys():
    print(key, '---->', cohort_10[key])
print()
print(cohort_10.items())
print()
for keys, values in cohort_10.items():
    print(keys, '---->', values)
print()



cohort_10 = [{dict()}, {dict()}]

