window.addEventListener('load',function () {
    let scroll_apis = document.getElementById('scroll_apis');
    if (scroll_apis) {
        scroll_apis.addEventListener('click',(e)=>{
            this.window.scrollBy(0,317);
        });   
    }
// pagina de contacto
    let href = window.location.href;
    if (/\/contacto$/i.test(href)) {
        console.log(`en ${href}`)
    }
});