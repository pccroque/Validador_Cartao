# Objetivo

- Desenvolver uma aplicação simples capaz de identificar a bandeira de um cartão de crédito (como Visa, MasterCard, etc.) com base no número do cartão.

# Desenvolvimento

- Para isso, foi utilizado o GitHub Copilot como assistente de codificação, explorando como a inteligência artificial pode acelerar o desenvolvimento, sugerindo trechos de código e melhorando a produtividade. 
- O script em Python utiliza o algoritmo 'luhn' para validar o número do cartão de crédito desejado.
- Em seguida, identifica a bandeira do cartão de crédito com base no número inicial.
- A imagem 'base.png' foi utilizada como base para gerar os números iniciais de cada bandeira no script. 

# Algoritmo de luhn:

O algoritmo de Luhn é uma técnica amplamente utilizada para validar números de cartões de crédito e outras identificações numéricas.

Principais características:
1. Simplicidade e eficiência,
2. Detecta erros comuns,
3. Uso universal.

Como ele funciona:
- Os dígitos do número do cartão são processados da direita para a esquerda.
- A cada segundo dígito, seu valor é dobrado. Se o resultado for maior que 9, subtrai-se 9.
- Todos os dígitos são somados.
- Se o total for múltiplo de 10, o número do cartão é válido.
