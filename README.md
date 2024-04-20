# Moved By Movies
Bem-vindo ao repositório da API Moved By Movies! Esta API simula o processo de compra de filmes, fornecendo aos usuários uma plataforma para descobrir, comprar e avaliar filmes. Integrada com a API OMDb, enriquece a experiência do usuário oferecendo informações detalhadas sobre os filmes disponíveis.

## Principais Recursos
- Autenticação Segura: Implementação de login seguro com senhas criptografadas para proteger as contas dos usuários.
- Compra de Filmes: Capacidade de adquirir filmes disponíveis.
- Avaliação de Filmes: Os usuários podem avaliar os filmes adquiridos para compartilhar suas opiniões.
- Catálogo de Filmes: Um catálogo extenso apresentando uma ampla variedade de filmes para escolher.
- Carrinho de Compras: Funcionalidade robusta para gerenciar itens selecionados para compra.
- Promoções Especiais: Ofertas exclusivas e promoções para proporcionar aos usuários uma experiência ainda mais gratificante.
- Painel Administrativo: Interface de administração para gerenciar preços, ofertas, banco de dados, saldos e vale-presentes.
- Interface Amigável: Design intuitivo e fácil de usar para uma navegação tranquila.
- Código Limpo: Desenvolvimento seguindo as melhores práticas para garantir um código de alta qualidade.
- Implantação Eficiente: Preparação para implantar a API em um ambiente de produção.

## Tecnologias Utilizadas
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

## Time spent:
[![wakatime](https://wakatime.com/badge/github/welli7ngton/moved-by-movies.svg)](https://wakatime.com/badge/github/welli7ngton/moved-by-movies)

## APIS implementadas:
  - OMDB API:`https://www.omdbapi.com/`
  - ViaCEP:`https://viacep.com.br/`

## Endpoints

| Endpoint                           | Methods    | Rule                            | Descrição                                           |
|----------------------------------- | --------- | ------------------------------- | -----------------------------------------------------|
| admin.delete_user                  | GET, POST | /admin/delete_user/<int:_id>   | Deleta um usuário específico pelo ID (admin apenas) |
| admin.home                         | GET       | /admin/                         | Página inicial do painel administrativo            |
| admin.login                        | GET, POST | /admin/login                    | Página de login do administrador                    |
| admin.logout                       | GET       | /admin/logout                   | Logout do administrador                             |
| admin.register_movie               | GET, POST | /admin/register                 | Página de registro do filme (admin apenas)          |
| admin.single_user                  | GET, POST | /admin/single_user/<int:_id>    | Visualiza ou atualiza detalhes de um usuário (admin)|
| admin.users                        | GET, POST | /admin/users                    | Lista todos os usuários (admin apenas)             |
| auth.login                         | GET, POST | /auth/login                     | Página de login do usuário                          |
| auth.logout                        | GET       | /auth/logout                    | Logout do usuário                                   |
| auth.register                      | GET, POST | /auth/register                  | Página de registro do usuário                       |
| cart.add_movie                     | GET       | /cart/add_movie/<int:movie_id>  | Adiciona um filme ao carrinho de compras            |
| cart.buy_credits                   | GET, POST | /cart/buy_credits               | Compra créditos para a conta do usuário            |
| cart.my_cart                       | GET, POST | /cart/my_cart                   | Visualiza o carrinho de compras                    |
| home                               | GET       | /                               | Página inicial                                      |
| movies.catalog                     | GET, POST | /movies/catalog                 | Catálogo de filmes                                  |
| movies.movie_detail                | GET, POST | /movies/movie_detail/<int:_id>  | Detalhes de um filme específico                     |
| movies.my_movies                   | GET       | /movies/my_movies               | Lista de filmes do usuário                          |
| movies.search                      | GET, POST | /movies/search                  | Pesquisa de filmes                                  |
| profile.change_password            | GET, POST | /profile/change_password        | Altera a senha do usuário                           |
| profile.change_username_and_birth  | GET, POST | /profile/changes                | Altera o nome de usuário e a data de nascimento     |
| profile.finish_profile             | GET, POST | /profile/finish_profile         | Finaliza o perfil do usuário                        |
| profile.profile                    | GET       | /profile/me                     | Visualiza o perfil do usuário                       |
| static                             | GET       | /static/style.css         | Serviço de arquivos estáticos (CSS, JS, imagens)    |


## Como Começar
Para começar a usar Moved By Movies, siga estes passos:
- Clonar o Repositório: `git clone https://github.com/seunomeusuario/moved-by-movies-api.git](https://github.com/welli7ngton/moved-by-movies`
- Instalar Dependências: `pip install -r requirements.txt`
- Executar a Aplicação:
  - inicie o banco de dados apenas na primeira vez usando esse comando:
    `flask --app movedbymovies init-db`
  - agora é só rodar o comando abaixo sempre que quiser iniciar a aplicação:
    `flask --app movedbymovies run`
- Acessar a API: Navegue até http://localhost:5000 em seu navegador web.

## Contribuições
Contribuições são bem-vindas! Por favor, sinta-se à vontade para enviar problemas ou solicitações de pull.

                                        
                                                                    
                                            
                        
                                    
                                        
                    
                  
                      
                                
