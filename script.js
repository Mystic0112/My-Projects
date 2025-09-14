async function buscarCEP() {
    const cepInput = document.getElementById('cep').value;
    const resultadoDiv = document.getElementById('resultado');

    // limpa tela
    resultadoDiv.innerHTML = 'Buscando...';
    
    // remove oq nao for cep
    const cepLimpo = cepInput.replace(/\D/g, ''); 

    // verificador dos 8 digitos
    if (cepLimpo.length !== 8) {
        resultadoDiv.innerHTML = 'CEP inválido. Por favor, digite 8 números.';
        return;
    }

    const url = `https://viacep.com.br/ws/${cepLimpo}/json/`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        if (data.erro) {
            resultadoDiv.innerHTML = 'CEP não encontrado.';
        } else {
            // mostra os dados
            resultadoDiv.innerHTML = `
                <p><strong>Logradouro:</strong> ${data.logradouro}</p>
                <p><strong>Bairro:</strong> ${data.bairro}</p>
                <p><strong>Cidade:</strong> ${data.localidade}</p>
                <p><strong>Estado:</strong> ${data.uf}</p>
            `;
        }
    } catch (error) {
        resultadoDiv.innerHTML = 'Não foi possível buscar o CEP. Tente novamente.';
    }
}