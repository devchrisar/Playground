const GetUserById = (id,callback) => {
    const user = {
        id,
        nombre: 'Christopher',
    }
    setTimeout(() => { callback(user) },1500)
}
GetUserById(5,(user) => {
    console.log(user.id) 
    console.log(user.nombre.toUpperCase())
});