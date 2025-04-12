const loginform=document.getElementById("login-form")
const baseendpoint="http://localhost:8000/api"

if (loginform){
    loginform.addEventListener("submit", handlelogin) 

}

function handlelogin(event){
    console.log(event)
    event.preventDefault()
    const loginendpoint =`${baseendpoint}/token/`
    let loginFormData=new FormData(loginform)
    let loginObjectData=Object.fromEntries(loginFormData)
    let bodyStr=JSON.stringify(loginObjectData)

    console.log(loginObjectData,bodyStr)
    const options={
        'method':'POST',
        headers:{
            "ContentType":"application/json"
        },
        body:""
    }
    fetch(loginendpoint,options)

}