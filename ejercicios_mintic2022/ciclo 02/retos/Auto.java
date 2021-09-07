public class Auto {
    private String Placa;
    private int DiasDesdeUltimoMantenimiento;
    private boolean TieneSeguro;
    
    public Auto (String Placa,int DiasDesdeUltimoMantenimiento,boolean TieneSeguro){
       this.Placa = Placa;
       this.DiasDesdeUltimoMantenimiento = DiasDesdeUltimoMantenimiento;
       this.TieneSeguro = TieneSeguro;
   }
     boolean NecesitaMantenimiento(){
        return DiasDesdeUltimoMantenimiento > 20;
    };
     boolean SePuedeRentar(){
        if(DiasDesdeUltimoMantenimiento <= 20 && TieneSeguro == true){
            return true;
        }else{
            return false;
        }
    };
};
