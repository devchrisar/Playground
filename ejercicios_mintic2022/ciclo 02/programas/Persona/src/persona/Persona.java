/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package persona;

/**
 *
 * @author chris
 */
public class Persona {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        String primerNombre="Christopher Henry";
        String primerApellido="Arias Arcia";
        int edad=21;
        String profession="estudiante";
        String genero="Masculino";
        int id=1140426842;
        String Mensaje="Nombre: "+primerNombre+ " "+primerApellido;
        System.out.println(Mensaje);
        System.out.println("Cedula: "+id);
        System.out.println("Edad: "+edad);
        System.out.println("Profesion: "+profession);
        System.out.println("Genero: "+genero);
        
        if(edad >=18){
            System.out.println("Es mayor de edad");
        }
        else{
            System.out.println("Es menor de edad");
        }

    }
    
}
