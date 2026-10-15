package bodega;

public class Producto {

    private static final int STOCK_MINIMO = 10;

    private final String nombre;
    private final int cantidad;
    private final double precioUnitario;

    public Producto(String nombre, int cantidad, double precioUnitario) {
        this.nombre = nombre;
        this.cantidad = cantidad;
        this.precioUnitario = precioUnitario;
    }

    public String getNombre() {
        return nombre;
    }

    public int getCantidad() {
        return cantidad;
    }

    public double subtotal() {
        return cantidad * precioUnitario;
    }

    public boolean necesitaReposicion() {
        return cantidad < STOCK_MINIMO;
    }
}
