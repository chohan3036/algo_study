def solution(snapshots, transactions):
    accounts = dict()
    for account, amount in snapshots:
        accounts[account] = int(amount)

    log_id = []
    for id, kind, account, amount in transactions:
        if id not in log_id:
            log_id.append(id)
            if kind == 'SAVE':
                if account not in accounts:
                    accounts[account] = int(amount)
                else:
                    accounts[account] += int(amount)
            else:
                accounts[account] -= int(amount)

    ans = []
    for account in accounts:
        ans.append([account, str(accounts[account])])

    # ascii 로 다 쪼개서 정렬!

    return ans


print(solution([['ACCOUNT1', '100'], ['ACCOUNT2', '150']],
               [['1', 'SAVE', 'ACCOUNT2', '100'],
                ['2', 'WITHDRAW', 'ACCOUNT1', '50'],
                ['1', 'SAVE', 'ACCOUNT2', '100'],
                ['4', 'SAVE', 'ACCOUNT3', '500'],
                ['3', 'WITHDRAW', 'ACCOUNT2', '30']]))
