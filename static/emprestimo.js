async function Excluir(id) {
    const confirmar = confirm('Tem certeza que deseja excluir esse item?');

    if (confirmar) {
        const data = new URLSearchParams();
        data.append('id', id);

        try {
            const response = await fetch('/emprestimo/excluirAjax', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: data.toString()
            });

            if (response.ok) {
                const result = await response.json();
                console.log('Empréstimo excluído com sucesso:', result.message); 
                window.location.href = '/emprestimo';
            } else {
                const errorResult = await response.json();
                console.error('Erro ao excluir emprestimo:', errorResult.message);
            }
        } catch (error) {
            console.error('Erro de rede:', error);
        }
    }
}

async function listarExemplares() {

    const select = document.getElementById("idPublicacoes");
    const valor = select.value.split('|');

    const data = new URLSearchParams();
    data.append('id', valor[0]);

    try {
        const response = await fetch('/emprestimo/exemplaresAjax', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: data.toString()
        });

        if (response.ok) {
            const result = await response.json();
            
            debugger
            const select = document.getElementById("idExemplares");

            // limpa antes, para evitar duplicações
            select.innerHTML = "";

            result.exemplares.forEach(ex => {
                dsCondicoes = "Bom estado";
                if (ex.condicoes == 2)
                    dsCondicoes = "Médio estado";
                if (ex.condicoes == 3)
                    dsCondicoes = "Péssimo estado";

                const option = document.createElement("option");
                option.value = ex.id + '|' + valor[1]  + '|' + ex.localizacao  + '|' + dsCondicoes;     
                option.text = "Localização: " + ex.localizacao + "| Status: " + (ex.status == 1? "Disponível":"Indisponível");  
                select.appendChild(option);
            });


    } else {
            const errorResult = await response.json();
            console.error('Erro ao excluir emprestimo:', errorResult.message);
        }
    } catch (error) {
        console.error('Erro de rede:', error);
    }
    
}


function adicionar(){
    const select = document.getElementById("idExemplares");

    // pega o valor
    const valor = select.value.split('|');

    // pega o texto
    //const texto = select.options[select.selectedIndex].text;

    if (valor[0] > 0){
        const tabela = document.querySelector("#tbLivros tbody");

        const tr = document.createElement("tr");

        tr.innerHTML = `
            <td class='col-id'>${valor[0]}</td>
            <td>${valor[1]}</td>
            <td>${valor[2]}</td>
            <td>   
                <a onclick="Excluir(this)" type="button" class="btn btn-danger"> Excluir</a>
            </td>
        `;

        tabela.appendChild(tr);

        document.getElementById("idPublicacoes").selectedIndex = 0;
        
        select.innerHTML = "<option value=''>--Selecione--</option>";
    }    
}

function Excluir(e) {

    const linha = e.closest("tr");
    linha.remove();
}

document.getElementById("formCadastro").addEventListener("submit", function (e) {
    e.preventDefault(); // impede envio imediato

    const tabela = document.querySelector("#tbLivros tbody");
    const ids = [];

    tabela.querySelectorAll("tr").forEach(tr => {

        const id = tr.querySelector(".col-id").textContent;

        ids.push(id);
    });

    if (ids.length == 0){
        alert("É necessário adicionar ao menos um livro para concluir o cadastro de empréstimo.");
        return;
    }

    document.getElementById('lsLivros').value = ids.join(',');

    this.submit();      // agora envia o form normalmente
});

document.getElementById("formEmprestimo").addEventListener("submit", function (e) {
    e.preventDefault(); 

    window.location.href = '/emprestimo/?cliente=1';

});