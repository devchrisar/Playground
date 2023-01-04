package main

import "fmt"

// !for clasico
func main() {
	for i := 0; i <= 10; i++ {
		fmt.Println(i)
	}
}

/*
// !for continuo = ciclo while
func main() {
	i := 0
	for ; i <= 10;  {
		fmt.Println(i)
		i++
	}
}
// !for forever = procesos en bucle (sockets, middlewares etc.)
func main() {
	i := 1
	for {
		fmt.Println(i)
		i++
	}
}
// !for range = para iterar arreglos,slices,mapas,strings
func main() {
	nums := []uint8{1, 2, 3,4}
	for i,v := range nums {
		fmt.Println("indice:",i,"valor",v)
	}
}
*/
