let monitoring = false 

/**
 * Function to request the server to start the motor
 */
async function requestStartMotor () {
  try {
    // Make request to server
    await axios.post('/start_motor') //get can also be used

    // Update status
    updateStatus('Processing......') //printing status
    startMonitoring()
  } catch (e) {
    updateStatus('The system has stopped, Please start again') // error control
  }
}

/** 
 * (Re)start monitoring
 */
async function startMonitoring () {
  monitoring = true
  while (monitoring) {
    let result = await axios.get('/monitor') //result taken from the end point
    updateMonitoringData(result.data)  //giving result to update function
    monitoring = false 
    
  }
  requestStartMotor ()
}

/** 
 * Stop monitoring
 */
function stopMonitoring () {
  monitoring = false
  updateStatus('The system has stopped, Please start again')  // Stopped after updating

  
  // document.getElementById('inZone').innerHTML= result.inZone
  //document.getElementById('distance').innerHTML= result.distance

  // if (result.inZone){
  //   updateStatus('The motor has stopped and the Object is in the Zone')
  //   document.getElementById('inZone').innerHTML= "Yes　　　　Last　updated　at　"+time
  // }
  // else
  // {
  //   updateStatus('The motor has stopped and the Object is not in the Zone')
  //   document.getElementById('inZone').innerHTML= "No　　　　Last　updated　at　"+time
  // }

}

/**
 * Function to request monitoring data to the server and display it in the main page
 */
function updateMonitoringData (result){
  var today = new Date();
  var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds(); //updating time of processing

  document.getElementById('Distance').innerHTML= result.distance //getting distance

  if (result.inZone){
    updateStatus('The motor has stopped after completing the cycle and the Object is in the Zone')
    document.getElementById('inZone').innerHTML= "Yes　　　　Last　updated　at　"+time 
  }
  else
  {
    updateStatus('The motor has stopped after completing the cycle and the Object is not in the Zone')
    document.getElementById('inZone').innerHTML= "No　　　　Last　updated　at　"+time
  }

}

/**
 * Function to request the server to stop the motor
 */
async function stopSystem () {
  //...
  try {
    // Make request to server
    
    await axios.post('/stop_system') //changed

    updateStatus('The system has stopped, Please start again')

    // Update status
    stopMonitoring()
  } catch (e) {
    
    updateStatus('The system has stopped, Please start again')
  }

}


function updateStatus(statusText) {
  // Get the HTML element where the status is displayed
  let motor_status_text = document.getElementById('status_text')
  motor_status_text.innerText = statusText
      

}
