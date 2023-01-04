package main

import "fmt"

func main() {
	emoji := "🌵"
	if emoji == "🌵" {
		fmt.Println("es un cactus")
	} else if emoji == "😒" {
		fmt.Println("es una carita")
	} else {
		fmt.Printf("el emoji es: %s\n", emoji)
	}
	/*
		//si las variables son declaradas dentro de la condicional su scope solo podra usarse dentro de la misma
			if emoji :== "cat"; emoji == "dog" {}
	*/
}
