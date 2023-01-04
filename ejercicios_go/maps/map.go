package main

import "fmt"

func main() {
	animals := make(map[string]string)
	animals["cat"] = "😺"
	animals["dog"] = "🐶"

	fmt.Println(animals)

	fruits := map[string]string{
		"apple":  "🍎",
		"banana": "🍌",
	}

	fmt.Println(fruits)
	delete(fruits, "banana")
	fmt.Println(fruits)

	fmt.Println(animals["gorilla"]) // out: 0

	if _, ok := animals["gorilla"]; !ok {
		animals["gorilla"] = "🦍"
	}
	fmt.Println(animals)

}
