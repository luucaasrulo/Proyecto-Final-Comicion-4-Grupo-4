const formulario = document.getElementById('formulario');
const inputs= document.querySelectorAll('#formulario input');


const expresiones = {
    nombre: /^[A-Z][a-zA-Z]{2,18}$/,
    apellido: /^[A-Z][a-zA-Z]{2,18}$/,
    fecha: /^\d{4}-\d{1,2}-\d{1,2}$/,
    username: /^[a-zA-Z0-9-]{2,199}$/,
    password: /^(?=.*[a-zA-Z\d])(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$/,
    email: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
};
const validarCampo = (campo, expresion, elementoFormulario) => {
    const valor = campo.value.trim();

    if (expresion.test(valor)) {
        elementoFormulario.classList.remove('formulario-error');
        elementoFormulario.classList.add('formulario-correcto');
        elementoFormulario.querySelector('#icon').classList.remove('fa-circle-xmark');
        elementoFormulario.querySelector('#icon').classList.add('fa-circle-check');
    } else {
        elementoFormulario.classList.remove('formulario-correcto');
        elementoFormulario.classList.add('formulario-error');
        elementoFormulario.querySelector('#icon').classList.remove('fa-circle-check');
        elementoFormulario.querySelector('#icon').classList.add('fa-circle-xmark');
    }
};

const validarFormulario = (e) => {
    switch (e.target.name) {
        case 'nombre':
            validarCampo(e.target, expresiones.nombre, document.getElementById('form_nombre'));
            break;
        case 'apellido':
            validarCampo(e.target, expresiones.apellido, document.getElementById('form_apellido'));
            break;
        case 'fecha_nacimiento':
            validarCampo(e.target, expresiones.fecha, document.getElementById('form_fecha_nacimiento'));
            break;
        case 'username':
            validarCampo(e.target, expresiones.username, document.getElementById('form_username'));
            break;
        case 'password1':
            validarCampo(e.target, expresiones.password, document.getElementById('form_password1'));
            break;
        case 'password2':
            const password1 = document.getElementById('id_password1').value;
            const password2 = e.target.value;
            
            if (password1 === password2) {
                document.getElementById('form_password2').classList.remove('formulario-error');
                document.getElementById('form_password2').classList.add('formulario-correcto');
                document.querySelector('#form_password2 #icon').classList.remove('fa-circle-xmark');
                document.querySelector('#form_password2 #icon').classList.add('fa-circle-check');
            } else {
                document.getElementById('form_password2').classList.remove('formulario-correcto');
                document.getElementById('form_password2').classList.add('formulario-error');
                document.querySelector('#form_password2 #icon').classList.remove('fa-circle-check');
                document.querySelector('#form_password2 #icon').classList.add('fa-circle-xmark');
            }
            break;
        case 'email':
            validarCampo(e.target, expresiones.email, document.getElementById('form_email'));
            break;
    }
};


inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
});


document.getElementById("id_nombre").placeholder = "Nombre";
document.getElementById("id_apellido").placeholder = "Apellido";
document.getElementById("id_fecha_nacimiento").placeholder = "Fecha de nacimiento";
document.getElementById("id_username").placeholder = "Nombre de usuario";
document.getElementById("id_password1").placeholder = "Contraseña";
document.getElementById("id_password2").placeholder = "Repite tu contraseña";
document.getElementById("id_email").placeholder = "Ingresa tu email";

