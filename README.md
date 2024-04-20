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
- Linguagem: Python
- Framework: Flask
- Banco de Dados: SQLite
- Integração Externa: OMDb API, ViaCEP

## Endpoints

| Rota                              | Métodos  | Endpoint                                 |
|-----------------------------------|----------|------------------------------------------|
| admin.delete_user                 | GET, POST| /admin/delete_user/<int:_id>            |
| admin.home                        | GET      | /admin/                                  |
| admin.login                       | GET, POST| /admin/login                             |
| admin.logout                      | GET      | /admin/logout                            |
| admin.register_movie              | GET, POST| /admin/register                          |
| admin.single_user                 | GET, POST| /admin/single_user/<int:_id>             |
| admin.users                       | GET, POST| /admin/users                             |
| auth.login                        | GET, POST| /auth/login                              |
| auth.logout                       | GET      | /auth/logout                             |
| auth.register                     | GET, POST| /auth/register                           |
| home                              | GET      | /                                        |
| movies.catalog                    | GET, POST| /movies/catalog                          |
| movies.movie_detail               | GET      | /movies/movie_detail/<int:_id>           |
| movies.search                     | GET, POST| /movies/search                           |
| profile.change_password           | GET, POST| /profile/change_password                 |
| profile.change_username_and_birth | GET, POST| /profile/changes                         |
| profile.finish_profile            | GET, POST| /profile/finish_profile                  |
| profile.profile                   | GET      | /profile/me                              |
| static                            | GET      | /static/style.css                        |

## Como Começar
Para começar a usar Moved By Movies, siga estes passos:
- Clonar o Repositório: `git clone https://github.com/seunomeusuario/moved-by-movies-api.git](https://github.com/welli7ngton/moved-by-movies`
- Instalar Dependências: `pip install -r requirements.txt`
- Executar a Aplicação: 
  - `flask --app movedbymovies init-db`
  - `flask --app movedbymovies run`
- Acessar a API: Navegue até http://localhost:5000 em seu navegador web.

## Contribuições
Contribuições são bem-vindas! Por favor, sinta-se à vontade para enviar problemas ou solicitações de pull.

                                        
                                                                    
                                            
                        
                                    
                                        
                    
                  
                      
                                
