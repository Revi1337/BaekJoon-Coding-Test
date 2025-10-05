def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    dic1, dic2 = {}, {}

    for idx in range(1, len(str1)):
        str = str1[idx - 1:idx + 1]
        if len(str) != 2 or not str.isalpha():
            continue
        dic1[str] = dic1.get(str, 0) + 1
    for idx in range(1, len(str2)):
        str = str2[idx - 1:idx + 1]
        if len(str) != 2 or not str.isalpha():
            continue
        dic2[str] = dic2.get(str, 0) + 1

    if not dic1 and not dic2:
        return 65536

    keys = set(dic1.keys()) | set(dic2.keys())

    inter = union = 0
    for key in keys:
        if key in dic1 and key not in dic2:
            union += dic1[key]
        elif key in dic2 and key not in dic1:
            union += dic2[key]
        elif key in dic1 and key in dic2:
            union += max(dic1[key], dic2[key])
            inter += min(dic1[key], dic2[key])

    return int(inter / union * 65536)