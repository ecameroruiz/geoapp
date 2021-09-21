-- -------------------------------------------------------------
-- POSTAL CODES TABLE
-- -------------------------------------------------------------

DROP TABLE IF EXISTS "public"."postal_codes" CASCADE;

-- Table Definition
CREATE TABLE IF NOT EXISTS "public"."postal_codes" (
    "id" INTEGER NOT NULL,
    "code" VARCHAR NOT NULL,
    "the_geom" GEOMETRY NOT NULL,
    PRIMARY KEY ("id")
);