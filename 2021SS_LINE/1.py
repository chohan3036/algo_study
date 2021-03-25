def solution(table, languages, preference):
    score = dict(zip(languages, preference))
    result = dict()
    for col in table:
        parse = col.split(' ')

        dept = parse[0]
        result[dept] = 0

        for i in range(1, 6):
            if parse[i] in score:
                result[dept] += (6 - i) * score[parse[i]]

    return sorted(result.items(), key=lambda x: (-x[1], x[0]))[0][0]


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
               ["JAVA", "JAVASCRIPT"],
               [7, 5]))
