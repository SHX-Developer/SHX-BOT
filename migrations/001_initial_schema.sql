CREATE TABLE IF NOT EXISTS user_access (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL UNIQUE,
    username TEXT,
    firstname TEXT,
    lastname TEXT,
    fullname TEXT,
    language TEXT,
    chat_id BIGINT,
    chat_type TEXT,
    is_premium BOOLEAN,
    date DATE,
    time TIME,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS user_data (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL UNIQUE,
    username TEXT,
    language TEXT NOT NULL DEFAULT '-',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS russian (
    id BIGSERIAL PRIMARY KEY,
    artist TEXT NOT NULL,
    name TEXT NOT NULL,
    path TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS english (
    id BIGSERIAL PRIMARY KEY,
    artist TEXT NOT NULL,
    name TEXT NOT NULL,
    path TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS playlists (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    name TEXT NOT NULL,
    path TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS new (
    id BIGSERIAL PRIMARY KEY,
    month INTEGER NOT NULL,
    name TEXT NOT NULL,
    callback TEXT NOT NULL UNIQUE,
    path TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_user_access_user_id ON user_access (user_id);
CREATE INDEX IF NOT EXISTS idx_user_data_user_id ON user_data (user_id);
CREATE INDEX IF NOT EXISTS idx_user_data_language ON user_data (language);

CREATE INDEX IF NOT EXISTS idx_russian_artist ON russian (artist);
CREATE INDEX IF NOT EXISTS idx_russian_name ON russian (name);
CREATE INDEX IF NOT EXISTS idx_english_artist ON english (artist);
CREATE INDEX IF NOT EXISTS idx_english_name ON english (name);

CREATE INDEX IF NOT EXISTS idx_playlists_user_id ON playlists (user_id);
CREATE INDEX IF NOT EXISTS idx_new_month ON new (month);
CREATE INDEX IF NOT EXISTS idx_new_callback ON new (callback);
