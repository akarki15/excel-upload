drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  url text,
  name text not null, 
  brand text, 
  oprice integer, 
  cprice integer, 
  stock text
);
