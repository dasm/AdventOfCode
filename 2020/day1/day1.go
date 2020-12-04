package main

import (
    "bufio"
    "fmt"
    "os"
    "sort"
    "strconv"
)

func main() {
    file, err := os.Open("input")
    if err != nil {
	fmt.Println("File reading error", err)
	return
    }
    defer file.Close()

    array := []int{}

    // NOTE: How to convert string file to list of ints?
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
	lineStr := scanner.Text()
	num, _ := strconv.Atoi(lineStr)
	array = append(array, num)
    }

    sort.Ints(array)

    start := 0
    end := len(array) - 1
    for start < end {
	sum := array[start] + array[end]
	result := array[start] * array[end]
	if sum == 2020 {
	    fmt.Println(result)
	    return
	} else if sum < 2020 {
	    start++
	} else {
	    end--
	}
    }
}
