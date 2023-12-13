// Cambiar entre modo claro y oscuro al hacer clic en el botón
const themeToggle = document.getElementById('theme-toggle');
themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
});

