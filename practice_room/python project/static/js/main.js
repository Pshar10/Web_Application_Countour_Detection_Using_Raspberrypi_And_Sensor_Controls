let monitoring = false 

/**
 * Function to request the server to start the motor
 */
async function requestStartMotor () {
  try {
    // Make request to server
    await axios.post('/start_motor') //get can be used

    // Update status
    updateStatus('Working')
    startMonitoring()
  } catch (e) {
    console.log('Error starting the motor', e)
    updateStatus('Error starting')
  }
}

/** 
 * (Re)start monitoring
 */
async function startMonitoring () {
  monitoring = true
  while (monitoring) {
    let result = await axios.get('/monitor')
    //console.log(result.data.inZone)
    //console.log(result.data.distance)
    updateMonitoringData(result.data)
  }
}

/** 
 * Stop monitoring
 */
function stopMonitoring (result) {
  monitoring = false

  document.getElementById('inZone').innerHTML= result.inZone
  document.getElementById('distance').innerHTML= result.distance
}

/**
 * Function to request monitoring data to the server and display it in the main page
 */
function updateMonitoringData (result){

  

  if (result.inZone){
    updateStatus('It is in zone')
    document.getElementById('inZone').innerHTML= "Yes"
  }
  else
  {
    updateStatus('It is not in Zone')
    document.getElementById('inZone').innerHTML= "No"
  }
  // Get HTML elements where results are displayed

  document.getElementById('distance').innerHTML= result.distance
  // ...
  
  
  
  
}

/**
 * Function to request the server to stop the motor
 */
async function stopSystem () {
  //...
  try {
    // Make request to server
    
    let res = await axios.post('/stop_system')

    // Update status
    updateStatus('The motor and sensor monitoring will stop')
    stopMonitoring(res.data)
  } catch (e) {
    console.log('Error starting the motor', e)
    updateStatus('Error starting')
  }


}


function updateStatus(statusText) {
  // Get the HTML element where the status is displayed
  let motor_status_text = document.getElementById('status_text')
  motor_status_text.innerText = statusText
      

}

function requestStopInZone(){

if(this.document.getElementById("should_stop_in_zone").checked = true)

      {console.log("Do this")}
     // this.document.getElementById("should_stop_in_zone").checked = false


}


