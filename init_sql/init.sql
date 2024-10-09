CREATE TABLE IF NOT EXISTS users (
    id serial NOT NULL,
    email TEXT,
    user_name TEXT,
    hashed_password TEXT NOT NULL,
    is_active BOOLEAN,
    PRIMARY KEY (id)
);

INSERT INTO users (
    email, 
    user_name, 
    hashed_password, 
    is_active
)
VALUES (
    'admin@admin.com',
    'admin',
    '$2b$12$UdDiQZ6th3gXDDO0se8fI.bDA5kUmC2/yJIe/lm24AQP6g2e/vBqi',
    '1'
);