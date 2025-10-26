# Problem E
# detention=None
# meeting=None
# week=int(input(''))
# word=''
# punishments=[]
# people=[]
# points={}
# while word!='END':
#     word=input('')
#     punishments.append(word)
# punishments.remove('END')
# for i in range(len(punishments)):
#     punishments[i]=punishments[i].split()
# for i in range(len(punishments)):
#     code=punishments[i][1]
#     if code=='GDX':
#         punishments[i][1]=5
#     elif code=='SNK':
#         punishments[i][1]=15
#     elif code=='PRV':
#         punishments[i][1]=25
#     elif code=='TWO':
#         punishments[i][1]=20
#     elif code=='LNO':
#         punishments[i][1]=15
#     elif code=='LRB':
#         punishments[i][1]=10
#     try:
#         people.remove(punishments[i][0])
#         people.append(punishments[i][0])
#     except ValueError:
#         people.append(punishments[i][0])
# for person in people:
#     points.update({person:0})
# print(points["Monica"][1])
# print('Students for detention:')
# print(detention)
# print('Parental meeting for:')
# print(meeting)