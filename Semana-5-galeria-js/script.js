const imageUrlInput = document.getElementById("imageUrl");
const addImageBtn = document.getElementById("addImageBtn");
const deleteImageBtn = document.getElementById("deleteImageBtn");
const gallery = document.getElementById("gallery");

let selectedImage = null;

// Agregar imagen
addImageBtn.addEventListener("click", () => {
    const imageUrl = imageUrlInput.value.trim();

    if (imageUrl === "") {
        alert("Por favor ingrese una URL válida");
        return;
    }

    const img = document.createElement("img");
    img.src = imageUrl;

    img.addEventListener("click", () => {
        if (selectedImage) {
            selectedImage.classList.remove("selected");
        }
        img.classList.add("selected");
        selectedImage = img;
    });

    gallery.appendChild(img);
    imageUrlInput.value = "";
});

// Eliminar imagen seleccionada
deleteImageBtn.addEventListener("click", () => {
    if (selectedImage) {
        gallery.removeChild(selectedImage);
        selectedImage = null;
    } else {
        alert("No hay ninguna imagen seleccionada");
    }
});

// Agregar imagen con Enter
imageUrlInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        addImageBtn.click();
    }
});
