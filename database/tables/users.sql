-- -------------------------------------------------------------
-- USERS TABLE
-- -------------------------------------------------------------

DROP TABLE IF EXISTS "public"."users" CASCADE;

-- Table Definition
CREATE TABLE IF NOT EXISTS "public"."users" (
    "id" SERIAL NOT NULL,
    "username" VARCHAR NOT NULL,
    "password" VARCHAR NOT NULL,
    PRIMARY KEY ("id")
);