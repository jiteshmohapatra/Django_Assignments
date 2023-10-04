
    let MenuBtn = document.getElementById('MenuBtn')
    MenuBtn.addEventListener('click',function(e){
        document.querySelector('body').classList.toggle('mobile-nav-active');
        this.classList.toggle('fa-xmark')
    })
    let typed = new Typed("auto-input",{
        Strings:['webdevloper','System Administrator','Uidesigner','blogger'],
        typeSpeed:100,
        backspeed:100,
        backDelay:2000,
        loop:true,
    
    })