import random
import sys


def switching(json, n, nx):
    objectHolder = json[n]
    json[n] = json[nx]
    json[nx] = objectHolder

## json[n], json[nx] = json[nx], json[n]


def nextPivot(json, attribute, start, length, currentPivotIndex):
    currentPivotObject = json[currentPivotIndex]
    switching(json, currentPivotIndex, (length-1))
    indexCurrentLoopObject = start
    for index in range(length):
        if json[attribute] <= currentPivotObject[attribute]:
            switching(json, indexCurrentLoopObject, index)
            indexCurrentLoopObject += 1
    switching(json, (length-1), indexCurrentLoopObject)
    return indexCurrentLoopObject


def quickSortIteration(json, attribute, start, length):
    if (length-1) > start:
        pivotIndex
        pivotIndex = start + (round(random.random()) * (length - start))
        pivotIndex = nextPivot(json, attribute, start, length, pivotIndex)
        quickSortIteration(json, attribute, start, pivotIndex)
        quickSortIteration(json, attribute, (pivotIndex+1), length)


def quickSort(json, attribute):
    start = 0
    length = len(json)
    quickSortIteration(json, attribute, start, length)


quickSort(sys.argv[1], sys.argv[2])


## use snake_case instead of camelCase