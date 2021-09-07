/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package alquilerauto;
import java.util.Scanner;
/**
 *
 * @author chris
 */
public class Auto {
    private String Placa;
    private int DiasDesdeUltimoMantenimiento;
    private boolean TieneSeguro;
    
    public boolean NecesitaMantenimiento(){
        return DiasDesdeUltimoMantenimiento > 20;
    }
    public boolean SePuedeRentar(){
        if(DiasDesdeUltimoMantenimiento <= 20 && TieneSeguro == true){
            return true;
        }else{
            return false;
        }
    }
    public void leerAuto(){
        Scanner dato = new Scanner(System.in);
        System.out.println("Digite la placa del auto: ");
        Placa = dato.nextLine();
        Scanner dato2 = new Scanner(System.in);
        System.out.println("Por favor indique cuantos dias han pasado desde el ultimo mantenimiento:  ");
        DiasDesdeUltimoMantenimiento = dato2.nextInt();
        System.out.println("Por favor indique si el vehiculo cuenta con seguro true/false de lo contrario se tomara como negativo:  ");
        TieneSeguro = dato.nextBoolean();
    }
}
