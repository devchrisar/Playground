package main

import "fmt"

func main() {
	//hello("chris", "arias")
	emoji := "😒"
	change(&emoji)
	fmt.Println(emoji)
}
func change(value *string) {
	*value = "🌵"
}

//func hello(firstName string, lastName string) {
//	fmt.Printf("Hello %s %s\n", firstName, lastName)
//}
