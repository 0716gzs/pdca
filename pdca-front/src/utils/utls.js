import CryptoJS from 'crypto-js'


/**
 * 加密方法
 * @param data
 * @returns {string}
 */
export const encrypt = (data) => {
    // 十六位十六进制数作为密钥
    const key = CryptoJS.enc.Utf8.parse("1234123412341234");
    // 十六位十六进制数作为密钥偏移量
    const iv = CryptoJS.enc.Utf8.parse("1234123412341234");
    let srcs = CryptoJS.enc.Utf8.parse(data);
    let encrypted = CryptoJS.AES.encrypt(srcs, key, {
        iv: iv,
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7,
    });
    return CryptoJS.enc.Base64.stringify(encrypted.ciphertext);
}


/**
 * 解密方法
 * @param data
 * @returns {string}
 */
export const decrypt = (data) => {
    // 十六位十六进制数作为密钥
    const key = CryptoJS.enc.Utf8.parse("1234123412341234");
    // const key = CryptoJS.enc.Utf8.parse("1234123412341234");
    // 十六位十六进制数作为密钥偏移量
    const iv = CryptoJS.enc.Utf8.parse("1234123412341234");
    // const iv = CryptoJS.enc.Utf8.parse("1234123412341234");
    const decrypt = CryptoJS.AES.decrypt(data, key, {iv: iv, mode: CryptoJS.mode.ECB, padding: CryptoJS.pad.Pkcs7});
    return CryptoJS.enc.Utf8.stringify(decrypt).toString();
}



