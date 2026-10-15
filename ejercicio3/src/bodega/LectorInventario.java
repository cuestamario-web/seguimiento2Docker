package bodega;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class LectorInventario {

    private final Path ruta;

    public LectorInventario() {
        String archivo = System.getenv().getOrDefault("ARCHIVO_INVENTARIO", "datos/inventario.txt");
        this.ruta = Path.of(archivo);
    }

    public List<Producto> leer() {
        List<Producto> productos = new ArrayList<>();
        try {
            for (String linea : Files.readAllLines(ruta)) {
                if (linea.isBlank() || linea.startsWith("#")) {
                    continue;
                }
                String[] partes = linea.split(";");
                productos.add(new Producto(
                        partes[0].trim(),
                        Integer.parseInt(partes[1].trim()),
                        Double.parseDouble(partes[2].trim())));
            }
        } catch (IOException e) {
            System.err.println("No fue posible leer el inventario: " + ruta);
            System.exit(1);
        }
        return productos;
    }
}
