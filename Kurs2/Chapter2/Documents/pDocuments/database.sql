create table t_document (
    -- TODO: 1. Сделать возможность сохранения в базе 
    -- TODO:    лополнительных полей.
    --  autoincrement означает, что база данных сама будет управлять идентификатором документа
    --  если мы что-то новое впихиваем в документ база формирует новый id.
    i_id     integer not null primary key autoincrement ,
    f_status integer     null
    f_kind   integer not null -- 1- тип документа (накладная)
);

create table t_nakladnay (
    r_id_document integer not   null primary key references t_document ( i_id ) ,
    f_itogo       numeric(22,2) null 
);

create table t_position (
    i_id           integer   not null primary key autoincrement,
    r_id_nakladnay integer   not null references t_nakladnay( i_id_document ) ,
    f_ordinal      integer   not null ,
    f_title        text          null ,
    f_unit         text          null ,
    f_amount       integer       null ,
    f_price        numeric(33,4) null ,
    f_summa        numeric(22,2) null
);