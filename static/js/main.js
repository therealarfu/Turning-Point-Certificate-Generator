const messages = [
    "Construímos sistemas, não soluções temporárias. O Turning Point cria estruturas replicáveis, capazes de crescer e se manter, não ações pontuais que desaparecem com o tempo.",
    "Os alunos Turning Point não são apenas “futuros líderes”. Eles são líderes agora. Confiamos responsabilidades reais a estudantes reais, formando protagonismo através de ação, não de discurso.",
    "Vestibular não é barreira: é estratégia. O Turning Point ensina aos estudantes a dominar o vestibular como um sistema, transformando uma prova excludente em uma ferramenta de ascensão acadêmica e social.",
    "O Turning Point está comprometido em desenvolver a próxima geração de líderes, estimulando o pensamento crítico e a resolução de problemas por meio de nosso modelo de ensino único, centrado no aluno.”",
    "Educação que cria mudanças mensuráveis. O Turning Point não existe para inspirar. Existe para transformar resultados acadêmicos, trajetórias e oportunidades de vida de forma concreta.",
]

async function generateCertificate() {
    const name = document.getElementById("name").value;
    const date = document.getElementById("date").value;

    if (!name || !date) {
        alert("Por favor, preencha o nome e a data antes de gerar o certificado.");
        return;
    }

    const formData = new FormData();
    formData.append("name", name);
    formData.append("date", date);

    const response = await fetch("/certificate/", {
        method: "POST",
        body: formData
    });

    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "TURNING POINT-Certificado.pdf";
    a.click();
}

function changeMessage(index) {
    document.getElementById("keyText").textContent = messages[index];
    const dots = document.querySelectorAll(".dot");

    dots.forEach(dot => dot.classList.remove("active"));
    dots[index].classList.add("active");
}