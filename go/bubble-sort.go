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
