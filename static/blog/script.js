// Função para atualizar o conteúdo do post
function atualizarPost(titulo, conteudo) {
    document.getElementById("post-titulo").innerText = titulo;
    document.getElementById("post-conteudo").innerText = conteudo;
}

document.addEventListener("DOMContentLoaded", function () {
    const accountButton = document.getElementById("accountButton");
    const accountContainer = document.getElementById("accountContainer");
    const overlay = document.getElementById("overlay");

    if (accountButton && accountContainer && overlay) {
        // Abre a janela e o overlay
        accountButton.addEventListener("click", () => {
            accountContainer.classList.toggle("show-account");
            overlay.classList.toggle("show-overlay");
        });

        // Fecha a janela ao clicar no overlay
        overlay.addEventListener("click", () => {
            accountContainer.classList.remove("show-account");
            overlay.classList.remove("show-overlay");
        });
    } else {
        console.error("Elementos não encontrados no DOM.");
    }
});