const btnCrearProducto = document.getElementById('btnCrearProducto')
const nombreProducto = document.getElementById('nombreProducto')
const descripcionProducto = document.getElementById('descripcionProducto')

btnCrearProducto.addEventListener('click', (e)=> {
    if(nombreProducto.value === ''){
        alert('El nombre es requerido')
        e.preventDefault()
    }

})