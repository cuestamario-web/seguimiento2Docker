const express = require("express");
const config = require("./config");
const menu = require("./menu");

const app = express();

app.get("/", (req, res) => {
  res.json({
    mensaje: `Bienvenido a la cafetería ${config.sede}`,
    rutas: ["/menu", "/menu/:categoria"],
  });
});

app.get("/menu", (req, res) => {
  res.json(menu);
});

app.get("/menu/:categoria", (req, res) => {
  const productos = menu.filter((p) => p.categoria === req.params.categoria);
  if (productos.length === 0) {
    return res.status(404).json({ error: "Categoría no encontrada" });
  }
  res.json(productos);
});

app.listen(config.puerto, () => {
  console.log(`Servidor escuchando en el puerto ${config.puerto}`);
});
