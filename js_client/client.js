const loginform=document.getElementById("login-form")
const contentcontainer=document.getElementById("content-container")


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
            "Content-Type":"application/json"
        },
        body:""
    }
    fetch(loginendpoint,options)
    .then(response=>{
        console.log(response)
        return response.json()
    })
    .then( handleauthdata)
    .catch(err=>{
        console.log("err",err)
    })

}

function writetocontent(){
    if (contentcontainer){
        contentcontainer.innerHTML="<pre>"+JSON.stringify(data)+"</pre>"
    }
}

function handleauthdata(authData){
    localStorage.setItem('access',authData.access)
    localStorage.setItem('refresh',authData.refresh)

}

function getproductlist(){
    const endpoint=`${baseendpoint}/products/`
    const options={
        method:"GET",
        headers:{
            "Content-Type":"application/json"
        }
    }
    fetch(endpoint,options)
    .then(response=>response.json())
    .then(data=>{
        console.log(data)
        writetocontent(data)
    })
}