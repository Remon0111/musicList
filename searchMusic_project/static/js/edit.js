const buttonOpen = document.getElementById('modalOpen');
const modal = document.getElementById('easyModal');
const buttonClose = document.getElementsByClassName('modalClose')[0];
const buttonOpen2 = document.getElementById('modalOpen2');
const modal2 = document.getElementById('easyModal2');
const buttonClose2 = document.getElementsByClassName('modalClose2')[0];

// ボタンがクリックされた時
buttonOpen.addEventListener('click', modalOpen);
function modalOpen() {
    modal.style.display = 'block';
}

// バツ印がクリックされた時
buttonClose.addEventListener('click', modalClose);
function modalClose() {
    modal.style.display = 'none';
}

// モーダルコンテンツ以外がクリックされた時
addEventListener('click', outsideClose);
function outsideClose(e) {
    if (e.target == modal) {
    modal.style.display = 'none';
    }
}

buttonOpen2.addEventListener('click', modalOpen2);
function modalOpen2() {
    modal2.style.display = 'block';
}

// バツ印がクリックされた時
buttonClose2.addEventListener('click', modalClose2);
function modalClose2() {
    modal2.style.display = 'none';
}

// モーダルコンテンツ以外がクリックされた時
addEventListener('click', outsideClose2);
function outsideClose2(e) {
    if (e.target == modal2) {
    modal2.style.display = 'none';
    }
}