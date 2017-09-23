package main

import (
    "fmt"
    //"sort"
)

func Sort(arr []int) {
    var min int
    for i := 0; i < len(arr) - 1; i ++ {
        min = i
        for j := min + 1; j < len(arr); j ++ {
            if (arr[min] > arr[j]) {
                min = j
            }
        }

        arr[min], arr[i] = arr[i], arr[min]
    }
}

func printArr(arr []int) {
    for _, i := range arr {
        fmt.Printf("%v ", i)
    }
}

func main() {
    var testArr []int = []int{21, 1, 52, 51, 66}
    printArr(testArr)
    fmt.Println()
    Sort(testArr)
    printArr(testArr)
    fmt.Println()
}
