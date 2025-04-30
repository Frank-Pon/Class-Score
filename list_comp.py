# 請產出每一筆訂單的組合：
# [('Alice', 'apple'), ('Alice', 'banana'), ('Bob', 'cherry'), ...]
orders = [
    {"customer": "Alice", "items": ["apple", "banana"]},
    {"customer": "Bob", "items": ["cherry"]},
    # for x in orders:
    {"customer": "Cindy", "items": ["banana", "mango", "peach"]}
]  # for item in x['items']:
#        a=[(x['customer'],item)]
a = [(x['customer'], item) for x in orders for item in x['items']]  # print(a)

for i in a:
    print(i)
print('====================')

# 請產出每位按讚者和對應的 post_id：
# [('Amy', 101), ('Bob', 101), ('Cindy', 102)]
posts = [
    {"post_id": 101, "likes": ["Amy", "Bob"]},
    {"post_id": 102, "likes": ["Cindy"]},
    # for x in posts:
    {"post_id": 103, "likes": []}
]  # for person in x['likes']:
#        b=[(person,x['post_id'])]
b = [(person, x['post_id'])
     for x in posts for person in x['likes']]  # print(b)

for i in b:
    print(i)
print('====================')

# 產出資料：
# [('John', 'Python', 3), ('John', 'JavaScript', 2), ('Amy', 'SQL', 4)]
employees = [
    {"name": "John", "skills": {"Python": 3, "JavaScript": 2}},
    {"name": "Amy", "skills": {"SQL": 4}},
    # for x in employees:
]
#    for j in x['skills']:
#        c=[(x['name'],x['skills'][j])]
c = [(x['name'], j, x['skills'][j])
     for x in employees for j in x['skills']]  # print(c)

for i in c:
    print(i)
print('====================')

# 輸出句子：
# "Amy 的 math 成績是 80"
# "Amy 的 eng 成績是 90"
# ...
students = [
    {"name": "Amy", "math": 80, "eng": 90},
    {"name": "Bob", "math": 70, "eng": 75}
]
# for x in students:
subjects = ['math', 'eng']
#    for j in subjects:
#        d=[f'{x["name"]} 的 {j} 成績是 {x[j]}']
# print(d)
d = [f'{x["name"]} 的 {j} 成績是 {x[j]}' for x in students for j in subjects]

for i in d:
    print(i)
print('====================')

# 輸出成：
# [('Amy', 'A1'), ('Amy', 'A2'), ('Bob', 'B3')]
seats = [
    {"name": "Amy", "seats": ["A1", "A2"]},
    {"name": "Bob", "seats": ["B3"]},
    # for x in seats:
]
#    for seat in x['seats']:
#        e=[(x['name'],seat)]
e = [(x['name'], seat) for x in seats for seat in x["seats"]]  # print(e)

for i in e:
    print(i)
print('====================')
