package main

import "fmt"

func main() {
	type course struct {
		Name      string
		Professor string
		Country   string
	}
	db := course{
		Name:      "Bases de datos",
		Professor: "Alexander",
		Country:   "Colombia",
	}

	git := course{"Beto", "Esteban", "Canada"}

	fmt.Printf("%+v\n", db)
	fmt.Printf("%+v\n", git)

	/*
	   // punteros

	   	p := &db
	   	(*p).Professor = "Alex" o p.Professor = "Alex"
	   	fmt.Printf("%+v\n", db)
	   	fmt.Printf("%+v\n", p)
	*/

}
