const imageInput = document.querySelector('input[type="file"]');
const fileLabel = document.getElementById("file-label");

if (imageInput) {
    imageInput.addEventListener("change", function(event) {
        const file = event.target.files[0];

        if (file) {
            let preview = document.getElementById("preview");
            if (fileLabel) {
                   fileLabel.innerText = file.name;
                }
            if (!preview) {
                preview = document.createElement("img");
                preview.id = "preview";
                preview.className = "preview-image";

                imageInput.parentElement.appendChild(preview);
            }

            preview.src = URL.createObjectURL(file);
            preview.style.display = "block";
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