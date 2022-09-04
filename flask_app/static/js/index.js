var formRegistro = document.getElementById('formRegistro');

formRegistro.onsubmit = function(event){
    event.preventDefault();

    var formulario = new FormData(formRegistro);

    fetch('/registro', {method: 'POST', body: formulario})
        .then(Response => Response.json())
        .then(data=>{
            if (data.message=="validado"){
                window.location.href = "/inicia_sesion"
            }

            var mensajeAlerta = document.getElementById('mensajeAlerta');
            mensajeAlerta.innerHTML = data.message;
            mensajeAlerta.classList.add("alert");
            mensajeAlerta.classList.add("alert-danger");

        });
}

