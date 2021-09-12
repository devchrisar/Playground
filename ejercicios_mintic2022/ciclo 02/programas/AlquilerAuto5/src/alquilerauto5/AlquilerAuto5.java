/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package alquilerauto5;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Arrays;
import java.util.Scanner;
/**
 *
 * @author chris
 */
public class AlquilerAuto5 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Cliente cliente_1 = new Cliente("1015143634",23,"Juan");
        
        Cliente cliente_historial_1 = new Cliente("1015143634",23,"Juan");
        Cliente cliente_historial_2 = new Cliente("1364726437",33,"Mateo");
        Cliente cliente_historial_3 = new Cliente("9685432432",43,"Ana");
        Cliente cliente_historial_4 = new Cliente("1015143634",23,"Juan");
        Cliente cliente_historial_5 = new Cliente("4567987652",50,"Alfredo");
        Cliente cliente_historial_6 = new Cliente("5468978655",58,"Gloria");
        Cliente cliente_historial_7 = new Cliente("1015143634",23,"Juan");
        Auto auto_1 = new Auto("DBZ645",2,true);
        
        Alquiler[] historial = new Alquiler[7];
        historial[0] = new Alquiler(cliente_historial_1,auto_1,LocalDate.parse("2021-02-14"),3);
        historial[1] = new Alquiler(cliente_historial_2,auto_1,LocalDate.parse("2021-02-15"),2);
        historial[2] = new Alquiler(cliente_historial_3,auto_1,LocalDate.parse("2021-02-16"),2);
        historial[3] = new Alquiler(cliente_historial_4,auto_1,LocalDate.parse("2021-02-18"),5);
        historial[4] = new Alquiler(cliente_historial_5,auto_1,LocalDate.parse("2021-02-18"),2);
        historial[5] = new Alquiler(cliente_historial_6,auto_1,LocalDate.parse("2021-03-15"),8);
        historial[6] = new Alquiler(cliente_historial_7,auto_1,LocalDate.parse("2021-03-20"),2);
        
        boolean puedeAlquilar = Alquiler.PuedeAlquilar(historial, cliente_1);
        System.out.println("1° CASO DE PRUEBA");
        System.out.println(puedeAlquilar);
        
        cliente_historial_1 = new Cliente("9078968512",58,"Camila");
        cliente_historial_2 = new Cliente("1364726437",33,"Mateo");
        cliente_historial_3 = new Cliente("9685432432",43,"Ana");
        cliente_historial_4 = new Cliente("847534654",38,"Liliana");
        cliente_historial_5 = new Cliente("4567987652",50,"Alfredo");
        cliente_historial_6 = new Cliente("5468978655",58,"Gloria");
        cliente_historial_7 = new Cliente("0896756443",23,"Mario");

        historial[0] = new Alquiler(cliente_historial_1,auto_1,LocalDate.parse("2021-02-14"),3);
        historial[1] = new Alquiler(cliente_historial_2,auto_1,LocalDate.parse("2021-02-15"),2);
        historial[2] = new Alquiler(cliente_historial_3,auto_1,LocalDate.parse("2021-02-16"),2);
        historial[3] = new Alquiler(cliente_historial_4,auto_1,LocalDate.parse("2021-02-18"),5);
        historial[4] = new Alquiler(cliente_historial_5,auto_1,LocalDate.parse("2021-02-18"),2);
        historial[5] = new Alquiler(cliente_historial_6,auto_1,LocalDate.parse("2021-03-15"),8);
        historial[6] = new Alquiler(cliente_historial_7,auto_1,LocalDate.parse("2021-03-20"),2);
        
        puedeAlquilar = Alquiler.PuedeAlquilar(historial, cliente_1);
        System.out.println("2° CASO DE PRUEBA");
        System.out.println(puedeAlquilar);
    }
    
}