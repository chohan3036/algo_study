def solution(program, flag_rules, commands):
    ans = []

    # flag_rules 의 정보를 딕셔너리에 저장
    # flag_name 으로 flag_argument_type 을 조회할 수 있음
    flag_rules_dict = dict()
    alias = dict()
    for rule in flag_rules:
        # ALIAS 가 문장이 포함돼 있으면 가명 저장 모드로 변환
        if 'ALIAS' in rule:
            flag_name1, _, flag_name2 = rule.split(' ')
            alias[flag_name1[1:]] = flag_name2[1:]
        else:
            flag_name, flag_argument_type = rule.split(' ')
            flag_rules_dict[flag_name[1:]] = flag_argument_type

    # 명령문을 순회하며 검증
    # 이때, ' -'으로 split 하여 program, flag1, flag2, ...의 형태로 산출한다.
    for command in commands:
        command = command.split(' -')

        # 1번 조건 검사
        # program 으로 시작하는가?
        if command[0] != program:
            ans.append(False)
            break

        # 3번 조건 검사를 위한 딕셔너리
        flag_cnt = dict(zip(flag_rules_dict.keys(), [0] * len(flag_rules_dict)))

        # 2, 4번 조건 검사에 쓰일 trigger
        # 조건에 어긋나면 trigger 를 false 로 표시하고 break
        trigger = True

        for name_arg in command[1:]:
            # 공백이 없다는 것은 argument 가 없다는 의미
            # None 을 배정하여 Null type 검사를 가능하게 함
            if ' ' not in name_arg:
                name, args = name_arg, None

            # argument 가 한 개이거나 여러 개인 경우 모두 고려
            else:
                name_arg = name_arg.split(' ')
                name, args = name_arg[0], name_arg[1:]

            # 4번 조건
            # flag_rules 에 있는 trigger 인가?
            # 만약 가명이라면, 원래 이름으로 바꾸어 flag_rules 를 조회 가능하게 함
            if name in alias:
                name = alias[name]
            elif name not in flag_rules_dict:
                trigger = False
                break

            # 3번 조건을 위한 가산
            # 가명을 바꾸는 작업 후에 실행한다
            flag_cnt[name] += 1

            # 2번 조건
            # argument_type 이 일치하는가?
            if flag_rules_dict[name] == 'NULL' and args is None:
                continue

            # argument 가 하나일 때는 0번째 인덱스의 원소만 취하고,
            # 여러 개 일 때는 리스트를 모두 검사
            elif flag_rules_dict[name] == 'NUMBER' and len(args) == 1 and args[0].isdigit():
                continue
            elif flag_rules_dict[name] == 'NUMBERS':
                for arg in args:
                    if not arg.isdigit():
                        trigger = False
                        break
                continue
            elif flag_rules_dict[name] == 'STRING' and len(args) == 1 and args[0].isalpha():
                continue
            elif flag_rules_dict[name] == 'STRINGS':
                for arg in args:
                    if not arg.isalpha():
                        trigger = False
                        break
                continue

            else:
                trigger = False
                break

        # 3번 조건
        # 각 flag 가 최대 한 번 사용됐는가?
        if max(flag_cnt.values()) > 1:
            trigger = False

        if not trigger:
            ans.append(False)
        else:
            ans.append(True)

    return ans


print(solution('line',
               ["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"],
               ["line -n 100 -s hi -e", "line -n 100 -e -num 150"]))
