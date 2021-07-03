const ffpp = document.querySelector("#ffpp")
ffpp.innerHTML="5"

async function setParaText(){
    let mam = await fetch('/paraPartial')
    mam = await mam.text()
    console.dir(mam); 
     console.log('^mam^');

     ffpp.innerHTML = mam
}

setParaText();

