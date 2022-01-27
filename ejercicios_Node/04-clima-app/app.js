require('dotenv').config();
const { leerInput, inquirerMenu, pausa, listarLugares } = require('./helpers/inquirer');
const Busquedas = require('./models/busquedas');

const main = async() => {
    console.clear();
    const busquedas = new Busquedas();
    let opt;
    do {
        opt = await inquirerMenu();

        switch (opt) {
            case 1:
                //Mostrar mensaje
                const termino = await leerInput('Ciudad: ');
                //Buscar los lugares
                const lugares = await busquedas.ciudad( termino )
                // Seleccionar el lugar
                const idSelected = await listarLugares(lugares);
                if ( idSelected === 0 ) continue;
                const lugarSelected =  lugares.find(l => l.id === idSelected)
                // Guardar en DB
                busquedas.agregarHistorial( lugarSelected.nombre )
                //Clima
                const clima = await busquedas.climaLugar(lugarSelected.lat, lugarSelected.lng)
                //Mostrar resultados
                console.clear()
                console.log('\nInformación de la ciudad\n'.green);
                console.log('Ciudad:', lugarSelected.nombre.green );
                console.log('Lat:', lugarSelected.lat );
                console.log('Lng:', lugarSelected.lng );
                console.log('Temp:', clima.temp );
                console.log('Min:', clima.min);
                console.log('Max:', clima.max);
                console.log('Como esta el clima:', clima.desc.green);
                break;
        
            case 2:
                busquedas.historialCapitalization.forEach( (lugar, i) => {
                    const idx = `${i + 1}.`.green;
                    console.log(`${idx} ${lugar}`);
                })
                break;
        }

        if (opt !== 0) await pausa();
    } while (opt !== 0);
    
}

main();