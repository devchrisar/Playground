package main

import "fmt"

func main() {
	func() {
		fmt.Println("Hola mundo")
	}()
	/*	x := func() {
			fmt.Println("Hola mundo")
		}
		x()*/
}
