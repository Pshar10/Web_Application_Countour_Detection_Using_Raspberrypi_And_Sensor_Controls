
  async function bols(){
    const [response] = await Promise.all([
      fetch("/monitor")]);
    
    const  res = await response.json()
    return res
    
  }
  setInterval(function(){ bols().then (res => {document.getElementById('inZone').innerHTML= res.inZone})
  .catch(error => {
    "request failed"
  })},100)



























































// setInterval(function(){
// async function bols(){
//   const [response] = await Promise.all([
//     fetch("/monitor")]);
  
//   const  res = await response.json()
//   return res
  
// }

// bols().then (res => {document.getElementById('inZone').innerHTML= res.inZone})
// .catch(error => {
//   "request failed"
// })
// },100)