/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.time.LocalDate;

/**
 *
 * @author chris
 */
public class Alquiler {
    private Cliente Cliente;
    private Auto Auto;
    private LocalDate Fecha;
    private int HorasAlquiler;
    
    public  Alquiler (Cliente cliente,Auto auto,LocalDate fecha,int horasAlquiler) {
        this.Cliente = cliente;
        this.Auto = auto;
        this.Fecha = fecha;
        this.HorasAlquiler = horasAlquiler;
    }
    
    public Cliente getCliente(){
        return Cliente;
    }
    
    public void  setCliente(Cliente Cliente){
         this.Cliente = Cliente;
    }
    
    public Auto getAuto(){
        return Auto;
    }
    
    public void  setAuto(Auto Auto){
         this.Auto = Auto;
    }
    
    public LocalDate getFecha(){
        return Fecha;
    }
    
    public void  setFecha(LocalDate Fecha){
         this.Fecha = Fecha;
    }
    
    public int getHorasAlquiler(){
        return HorasAlquiler;
    }
    
    public void  setHorasAlquiler(int HorasAlquiler){
         this.HorasAlquiler = HorasAlquiler;
    }
    
    public int ObtenerDescuento(Alquiler[] alquileres)
    {
        int descuento;
        if(this.Auto.NecesitaMantenimiento() == true || this.Auto.SePuedeRentar() == false)
        {
            return 0;
        }
        LocalDate fechaActual = this.Fecha;
        LocalDate fechaAnterior = fechaActual.minusDays(30);
        int horasAcumuladas = this.HorasAlquiler;
        for(int i=0; i< alquileres.length; i++)
        {
            if(alquileres[i].getCliente().getCedula().equals(this.Cliente.getCedula())&& alquileres[i].getFecha().compareTo(fechaAnterior) >=0)
            {
                horasAcumuladas = horasAcumuladas + alquileres[i].getHorasAlquiler();
            }
        }
        if(horasAcumuladas < 20)
            {
                return 0;
            }
        else if(horasAcumuladas >=20 && horasAcumuladas <= 50)
        {
            return 2;
        }
        else
        {
            return 5;
        }    
    }
    public double CalcularCosto(boolean aplicaDescuento)
    {
        double costoTotal = this.HorasAlquiler * 5000;
        double descuento = 0;
        if (aplicaDescuento == true)
        {
            descuento = (double)this.HorasAlquiler * 5000 *0.02 ;
        }
        return(costoTotal - descuento);
    }
    public static boolean PuedeAlquilar(Alquiler[] historial, Cliente cliente)
    {
        for(int i=0; i< historial.length; i++)
        {

        }
        return false;
    }
}