const icono =document.querySelector('.menu-icon');
const enlaces = document.querySelector('.enlaces');
const registrar = document.querySelector('.registrar')
const modal = document.querySelector('.modal')

icono.addEventListener('click', () => {
    enlaces.classList.toggle('verlinks');
});

registrar.addEventListener('click', () => {
    modal.style.display = 'block'
})

/*
const formularioUser = document.querySelector('#formularioUsuario');

formularioUser.addEventListener('submit', async e => {
    e.preventDefault();
    
    const nombre = formularioUser['nombre'].value;
    const apellidoP = formularioUser['apellidoP'].value;
    const apellidoM = formularioUser['apellidoM'].value;
    const email = formularioUser['email'].value;

    const response = await fetch('/api/user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nombre,
            apellidoP,
            apellidoM,
            email
        })
    }).then(res => {
        if (!res.ok){
            throw Error(res.statusText);
        }
        return res.json;
    })
    .then(data => {
        console.log(data);
    })
    .catch(error => console.error('Error:', error));

    const data = await response.json();
    console.log(data);


    formularioUser.reset();
})
*/
// Obtener una referencia al formulario y a los elementos de formulario
const form = document.getElementById('formularioUsuario');
const nombre = document.getElementById('nombre').value;
const apellidoPaterno = document.getElementById('apellidoP').value;
const apellidoMaterno = document.getElementById('apellidoM').value;
const email = document.getElementById('email').value;

// Crear un objeto FormData y agregar los datos del formulario
const formData = new FormData();
formData.append('nombre', nombre);
formData.append('apellidoPaterno', apellidoPaterno);
formData.append('apellidoMaterno', apellidoMaterno);
formData.append('email', email);

// Enviar los datos al backend utilizando la Fetch API
fetch('/api/user', {
    method: 'POST',
    body: formData
  }).then(response => {
    if (response.ok) {
      return response.json();
    }
    throw new Error('Ocurrió un error al enviar los datos del formulario');
  }).then(data => {
    console.log(data);
  })
    