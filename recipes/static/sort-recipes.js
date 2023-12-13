function sortRecipes(valor) {
    fetch(`/sort_recipes/${valor}`)
        .then(response => response.json())
        .then(data => {
            const recetasContainer = document.getElementById('recipe-container');
            recetasContainer.innerHTML = '';

            data.recipes.forEach(recipe => {
                recetasContainer.innerHTML += `
                    <div class="recipe">
                        <h2>${recipe.title}</h2>
                        <p>User: ${recipe.user.name}</p>
                        <img src="/static/main_photos/${recipe.main_photo}" alt="Foto de la Receta">
                        <p><a class = "recipe-link" href="/recipe_view/${recipe.id}">See Recipe</a></p>
                    </div>
                `;
            });
        })
}