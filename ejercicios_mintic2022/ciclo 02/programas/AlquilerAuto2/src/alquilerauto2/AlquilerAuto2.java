/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package alquilerauto2;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Arrays;
import java.util.Scanner;
/**
 *
 * @author chris
 */
public class AlquilerAuto2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Alquiler[] historialAlquiler = new Alquiler[5];
        Cliente cliente_1 = new Cliente("Cliente1",25,"Jose Manuel Raigoza");
        Cliente cliente_2 = new Cliente("Cliente2",40,"Sandra Gonzales");
        Cliente cliente_3 = new Cliente("Cliente3",25,"Marcos Perez");
        Auto auto_1 = new Auto("DBZ645",2,true);
        
        Alquiler alquiler_1 = new Alquiler(cliente_1,auto_1,LocalDate.parse("12/06/2021",DateTimeFormatter.ofPattern("d/M/yyyy")),48);
        Alquiler alquiler_2 = new Alquiler(cliente_2,auto_1,LocalDate.parse("12/07/2021",DateTimeFormatter.ofPattern("d/M/yyyy")),30);
        Alquiler alquiler_3 = new Alquiler(cliente_1,auto_1,LocalDate.parse("14/07/2021",DateTimeFormatter.ofPattern("d/M/yyyy")),25);
        Alquiler alquiler_4 = new Alquiler(cliente_3,auto_1,LocalDate.parse("14/07/2021",DateTimeFormatter.ofPattern("d/M/yyyy")),12);
        Alquiler alquiler_5 = new Alquiler(cliente_1,auto_1,LocalDate.parse("16/07/2021",DateTimeFormatter.ofPattern("d/M/yyyy")),8);
        
        historialAlquiler[0] = alquiler_1;
        historialAlquiler[1] = alquiler_2;
        historialAlquiler[2] = alquiler_3;
        historialAlquiler[3] = alquiler_4;
        historialAlquiler[4] = alquiler_5;
        
        Cliente clienteActual_1 = cliente_1;
        Auto  autoActual_1 = auto_1;
        LocalDate fechaActual = LocalDate.parse("19/08/2021",DateTimeFormatter.ofPattern("d/M/yyy"));
        int horasAlquilerActual = 8;
        Alquiler alquilerActual = new Alquiler(clienteActual_1,autoActual_1, fechaActual,horasAlquilerActual);
        int descuento = alquilerActual.ObtenerDescuento(historialAlquiler);
        System.out.println(descuento);
        
        System.out.println("Segundo caso de prueba");
        fechaActual = LocalDate.parse("19/07/2021",DateTimeFormatter.ofPattern("d/M/yyy"));
        auto_1 = new Auto("DBZ645",2,false);
        autoActual_1 = auto_1;
        alquilerActual = new Alquiler(clienteActual_1,autoActual_1, fechaActual, horasAlquilerActual);
        descuento = alquilerActual.ObtenerDescuento(historialAlquiler);
        System.out.println(descuento);
        
        System.out.println("Tercer caso de prueba");
        fechaActual = LocalDate.parse("19/07/2021",DateTimeFormatter.ofPattern("d/M/yyy"));
        auto_1 = new Auto("DBZ645",2,true);
        horasAlquilerActual = 26;
        autoActual_1 = auto_1;
        alquilerActual = new Alquiler(clienteActual_1,autoActual_1, fechaActual, horasAlquilerActual);
        descuento = alquilerActual.ObtenerDescuento(historialAlquiler);
        System.out.println(descuento);
        
        System.out.println("Cuarto caso de prueba");
        fechaActual = LocalDate.parse("19/07/2021",DateTimeFormatter.ofPattern("d/M/yyy"));
        System.out.println("la fecha es: " + fechaActual);
        auto_1 = new Auto("DBZ645",2,true);
        horasAlquilerActual = 12;
        autoActual_1 = auto_1;
        alquilerActual = new Alquiler(clienteActual_1,autoActual_1, fechaActual, horasAlquilerActual);
        descuento = alquilerActual.ObtenerDescuento(historialAlquiler);
        System.out.println(descuento);
    }
    
}
