package conversor;

import java.util.LinkedHashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
        String moneda = System.getenv().getOrDefault("MONEDA_DESTINO", "USD");
        Conversor conversor = new Conversor();

        if (!conversor.soporta(moneda)) {
            System.out.println("Moneda no soportada: " + moneda + ". Use USD, EUR o MXN.");
            System.exit(1);
        }

        Map<String, Double> compras = new LinkedHashMap<>();
        compras.put("Portatil", 2_800_000.0);
        compras.put("Celular", 1_150_000.0);
        compras.put("Audifonos", 180_000.0);
        compras.put("Silla ergonomica", 650_000.0);

        System.out.println("CONVERSOR DE MONEDAS (version Java " + System.getProperty("java.version") + ")");
        System.out.println("Moneda destino: " + moneda);
        System.out.println("+----------------------+------------------+--------------+");
        System.out.printf("| %-20s | %16s | %12s |%n", "Producto", "Precio COP", "Precio " + moneda);
        System.out.println("+----------------------+------------------+--------------+");
        for (Map.Entry<String, Double> c : compras.entrySet()) {
            System.out.printf("| %-20s | %,16.0f | %,12.2f |%n",
                    c.getKey(), c.getValue(), conversor.convertir(c.getValue(), moneda));
        }
        System.out.println("+----------------------+------------------+--------------+");
    }
}
