const formulario = document.getElementById("formulario");
const inputs = document.querySelectorAll("input");
const botonEnviar = document.getElementById("enviar");

function validarNombre() {
    const nombre = document.getElementById("nombre");
    const error = nombre.nextElementSibling;

    if (nombre.value.length >= 3) {
        nombre.className = "valido";
        error.textContent = "";
        return true;
    } else {
        nombre.className = "invalido";
        error.textContent = "Mínimo 3 caracteres";
        return false;
    }
}

function validarCorreo() {
    const correo = document.getElementById("correo");
    const error = correo.nextElementSibling;
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (regex.test(correo.value)) {
        correo.className = "valido";
        error.textContent = "";
        return true;
    } else {
        correo.className = "invalido";
        error.textContent = "Correo no válido";
        return false;
    }
}

function validarPassword() {
    const pass = document.getElementById("password");
    const error = pass.nextElementSibling;
    const regex = /^(?=.*\d)(?=.*[\W_]).{8,}$/;

    if (regex.test(pass.value)) {
        pass.className = "valido";
        error.textContent = "";
        return true;
    } else {
        pass.className = "invalido";
        error.textContent = "Mín. 8 caracteres, número y símbolo";
        return false;
    }
}

function validarConfirmacion() {
    const pass = document.getElementById("password");
    const conf = document.getElementById("confirmar");
    const error = conf.nextElementSibling;

    if (conf.value === pass.value && conf.value !== "") {
        conf.className = "valido";
        error.textContent = "";
        return true;
    } else {
        conf.className = "invalido";
        error.textContent = "Las contraseñas no coinciden";
        return false;
    }
}

function validarEdad() {
    const edad = document.getElementById("edad");
    const error = edad.nextElementSibling;

    if (edad.value >= 18) {
        edad.className = "valido";
        error.textContent = "";
        return true;
    } else {
        edad.className = "invalido";
        error.textContent = "Debe ser mayor de 18";
        return false;
    }
}

function validarFormulario() {
    if (
        validarNombre() &&
        validarCorreo() &&
        validarPassword() &&
        validarConfirmacion() &&
        validarEdad()
    ) {
        botonEnviar.disabled = false;
    } else {
        botonEnviar.disabled = true;
    }
}

inputs.forEach(input => {
    input.addEventListener("input", validarFormulario);
});

formulario.addEventListener("submit", function (e) {
    e.preventDefault();
    alert("✅ Formulario validado correctamente");
});

