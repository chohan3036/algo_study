from collections import defaultdict

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def solution(genres, plays):
    songs = list(zip(genres, plays))
    ranks = defaultdict(lambda: [])
    total_plays = defaultdict(lambda: 0)

    for i in range(len(songs)):
        ranks[songs[i][0]].append((songs[i][1], i))
        total_plays[songs[i][0]] += songs[i][1]

    total_plays = sorted(total_plays.items(), key=lambda x: -x[1])

    release = []
    for t in total_plays:
        tmp = sorted(ranks[t[0]], key=lambda x: x[0], reverse=True)
        release.append(tmp[0][1])
        if len(tmp) > 1:
            release.append(tmp[1][1])

    return release

print(solution(genres, plays))
