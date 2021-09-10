/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package alquilerauto5;

/**
 *
 * @author chris
 */
public class Auto {
    private String Placa;
    private int DiasDesdeUltimoMantenimiento;
    private boolean TieneSeguro;
    
    public Auto (String Placa,int DiasDesdeUltimoMantenimiento,boolean TieneSeguro){
       this.Placa = Placa;
       this.DiasDesdeUltimoMantenimiento = DiasDesdeUltimoMantenimiento;
       this.TieneSeguro = TieneSeguro;
   }
    public Auto(){
    }
     public boolean NecesitaMantenimiento(){
        return DiasDesdeUltimoMantenimiento > 20;
    };
     public boolean SePuedeRentar(){
        if(DiasDesdeUltimoMantenimiento <= 20 && TieneSeguro == true){
            return true;
        }else{
            return false;
        }
    };
};