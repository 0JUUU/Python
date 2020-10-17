def solution(skill, skill_trees):
    answer = 0
    delete = []

   
    for skill_tree in skill_trees:
         # 스킬트리에 들어가지 않는 스킬 제거
        for i in range (len(skill_tree)):
            if (skill_tree[i] in skill) == False:
                delete.append(skill_tree[i])
        for element in delete:
            skill_tree = skill_tree.replace(element,"")
        
        delete.clear()

        for i in range(len(skill)):
            skill_tree = skill_tree.replace(skill[i],str(i))
        
        avail = True
        min = 0
        for i in range(len(skill_tree)):
            # print("min : {}, skill_tree[i] : {}".format(min, skill_tree[i]))
            if min == int(skill_tree[i]):
                min += 1
            else:
                avail = False
        
        if avail == True:
            answer += 1

   



    
    
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))