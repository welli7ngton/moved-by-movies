# Moved By Movies API
Este repositório contém uma API para simulação de compra de filmes
proporcionando aos usuários uma plataforma para descobrir, comprar
e avaliar filmes. A integração com a OMDb API enriquece a experiência
do usuário, fornecendo informações detalhadas sobre os filmes disponíveis.

# Funcionalidades Principais
Autenticação Segura: Implementação de login seguro com senhas criptografadas para proteger as contas dos usuários.

Compra de Filmes: Possibilidade de adquirir filmes disponíveis para compra.

Avaliação de Filmes: Os usuários podem avaliar os filmes adquiridos para compartilhar suas opiniões.

Catálogo de Filmes: Um extenso catálogo que apresenta uma ampla variedade de filmes para escolher.

Carrinho de Compras: Funcionalidade robusta para gerenciar itens selecionados para compra.

Promoções Especiais: Ofertas exclusivas e promoções para proporcionar aos usuários uma experiência ainda mais gratificante.

Painel Administrativo: Interface de administração para gerenciar preços, ofertas, banco de dados, saldos e vale-presentes.

Interface Amigável: Design intuitivo e fácil de usar para uma navegação tranquila.

Código Limpo: Desenvolvimento seguindo as melhores práticas para garantir um código de alta qualidade.

Implantação Eficiente: Preparação para implantação da API em um ambiente de produção.

# Tecnologias Utilizadas
Linguagem: Python

Framework: Flask

Banco de Dados: SQLite

Integração Externa: OMDb API, ViaCEP

# Endpoints

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



                                        
                                                                    
                                            
                        
                                    
                                        
                    
                  
                      
                                
