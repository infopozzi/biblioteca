async function Excluir(id){
    const excluir = confirm('Tem certeza que deseja excluir esse usuário?');

    if (excluir) {
        const data = new URLSearchParams();
        data.append('id', id);

        try {
            const response = await fetch('/usuario/excluirAjax', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: data.toString()
            });

            if (response.ok) {
                const result = await response.json();
                console.log('Usuário excluído com sucesso:', result.message);
                window.location.href = '/usuario';
            } else {
                const errorResult = await response.json().catch(() => ({ message: response.statusText }));
                console.error('Erro ao excluir usuário:', errorResult.message);
                alert('Erro ao excluir usuário: ' + (errorResult.message || response.statusText));
            }
        } catch (error) {
            console.error('Erro de rede:', error);
            alert('Erro de rede ao excluir usuário.');
        }
    }
}