function showLoading() {
    console.log('Loading started...'); // 콘솔에 로그 출력
    document.getElementById('loading-overlay').style.display = 'flex';
}

function hideLoading() {
    console.log('Loading ended...'); // 콘솔에 로그 출력
    document.getElementById('loading-overlay').style.display = 'none';
}