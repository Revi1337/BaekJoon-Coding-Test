def solution(price):
    if price >= 500000:
        price = int(price*0.8)
    elif price >= 300000:
        price = int(price*0.9)
    elif price >= 100000:
        price = int(price*0.95)
    else:
        price = int(price)
    return price
  

# 10만원 --> 5퍼 할인
# 30만원 --> 10퍼 할인
# 50만원 --> 20퍼 할인