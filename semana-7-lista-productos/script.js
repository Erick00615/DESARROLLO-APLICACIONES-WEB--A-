// Arreglo de productos
let productos = [
    {
        nombre: "Laptop",
        precio: 850,
        descripcion: "Laptop para uso académico"
    },
    {
        nombre: "Mouse inalámbrico",
        precio: 15,
        descripcion: "Mouse ergonómico USB"
    },
    {
        nombre: "Teclado",
        precio: 25,
        descripcion: "Teclado estándar en español"
    }
];

// Referencia al <ul>
const lista = document.getElementById("lista-productos");

// Función para mostrar productos
function mostrarProductos() {
    lista.innerHTML = "";

    productos.forEach(producto => {
        const li = document.createElement("li");
        li.innerHTML = `<strong>${producto.nombre}</strong> - $${producto.precio} <br> ${producto.descripcion}`;
        lista.appendChild(li);
    });
}

// Mostrar productos al cargar la página
mostrarProductos();

// Botón agregar producto
document.getElementById("btnAgregar").addEventListener("click", () => {
    const nuevoProducto = {
        nombre: "Producto nuevo",
        precio: 10,
        descripcion: "Descripción del nuevo producto"
    };

    productos.push(nuevoProducto);
    mostrarProductos();
});
