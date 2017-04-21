package main

// NOTE: Google Research Blog:
// Extra, Extra - Read All About It: Nearly All Binary Searches and Mergesorts are Broken
// https://research.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html

import "fmt"

func binarySearch(arr []int, target int) int {
	var low, high, midVal int
	low = 0
	high = len(arr) - 1

	for low <= high {
		mid := low + ((high - low) / 2)
		midVal = arr[mid]

		if midVal > target {
			high = mid - 1
		} else if midVal < target {
			low = mid + 1
		} else {
			return mid
		}
	}

	return -(low + 1)
}

func main() {
	arr := []int{1, 2, 4, 5, 6, 10, 23, 53, 56, 99}
	fmt.Println("Find address of", 1, binarySearch(arr, 1))
}
