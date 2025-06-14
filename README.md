PROJETO DE MANIPULAÇÃO DA API FEEGOW - AGENDAMENTOS
====

### Extração da base agendamentos da [API feegow](https://staging-docs.feegow.com/#9b9c5165-c3ba-4b27-8485-f747bfcdc0fc)

<br>


<details close>
<summary><strong>CONFIGURAÇÃO DO PROJETO</strong></summary>

## Criando Esttrutura

<br>

- *Criar projeto:*
    ```sh
    poetry add prj_agenda
    ```
    <br>

- *Definir versão Python do Projeto:*
    ```sh
    poetry env use 3.11.5
    ```
    <br>

- *Ativando ambiente virtual:*
    ```sh
    source ./.venv/bin/activate
    ```

    <br>

## Instalação das Dependências:

<br>

- *Instalar dependências:*
    ```sh
    poetry add psycopg2-binary dlt
    ```

    <br>


## SSH

<br>

- *Gerando uma Chave SSH no Windows:*
    ```sh
    ssh-keygen -t rsa -f $env:user/meu.usuario/.ssh/pasta_da_chave -C "nome_da_chave"
    ```

<br>

- *Copiando a Chave Pública:*
    ```sh
    # no bash
    cat .ssh/dwlinux.pub
    ```
<br>

- *Iniciar Versionamento git local:*
    ```sh
    git init
    ```
<br>

- *[Configurando SSH no Github](https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?platform=linux#adding-a-new-ssh-key-to-your-account)*

<br>

## git local:


<br>

- *Alterar nome da Branch principal:*
    ```sh
    git branch -M main
    ```

<br>

- *Vincular repositório remoto:*
    ```sh
    git remote add origin git@github.com:seu-repository/feegow_agendamentos.git
    ```
<br>

- *Primmeiro Commit:*
    ```sh
    git add README.md
    git commit -m"Primeiro commit"
    git push -U origin main
    ```
<br>

---

<br>

### Configuração Projeto Astro:

- *Criando Projeto Astro:*
    ```sh
    astro dev init
    ```
<br>

- *Iniciando Projeto Astro:*
    ```sh
    astro dev start
    ```

</details>

<br>




