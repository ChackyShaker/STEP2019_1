
words = open("words.txt","r")
words_list = words.readlines()#list(type関数)
#print(words_list)#\nが含まれていた

#words_list = words_list.replace('\n','')
#words_list = words_list.rstrip('\n')

words_list_cut_n = []
for word in words_list:
    words_list_cut_n.append(word[:-2])

words_list_cut_n = [str.upper() for str in words_list_cut_n]
print(words_list_cut_n)

parts = list(input().split())

import itertools
parts_comb = list(itertools.permutations(parts))
#print(parts_comb[0])

result = ["".join(x) for x in parts_comb]
#print(result)

for word in result:
    if word in words_list_cut_n:
        print(word)
    else:
        pass




#if "ao" in words_list_cut_n:
# print("Yeeeeeee!!")
#else:
#    print("Oh,no!!")


#print(type(words_list))

#for word in words:
#    print(word)



