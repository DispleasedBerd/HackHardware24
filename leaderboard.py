import heapq as hq
scores = {"Player 1": 0, "Player 2": 0, "Player 3": 0, "Player 4": 0, "Player 5": 0}

def add_score(playerId, score):
    global scores
    if scores[playerId] > -score:
        scores[playerId] = -score

    heap = []
    for i in scores.values():
        heap.append(i)
    hq.heapify(heap)   
    print('heapify',heap)
    new_dict=[]
    for i in range(0,len(heap)):
     
    # Iterating the oringinal dictionary
        for k,v in scores.items():
        
            if v==heap[i] and (k,v) not in new_dict:
                new_dict.append((k,v))
    
    scores = dict(new_dict)
    print(scores)


def top(K):
    heap = []

    for score in scores.values():
        if len(heap) < K:
            hq.heappush(heap,score)
        else:
            if score < heap[0]:
                hq.heappop(heap)
                hq.heappush(heap, score)

    res = 0

    for num in heap:
        res += num
        
    return res

            
def reset(playerId):
    scores[playerId] = [0]

if __name__ == "__main__":
    add_score("Player 1", 1)
    add_score("Player 2", 5)
    
