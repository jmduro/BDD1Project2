cui = document.getElementById('id_cui');
usuario = document.getElementById('usuario');
cui.oninput = () => {
    usuario.innerHTML = cui.value
};