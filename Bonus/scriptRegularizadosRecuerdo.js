//Constantes
const valueProceso =["operaciones","cuentas","riesgo","ti","financiero","continuidad","contabilidad","gobierno"]
const valueSeveridad={"bajo":"0","medio":"1","alto":"2"}
                 
const regular={temp}
const buttonSubmit=document.getElementById("submit")
const process = document.getElementById("process")
const tipo_riesgo = document.getElementById("tipo_riesgo")
const severidad = document.getElementById("severidad")
const res = document.getElementById("res")
const date = document.getElementById("date")
const obs = document.getElementById("obs")

console.log(regular[3].toLowerCase().trim())
process.value=regular[0].toLowerCase().split(" ")[0]
tipo_riesgo.value=regular[2]
severidad.value=valueSeveridad[regular[3].toLowerCase().trim()]
//severidad.value=0
res.value=regular[6]
//Formateo Fecha antes de setear el input
const partesFecha = regular[5].split("-");
const fechaFormateada = partesFecha[2] + "-" + partesFecha[1] + "-" + partesFecha[0];
date.value= fechaFormateada
obs.value=regular[1]