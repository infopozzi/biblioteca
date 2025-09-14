async function Excluir(id){
    const excluir = confirm('Tem certeza que deseja excluir esse item?');

    if (excluir) {
        const data = new URLSearchParams();
        data.append('id', id);

        try {
            const response = await fetch('/categoria/excluirAjax', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: data.toString()
            });

            debugger
            if (response.ok) {
                const result = await response.json();
                console.log('Categoria excluída com sucesso:', result.message); 
                window.location.href = '/categoria'           
            } else {
                const errorResult = await response.json();
                console.error('Erro ao excluir categoria:', errorResult.message);
            }
        } catch (error) {
            console.error('Erro de rede:', error);
        }
    }
}