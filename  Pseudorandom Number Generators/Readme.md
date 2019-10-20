# Pseudorandom Number Generators

## Como as bibliotecas criptográficas podem gerar entropia para o gerador de números aleatórios.

Eles permitem acesso aos ruídos do ambiente coletados de controladores de dispositivos e outras fontes, desta forma acessam funções de hardware sem precisar saber detalhes precisos sobre o hardware que está sendo usado  e obtem valores para gerar os valores pseudoaleatorio. Em sistemas linux o ```/dev/random (responsavel por gerar pseudorandom)``` normalmente bloqueia se houver menos entropia disponível do que o solicitado.