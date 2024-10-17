import cookie from 'js-cookie'

export  function setCookie(key, value){
    cookie.set(key,value)
}

export function getCookie(key){
    return cookie.get(key)
}

export  function  removeCookie(key){
    cookie.remove(key)
}

// 存入Storage中
export  function SetStorage(key, value){
    localStorage.setItem(key, value)
}


export function GetStorage(){
    return JSON.parse(localStorage.getItem('user_data'));
}

export function RemoveStorage(){
    localStorage.removeItem('user_data')
}

