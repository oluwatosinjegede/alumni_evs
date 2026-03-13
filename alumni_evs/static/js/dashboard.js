async function updateStats(){

const response = await fetch("/api/dashboard-stats/")

const data = await response.json()

document.getElementById("votes_cast").innerText = data.votes

document.getElementById("turnout").innerText = data.turnout + "%"

}

setInterval(updateStats,5000)


const ctx = document.getElementById('turnoutChart')

new Chart(ctx,{
type:'doughnut',
data:{
labels:['Votes Cast','Remaining'],
datasets:[{
data:[{{ votes_cast }}, {{ total_voters }}-{{ votes_cast }}]
}]
}
})