// const https = require('https');

const data = [
  {
    "id": 1,
    "especialidad": "odontología",
    "nombre": "Dr. Juan",
    "fecha": "2020-01-01",
    "hora": "08:00"
  },
  {
    "id": 2,
    "especialidad": "odontología",
    "nombre": "Dr. Juan",
    "fecha": "2020-01-01",
    "hora": "9:00"
  },
  {
    "id": 3,
    "especialidad": "odontología",
    "nombre": "Dr. Juan",
    "fecha": "2020-01-01",
    "hora": "10:00"
  },
  {
    "id": 4,
    "especialidad": "odontología",
    "nombre": "Dr. Juan",
    "fecha": "2020-01-01",
    "hora": "11:00"
  },
  {
    "id": 5,
    "especialidad": "odontología",
    "nombre": "Dr. Juan",
    "fecha": "2020-01-01",
    "hora": "12:00"
  },
  {
    "id": 6,
    "especialidad": "odontología",
    "nombre": "Dr. Juan",
    "fecha": "2020-01-01",
    "hora": "13:00"
  },
  {
    "id": 7,
    "especialidad": "odontología",
    "nombre": "Dr. Juan",
    "fecha": "2020-01-01",
    "hora": "14:00"
  },
  {
    "id": 8,
    "especialidad": "odontología",
    "nombre": "Dr. Juan",
    "fecha": "2020-01-01",
    "hora": "15:00"
  },
  {
    "id": 9,
    "especialidad": "odontología",
    "nombre": "Dr. Juan",
    "fecha": "2020-01-01",
    "hora": "16:00"
  },
  {
    "id": 10,
    "especialidad": "odontología",
    "nombre": "Dr. Juan",
    "fecha": "2020-01-01",
    "hora": "17:00"
  },
  {
    "id": 11,
    "especialidad": "medicina",
    "nombre": "Dr. Mario",
    "fecha": "2020-01-01",
    "hora": "08:00"
  },
  {
    "id": 12,
    "especialidad": "medicina",
    "nombre": "Dr. Mario",
    "fecha": "2020-01-01",
    "hora": "9:00"
  },
  {
    "id": 13,
    "especialidad": "medicina",
    "nombre": "Dr. Mario",
    "fecha": "2020-01-01",
    "hora": "10:00"
  },
  {
    "id": 14,
    "especialidad": "medicina",
    "nombre": "Dr. Mario",
    "fecha": "2020-01-01",
    "hora": "11:00"
  },
  {
    "id": 15,
    "especialidad": "medicina",
    "nombre": "Dr. Mario",
    "fecha": "2020-01-01",
    "hora": "12:00"
  },
  {
    "id": 16,
    "especialidad": "medicina",
    "nombre": "Dr. Mario",
    "fecha": "2020-01-01",
    "hora": "13:00"
  },
  {
    "id": 17,
    "especialidad": "medicina",
    "nombre": "Dr. Mario",
    "fecha": "2020-01-01",
    "hora": "14:00"
  },
  {
    "id": 18,
    "especialidad": "medicina",
    "nombre": "Dr. Mario",
    "fecha": "2020-01-01",
    "hora": "15:00"
  },
  {
    "id": 19,
    "especialidad": "medicina",
    "nombre": "Dr. Mario",
    "fecha": "2020-01-01",
    "hora": "16:00"
  },
  {
    "id": 20,
    "especialidad": "medicina",
    "nombre": "Dr. Mario",
    "fecha": "2020-01-01",
    "hora": "17:00"
  },
  {
    "id": 21,
    "especialidad": "optometría",
    "nombre": "Dr. Mario",
    "fecha": "2020-01-01",
    "hora": "8:00"
  },
  {
    "id": 22,
    "especialidad": "optometría",
    "nombre": "Dr. Mario",
    "fecha": "2020-01-01",
    "hora": "9:00"
  },
  {
    "id": 23,
    "especialidad": "optometría",
    "nombre": "Dr. Mario",
    "fecha": "2020-01-01",
    "hora": "10:00"
  },
  {
    "id": 24,
    "especialidad": "optometría",
    "nombre": "Dr. Mario",
    "fecha": "2020-01-01",
    "hora": "11:00"
  },
  {
    "id": 25,
    "especialidad": "optometría",
    "nombre": "Dr. Mario",
    "fecha": "2020-01-01",
    "hora": "12:00"
  },
  {
    "id": 26,
    "especialidad": "optometría",
    "nombre": "Dr. Mario",
    "fecha": "2020-01-01",
    "hora": "13:00"
  },
  {
    "id": 27,
    "especialidad": "optometría",
    "nombre": "Dr. Mario",
    "fecha": "2020-01-01",
    "hora": "14:00"
  },
  {
    "id": 28,
    "especialidad": "optometría",
    "nombre": "Dr. Mario",
    "fecha": "2020-01-01",
    "hora": "15:00"
  },
  {
    "id": 29,
    "especialidad": "optometría",
    "nombre": "Dr. Mario",
    "fecha": "2020-01-01",
    "hora": "16:00"
  },
  {
    "id": 30,
    "especialidad": "optometría",
    "nombre": "Dr. Mario",
    "fecha": "2020-01-01",
    "hora": "16:00"
  }
]

// const obtenerCitasDisponibles = async (
//   especialidad,
//   fecha_inicio,
//   fecha_final
// ) => {
//   https.get('https://api-leo.herokuapp.com/api/medical-appointments/appointments', (resp) => {
//     let data = '';
//     resp.on('data', (chunk) => {
//       data += chunk;
//     });
//     resp.on('end', () => {
//       const response = JSON.parse(data)

//       const resultado = response.filter(
//         (cita) =>
//           cita.especialidad === especialidad &&
//           cita.fecha >= fecha_inicio &&
//           cita.fecha <= fecha_final
//       );
//       console.log(resultado.length)
//       return resultado

//     });
//   })
// };

const obtenerCitasDisponibles = (especialidad, fecha_inicio, fecha_final) => {
  return data.filter(cita =>
    cita.especialidad === especialidad &&
    cita.fecha >= fecha_inicio &&
    cita.fecha <= fecha_final)
}

// obtenerCitasDisponibles("odontología", "2020-01-01", "2020-01-01")

const confirmarCita = (idCita) => {
  return "Cita confirmada satisfactoriamente, desafortunadamente esta es una API fake, por lo cuál no tendrá ningún efecto sobre las citas"
  // let response = await fetch(
  //   "http://api-leo.herokuapp.com/api/medical-appointments/confirm/" + idCita,
  //   {
  //     method: "POST",
  //     headers: {
  //       "Content-Type": "application/json"
  //     },
  //   }
  // )
  // .then(response => response.json())
  // .then(data => console.log(data))

  // https.get('https://api-leo.herokuapp.com/api/medical-appointments/confirm/' + idCita, (resp) => {
  //   let data = '';
  //   resp.on('data', (chunk) => {
  //     data += chunk;
  //   });
  //   resp.on('end', () => {
  //     const response = JSON.parse(data)
  //     return "Cita confirmada satisfactoriamente, desafortunadamente esta es una API fake, por lo cuál no tendrá ningún efecto sobre las citas"
  //   });
  // })
};

//console.log(confirmarCita(8))

module.exports.obtenerCitasDisponibles = obtenerCitasDisponibles;
module.exports.confirmarCita = confirmarCita;
