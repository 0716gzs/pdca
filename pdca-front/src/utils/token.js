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


export function GetStorage(key, flag=true){
    if (flag){
        return JSON.parse(localStorage.getItem(key));
    }
    return localStorage.getItem(key);
}

export function RemoveStorage(key){
    localStorage.removeItem(key)
}

