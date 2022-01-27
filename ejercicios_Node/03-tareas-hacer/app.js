require('colors');
const { guardarDB, leerDB } = require('./helper/guardarArchivo');
const 
{ 
    inquirerMenu, 
    pausa, 
    leerInput, 
    listadoTareasBorrar,
    confirmar,
    mostrarListadoChecklist
} = require('./helper/inquirer');
const Tareas = require('./models/tareas');


const main = async () => 
{
    let opt = "";
    const tareas = new Tareas();
    const tareasDB = leerDB();

    if (tareasDB) {
        tareas.cargarTareasFromArray(tareasDB);
    }

    do {
        opt = await inquirerMenu();

        switch (opt) {
            case '1': //crear opcion
                const desc = await leerInput('Descripcion:');
                tareas.crearTarea( desc );
            break;
            case '2': //Listar todas
                tareas.listadoCompleto();
            break;
            case '3': //Listar completadas
                tareas.listarPendientesCompletadas(true);
            break;
            case '4': //Listar pendientes
                tareas.listarPendientesCompletadas(false);
            break;
            case '5': //Checklist
                const ids = await mostrarListadoChecklist( tareas.listadoArr );
                tareas.toggleCompletadas(ids);
            break;
            case '6': //Borrar tareas
                const id = await listadoTareasBorrar( tareas.listadoArr);
                if (id !== '0') {
                    const ok = await confirmar('¿Esta seguro?')
                    if (ok) {
                        tareas.borrarTarea( id );
                        console.log('Tarea borrada');
                    }
                }
            break;

        }
        guardarDB( tareas.listadoArr )

        await pausa();
    } while(opt !== "0");


}
main();