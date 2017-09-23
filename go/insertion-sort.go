package main

import (
    "fmt"
    //"sort"
)

func Sort(arr []int) {
    var j int
    if len(arr) < 2 {
        return
    }
    for i := 1; i < len(arr); i ++ {
        temp := arr[i]
        for j = i - 1; j >= 0 && arr[j] > temp; j -- {
            arr[j + 1] = arr[j]
        }

        arr[j + 1] = temp
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
