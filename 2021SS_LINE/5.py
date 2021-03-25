def solution(program, flag_rules, commands):
    ans = []

    # flag_rules 의 정보를 딕셔너리에 저장
    # flag_name 으로 flag_argument_type 을 조회할 수 있음
    flag_rules_dict = dict()
    for rule in flag_rules:
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

        # 2, 3, 4번 조건 검사에 쓰일 trigger
        # 조건에 어긋나면 trigger 를 false 로 표시하고 즉시 break
        trigger = True
        for name_args in command[1:]:
            # 각 flag 의 argument 개수를 확인

            # 공백이 없다는 것은 argument 가 없다는 의미
            # None 을 배정하여 Null type 검사를 가능하게 함
            if ' ' not in name_args:
                name, args = name_args, None

            # 공백이 있을 때 argument 가 한 개인지, 그 이상인지 검사
            else:
                name_args = name_args.split(' ')
                name, args = name_args[0], name_args[1:]
                if len(args) > 1:
                    trigger = False
                    break

            # 4번 조건
            # flag_rules 에 있는 flag 인가?
            if name not in flag_rules_dict:
                trigger = False
                break

            # 3번 조건을 위한 가산
            flag_cnt[name] += 1

            # 2번 조건
            # argument_type 이 일치하는가?
            if flag_rules_dict[name] == 'NULL' and args is None:
                continue
            elif flag_rules_dict[name] == 'NUMBER' and args[0].isdigit():
                continue
            elif flag_rules_dict[name] == 'STRING' and args[0].isalpha():
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
