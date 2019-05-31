
words = open("words.txt","r")
words_list = words.readlines()#list(type関数)
#print(words_list)#\nが含まれていた

#words_list = words_list.replace('\n','')
#words_list = words_list.rstrip('\n')

words_list_cut_n = []
for word in words_list:
    words_list_cut_n.append(word[:-2])

words_list_cut_n = [str.upper() for str in words_list_cut_n]
#print(words_list_cut_n)
#print(len(words_list_cut_n))#72412

parts = list(input().split())
#import copy
#parts_unique = copy.copy(parts)#参照先を変更（これでpartsに変更が及ばなくなる）

##うまくいかない（減らす発想はやめたほうがいい）
#for compare in words_list_cut_n:
#    for i in range(len(parts)):
#            if parts[i] not in compare:
#                words_list_cut_n.remove(compare)


words_list = [[] for i in range(17)]
for word in words_list_cut_n:
    words_list[len(word)].append(word)

#print(words_list[3])

##処理量減るかわかんないのでとりあえずかっと
#parts_unique = list(set(parts))
#word_start_match = [[] for i in range(17)]
#for check_list in words_list:
#for check_word in check_list:
#        for i in parts_unique:
#            if check_word.startswith(i) == True:
#            word_start_match[len(check_word)].append(check_word)

import itertools
comb_parts = [[] for i in range(17)]
for i in range(17):
   comb_parts[i]  = list(itertools.combinations(parts,i))


def contains_all(parts, word):
    for part in parts:
        if not part in word:
            return False
    return True

result = []
for i in range(17):
    for word in words_list[i]:
        for parts in comb_parts[i]:
                if contains_all(parts,word) == True:
                    sorted_parts = sorted(list(parts))
                    sorted_word = sorted(list(word))
                    if sorted_parts == sorted_word:
                            result.append(word)


print(result)






#for i in words_list:
#    print(len(i))


##重すぎて現実的でない
#import itertools
#parts_comb = list(itertools.permutations(parts))
#print(parts_comb[0])

#result = ["".join(x) for x in parts_comb]
#print(result)
#for word in result:
#    if word in words_list_cut_n:
#        print(word)
#    else:
#        pass








#words_list_16 = []
#for word in words_list_cut_n:
#    if  len(word) == 16:
#        words_list_16.append(word)
#    else:
#        pass
#print(words_list_16)


#if "ao" in words_list_cut_n:
# print("Yeeeeeee!!")
#else:
#    print("Oh,no!!")


#print(type(words_list))





