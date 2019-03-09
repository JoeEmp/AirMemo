CREATE TABLE Msg (
    id       INTEGER PRIMARY KEY,
    message  TEXT    NOT NULL,
    detail   TEXT,
    user     TEXT    DEFAULT visitor,
    is_del   INTEGER DEFAULT 0,
    del_time TEXT    DEFAULT NULL
);

INSERT INTO  Msg (message,detail) VALUES ('Welcome','Welcome use AirMemo');