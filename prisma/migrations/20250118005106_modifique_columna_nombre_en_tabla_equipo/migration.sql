/*
  Warnings:

  - A unique constraint covering the columns `[nombre]` on the table `equipos` will be added. If there are existing duplicate values, this will fail.

*/
-- CreateIndex
CREATE UNIQUE INDEX "equipos_nombre_key" ON "equipos"("nombre");
