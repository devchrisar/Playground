/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package alquilerauto;


/**
 *
 * @author chris
 */
public class AlquilerAuto {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Auto auto1 = new Auto();
        auto1.leerAuto();
        boolean mantenimiento = auto1.NecesitaMantenimiento();
        System.out.println("¿ auto 1 Necesita mantenimiento?:  " + mantenimiento);
        
         Auto auto2 = new Auto();
        auto2.leerAuto();
        boolean rentar = auto2.SePuedeRentar();
        System.out.println("¿auto 2 Se puede rentar?:  " + rentar);
        
         Auto auto3 = new Auto();
        auto3.leerAuto();
        rentar = auto3.SePuedeRentar();
        System.out.println("¿auto 3 Se puede rentar?:  " + rentar);
        
        rentar = auto1.SePuedeRentar();
        System.out.println("¿auto 1 Se puede rentar?:   "+ rentar);
    }
    
}
