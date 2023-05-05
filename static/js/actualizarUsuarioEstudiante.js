carnet = document.getElementById('id_carnet');
usuario = document.getElementById('usuario');
carnet.oninput = () => {
    usuario.innerHTML = carnet.value
};