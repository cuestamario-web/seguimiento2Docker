const sede = process.env.SEDE_CAFETERIA;

if (!sede) {
  console.error("Error: configuración incompleta, la aplicación no puede iniciar.");
  process.exit(1);
}

module.exports = {
  sede,
  puerto: 3000,
};
