package main

import "fmt"

// defer : USO -> cerrar archivos, conexiones, liberar recursos,
// controladores de consultas a la base de datos

// Encuentra la función y la agrega a la pila o stack
// cuando termina el main, se ejecutan las funciones desde la última a
// la primera agregada
//
//	fmt.Println(2)
//	fmt.Println(3)
//	fmt.Println(1)
func main() {
	/*	defer fmt.Println(3)
		defer fmt.Println(2)
		defer fmt.Println(1)*/

	// cuando se asignó el valor 5 a a, se aplazó su ejecución
	// gracias al método defer guardándose un snapshot de la variable
	// en el momento de la ejecución del defer
	a := 5
	defer fmt.Println("Defer:", a)
	a = 10
	fmt.Println(a)
}
