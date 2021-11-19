const obtenerCitasDisponibles=(especialidad,fecha_inicio,fecha_final)=>{
    return CITAS.filter(cita => cita.especialidad === especialidad && cita.fecha >= fecha_inicio && cita.fecha <=fecha_final)
};


const obtenerCitasPorJornada=(especialidad,fecha_inicio,fecha_final,jornadaPreferida)=>{
    //let resultados= obtenerCitasDisponibles(especialidad,fecha_inicio,fecha_final);
    let resultados= obtenerCitasDisponibles(especialidad,fecha_inicio,fecha_final);
     return resultados.filter(cita=>{ let horayminuto=cita.hora.split(":"); let hora=parseInt(horayminuto[0]); if(hora<=12){
     return jornadaPreferida==="mañana"; } if(hora>12){ return jornadaPreferida==="tarde"; } return false; }); 
}
    //return resultados.filter(cita => cita.especialidad === especialidad && cita.fecha >= fecha_inicio && cita.fecha <=fecha_final && ObtenerJornada(jornadaPreferida,cita.hora)==1);






CITAS=[
    {
      especialidad: "odontología",
      nombre: "Dr. Juan",
      fecha: "2021-01-01",
      hora: "08:00",
    },
    {
      especialidad: "medicina",
      nombre: "Dr. Mario",
      fecha: "2020-01-01",
      hora: "15:00",
    },
    {
      especialidad: "optometría",
      nombre: "Dr. Mario",
      fecha: "2020-01-01",
      hora: "16:00",
    }
]

module.exports.obtenerCitasDisponibles= obtenerCitasDisponibles;
module.exports.obtenerCitasPorJornada= obtenerCitasPorJornada;