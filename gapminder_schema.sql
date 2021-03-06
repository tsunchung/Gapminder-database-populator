CREATE TABLE YEAR (
    YearID INTEGER CONSTRAINT year_pk PRIMARY KEY
);

CREATE TABLE GM_POP (
    Country VARCHAR(50),
    Pop_year INTEGER
        REFERENCES YEAR DEFERRABLE INITIALLY DEFERRED,
    Population INTEGER,
    CONSTRAINT gmpop_pk PRIMARY KEY (Country, Pop_year)
);

CREATE TABLE GM_LE (
    Country VARCHAR(50),
    LE_year INTEGER
        REFERENCES YEAR DEFERRABLE INITIALLY DEFERRED,
    Life_exp REAL,
    CONSTRAINT gmle_pk PRIMARY KEY (Country, LE_year)
);

CREATE TABLE GM_INCOME (
    Country VARCHAR(50),
    Income_year INTEGER
        REFERENCES YEAR DEFERRABLE INITIALLY DEFERRED,
    Income REAL,
    CONSTRAINT gmincome_pk PRIMARY KEY (Country, Income_year)
);

CREATE TABLE GM_HS (
    Country VARCHAR(50),
    HS_year INTEGER
        REFERENCES YEAR DEFERRABLE INITIALLY DEFERRED,
    Health_spending integer,
    CONSTRAINT gmhs_pk PRIMARY KEY (Country, HS_year)
);

CREATE TABLE GM_ELECTRICITY (
    Country VARCHAR(50),
    Elec_year INTEGER
        REFERENCES YEAR DEFERRABLE INITIALLY DEFERRED,
    Electricity REAL,
    CONSTRAINT gmelectricity_pk PRIMARY KEY (Country, Elec_year)
);