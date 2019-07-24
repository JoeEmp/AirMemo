CREATE TABLE Msg (
    id         INTEGER       PRIMARY KEY,
    username   VARCHAR (320) DEFAULT visitor,
    message    VARCHAR (20)  NOT NULL,
    detail     VARCHAR (500),
    color      VARCHAR (10)  DEFAULT c4ffff,
    clouds_key VARCHAR (50),
    is_del     INTEGER       DEFAULT 0,
    del_time   VARCHAR (40)  DEFAULT NULL
);

CREATE TABLE Reminder (
    id       INTEGER       PRIMARY KEY,
    username VARCHAR (320) DEFAULT visitor,
    time     VARCHAR (20),
    sequence INT           DEFAULT (999)
);

CREATE TABLE User (
    id       INTEGER PRIMARY KEY,
    username TEXT    UNIQUE,
    token    TEXT    DEFAULT NULL
);

CREATE TABLE Email_settings (
    id          INTEGER       PRIMARY KEY,
    username    VARCHAR (320) NOT NULL,
    addr        VARCHAR (320) NOT NULL,
    password    VARCHAR (20),
    sender_name VARCHAR (30),
    ssl_port    INTEGER,
    user_ssl    INTEGER       DEFAULT (0),
    is_default  INTEGER       DEFAULT (0)
);

insert into User(username) values ('visitor');
insert into Msg(username, message, detail) values ('visitor','Welcome use AirMemo','Thanks you support');
insert into Reminder(time) values ('00:15:00');
insert into Reminder(time) values ('00:30:00');
insert into Reminder(time) values ('01:00:00');