var formLogin = document.getElementById('login');

formLogin.onsubmit = function(event){
    event.preventDefault();

    var formulario = new FormData(formLogin);

    fetch('/login', {method: 'POST', body: formulario})
        .then(Response => Response.json())
        .then(data=>{
            if (data.message=="validado"){
                window.location.href = "/bienvenido"
            }

            var mensajeAlerta = document.getElementById('mensajeLogin');
            mensajeAlerta.innerHTML = data.message;
            mensajeAlerta.classList.add("alert");
            mensajeAlerta.classList.add("alert-danger");

        });
}