package main

import (
	"fmt"
)

func appendCharacters(s string, t string) int {
	longest := 0
	j := 0
    for i := 0; i < len(s) && j < len(t); i++ {
		if s[i] == t[j] {
			longest++
			j++
		}
	}
	return len(t) - longest
}

func main() {
	fmt.Println(appendCharacters("coaching", "coding"))
	fmt.Println(appendCharacters("abcde", "a"))
	fmt.Println(appendCharacters("z", "abcde"))
}