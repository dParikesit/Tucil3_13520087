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

def solve(initState, path, simpulTime):
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
        return False

    prioQueue.insert(initState)
    allPath = []  
    done = []
    inQueue = []

    while prioQueue.isEmpty()==False:
        currState = prioQueue.pop()
        done.append(currState[0])
        allPath.append(currState)

        if solvable(currState):
            if (currState[1]==currState[2]):
                path.insert(0, currState)
                while path[0][3]!=-1:
                    path.insert(0, allPath[path[0][3]])

                print("Here")
                for i in range(len(path)):
                    print(path[i][0])
                
                print()
                print("Jumlah simpul dibangkitkan =", prioQueue.simpulCount())
                print("Waktu =","{:.5f}".format(time.perf_counter()-start), "detik")

                simpulTime.append(prioQueue.simpulCount())
                simpulTime.append(time.perf_counter()-start)
                return True

            print(currState)
            print(prioQueue.length())
            newTop = move(currState, "top")
            newBot = move(currState, "bottom")
            newLeft = move(currState, "left")
            newRight = move(currState, "right")

            f = currState[1] + 1
            gTop = costFuncG(newTop) if (newTop not in done) and (newTop not in inQueue) else -1
            gBot = costFuncG(newBot) if (newBot not in done) and (newBot not in inQueue) else -1
            gLeft = costFuncG(newLeft) if (newLeft not in done) and (newLeft not in inQueue) else -1
            gRight = costFuncG(newRight) if (newRight not in done) and (newRight not in inQueue) else -1

            if gTop != -1:
                stateTop = (newTop, f, f + gTop, len(done)-1)
                prioQueue.insert(stateTop)
                inQueue.append(newTop)
            if gBot != -1:
                stateBot = (newBot, f, f + gBot, len(done)-1)
                prioQueue.insert(stateBot)
                inQueue.append(newBot)
            if gLeft -1:
                stateLeft = (newLeft, f, f + gLeft,len(done)-1)
                prioQueue.insert(stateLeft)
                inQueue.append(newLeft)
            if gRight != -1:
                stateRight = (newRight, f, f + gRight,len(done)-1)
                prioQueue.insert(stateRight)
                inQueue.append(newRight)     
    print("Unknown Error")