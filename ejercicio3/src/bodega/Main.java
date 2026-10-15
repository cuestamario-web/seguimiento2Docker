package bodega;

import java.util.List;

public class Main {

    public static void main(String[] args) {
        LectorInventario lector = new LectorInventario();
        List<Producto> productos = lector.leer();

        System.out.println("==================================================");
        System.out.println("              INVENTARIO DE BODEGA");
        System.out.println("==================================================");
        System.out.printf("%-22s%10s%16s%n", "Producto", "Cantidad", "Subtotal");
        System.out.println("--------------------------------------------------");

        double total = 0;
        int alertas = 0;
        for (Producto p : productos) {
            String marca = p.necesitaReposicion() ? "  (!)" : "";
            System.out.printf("%-22s%10d%16.0f%s%n",
                    p.getNombre(), p.getCantidad(), p.subtotal(), marca);
            total += p.subtotal();
            if (p.necesitaReposicion()) {
                alertas++;
            }
        }

        System.out.println("--------------------------------------------------");
        System.out.printf("Valor total del inventario: $%,.0f%n", total);
        System.out.println("Productos por reponer (!): " + alertas);
        System.out.println("==================================================");
    }
}
