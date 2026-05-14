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

const form = document.querySelector('form[action="/generate"]');

if (form) {
    form.addEventListener("submit", function() {
        const button = form.querySelector("button");

        button.innerHTML = `
            <span class="loader-sequence">
                <span class="loader-item">🍴</span>
                <span class="loader-item">🥄</span>
                <span class="loader-item">🔪</span>
            </span>
            Generating...
        `;

        button.disabled = true;
    });
}

const darkModeToggle = document.getElementById("dark-mode-toggle");

if (localStorage.getItem("darkMode") === "enabled") {
    document.body.classList.add("dark-mode");

    if (darkModeToggle) {
        darkModeToggle.innerText = "☀️";
    }
}

if (darkModeToggle) {
    darkModeToggle.addEventListener("click", function() {
        document.body.classList.toggle("dark-mode");

        if (document.body.classList.contains("dark-mode")) {
            localStorage.setItem("darkMode", "enabled");
            darkModeToggle.innerText = "☀️";
        } else {
            localStorage.setItem("darkMode", "disabled");
            darkModeToggle.innerText = "🌙";
        }
    });
}

const languageToggle = document.getElementById("language-toggle");
let currentLanguage = localStorage.getItem("language") || "en";

function translateFavoriteMeta(language) {
    document.querySelectorAll(".favorite-time").forEach(function(el) {
        const value =
            el.dataset.value ||
            el.innerText.split(": ").slice(1).join(": ");

        el.dataset.value = value;

        if (language === "ru") {
            el.innerText = "Время: " + value;
        } else if (language === "lt") {
            el.innerText = "Laikas: " + value;
        } else {
            el.innerText = "Time: " + value;
        }
    });

    document.querySelectorAll(".favorite-difficulty").forEach(function(el) {
        const value =
            el.dataset.value ||
            el.innerText.split(": ").slice(1).join(": ");

        el.dataset.value = value;

        if (language === "ru") {
            el.innerText = "Сложность: " + value;
        } else if (language === "lt") {
            el.innerText = "Sudėtingumas: " + value;
        } else {
            el.innerText = "Difficulty: " + value;
        }
    });
}

function applyLanguage(language) {
    const title = document.querySelector("h1");
    const description = document.querySelector(".home-description");
    const fileLabel = document.getElementById("file-label");
    const smallText = document.querySelector(".upload-box small");
    const generateBtn = document.getElementById("generate-btn");

    const resultsTitle = document.querySelector(".results-title");
    const ingredientsTitle = document.querySelector(".ingredients-title");
    const mealsTitle = document.querySelector(".meals-title");

    const favoritesPageTitle = document.querySelector(".favorites-page-title");
    const emptyFavorites = document.getElementById("empty-favorites");

    const savedPageTitle = document.querySelector(".saved-page-title");
    const emptySaved = document.getElementById("empty-saved");

    const historyPageTitle = document.querySelector(".history-page-title");
    const emptyHistory = document.getElementById("empty-history");

    const navHome = document.querySelector(".nav-home");
    const navSaved = document.querySelector(".nav-saved");
    const navFavorites = document.querySelector(".nav-favorites");
    const navHistory = document.querySelector(".nav-history");

    const favoriteTexts = document.querySelectorAll(".favorite-text");
    const timeTexts = document.querySelectorAll(".time-text");
    const difficultyTexts = document.querySelectorAll(".difficulty-text");
    const caloriesTexts = document.querySelectorAll(".calories-text");
    const proteinTexts = document.querySelectorAll(".protein-text");
    const carbsTexts = document.querySelectorAll(".carbs-text");
    const fatTexts = document.querySelectorAll(".fat-text");
    const ingredientsTexts = document.querySelectorAll(".ingredients-text");
    const stepsTexts = document.querySelectorAll(".steps-text");

    const backLink = document.querySelector(".back-link");

    if (language === "ru") {
        if (title) title.innerText = "Easy Food";
        if (description) description.innerText = "Загрузите фото ингредиентов и получите рецепты.";
        if (fileLabel) fileLabel.innerText = "Перетащите фото ингредиентов сюда";
        if (smallText) smallText.innerText = "или нажмите, чтобы выбрать файл";
        if (generateBtn) generateBtn.innerText = "Создать рецепты";

        if (resultsTitle) resultsTitle.innerText = "Сгенерированные рецепты";
        if (ingredientsTitle) ingredientsTitle.innerText = "Найденные ингредиенты";
        if (mealsTitle) mealsTitle.innerText = "Предложения блюд";

        if (favoritesPageTitle) favoritesPageTitle.innerText = "Избранные рецепты";
        if (emptyFavorites) emptyFavorites.innerText = "Пока нет избранных рецептов.";

        if (savedPageTitle) savedPageTitle.innerText = "Сохранённые рецепты";
        if (emptySaved) emptySaved.innerText = "Пока нет сохранённых рецептов.";

        if (historyPageTitle) historyPageTitle.innerText = "История просмотров";
        if (emptyHistory) emptyHistory.innerText = "Пока нет просмотренных рецептов.";

        if (navHome) navHome.innerText = "Главная";
        if (navSaved) navSaved.innerText = "Сохранённые";
        if (navFavorites) navFavorites.innerText = "Избранное";
        if (navHistory) navHistory.innerText = "История";

        favoriteTexts.forEach(el => el.innerText = "Избранное");
        timeTexts.forEach(el => el.innerText = "Время:");
        difficultyTexts.forEach(el => el.innerText = "Сложность:");
        caloriesTexts.forEach(el => el.innerText = "Калории");
        proteinTexts.forEach(el => el.innerText = "Белки");
        carbsTexts.forEach(el => el.innerText = "Углеводы");
        fatTexts.forEach(el => el.innerText = "Жиры");
        ingredientsTexts.forEach(el => el.innerText = "Ингредиенты:");
        stepsTexts.forEach(el => el.innerText = "Шаги");

        if (backLink) backLink.innerText = "Назад";
        if (languageToggle) languageToggle.innerText = "RU";

    } else if (language === "lt") {
        if (title) title.innerText = "Easy Food";
        if (description) description.innerText = "Įkelkite ingredientų nuotrauką ir gaukite receptų idėjų.";
        if (fileLabel) fileLabel.innerText = "Įkelkite arba nutempkite ingredientų nuotrauką čia";
        if (smallText) smallText.innerText = "arba spustelėkite, kad pasirinktumėte failą";
        if (generateBtn) generateBtn.innerText = "Generuoti receptus";

        if (resultsTitle) resultsTitle.innerText = "Sugeneruoti receptai";
        if (ingredientsTitle) ingredientsTitle.innerText = "Aptikti ingredientai";
        if (mealsTitle) mealsTitle.innerText = "Patiekalų pasiūlymai";

        if (favoritesPageTitle) favoritesPageTitle.innerText = "Mėgstamiausi receptai";
        if (emptyFavorites) emptyFavorites.innerText = "Kol kas nėra mėgstamiausių receptų.";

        if (savedPageTitle) savedPageTitle.innerText = "Išsaugoti receptai";
        if (emptySaved) emptySaved.innerText = "Kol kas nėra išsaugotų receptų.";

        if (historyPageTitle) historyPageTitle.innerText = "Peržiūrėtų receptų istorija";
        if (emptyHistory) emptyHistory.innerText = "Kol kas nėra peržiūrėtų receptų.";

        if (navHome) navHome.innerText = "Pradžia";
        if (navSaved) navSaved.innerText = "Išsaugoti";
        if (navFavorites) navFavorites.innerText = "Mėgstamiausi";
        if (navHistory) navHistory.innerText = "Istorija";

        favoriteTexts.forEach(el => el.innerText = "Mėgstamiausi");
        timeTexts.forEach(el => el.innerText = "Laikas:");
        difficultyTexts.forEach(el => el.innerText = "Sudėtingumas:");
        caloriesTexts.forEach(el => el.innerText = "Kalorijos");
        proteinTexts.forEach(el => el.innerText = "Baltymai");
        carbsTexts.forEach(el => el.innerText = "Angliavandeniai");
        fatTexts.forEach(el => el.innerText = "Riebalai");
        ingredientsTexts.forEach(el => el.innerText = "Ingredientai:");
        stepsTexts.forEach(el => el.innerText = "Žingsniai");

        if (backLink) backLink.innerText = "Atgal";
        if (languageToggle) languageToggle.innerText = "LT";

    } else {
        if (title) title.innerText = "Easy Food";
        if (description) description.innerText = "Upload a photo of your ingredients and get meal ideas.";
        if (fileLabel) fileLabel.innerText = "Drag & Drop ingredient image here";
        if (smallText) smallText.innerText = "or click to browse files";
        if (generateBtn) generateBtn.innerText = "Generate Recipes";

        if (resultsTitle) resultsTitle.innerText = "Generated Recipes";
        if (ingredientsTitle) ingredientsTitle.innerText = "Detected Ingredients";
        if (mealsTitle) mealsTitle.innerText = "Meal Suggestions";

        if (favoritesPageTitle) favoritesPageTitle.innerText = "Favorite Recipes";
        if (emptyFavorites) emptyFavorites.innerText = "No favorite recipes yet.";

        if (savedPageTitle) savedPageTitle.innerText = "Saved Recipes";
        if (emptySaved) emptySaved.innerText = "No saved recipes yet.";

        if (historyPageTitle) historyPageTitle.innerText = "Recently Viewed";
        if (emptyHistory) emptyHistory.innerText = "No recently viewed recipes.";

        if (navHome) navHome.innerText = "Home";
        if (navSaved) navSaved.innerText = "Saved Recipes";
        if (navFavorites) navFavorites.innerText = "Favorites";
        if (navHistory) navHistory.innerText = "History";

        favoriteTexts.forEach(el => el.innerText = "Favorite");
        timeTexts.forEach(el => el.innerText = "Time:");
        difficultyTexts.forEach(el => el.innerText = "Difficulty:");
        caloriesTexts.forEach(el => el.innerText = "Calories");
        proteinTexts.forEach(el => el.innerText = "Protein");
        carbsTexts.forEach(el => el.innerText = "Carbs");
        fatTexts.forEach(el => el.innerText = "Fat");
        ingredientsTexts.forEach(el => el.innerText = "Ingredients:");
        stepsTexts.forEach(el => el.innerText = "Steps");

        if (backLink) backLink.innerText = "Back";
        if (languageToggle) languageToggle.innerText = "EN";
    }

    translateFavoriteMeta(language);
}

applyLanguage(currentLanguage);

if (languageToggle) {
    languageToggle.addEventListener("click", function() {
        if (currentLanguage === "en") {
            currentLanguage = "ru";
        } else if (currentLanguage === "ru") {
            currentLanguage = "lt";
        } else {
            currentLanguage = "en";
        }

        localStorage.setItem("language", currentLanguage);
        applyLanguage(currentLanguage);
    });
}

function showToast(message) {
    const toast = document.createElement("div");

    toast.className = "toast";
    toast.innerText = message;

    document.body.appendChild(toast);

    const existingToasts = document.querySelectorAll(".toast");

    existingToasts.forEach(function(toast, index) {
        toast.style.top = 25 + (index * 80) + "px";
    });

    setTimeout(function() {
        toast.classList.add("hide");

        setTimeout(function() {
            toast.remove();
        }, 500);
    }, 3000);
}

const favoriteButtons = document.querySelectorAll(".favorite-btn");

favoriteButtons.forEach(function(button, index) {
    const favoriteKey = "favoriteRecipe_" + index;

    if (localStorage.getItem(favoriteKey) === "true") {
        button.classList.add("active");
        button.innerHTML = `❤️ <span class="favorite-text">Favorite</span>`;
    }

    button.addEventListener("click", function() {
        const recipeCard = button.closest(".recipe-card");

        const recipeTitle = recipeCard.querySelector("h3").innerText.trim();

        const recipeTime = recipeCard
            .querySelector(".time-text")
            .parentElement
            .innerText
            .replace("Time:", "")
            .replace("Время:", "")
            .replace("Laikas:", "")
            .trim();

        const recipeDifficulty = recipeCard
            .querySelector(".difficulty-text")
            .parentElement
            .innerText
            .replace("Difficulty:", "")
            .replace("Сложность:", "")
            .replace("Sudėtingumas:", "")
            .trim();

        button.classList.toggle("active");

        if (button.classList.contains("active")) {
            button.innerHTML = `❤️ <span class="favorite-text">Favorite</span>`;

            localStorage.setItem(favoriteKey, "true");
            localStorage.setItem(favoriteKey + "_title", recipeTitle);
            localStorage.setItem(favoriteKey + "_time", recipeTime);
            localStorage.setItem(favoriteKey + "_difficulty", recipeDifficulty);

            showToast("❤️ Added to favorites");

        } else {
            button.innerHTML = `🤍 <span class="favorite-text">Favorite</span>`;

            localStorage.setItem(favoriteKey, "false");
            localStorage.removeItem(favoriteKey + "_title");
            localStorage.removeItem(favoriteKey + "_time");
            localStorage.removeItem(favoriteKey + "_difficulty");

            showToast("❌ Removed from favorites");
        }

        applyLanguage(currentLanguage);
    });
});

const saveForms = document.querySelectorAll(".save-form");

saveForms.forEach(function(form, index) {
    const button = form.querySelector(".save-bookmark-btn");
    const saveKey = "savedRecipe_" + index;

    if (localStorage.getItem(saveKey) === "true") {
        button.classList.add("saved");
    }

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        if (button.classList.contains("saved")) {
            button.classList.remove("saved");
            localStorage.setItem(saveKey, "false");
            showToast("❌ Recipe removed");
        } else {
            button.classList.add("saved");
            localStorage.setItem(saveKey, "true");
            showToast("✅ Recipe saved successfully");
        }
    });
});

const searchInput = document.getElementById("recipe-search");
const filterButtons = document.querySelectorAll(".filter-btn");
const recipeCards = document.querySelectorAll(".recipe-card");

let currentFilter = "all";

function filterRecipes() {
    if (!searchInput) return;

    const searchValue = searchInput.value.toLowerCase();

    recipeCards.forEach(function(card) {
        const recipeName = card.querySelector("h3").innerText.toLowerCase();

        const recipeTime =
            (card.dataset.time || "").toLowerCase();

        const recipeDifficulty =
            (card.dataset.difficulty || "").toLowerCase();

        let matchesSearch =
            recipeName.includes(searchValue);

        let matchesFilter = true;

        if (currentFilter === "quick") {
            matchesFilter =
                recipeTime.includes("10") ||
                recipeTime.includes("15") ||
                recipeTime.includes("20") ||
                recipeTime.includes("25");

        } else if (currentFilter === "easy") {
            matchesFilter =
                recipeDifficulty.includes("easy");

        } else if (currentFilter === "protein") {
            matchesFilter =
                card.innerText.toLowerCase().includes("protein");
        }

        if (matchesSearch && matchesFilter) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
}

if (searchInput) {
    searchInput.addEventListener("input", filterRecipes);
}

filterButtons.forEach(function(button) {
    button.addEventListener("click", function() {
        filterButtons.forEach(function(btn) {
            btn.classList.remove("active");
        });

        button.classList.add("active");
        currentFilter = button.dataset.filter;

        filterRecipes();
    });
});

const modal = document.getElementById("recipe-modal");
const modalBody = document.getElementById("modal-body");
const closeModal = document.getElementById("close-modal");
const viewButtons = document.querySelectorAll(".view-recipe-btn");

function saveToHistory(recipeName) {
    let viewedRecipes =
        JSON.parse(localStorage.getItem("recentRecipes")) || [];

    viewedRecipes =
        viewedRecipes.filter(function(recipe) {
            return recipe !== recipeName;
        });

    viewedRecipes.unshift(recipeName);
    viewedRecipes = viewedRecipes.slice(0, 5);

    localStorage.setItem(
        "recentRecipes",
        JSON.stringify(viewedRecipes)
    );
}

viewButtons.forEach(function(button) {
    button.addEventListener("click", function() {
        const card = button.closest(".recipe-card");
        const recipeName = card.querySelector("h3").innerText.trim();

        if (modal && modalBody) {
            modalBody.innerHTML = card.innerHTML;
            modal.classList.add("show");
        }

        saveToHistory(recipeName);
    });
});

if (closeModal && modal) {
    closeModal.addEventListener("click", function() {
        modal.classList.remove("show");
    });
}

if (modal) {
    modal.addEventListener("click", function(event) {
        if (event.target === modal) {
            modal.classList.remove("show");
        }
    });
}
const loginForm =
    document.getElementById("login-form");

if (loginForm) {

    loginForm.addEventListener("submit", function(event) {

        event.preventDefault();

        const username =
    document.getElementById("login-username").value;

        localStorage.setItem("isLoggedIn", "true");
        localStorage.setItem("username", username);

        window.location.href = "/home";
    });
}

const registerForm =
    document.getElementById("register-form");

if (registerForm) {

    registerForm.addEventListener("submit", function(event) {

        event.preventDefault();

        const username =
            document.getElementById("register-username").value;

        localStorage.setItem("isLoggedIn", "true");
        localStorage.setItem("username", username);

        window.location.href = "/home";
    });
}
function updateAuthNavbar() {
    const isLoggedIn =
        localStorage.getItem("isLoggedIn");

    const username =
        localStorage.getItem("username");

    const navLogin =
        document.querySelector(".nav-login");

    const navRegister =
        document.querySelector(".nav-register");

    const navLinks =
        document.querySelector(".nav-links");

    if (
        isLoggedIn === "true" &&
        username &&
        navLinks
    ) {
        if (navLogin) {
            navLogin.style.display = "none";
        }

        if (navRegister) {
            navRegister.style.display = "none";
        }

        if (!document.querySelector(".nav-user")) {
            const userText =
                document.createElement("span");

            userText.className = "nav-user";
            userText.innerText = "Hi, " + username;

            const logoutBtn =
                document.createElement("button");

            logoutBtn.className = "logout-btn";
            logoutBtn.innerText = "Logout";

            logoutBtn.addEventListener("click", function() {
                localStorage.removeItem("isLoggedIn");
                localStorage.removeItem("username");

                window.location.href = "/login";
            });

            navLinks.insertBefore(
                userText,
                navLinks.querySelector("#dark-mode-toggle")
            );

            navLinks.insertBefore(
                logoutBtn,
                navLinks.querySelector("#dark-mode-toggle")
            );
        }
    }
}

updateAuthNavbar();
const protectedPages = [
    "/home",
    "/saved",
    "/favorites",
    "/history"
];

const currentPath =
    window.location.pathname;

const isLoggedIn =
    localStorage.getItem("isLoggedIn");

if (
    protectedPages.includes(currentPath) &&
    isLoggedIn !== "true"
) {
    window.location.href = "/login";
}