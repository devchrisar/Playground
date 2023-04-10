package main

import (
	"ejercicios_go/interfaz01/Models"
	i "ejercicios_go/interfaz01/ejer_interfaces"
)

func main() {
	Chris := new(Models.Hombre)
	i.HumanosRespirando(Chris)
	Maria := new(Models.Mujer)
	i.HumanosRespirando(Maria)
}
