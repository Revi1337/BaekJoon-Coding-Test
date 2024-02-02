def solution(genres, plays):
    music = {}
    counter = {}
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        music[genre] = music.get(genre, [])
        music[genre].append([idx, play])
        counter[genre] = counter.get(genre, 0) + play

    answer = []
    for genre, _ in sorted(counter.items(), key=lambda x: -x[1]):
        for index, play in sorted(music[genre], key=lambda x: -x[1])[:2]:
            answer.append(index)
    return answer