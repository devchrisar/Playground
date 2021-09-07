/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pjoptionpane;

/**
 *
 * @author chris
 */
import javax.swing.JOptionPane;
import java.lang.Math;
public class Pjoptionpane {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int esEntero1;
        int esEntero2;
        String esString;
        double esDouble;
        char esCar;
        double suma;
        double raiz_suma;

esEntero1 = Integer.parseInt(JOptionPane.showInputDialog("Ingresa el primer valor entero: "));

esEntero2 = Integer.parseInt(JOptionPane.showInputDialog("Ingresa el segundo valor entero: "));

esString = JOptionPane.showInputDialog("Ingrese un mensaje para mostrar");

esDouble = Double.parseDouble(JOptionPane.showInputDialog("Ingrese el costo del producto"));

esCar = JOptionPane.showInputDialog("Ingresa un caracter").charAt(0);

suma = esEntero1 + esEntero2;
raiz_suma = Math.sqrt(suma);
JOptionPane.showMessageDialog(null,"Los valores ingresados son:"
+"\nPara el entero 1: "+esEntero1
+ "\nPara el entero 2: "+esEntero2
+ "\nPara el mensaje: "+esString
+ "\nPara el caracter: "+esCar
+"\nPara el costo: "+esDouble
+"\nLa suma de valores es: "+suma
+ "\nLa raiz cuadrada del resultado de la suma es: "+raiz_suma
);
    }
    
    
}
