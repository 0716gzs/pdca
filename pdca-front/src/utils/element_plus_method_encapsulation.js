export const SuccessMessage = (el_this, msg) =>{
    el_this.$notify({
        message: msg,
        type: 'success'
    });
}


export const WarningMessage = (el_this, msg) =>{
    el_this.$notify({
        message: msg,
        type: 'warning'
    });
}


export const FailMessage = (el_this, msg) =>{
    el_this.$notify.error({
        message: msg
    });
}
