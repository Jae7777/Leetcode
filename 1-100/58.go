package main

import (
	"fmt"
)

func lengthOfLastWord(s string) int {
	res := 0
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] == ' ' && res != 0 {
			break
		}
		if s[i] == ' ' {
			continue
		}
		res += 1
	}
	return res
}

func main() {
	fmt.Println(lengthOfLastWord("Hello World"))
	fmt.Println(lengthOfLastWord("   fly me   to   the moon  "))
	fmt.Println(lengthOfLastWord("luffy is still joyboy"))
}
