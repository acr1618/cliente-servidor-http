# Cliente/servidor HTTP

Trabalho prático da disciplina _Redes de Computadores_ parte do curso de graduação em Ciência da Computação da UFSJ. A proposta do trabalho é a codificação de um navegador modo texto e de um servidor web. 
O objetivo é entender uso de socket e do método get do _HTTP_

**Aluno:** [Allyson da Cruz Rodrigues]
**Professor:** [Dr. Flávio Luiz Schiavoni]


### Navegador
O programa se conecta ao sevidor e realiza uma requisção de um arquivo (_GET_). Caso seja encontrado, ele salva este arquivo na sua pasta raiz. A porta 80 é utilizada como padrão caso o argumento não seja passado.

```sh
$ ./ernesto.py enderecodo_arquivo porta
```
### Servidor
Responde a requisições _GET_, devolvendo a mensagem de status da requisao 200 OK ou 404 - Not found.
A porta 80 é utilizada como padrão caso o argumento não seja passado.

```sh
$ python3 servidor.py diretorio porta
```

## Licença
Este trabalho é licenciado pela licença [![wtfpl](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-2.png)](http://www.wtfpl.net/about/)


    
