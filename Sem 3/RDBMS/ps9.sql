create table person
(
  name varchar(30) primary key,
  age number(2) not null, 
  gender varchar(10) not null  
);

insert into person values ('Amy', 16, 'Female');
insert into person values ('Ben', 21, 'Male');
insert into person values ('Cal', 33, 'Male');
insert into person values ('Dan', 13, 'Male');
insert into person values ('Eli', 45, 'Male');
insert into person values ('Fay', 21, 'Female');
insert into person values ('Gus', 24, 'Male');
insert into person values ('Hil', 30, 'Female');
insert into person values ('Ian', 18, 'Male');

create table frequents
(
  name varchar(30),
  pizzeria varchar(30),
  constraint pk primary key (name, pizzeria),
  constraint fk_name foreign key (name) references person(name)
);

insert into frequents values ('Amy', 'Pizza Hut');
insert into frequents values ('Ben', 'Chicago Pizza');
insert into frequents values ('Ben', 'Pizza Hut');
insert into frequents values ('Cal', 'New York Pizza');
insert into frequents values ('Cal', 'Straw Hut');
insert into frequents values ('Dan', 'New York Pizza');
insert into frequents values ('Dan', 'Straw Hut');
insert into frequents values ('Fay', 'Dominos');
insert into frequents values ('Fay', 'Little Caesars');
insert into frequents values ('Gus', 'Chicago Pizza');
insert into frequents values ('Gus', 'Pizza Hut');
insert into frequents values ('Hil', 'Dominos');
insert into frequents values ('Hil', 'Pizza Hut');
insert into frequents values ('Hil', 'Straw Hut');
insert into frequents values ('Ian', 'Dominos');
insert into frequents values ('Ian', 'New York Pizza');
insert into frequents values ('Ian', 'Straw Hut');

create table eats 
(
  name varchar (30),
  pizza varchar(30)
  constraint pk primary key (name, pizza),
  constraint fk_name foreign key (name) references person(name)
);
