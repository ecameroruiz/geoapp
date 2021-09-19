-- -------------------------------------------------------------
-- PAYSTATS TABLE
-- -------------------------------------------------------------

DROP TABLE IF EXISTS "public"."paystats" CASCADE;

-- Table Definition
CREATE TABLE IF NOT EXISTS "public"."paystats" (
    "id" INTEGER NOT NULL,
    "amount" FLOAT NOT NULL,
    "p_age" VARCHAR NOT NULL,
    "p_gender" VARCHAR NOT NULL,
    "p_month" DATE NOT NULL,
    "postal_code_id" INTEGER,
    CONSTRAINT "postal_code_id_fkey" FOREIGN KEY ("postal_code_id") REFERENCES "public"."postal_codes"("id") ON DELETE CASCADE,
    PRIMARY KEY (id)
);