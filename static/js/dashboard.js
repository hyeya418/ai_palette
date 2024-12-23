document.addEventListener("DOMContentLoaded", () => {
    const menuItems = document.querySelectorAll(".menu-item");
    const contentSections = document.querySelectorAll(".content-section");

    menuItems.forEach(item => {
        item.addEventListener("click", () => {
            // 모든 메뉴에서 active 클래스 제거
            menuItems.forEach(i => i.classList.remove("active"));
            // 클릭된 메뉴에 active 클래스 추가
            item.classList.add("active");

            // 모든 콘텐츠 섹션 숨기기
            contentSections.forEach(section => section.classList.remove("active"));
            // 클릭된 메뉴와 연결된 섹션만 보이도록 설정
            const contentId = item.getAttribute("data-content");
            document.getElementById(contentId).classList.add("active");
        });
    });
});
