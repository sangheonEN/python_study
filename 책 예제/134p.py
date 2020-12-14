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



