package main

import "fmt"

func main() {
	//operadores aritmeticos
	var a = 4 + 2*5
	fmt.Println(a)
	//operadores asignacion
	var b = 10
	b += 5
	fmt.Println(b)
	//decalarion post-incremento ++ y post-decremento --
	var x = 3
	x++
	fmt.Println(x)
	// operadores de comparacion >,<,==,!=,>=,<=
	fmt.Println(4 == 4)
	// operadores logicos &&, ||
	var age = 30
	fmt.Println("edad: ", age >= 18 && age <= 60)
	// unario
	fmt.Println(4 != 4)
}
