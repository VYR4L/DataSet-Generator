# Gerador de DataSet
Script para download, tratamento e organização de imagens de rostos para criação de um DataSet a ser utilizado em treinamento para uma Rede Neural reconhecedora de expressões faciais.
As imagens são obtidas do site https://thispersonnotexist.org/, convertidas para a escala de cinza e serão por fim modificadas para se adequarem às expressões utilizadas no modelo.
## Como usar:
* Clone o repositório, você pode fazer isso através do comando:<br><code>git clone https://github.com/VYR4L/DataSet-Generator.git</code>
* Instale as dependências:<br><code>pip install -r requirements.txt</code>
* Execute o arquivo <code>main.py</code>