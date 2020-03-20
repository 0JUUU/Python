character = {
    "name":"기사",
    "level":12,
    "items": {
        "sword" :"불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is list:
        for index in character[key]:
            print(key," : ",index)
    else:
        if type(character[key]) is dict:
            for in_key in character[key]:
                print(in_key," : ",character[key][in_key])

        else:
            print(key," : ",character[key])
   