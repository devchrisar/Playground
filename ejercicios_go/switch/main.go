package main

import "fmt"

func main() {
	emoji := "cat"
	switch emoji {
	case "cat":
		fmt.Println("es un gato")
	case "dog":
		fmt.Println("es un perro")
	case "banana":
		fmt.Println("es una banana")
	case "manzana":
		fmt.Println("es una manzana")
	default:
		fmt.Println("No es ni un animal ni tampoco una fruta")
	}
}
