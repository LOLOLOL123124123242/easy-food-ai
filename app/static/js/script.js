const imageInput = document.querySelector('input[type="file"]');
const fileLabel = document.getElementById("file-label");
const uploadBox = document.querySelector(".upload-box");

if (uploadBox) {

    uploadBox.addEventListener("dragover", function(e) {
        e.preventDefault();
        uploadBox.classList.add("drag-over");
    });

    uploadBox.addEventListener("dragleave", function() {
        uploadBox.classList.remove("drag-over");
    });

    uploadBox.addEventListener("drop", function(e) {
        e.preventDefault();

        uploadBox.classList.remove("drag-over");

        const file = e.dataTransfer.files[0];

        if (file) {
            imageInput.files = e.dataTransfer.files;

            handleFile(file);
        }
    });
}

function handleFile(file) {

    if (fileLabel) {
        fileLabel.innerText = file.name;
    }

    let preview = document.getElementById("preview");

    if (!preview) {

        preview = document.createElement("img");

        preview.id = "preview";
        preview.className = "preview-image";

        uploadBox.appendChild(preview);
    }

    preview.src = URL.createObjectURL(file);

    preview.style.display = "block";
}

if (imageInput) {

    imageInput.addEventListener("change", function(event) {

        const file = event.target.files[0];

        if (file) {
            handleFile(file);
        }
    });
}

const form = document.querySelector("form");

if (form) {

    form.addEventListener("submit", function() {

        const button = form.querySelector("button");

        button.innerHTML = `
            <span class="loader-icons">
                <span>🍴</span>
                <span>🥄</span>
                <span>🔪</span>
            </span>
            Generating...
        `;

        button.disabled = true;
    });
}