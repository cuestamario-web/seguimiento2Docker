package conversor;

import java.util.Map;

public class Conversor {

    // Pesos colombianos que vale 1 unidad de cada moneda (valores de ejemplo)
    private static final Map<String, Double> TASAS = Map.of(
            "USD", 4000.0,
            "EUR", 4400.0,
            "MXN", 220.0);

    public boolean soporta(String moneda) {
        return TASAS.containsKey(moneda);
    }

    public double convertir(double pesos, String moneda) {
        return pesos / TASAS.get(moneda);
    }
}
