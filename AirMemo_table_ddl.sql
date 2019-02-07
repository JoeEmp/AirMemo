CREATE TABLE Msg (
    id       INTEGER PRIMARY KEY,
    message  TEXT    NOT NULL,
    detail   TEXT,
    is_del   INTEGER DEFAULT 0,
    del_time TEXT    DEFAULT 'NULL'
);