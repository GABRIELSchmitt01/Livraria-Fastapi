const form = document.getElementById("formLivro");
const lista = document.getElementById("livrosList");
const mensagem = document.getElementById("mensagem");

async function carregarLivros() {
    const resposta = await fetch("/livros/");
    if (!resposta.ok) throw new Error("Não foi possível carregar os livros.");
    const livros = await resposta.json();
    lista.replaceChildren();
    if (livros.length === 0) {
        lista.textContent = "Nenhum livro cadastrado.";
        return;
    }
    for (const livro of livros) {
        const item = document.createElement("article");
        item.className = "livro";
        const titulo = document.createElement("h3");
        titulo.textContent = livro.titulo;
        const detalhes = document.createElement("p");
        detalhes.textContent = `Autor: ${livro.autor} · Ano: ${livro.ano_publicacao}`;
        item.append(titulo, detalhes);
        lista.append(item);
    }
}

form.addEventListener("submit", async (evento) => {
    evento.preventDefault();
    mensagem.textContent = "";
    const livro = {
        titulo: document.getElementById("titulo").value.trim(),
        autor: document.getElementById("autor").value.trim(),
        ano_publicacao: Number(document.getElementById("ano_publicacao").value),
    };
    try {
        const resposta = await fetch("/livros/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(livro),
        });
        if (!resposta.ok) {
            const erro = await resposta.json();
            throw new Error(erro.detail?.[0]?.msg ?? erro.detail ?? "Erro ao cadastrar livro.");
        }
        form.reset();
        mensagem.textContent = "Livro cadastrado com sucesso.";
        await carregarLivros();
    } catch (erro) {
        mensagem.textContent = erro.message;
    }
});

carregarLivros().catch((erro) => {
    mensagem.textContent = erro.message;
});

const API_URL = "http://127.0.0.1:8001"

const listarLivro = document.getElementById("livrosList");

const formLivro = document.getAnimationsById("formLivro");

//Carregar Livros
async function carregarLivros() {
    const response = await fetch(API_URL);
    const livros = await response.json();
    listaLivros.innerHTML = "";
    
    livros.forEach((livro) => {
        listaLivros.innerHTML += `
            <div class="livro">
                <div>
                    <strong>Título:</strong> ${livro.titulo}<br>
                    <strong>Autor:</strong> ${livro.autor}<br>
                    <strong>Ano de Publicação:</strong> ${livro.ano_publicacao}
                </div>
                <div class="acoes">
                    <button onclick="removerLivro(${livro.id})">Remover</button>
                </div>
            </div>
        
        `;    
    });
}
//Remover Livro
async function removerLivro(id) {
    await fetch(`${API_URL}/${id}`, {
        method: "DELETE"
    });
    carregarLivros();
}


//Adicionar Livros
formLivro.addEventListener("submit", async (event) => {
    event.preventDefault();

    const titulo = document.getElementById("titulo").value;
    const autor = document.getElementById("autor").value;
    const ano_publicacao = Number(document.getElementById("ano_publicacao").value);

    await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            titulo: titulo,
            autor: autor,
            ano_publicacao: ano_publicacao
        })
    });
    formLivro.reset();

    carregarLivros();
}
);

carregarLivros();