while True:
    try:
        _ = int(input())
        datas = list(map(int, input().split()))
        print(f"{min(datas)} {max(datas)}")
    except Exception as e:
        break

# while True:
#     try:
#         _ = int(input())
#         datas = list(map(int, input().split()))
#         mi = 1_000_001
#         ma = 0
#         for data in datas:
#             if data < mi:
#                 mi = data
#             if data > ma:
#                 ma = data
#         print(mi, ma)
#     except Exception as e:
#         break