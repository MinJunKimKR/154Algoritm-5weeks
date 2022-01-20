def solution(record):
    answer = []
    data = {}
    result = []

    for idx, rec in enumerate(record):
        if len(rec.split()) == 2:
            order, uid = rec.split()
            answer.append([uid, "Leave"])

        else:
            order, uid, nickname = rec.split()
            data[uid] = nickname

            if order == "Enter":
                answer.append([uid, "Enter"])

    for idx, uidRec in enumerate(answer):
        uid, order = uidRec

        if order == "Enter":
            name = data[uid] + "님이 들어왔습니다."
            result.append(name)
        else:
            name = data[uid] + "님이 나갔습니다."
            result.append(name)
    return result

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))