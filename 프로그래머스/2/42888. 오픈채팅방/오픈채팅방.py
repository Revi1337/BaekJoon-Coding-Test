def solution(record):
    id_nickname_mapper = {}
    for operation in record:
        opcode, user_id, *nickname = operation.split()
        if opcode != 'Leave':
            id_nickname_mapper[user_id] = nickname[0]

    answer = []
    for operation in record:
        opcode, user_id, *nickname = operation.split()
        if opcode == 'Enter':
            answer.append(f'{id_nickname_mapper[user_id]}님이 들어왔습니다.')
        elif opcode == 'Leave':
            answer.append(f'{id_nickname_mapper[user_id]}님이 나갔습니다.')
    return answer