# # 5.1번 m 으로 시작하는 단어 대문자로 변환하자.
# song = """When an eel grabs your arms.
#         And it causes great harm,
#         That's a- moray!!"""
# a = song.upper().find("m")
# print(a)

# 5.2번 리스트의 질문과 답을 차례로 출력
questions = ["We don't serve strings around here. Are you a string?",
             "What is said on Father's DAY in the forest?",
             "What makes the sound /'Sis! Boom! Bah!/'?"
             ]
answers = ["An exploding sheep.",
           "No, I'm a frayed knot.",
           "Pop\' goes the weasel."
           ]
for _ in range(3):
    print(f"{_+1}번 문답. {questions[_]} : {answers[_]}")

# 삽질
# print(questions)
# print(answers)
# print(questions[0])
# count = 1
# for i in questions, answers:
#     # print(f"{count} : {questions[count]} {answers[count]}")
#     # count += 1

# # 5.3번 문자열 포맷팅
# b = ["roast beef", "ham", "head", "clam"]
# print(f"""My kitty cat likes {b[0]},\nMy kitty cat likes {b[1]},\nMy kitty cat fell on his {b[2]} And now thinks he's a {b[3]}.""")

# # 5.5번
# # 'salutation', 'name', 'product', 'verbed', 'room', 'animals', 'amount', 'percent', 'spokesman', 'job_title'
# # letter.format() 사용
# alist = ['salutation', 'name', 'product', 'verbed', 'room', 'animals', 'amount', 'percent', 'spokesman', 'job_title']
# for i in alist:
#     print("{}@gmail.com".format(i))

# zip()함수!
a1list = ["jteks5@", "alqlwlel@", "dltkdgjs@", "zzzz@", "dkfsdk@"]
blist = ["naver.com", "gmail.com", "hanmail.net", "nate.com", "yahoo.com", ]
for i, j in zip(a1list, blist):
    print("{}{}".format(i, j))

# # 5.6번
# a = 'duck', 'gourd', 'spitz'
# print("{} McDuckface\n{} McGourdface\n{} McSpitzface".format(a[0], a[1], a[2]))
# print(f"{a[0]} McDuckface\n{a[1]} McGourdface\n{a[2]} McSpitzface")
