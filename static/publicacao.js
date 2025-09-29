window.onload = function() {
    const formAutor = document.getElementById('formAutor');
    if(formAutor) {
        formAutor.addEventListener('submit', function(e) {
            e.preventDefault();
            salvarAutor();
        });
    }

    const formCategoria = document.getElementById('formCategoria');
    if(formCategoria) {
        formCategoria.addEventListener('submit', function(e) {
            e.preventDefault();
            salvarCategoria();
        });
    }

    const formEditora = document.getElementById('formEditora');
    if(formEditora) {
        formEditora.addEventListener('submit', function(e) {
            e.preventDefault();
            salvarEditora();
        });
    }
}

async function Excluir(id) {
    const confirmado = confirm('Tem certeza que deseja excluir este item?');

    if (confirmado) {
        const data = new URLSearchParams();
        data.append('id', id);

        try {
            const response = await fetch('/publicacao/excluirAjax', {
                method: 'POST',
                body: data
            });

            if (response.ok) {
                window.location.href = '/publicacao';
            } else {
                const errorResult = await response.json();
                console.error('Erro ao excluir publicação:', errorResult.message);
                alert('Ocorreu um erro ao excluir a publicação.');
            }
        } catch (error) {
            console.error('Erro de rede:', error);
            alert('Erro de conexão. Verifique sua rede.');
        }
    }
}

async function salvarAutor() {
    const nomeAutor = document.getElementById('nomeAutor').value;
    if (!nomeAutor) {
        alert('O nome do autor não pode estar vazio.');
        return;
    }

    const data = new URLSearchParams();
    data.append('id', 0);
    data.append('nome', nomeAutor);

    try {
        const response = await fetch('/autor/cadastroAjax', {
            method: 'POST',
            body: data
        });

        if (response.ok) {
            const result = await response.json();
            
            const select = document.getElementById('idAutor');
            select.innerHTML = "<option value=''>--Selecione--</option>";
            result.autores.forEach(autor => {
                const option = document.createElement('option');
                option.value = autor.id;
                option.text = autor.nome;
                select.add(option);
            });

            document.getElementById('nomeAutor').value = '';

            const modalElement = document.getElementById('modalAutor');
            const modalInstance = bootstrap.Modal.getInstance(modalElement);
            modalInstance.hide();
        } else {
            const errorResult = await response.json();
            alert('Erro ao salvar autor: ' + errorResult.message);
        }
    } catch (error) {
        console.error('Erro de rede:', error);
        alert('Erro de conexão ao salvar autor.');
    }
}

async function salvarCategoria() {
    const nomeCategoria = document.getElementById('nomeCategoria').value;
    if (!nomeCategoria) {
        alert('O nome da categoria não pode estar vazio.');
        return;
    }
    
    const data = new URLSearchParams();
    data.append('id', 0);
    data.append('nome', nomeCategoria);

    try {
        const response = await fetch('/categoria/cadastroAjax', {
            method: 'POST',
            body: data
        });

        if (response.ok) {
            const result = await response.json();

            const select = document.getElementById('idCategoria');
            select.innerHTML = "<option value=''>--Selecione--</option>";
            result.categorias.forEach(categoria => {
                const option = document.createElement('option');
                option.value = categoria.id;
                option.text = categoria.nome;
                select.add(option);
            });

            document.getElementById('nomeCategoria').value = '';
            
            const modalElement = document.getElementById('modalCategoria');
            const modalInstance = bootstrap.Modal.getInstance(modalElement);
            modalInstance.hide();
        } else {
            const errorResult = await response.json();
            alert('Erro ao salvar categoria: ' + errorResult.message);
        }
    } catch (error) {
        console.error('Erro de rede:', error);
        alert('Erro de conexão ao salvar categoria.');
    }
}

async function salvarEditora() {
    const nomeEditora = document.getElementById('nomeEditora').value;
    if (!nomeEditora) {
        alert('O nome da editora не pode estar vazio.');
        return;
    }

    const data = new URLSearchParams();
    data.append('id', 0);
    data.append('nome', nomeEditora);

    try {
        const response = await fetch('/editora/cadastroAjax', {
            method: 'POST',
            body: data
        });

        if (response.ok) {
            const result = await response.json();

            const select = document.getElementById('idEditora');
            select.innerHTML = "<option value=''>--Selecione--</option>";
            result.editoras.forEach(editora => {
                const option = document.createElement('option');
                option.value = editora.id;
                option.text = editora.nome;
                select.add(option);
            });

            document.getElementById('nomeEditora').value = '';

            const modalElement = document.getElementById('modalEditora');
            const modalInstance = bootstrap.Modal.getInstance(modalElement);
            modalInstance.hide();
        } else {
            const errorResult = await response.json();
            alert('Erro ao salvar editora: ' + errorResult.message);
        }
    } catch (error) {
        console.error('Erro de rede:', error);
        alert('Erro de conexão ao salvar editora.');
    }
}