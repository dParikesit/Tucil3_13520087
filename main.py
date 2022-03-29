import prioqueue
import copy
import time

# state adalah tuple dengan urutan (array 15 puzzle, int distFromRoot, int cost, int idx parent di array done)

def kurang(num, state):
    idx = -1
    for i in range(16):
        if state[0][i] == num:
            idx = i

    count = 0
    for i in range(idx, 16):
        if state[0][i] != -1 and state[0][i] < num:
            count += 1

    return count


def sumKurang(state):
    count = 0
    for i in range(1, 17):
        count += kurang(i, state)
    return count


def findX(state):
    shadowed = [1, 3, 4, 6, 9, 11, 12, 14]
    for i in range(1, 16):
        if state[0][i] == 16 and i in shadowed:
            return 1
    return 0


def kurangPlusX(state):
    return sumKurang(state) + findX(state)


def solvable(state):
    return kurangPlusX(state) % 2 == 0


def costFuncG(matrix):
    count = 0
    for i in range(16):
        if matrix[i] != i + 1 and matrix[i]!=16:
            count += 1
    return count


def move(state, direction):
    newMatrix = copy.deepcopy(state[0])

    idx = -1
    for i in range(16):
        if newMatrix[i] == 16:
            idx = i

    idxTukar = -1
    if direction == "top":
        if idx < 4:
            return newMatrix
        idxTukar = idx - 4
    elif direction == "bottom":
        if idx > 11:
            return newMatrix
        idxTukar = idx + 4
    elif direction == "left":
        if idx % 4 == 0:
            return newMatrix
        idxTukar = idx - 1
    elif direction == "right":
        if (idx + 1) % 4 == 0:
            return newMatrix
        idxTukar = idx + 1

    newMatrix[idx] = newMatrix[idxTukar]
    newMatrix[idxTukar] = 16

    return newMatrix

def solve(initState):
    start = time.perf_counter()

    # Nilai fungsi Kurang(i) tiap ubin awal
    for i in range(1, 17):
        print("Kurang",i, kurang(i, initState))
    
    # Nilai sumKurang(i)+X
    print()
    print("sumKurang(i)+X =",kurangPlusX(initState))
    print()

    prioQueue = prioqueue.PriorityQueue()

    if solvable(initState) == False:
        print("Jumlah simpul dibangkitkan =", prioQueue.simpulCount())
        return "Unsolvable"

    prioQueue.insert(initState)    
    done = []

    while prioQueue.isEmpty()==False:
        currState = prioQueue.pop()
        done.append(currState)

        if solvable(currState):
            if (currState[2] == currState[1]):
                path = []
                path.insert(0, currState)
                while path[0][3]!=-1:
                    path.insert(0, done[path[0][3]])

                for i in range(len(path)):
                    print(path[i][0])
                
                print()
                print("Jumlah simpul dibangkitkan =", prioQueue.simpulCount())
                print("Waktu =","{:.5f}".format(time.perf_counter()-start), "detik")
                return "Yey"

            newTop = move(currState, "top")
            newBot = move(currState, "bottom")
            newLeft = move(currState, "left")
            newRight = move(currState, "right")

            f = currState[1] + 1
            gTop = costFuncG(newTop) if newTop not in done else 9999
            gBot = costFuncG(newBot) if newBot not in done else 9999
            gLeft = costFuncG(newLeft) if newLeft not in done else 9999
            gRight = costFuncG(newRight) if newRight not in done else 9999

            if gTop != 9999:
                stateTop = (newTop, f, f + gTop, len(done)-1)
                prioQueue.insert(stateTop)
                # print(stateTop)
            if gBot != 9999:
                stateBot = (newBot, f, f + gBot, len(done)-1)
                prioQueue.insert(stateBot)
                # print(stateBot)
            if gLeft != 9999:
                stateLeft = (newLeft, f, f + gLeft,len(done)-1)
                prioQueue.insert(stateLeft)
                # print(stateLeft)
            if gRight != 9999:
                stateRight = (newRight, f, f + gRight,len(done)-1)
                prioQueue.insert(stateRight)
                # print(stateRight)
            # print(prioQueue.length())          
    print("Unknown Error")

if __name__ == '__main__':
    matrix = [1,16,2,3,5,6,7,4,9,10,11,8,13,14,15,12]
    # matrix = [3,5,6,4,1,16,12,15,13,2,10,7,14,9,11,8]
    initState = (matrix, 0, 0+costFuncG(matrix), -1)
    print(solve(initState))
