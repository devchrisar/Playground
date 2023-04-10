package main

import "fmt"

func main() {
	/*	nums := []int{1, 2, 3, 4, 50, 6, 7, 8, 9, 10}
		result := filter(nums, func(num int) bool {
			if num <= 10 {
				return true
			}
			return false
		})
		fmt.Println(result)*/
	x := hello("Chris")()
	fmt.Println(x)
}

func hello(name string) func() string {
	return func() string {
		return "Hello " + name
	}
}

/*func filter(nums []int, callback func(int) bool) []int {
	result := []int{}
	for _, v := range nums {
		if callback(v) {
			result = append(result, v)
		}
	}
	return result
}
*/
