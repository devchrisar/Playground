package main

import "fmt"

var calculo func(int, int) int = func(num1 int, num2 int) int {
	return num1 + num2
}

func main() {
	fmt.Printf("Sumo 5 + 7 = %d \n	", calculo(5, 7))

	//Resta
	calculo = func(num1 int, num2 int) int {
		return num1 - num2
	}
	fmt.Printf("Resto 6 - 4 = %d \n ", calculo(6, 4))

	//División
	calculo = func(num1 int, num2 int) int {
		return num1 / num2
	}
	fmt.Printf("Divido 12 / 3 = %d \n ", calculo(12, 3))

	//Closures
	tablaDel := 2
	miTabla := Tabla(tablaDel)
	for i := 1; i < 11; i++ {
		fmt.Println(miTabla())
	}
}

func operaciones() {
	resultado := func() int {
		var a int = 23
		var b int = 13
		return a + b
	}
	fmt.Println(resultado())
}

func Tabla(valor int) func() int {
	numero := valor
	secuencia := 0
	return func() int {
		secuencia += 1
		return numero * secuencia
	}
}
