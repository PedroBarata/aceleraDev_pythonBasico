# Stats API

API Rest feita em Python como estudo do Acelera Dev da Codenation. 

## Installation

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar os packages do projeto.

```bash
pip install flask
pip install jsonify
pip install loguru
pip install requests
pip install pytest
```

## Usage
Primeiro precisamos subir o servidor

```bash
$ python app.py
```
Após isso, podemos realizar as operações do arquivo ```client.py```.

Operações aceitas: 
* min: retorna o valor mínimo da lista;
* max: retorna o valor máximo da lista;
* mean: retorna o valor médio da lista;

```bash
#Cria uma lista e a salva em memória (retorna um UUID)

$ python client.py --send --data "[1,2,3,4]" 

#Com o UUID, podemos fazer consultas
$ python client.py --get --uuid <UUID>

#E operações
$ python client.py --op <op_name> --uuid <UUID>

```


## Tests

```bash
#Para rodar todos os testes
$ pytest tests/

$ pytest -v tests/ #Mais verboso

#Para rodar um teste em específico
$ pytest <nome_do_teste>.py
```

## Task list
* [ ] Verificar se é uma UUID válida ao realizar o método ```GET``` no ``data_store.py``

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.-->

## License
[MIT](https://choosealicense.com/licenses/mit/)