
from itertools import combinations, chain

ratings = [
    28380,
    28220,
    28170,
    28110,
    28030, #5
    27930,
    27860,
    27830,
    27740,
    27720, #10
    27713,
    27610,
    27590,
    27551,
    27511, # 15
    27510,
    27500,
    27496,
    27468,
    27450, # 20
    27410,
    27390,
    27340,
    27320,
    27286, #25
    # 27280,
    # 27269,
    # 27240,
    # 27226,
    # 27200,
    # 27180,
    # 27140,
    # 27120,
    # 27102,
    # 27101,
    # 27100,
    # 27091,
    # 27090,
    # 27086,
    # 27074,
    # 27060,
    # 27024,
    # 27011,
    # 27010,
]

count = 1 + len(ratings) # The tournament containing all players + all tournaments missing 1 player

def ct(t):
    return listdiff(ratings, t)[-2:]
    
def listdiff(a, b):
    return [e for e in a if e not in b]

def average(t):
    return sum(t)/(len(t)*1.0)

def manda(ct):
    max_ct = max(ct)
    min_ct = min(ct)
    #print max_ct, min_ct
    return [e for e in ratings if e > min_ct and e != max_ct]

def nextplayer(p):
    if p > ratings[-1]:
        return ratings[ratings.index(p)+1]


tournaments = []
def gent(t, ct):
    global count
    
    if len(t) == 0:#happens when ct is number 1 and 2
        return
    if average(t) <= average(ct):
        #print t
        return
    else:
        if(len(t)>1):#do not count tournament consisting of only Magnus
            
            t = sorted(t, reverse = True) # not sure why they would be unsorted...
            if t not in tournaments:
                tournaments.append(t)
                #print t
                
                count += 1
                #print average(ct), average(t), ct, t
            else:
                return
        used = t+ct
        remaining = listdiff(ratings, used)
        last = min(used)
        recruits = listdiff(t, manda(ct))# players added after manda
        
        if(last > ratings[-1]): # addnext
            nt = list(t)
            nt.append(nextplayer(last))
            gent(nt, ct)
        

        for r in recruits:#moveonce
            if nextplayer(r) not in t and r > ratings[-1]: #there is space after r, and r is not the last
                nt = list(t)
                nt.append(nextplayer(r))
                nt.remove(r)
                gent(nt,ct)


def points(a):
    return sum([ratings.index(p) for p in a])

tournaments2 = []

def gent2(ct):
    global count
    t = manda(ct)
    
    if len(t) == 0:#happens when ct is number 1 and 2
        return
    if average(ct) >= average(t): # mandas didnt make it
        #print t
        return


    
    remaining = ratings[ratings.index(min(t+ct))+1:] # cuts off the used players
    #remaining = listdiff(ratings, t+ct)
    if len(t) >= 2:# but not the tournament consisting of only one player
        tournaments2.append(t)
        count +=1 # mandas made it
        
    for l in range(1, len(remaining)+1):
        
        firsts = remaining[:l] # abcde
        Q = [firsts]
        i = 0
        s = Q[i]
        #s = list(Q.popleft())
        #impscore = (len(ratings)*(len(ratings)+1.0))/2 # impossible to score more than this
        while True:
            #print s, l
            
            
            if average(s+t) > average(ct):
                count += 1
                for e in s:#moveonce
                    if nextplayer(e) not in s and e > ratings[-1]: #there is space after r, and r is not the last
                        ns = list(s)
                        
                        ns.insert(ns.index(e), nextplayer(e))
                        #ns.append(nextplayer(e))
                        ns.remove(e)
                    
                        if ns not in Q:
                            Q.append(ns)
            i += 1
            if i < len(Q):
                s = Q[i]
                #s = list(Q.popleft())
            else:
                break
        
# for i in range(1, 44):
#     start = time.time()
#     ratings = rating[:i]
#     cts = list(combinations(ratings, 2))
#     count = i+1
#     for ct in cts:
#         ct = list(ct)
#         gent2(ct)
#     end = time.time()
#     print i, count, "{0}s".format(int(round(end-start)))


cts = list(combinations(ratings, 2))

for ct in cts:
    ct = list(ct)

    gent2(ct)
    #gent(manda(ct), ct)

print count

# gent(manda([28030, 27930]), [28030, 27930])
# gent2([28030, 27930])

# print len(set(tuple(x) for x in tournaments))
# # for t in tournaments:
# #     print t

    


# print len(set(tuple(x) for x in tournaments2))
# # for t in tournaments:
# #     print t

    


#print [x for x in tournaments if x not in tournaments2]
