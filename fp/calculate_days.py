"""
Сначала решил в императивном стиле.
Писал изначально на java, т.к. ее синтаксис знаю лучше.
Потом перевел циклы на рекурсии. 

Затем перевел на python.
"""
def conquestCampaign(N: int, M: int, L: int, battalion):

    return calcaulateDays(
        1,
        N,
        M,
        L,
        battalion,
        [],
        0,
        1)
  

def calcaulateDays(
      daysAmount: int,
      N: int,
      M: int,
      L: int,
      battalion,
      outBattalion,
      i,
      j):

    print("outBattalion пришедший на вход в calcaulateDays: ")
    print(outBattalion)
    maxPointsAmount: int = N * M
    listPairsPoints = getListPairsPoints(
        battalion,
        outBattalion,
        L)
    print("listPairsPoints: ")
    print(listPairsPoints)
    pointSet = list(dict.fromkeys(listPairsPoints))
    print("pointSet.size(): ")
    print(len(pointSet))
    print("pointSet: ")
    print(pointSet)

    print("daysAmount: ")
    print(daysAmount)
    if (maxPointsAmount <= len(pointSet)):
      return daysAmount
      
    daysAmount = daysAmount + 1

    if (len(outBattalion) == 0):
      outBattalion = battalion

    nextOutBattalion = caclulateNextPointRecursiveWithotIterate(
        N,
        M,
        L,
        outBattalion,
        i,
        [])

    print("nextOutBattalion: ")
    print(nextOutBattalion)
    Lnext: int = len(nextOutBattalion) // 2
    listNextPairsPoints = getListPairsPointsShort(
        nextOutBattalion,
        Lnext)
    print("listNextPairsPoints: ")
    print(listNextPairsPoints)

    nextPointSet = list(dict.fromkeys(listNextPairsPoints))
    uniqueOutBattalion = list(sum(nextPointSet, ()))
        
    uniqueL: int = len(nextPointSet)
    Inext: int = i + 2
    Jnext: int = j + 2
    print("nextPointSet: ")
    print(nextPointSet)
    return calcaulateDays(
        daysAmount,
        N,
        M,
        uniqueL,
        battalion,
        uniqueOutBattalion,
        Inext,
        Jnext)

def caclulateNextPointRecursiveWithotIterate(
      N: int,
      M: int,
      L: int,
      outBattalion,
      i,
      nextOutBattalion):

    currentK: int = i
    maxK: int = L * 2
    iterate = lambda i: i + 2

    return caclulateNextPointRecursive(
        N,
        M,
        outBattalion,
        nextOutBattalion,
        currentK,
        maxK,
        iterate
    )
 

def caclulateNextPointRecursive(
      N: int,
      M: int,
      outBattalion,
      nextOutBattalion,
      currentK: int,
      maxK: int,
      iterate):

    if (currentK >= maxK):
      return nextOutBattalion
    

    nextOutBattalionForCurrentPair = calcaulateNextPoints(
        N,
        M,
        outBattalion,
        currentK,
        currentK + 1)

    nextOutBattalion.extend(nextOutBattalionForCurrentPair)

    nextCurrentK: int = iterate(currentK)
    return caclulateNextPointRecursive(
        N,
        M,
        outBattalion,
        nextOutBattalion,
        nextCurrentK,
        maxK,
        iterate
    )


def getListPairsPointsShort(
      outBattalion,
      L: int):
    nextList = []

    currentI: int = 1
    maxI: int = L * 2
    iterate = lambda i: i + 2
    return getListPairsPointsRecursive(
        outBattalion,
        nextList,
        currentI,
        maxI,
        iterate
    )



def getListPairsPointsRecursive(
      outBattalion,
      nextList,
      currentI: int,
      maxI: int,
      iterate):

    if (currentI >= maxI):
      return nextList
    
    
    pairNumber = (outBattalion[currentI - 1], outBattalion[currentI])
    nextList.append(pairNumber)

    nextCurrentI: int = iterate(currentI)
    return getListPairsPointsRecursive(
        outBattalion,
        nextList,
        nextCurrentI,
        maxI,
        iterate
    )
  

def getListPairsPoints(
      battalion,
      outBattalion,
      L: int):
    isFirstIteration: bool = len(outBattalion) == 0
    nextList = []
    if (isFirstIteration):
      return getListPairsPointsFirstIteration(battalion, L, nextList)
    return getListPairsPointsShort(outBattalion, L)



def getListPairsPointsFirstIteration( battalion, L: int, nextList):
    print("isFirstIteration")
    print("battalion.length: ")
    print(len(battalion))

    currentI = 1
    maxI = L * 2
    iterate = lambda i: i + 2
    return getListPairsPointsFirstIterationRecursion(
        battalion,
        nextList,
        currentI,
        maxI,
        iterate
    )

def getListPairsPointsFirstIterationRecursion(battalion, nextList, currentI: int, maxI: int, iterate):

    if (currentI >= maxI):
        return nextList
    
    pairNumber = (battalion[currentI - 1], battalion[currentI])
    nextList.append(pairNumber)
    nextCurrentI: int = iterate(currentI)
    return getListPairsPointsFirstIterationRecursion(
        battalion,
        nextList,
        nextCurrentI,
        maxI,
        iterate
    );
  

def calcaulateNextPoints(N: int, M: int, outBattalion, i: int, j: int):
    if (i is None and j is None):
        i = 0
        j = 1
    

    cureentN: int = outBattalion[i]
    cureentM: int = outBattalion[j]

    outBattalionFirst = calcaulateNextPointsFromCurrent(N, M, cureentN, cureentM);

    outBattalion.extend(outBattalionFirst)
    return outBattalion;
  


def calcaulateNextPointsFromCurrent(N: int, M: int, cureentN: int ,cureentM: int):
    moveLeft: int = cureentM - 1
    moveRight: int = cureentM + 1

    moveBottom: int = cureentN + 1
    moveTop: int = cureentN - 1
    
    outBattalionFirst = []
    if (moveRight <= M):
      print("outBattalion moveRight")
      outBattalionFirst.append(cureentN)
      outBattalionFirst.append(moveRight)
 
    if (moveLeft > 0):
      print("outBattalion moveLeft")
      outBattalionFirst.append(cureentN)
      outBattalionFirst.append(moveLeft)
    

    if (moveBottom <= N):
      print("outBattalion moveBottom")
      outBattalionFirst.append(moveBottom)
      outBattalionFirst.append(cureentM)
    
    if (moveTop > 0):
      print("outBattalion moveTop")
      outBattalionFirst.append(moveTop)
      outBattalionFirst.append(cureentM)
    
    return outBattalionFirst

def test():
    battalion = [2, 2, 3, 4];
    N = 3
    M = 4
    L = 2
    print(conquestCampaign(N, M, L, battalion))

test()
