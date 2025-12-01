package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"time"
)

func main() {
	start := time.Now()
	file, err := os.Open("bigboy.txt")
	if err != nil {
		fmt.Println(err)
	}
	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	pointer := 50
	count := 0
	for _, line := range lines {
		value, _ := strconv.Atoi(line[1:])
		if line[0] == 'L' {
			value = value * -1
		}
		pointer = (pointer + value) % 100
		if pointer == 0 {
			count++
		}
	}
	fmt.Println(count)

	pointer = 50
	count2 := 0
	for _, line := range lines {
		value, _ := strconv.Atoi(line[1:])
		sign := 1
		if line[0] == 'L' {
			sign = -1
		}
		for range value {
			pointer = (pointer + sign) % 100
			if pointer == 0 {
				count2++
			}
		}
		if pointer == 0 {
			count2++
		}
	}
	fmt.Println(count2)
	fmt.Println("Execution time:", time.Since(start).Seconds())
}
