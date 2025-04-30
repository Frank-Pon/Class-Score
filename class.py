students = [
    {"name": "Amy", "math": 85, "english": 78},
    {"name": "Bob", "math": 58, "english": 62},
    {"name": "Cindy", "math": 92, "english": 88},
    {"name": "Anna", "math": 70, "english": 75}
]
subjects = ["math", "english"]
# ----------------------列表變數------------------------


def class_avg(subjects):
    return {sub: round(sum(student[sub] for student in students)/len(students), 1) for sub in subjects}
    # 帶入科目列表,回傳一個 key:科目 value:科目平均 的 dict
    # 這邊一行用到兩次生成式,要多注意混淆


def student_avg(student):
    total = sum(student[sub] for sub in subjects)
    return round(total/len(subjects), 1)
    # 帶入每個學生的資料 (dict),回傳平均成績


def get_passed(student):
    return all(student[sub] >= 60 for sub in subjects)
    # 帶入每個學生資料,回傳 boolean 每個科目都要超過60分才會 True(all的用意)


def pass_stu(students):
    c = sum(1 for i in students if i['passed'])
    n = [i['name'] for i in students if i['passed']]
    return (c, n)
    # 帶入全班資料,回傳通過人數及通過名單 (tuple)


def no_pass(students):
    c = sum(1 for i in students if not i['passed'])
    n = [i['name'] for i in students if not i['passed']]
    return (c, n)
    # 帶入全班資料,回傳未通過人數及未通過名單 (tuple)


def comment(student):
    if student['avg'] >= 90:
        return '優秀'
    elif student['avg'] >= 70 and student['avg'] <= 89:
        return '良好'
    elif student['avg'] >= 60 and student['avg'] <= 69:
        return '普通'
    return '不及格'


for student in students:  # 從全班裡面找到個人
    avg = student_avg(student)  # 取得個人平均成績
    student['avg'] = avg  # 將平均成績加入個人成績資料
    student['passed'] = get_passed(student)  # 將是否通過加入個人成績資料
    student['comment'] = comment(student)  # 將評語加入個人成績資料

sub_avg = class_avg(subjects)  # 取得班級各科目及其平均成績

# 依照學生平均成績做排序(降冪)
students = sorted(students, key=lambda x: x['avg'], reverse=True)
print('Grades:')
for student in students:
    print(student)
    # 輸出全班成績
print('===========================')
print('Avg:')
for sub, avg in sub_avg.items():
    print(f'Class {sub.capitalize()} avg : {avg}')
    # 輸出班級各科目平均
print('===========================')
print(f'通  過  人  數 : {pass_stu(students)[0]}  名 單 : {pass_stu(students)[1]}')
print(f'未 通 過 人 數 : {no_pass(students)[0]}  名 單 : {no_pass(students)[1]}')
# 輸出通過及未通過人數及名單 (tuple形式,可以使用索引值取資料)
