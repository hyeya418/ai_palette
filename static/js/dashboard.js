document.addEventListener("DOMContentLoaded", function () {
    const currentPath = window.location.pathname; // 현재 URL 경로
    const menuItems = document.querySelectorAll(".menu-item a");

    menuItems.forEach((menu) => {
        if (menu.getAttribute("href") === currentPath) {
            menu.parentElement.classList.add("active"); // 해당 <li> 활성화
        }
    });

    const tabs = document.querySelectorAll(".content-options .option");
    const sections = document.querySelectorAll(".summary-body");

    tabs.forEach((tab) => {
        tab.addEventListener("click", () => {
            // 모든 탭의 active 클래스 제거
            tabs.forEach((t) => t.classList.remove("active"));

            // 현재 클릭된 탭에 active 클래스 추가
            tab.classList.add("active");

            // 모든 섹션 숨김 처리
            sections.forEach((section) => section.classList.remove("active"));

            // 클릭된 탭과 연결된 섹션만 활성화
            const targetTab = tab.getAttribute("data-tab");
            const targetSection = document.getElementById(targetTab);
            if (targetSection) {
                targetSection.classList.add("active");
            }
        });
    });

    // 초기 상태: 첫 번째 섹션만 보이도록 설정
    sections.forEach((section, index) => {
        if (index === 0) {
            section.classList.add("active");
        } else {
            section.classList.remove("active");
        }
    });
});
