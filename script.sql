create database fastfood;
use fastfood;

create table produto (
    id int auto_increment primary key,
    nomeProduto varchar(255) not null,
    descricaoProduto varchar(255) not null,
    imagemProduto VARCHAR(255)not null
);
