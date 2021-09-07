/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pscanner;

/**
 *
 * @author chris
 */
import java.util.Scanner;
public class Pscanner {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int primerNumero;
        int segundoNumero;
        double resultado_suma;
        Scanner in = new Scanner(System.in);
        
        System.out.print("ingrese el primer numero: ");
        primerNumero= in.nextInt();
        
        System.out.print("ingrese el segundo numero: ");
        segundoNumero= in.nextInt();
        
        resultado_suma = primerNumero + segundoNumero;
        System.out.println("El resultado es"+resultado_suma);
    }
    
}
