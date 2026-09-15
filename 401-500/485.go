package main

import (
	"fmt"
)

func findMaxConsecutiveOnes(nums []int) int {
	m, curr_m := 0, 0
	for _, n := range nums {
		if n == 1 {
			curr_m++
			m = max(m, curr_m)
		} else {
			curr_m = 0
		}
	}
	return m
}

func main() {
	fmt.Println(findMaxConsecutiveOnes([]int{1,1,0,1,1,1}))
    fmt.Println(findMaxConsecutiveOnes([]int{1,0,1,1,0,1}))
}