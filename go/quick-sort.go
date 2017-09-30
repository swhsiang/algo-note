package main

import (
    "fmt"
    //"sort"
)

func Sort(arr []int) {
    for i := 0; i < len(arr) - 1; i ++ {
        for j := 0; j < len(arr) - i - 1; j ++ {
            if (arr[j] > arr[j + 1]) {
                arr[j], arr[j+1] = arr[j+1], arr[j]
            }
        }
    }
}

func quickSort(array []int) {
    if len(array) < 1 {
        return
    }
    qSort(array)
}

func qSort(array []int) {
    if 0 < len(array) - 1 {
        left := -1
        end := len(array) - 1
        for j := 0; j < len(array); j ++ {
            if array[left] <= array[end] {
                left ++
                array[left], array[j] = array[j], array[left]
            }
        }
        array[left + 1], array[end] = array[end], array[left + 1]

        //pa := partition(array[:])
//        qSort(array[:pa - 1])
 //       qSort(array[pa + 1:])
        qSort(array[:left])
        qSort(array[left + 2:])
    }
}

func partition(array []int) (int) {
    left := -1
    end := len(array) - 1
    for j := 0; j < len(array); j ++ {
        if array[left] <= array[end] {
            left ++
            array[left], array[j] = array[j], array[left]
        }
    }
    array[left + 1], array[end] = array[end], array[left + 1]
    return left + 1
}

func quickSort2(sortArray []int, left, right int) {
    if left < right {
        key := sortArray[(left+right)/2]
        i := left
        j := right

        for {
            for sortArray[i] < key {
                i++
            }
            for sortArray[j] > key {
                j--
            }
            if i >= j {
                break
            }
            sortArray[i], sortArray[j] = sortArray[j], sortArray[i]
        }

        quickSort2(sortArray, left, i-1)
        quickSort2(sortArray, j+1, right)
    }
}

func QuickSort2(values []int){
    quickSort2(values, 0, len(values) - 1)
}

func printArr(arr []int) {
    for _, i := range arr {
        fmt.Printf("%v ", i)
    }
    fmt.Println()
}

func main() {
    var testArr []int = []int{1, 21, 1, 52, 51, 66, 3, 4, 3,95}
    printArr(testArr)
    //Sort(testArr)
    QuickSort2(testArr)
    printArr(testArr)
}
