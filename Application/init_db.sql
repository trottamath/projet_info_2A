DROP TABLE IF EXISTS parcelle CASCADE;
CREATE TABLE parcelle (
	id_parc TEXT PRIMARY KEY,
	id_com_inclus TEXT,
    limite_com BOOLEAN,
    nom_commune TEXT,
    date TEXT
);


DROP TABLE IF EXISTS parcelle_parcelle CASCADE;
CREATE TABLE parcelle_parcelle (
id_parc1 TEXT,
id_parc2 TEXT,
date TEXT
);

