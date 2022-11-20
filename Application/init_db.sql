DROP TABLE IF EXISTS commune CASCADE;
CREATE TABLE commune (
  id_com TEXT PRIMARY KEY,
  nom_commune TEXT,
  id_dep TEXT
);

DROP TABLE IF EXISTS parcelle CASCADE;
CREATE TABLE parcelle (
  id_parc TEXT PRIMARY KEY,
  id_com_limit TEXT REFERENCES commune(id_com)
);

DROP TABLE IF EXISTS parcelle_commune CASCADE;
CREATE TABLE parcelle_commune (
    id_parc TEXT REFERENCES parcelle(id_parc),
    id_com TEXT REFERENCES commune(id_com),
    date TEXT,
    PRIMARY KEY (id_parc, id_com, date)
);

DROP TABLE IF EXISTS commune_commune CASCADE;
CREATE TABLE commune_commune (
    id_com1 TEXT REFERENCES commune(id_com),
    id_com2 TEXT REFERENCES commune(id_com),
    date TEXT,
    PRIMARY KEY (id_com1, id_com2, date)
);

