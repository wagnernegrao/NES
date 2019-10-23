# Pseudorandom Number Generators

## Como as bibliotecas criptográficas podem gerar entropia para o gerador de números aleatórios.

As bibliotecas utilizam os valores pseudodo aleatórios do sistema como por exemplo ```urandom()``` que obtem os seus valores a partir dos acessos aos ruídos do ambiente coletados de controladores de dispositivos e outras fontes e posteriormente sendo convertido em um número inteiro utilizando o ```int.from_bytes()``` .
