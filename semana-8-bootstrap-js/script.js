function mostrarAlerta() {
    alert("Hola, soy ERICK ANDERSON SARCHI GONZÁLEZ y esta es mi página interactiva");
}

function validarFormulario() {
    let nombre = document.getElementById("nombre").value.trim();
    let correo = document.getElementById("correo").value.trim();
    let mensaje = document.getElementById("mensaje").value.trim();

    let valido = true;

    document.getElementById("errorNombre").innerText = "";
    document.getElementById("errorCorreo").innerText = "";
    document.getElementById("errorMensaje").innerText = "";

    if (nombre === "") {
        document.getElementById("errorNombre").innerText = "Ingrese su nombre";
        valido = false;
    }

    if (correo === "") {
        document.getElementById("errorCorreo").innerText = "Ingrese su correo electrónico";
        valido = false;
    }

    if (mensaje === "") {
        document.getElementById("errorMensaje").innerText = "Ingrese un mensaje";
        valido = false;
    }

    if (valido) {
        alert("Formulario enviado correctamente");
    }

    return valido;
}
