async function Excluir(id){
    excluir = confirm('Tem certeza que deseja excluir esse item?');

    if (excluir)
    {
        const data = new URLSearchParams();
        data.append('id', id);

        try {
            const response = await fetch('/editora/excluirAjax', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: data.toString()
            });

            debugger
            if (response.ok) {
                const result = await response.json();
                console.log('Editora excluída com sucesso:', result.message); 
                window.location.href = '/editora'           
            } else {
                const errorResult = await response.json();
                console.error('Erro ao excluir editora:', errorResult.message);
            }
        } catch (error) {
            console.error('Erro de rede:', error);
        }
    }
}