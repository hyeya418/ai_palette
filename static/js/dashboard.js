document.addEventListener("DOMContentLoaded", function () {
    const currentPath = window.location.pathname; // 현재 URL 경로
    const menuItems = document.querySelectorAll(".menu-item a");

    menuItems.forEach((menu) => {
        if (menu.getAttribute("href") === currentPath) {
            menu.parentElement.classList.add("active"); // 해당 <li> 활성화
        }
    });
});
