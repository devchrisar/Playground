package main

import "fmt"

func main() {
	division(10, 2)
	division(40, 3)
	division(12, 0)
	division(20, 4)
}

func division(dividendo, divisor int) {
	validarDivisor(divisor)
	fmt.Println(dividendo / divisor)
}

func validarDivisor(divisor int) {
	if divisor == 0 {
		panic("No se puede dividir entre cero")
	}
}

/*
	func EjemploPanicConRecover() {
		defer func() {
            reco := recover()
			if reco != nil {
				log.Fatalf("ocurrió un error que generó panic: \n %v", reco)
			}
		}()
		a := 1
        if a == 1 {
          panic("se encontró el valor de uno")
        }
*/
