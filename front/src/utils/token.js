import cookie from 'js-cookie'

export  function setToken(token){
    cookie.set('user_token',token)
}

export function getToken(){
    return cookie.get('user_token')
}

export  function  removeToken(){
    cookie.remove('user_token')
}


export  function SetCookie(key, value){
    cookie.set(key, value)
}

export function GetCookie(key){
    return cookie.get(key)
}

export function RemoveCookie(key){
    cookie.remove(key)
}

// 存入Storage中
export  function SetStorage(key, value){
    localStorage.setItem(key, value)
}


export function GetStorage(key){
    return localStorage.getItem(key)
}

export function RemoveStorage(key){
    localStorage.removeItem(key)
}

