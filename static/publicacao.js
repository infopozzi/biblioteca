
window.onload = function()
{
    formAutor = document.getElementById('formAutor');
    formAutor.addEventListener('submit', function(e)
    {
        debugger
        e.preventDefault();
    
        salvarAutor();
    });


    formCategoria = document.getElementById('formCategoria');
    formCategoria.addEventListener('submit', function(e)
    {
        debugger
        e.preventDefault();
    
        salvarCategoria();
    });


    formEditora = document.getElementById('formEditora');
    formEditora.addEventListener('submit', function(e)
    {
        debugger
        e.preventDefault();
    
        salvarEditora();
    });
}

async function Excluir(id){
    excluir = confirm('Tem certeza que deseja excluir esse item?');

    if (excluir)
    {
        const data = new URLSearchParams();
        data.append('id', id);

        try {
            const response = await fetch('/publicacao/excluirAjax', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: data.toString()
            });

            debugger
            if (response.ok) {
                const result = await response.json();
                console.log('publicação excluído com sucesso:', result.message); 
                window.location.href = '/publicacao'           
            } else {
                const errorResult = await response.json();
                console.error('Erro ao excluir publicação:', errorResult.message);
            }
        } catch (error) {
            console.error('Erro de rede:', error);
        }
    }
}

async function salvarAutor(){
    const data = new URLSearchParams();
    data.append('id', 0);
    data.append('nome', document.getElementById('nomeAutor').value);

    try {
        const response = await fetch('/autor/cadastroAjax', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: data.toString()
        });

        if (response.ok) {
            const result = await response.json();
            console.log('Autor salvo com sucesso:', result.message);
            console.log('Lista de autores:', result.autores);

            // Limpar o <select> antes de populá-lo novamente
            const select = document.getElementById('idAutor');
            select.innerHTML = "<option value=''> --Selecione-- </option>";

            // Popular o <select> com os novos dados
            result.autores.forEach(autor => {
                const option = document.createElement('option');
                option.value = autor.id;
                option.text = autor.nome;
                select.add(option);

                document.getElementById('nomeAutor').value = '';
                const modalElement = document.getElementById('modalAutor');
                const modalInstance = bootstrap.Modal.getInstance(modalElement);
                modalInstance.hide();
            });
        } else {

            const errorResult = await response.json();
            console.error('Erro ao salvar autor:', errorResult.message);
        }
    } catch (error) {
        console.error('Erro de rede:', error);
    }
}


async function salvarCategoria(){
    const data = new URLSearchParams();
    data.append('id', 0);
    data.append('nome', document.getElementById('nomeCategoria').value);

    try {
        const response = await fetch('/categoria/cadastroAjax', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: data.toString()
        });

        if (response.ok) {
            const result = await response.json();
            console.log('categoria salvo com sucesso:', result.message);
            console.log('Lista de categorias:', result.autores);

            // Limpar o <select> antes de populá-lo novamente
            const select = document.getElementById('idCategoria');
            select.innerHTML = "<option value=''> --Selecione-- </option>";

            // Popular o <select> com os novos dados
            result.autores.forEach(autor => {
                const option = document.createElement('option');
                option.value = autor.id;
                option.text = autor.nome;
                select.add(option);

                document.getElementById('nomeCategoria').value = '';
                const modalElement = document.getElementById('modalCategoria');
                const modalInstance = bootstrap.Modal.getInstance(modalElement);
                modalInstance.hide();
            });
        } else {

            const errorResult = await response.json();
            console.error('Erro ao salvar categoria:', errorResult.message);
        }
    } catch (error) {
        console.error('Erro de rede:', error);
    }
}


async function salvarEditora(){
    const data = new URLSearchParams();
    data.append('id', 0);
    data.append('nome', document.getElementById('nomeEditora').value);

    try {
        const response = await fetch('/editora/cadastroAjax', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: data.toString()
        });

        if (response.ok) {
            const result = await response.json();
            console.log('editora salvo com sucesso:', result.message);
            console.log('Lista de editoras:', result.autores);

            // Limpar o <select> antes de populá-lo novamente
            const select = document.getElementById('idEditora');
            select.innerHTML = "<option value=''> --Selecione-- </option>";

            // Popular o <select> com os novos dados
            result.autores.forEach(autor => {
                const option = document.createElement('option');
                option.value = autor.id;
                option.text = autor.nome;
                select.add(option);

                document.getElementById('nomeEditora').value = '';
                const modalElement = document.getElementById('modalEditora');
                const modalInstance = bootstrap.Modal.getInstance(modalElement);
                modalInstance.hide();
            });
        } else {

            const errorResult = await response.json();
            console.error('Erro ao salvar editora:', errorResult.message);
        }
    } catch (error) {
        console.error('Erro de rede:', error);
    }
}

