async function Excluir(id) {
    const confirmar = confirm('Tem certeza que deseja excluir esse item?');

    if (confirmar) {
        const data = new URLSearchParams();
        data.append('id', id);

        try {
            const response = await fetch('/autor/excluirAjax', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: data.toString()
            });

            if (response.ok) {
                const result = await response.json();
                console.log('Autor excluído com sucesso:', result.message); 
                window.location.href = '/autor';
            } else {
                const errorResult = await response.json();
                console.error('Erro ao excluir autor:', errorResult.message);
            }
        } catch (error) {
            console.error('Erro de rede:', error);
        }
    }
}
