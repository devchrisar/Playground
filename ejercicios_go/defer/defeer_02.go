package main

import (
	"fmt"
	"os"
)

func main() {
	file, err := os.Create("test.txt")
	if err != nil {
		fmt.Printf("Ocurrió un error al crear el archivo: %v\n", err)
		return
	}
	defer file.Close()

	_, err = file.Write([]byte("Hola Chris"))
	if err != nil {
		fmt.Printf("Ocurrió un error al escribir el archivo: %v\n", err)
		return
	}
}
