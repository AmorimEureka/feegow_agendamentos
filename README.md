PROJETO DE MANIPULAÇÃO DA API FEEGOW - AGENDAMENTOS
====

### Extração da base agendamentos da [API feegow](https://staging-docs.feegow.com/#9b9c5165-c3ba-4b27-8485-f747bfcdc0fc)

<br>


<details open>

<summary><strong>STACKS UTILIZADAS</strong></summary>

<br>

![Python](https://img.shields.io/badge/Python-FFD43B?&logo=python&logoColor=blue)
![Airflow 2.8.0](https://img.shields.io/badge/Airflow-2.8.0-EA1D2C?logo=apache-airflow&logoColor=white)
[![Astro](https://img.shields.io/badge/Astro-Astronomer.io-5A4FCF?logo=Astronomer&logoColor=white)](https://www.astronomer.io/)
[![cosmos version](https://img.shields.io/pypi/v/astronomer-cosmos?label=cosmos&color=purple&logo=apache-airflow)](https://pypi.org/project/astronomer-cosmos/) <br>
![dlt version](https://img.shields.io/pypi/v/dlt?label=dlt&color=blue&logo=python&logoColor=white)
![dbt version](https://img.shields.io/pypi/v/dbt-core?label=dbt-core&color=orange&logo=databricks&logoColor=white)
![Docker Engine](https://img.shields.io/badge/Docker-Engine-2496ED?logo=docker&logoColor=white)
![Ubuntu](https://img.shields.io/badge/OS-Ubuntu-E95420?logo=ubuntu&logoColor=white) <br>
![WSL](https://img.shields.io/badge/WSL-2.0+-brightgreen?logo=windows&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?&logo=postgresql&logoColor=white)
[![DBeaver](https://img.shields.io/badge/DBeaver-Tool-372923?logo=dbeaver&logoColor=white)](https://dbeaver.io/)
[![API Feegow](https://img.shields.io/badge/API-Feegow-blue?logo=fastapi&logoColor=white)](https://documenter.getpostman.com/view/3897235/S1ENwy59)
![Power Bi](https://img.shields.io/badge/power_bi-F2C811?&logo=powerbi&logoColor=black)


</details>

<br>


<details close>
<summary><strong>CONFIGURAÇÃO DO PROJETO</strong></summary>

## Criando Esttrutura


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


- *Instalar dependências:*
    ```sh
    poetry add psycopg2-binary dlt
    ```

    <br>


## SSH


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


## Configuração Projeto Astro:

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




