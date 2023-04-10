package main

import (
	"ejercicios_go/routines01/routines"
	"fmt"
)

/*
	func main() {
		go routines.MiNombrelentoo("Christopher Arias")

		fmt.Println("estoy aqui")
		var x string
		fmt.Scanln(&x)
	}
*/
func main() {
	canal1 := make(chan bool)
	go routines.MiNombrelentoo("Christopher Arias", canal1)
	fmt.Println("estoy aqui")

	//<-canal1
	defer func() {
		<-canal1
	}()
}
