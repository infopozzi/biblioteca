async function Excluir(id) {
    const confirmado = confirm('Tem certeza que deseja excluir este exemplar?');
    if (confirmado) {
        const data = new URLSearchParams();
        data.append('id', id);

        try {
            const response = await fetch('/exemplar/excluirAjax', {
                method: 'POST',
                body: data
            });

            if (response.ok) {
                window.location.href = '/exemplar';
            } else {
                const errorResult = await response.json();
                console.error('Erro ao excluir exemplar:', errorResult.message);
                alert('Ocorreu um erro ao excluir o exemplar.');
            }
        } catch (error) {
            console.error('Erro de rede:', error);
            alert('Erro de conexão. Verifique sua rede.');
        }
    }
}

function addCarrinhoExemplar(titulo, id) {
    alert(`Exemplar "${titulo}" (ID: ${id}) adicionado ao carrinho de empréstimo!`);
}
