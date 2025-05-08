# Gerador de DataSet
Script para download, tratamento e organização de imagens de rostos para criação de um DataSet a ser utilizado em treinamento para uma Rede Neural reconhecedora de expressões faciais.
As imagens são obtidas do site https://thispersonnotexist.org/, convertidas para a escala de cinza e serão por fim modificadas para se adequarem às expressões utilizadas no modelo.
O presente projeto também faz uso da biblioteca GANimation para poder gerar as expressões faciais.
## Como usar
* Clone o repositório, você pode fazer isso através do comando:<br><code>git clone https://github.com/VYR4L/DataSet-Generator.git</code>
* Instale as dependências:<br><code>pip install -r requirements.txt</code>
* Execute o arquivo <code>main.py</code>
## Sobre o Código da GANimation
Este repositório incorpora uma versão modificada do GANimation, publicado originalmente por A. Pumarola et al., para fins de pesquisa acadêmica e desenvolvimento experimental.

O código da GANimation está localizado na pasta ganimation/, com algumas atualizações e correções para compatibilidade com versões modernas do Python.

Licença da GANimation:
O conteúdo da pasta ganimation/ está licenciado sob Creative Commons BY-NC-SA 4.0.
Você pode reutilizá-lo e modificá-lo para fins não comerciais, desde que atribua os autores originais e compartilhe suas modificações sob a mesma licença.

@article{Pumarola_ijcv2019,
    title={GANimation: One-Shot Anatomically Consistent Facial Animation},
    author={A. Pumarola and A. Agudo and A.M. Martinez and A. Sanfeliu and F. Moreno-Noguer},
    booktitle={International Journal of Computer Vision (IJCV)},
    year={2019}
}