NUMS = [str(i) for i in range(10)]


def solution(files):
    file_info = []
    idx = 0
    for file in files:
        info = ['', '', 0]    # head, num, idx 3개
        flag = 0
        for i in range(len(file)):
            if flag == 0 and file[i] in NUMS:
                flag = 1
            if flag == 1 and file[i] not in NUMS:
                flag = 2

            if flag == 0 or flag == 1:
                info[flag] += file[i].lower()

        info[1] = int(info[1])
        info[2] = idx
        idx += 1

        file_info.append(info)

    file_info = sorted(file_info, key=lambda x: (x[0], x[1], x[2]))

    sorted_files = []
    for f in file_info:
        sorted_files.append(files[f[2]])

    return sorted_files


print(solution(['img12.png', 'img10.png',
                'img02.png', 'img1.png',
                'IMG01.GIF', 'img2.JPG']))