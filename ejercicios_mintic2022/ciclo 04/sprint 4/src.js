const express = require("express");
const app = express();

app.use(express.urlencoded({ extended: false }))
app.use(express.json())



app.get("/api/medical-appointments/apointments", (req, res) => {
    res.status(200).json(appointments);


});

app.post("/api/medical-appointments/confirm/:appointment_id", (req, res) => {
    const { appointment_id } = req.params;


    appointments = appointments.map(appointment => {

        if (appointment.id == appointment_id) {
            appointment.status = "confirmed";
        }
        return appointment;
    })

    res.status(200).json(appointments);

});


module.exports = app;