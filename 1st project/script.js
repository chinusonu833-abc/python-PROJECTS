// SUBJECT DATABASE
// days = number of working days
// hoursPerDay = assumed class duration

const subjects = {

"BT/JAVA": {days:86, hoursPerDay:1},
"CC": {days:68, hoursPerDay:1},
"ML": {days:68, hoursPerDay:1},
"PM": {days:87, hoursPerDay:1},
"IKS": {days:16, hoursPerDay:1},
"NSS": {days:17, hoursPerDay:1},
"LIBRARY": {days:17, hoursPerDay:1},
"PLACEMENT TRAINING": {days:16, hoursPerDay:1},
"PROCTORING": {days:16, hoursPerDay:1},
"MAJOR PROJECT PHASE-I": {days:18, hoursPerDay:2},
"CC LAB / GEN AI LAB": {days:16, hoursPerDay:2},
"GEN AI LAB / ML LAB": {days:19, hoursPerDay:2},
"ML LAB / CC LAB": {days:17, hoursPerDay:2}

};


// CREATE BUTTONS AUTOMATICALLY
const container = document.getElementById("subjectButtons");

Object.keys(subjects).forEach(sub => {

    let btn = document.createElement("button");
    btn.innerText = sub;
    btn.onclick = () => showDetails(sub);

    container.appendChild(btn);
});


// GENERATE SAMPLE DATE LIST
function generateDates(totalDays){

    let start = new Date("2026-01-27");
    let result = [];

    for(let i=0;i<totalDays;i++){

        let d = new Date(start);
        d.setDate(start.getDate()+i);

        result.push({
            date:d.toLocaleDateString(),
            day:d.toLocaleString('en-US',{weekday:'long'})
        });
    }

    return result;
}


// SHOW SUBJECT DETAILS
function showDetails(subject){

    let data = subjects[subject];

    let dates = generateDates(data.days);

    let totalHours = data.days * data.hoursPerDay;

    let html = `
        <h3>${subject}</h3>
        <p><b>Total Working Days:</b> ${data.days}</p>
        <p><b>Total Hours:</b> ${totalHours}</p>

        <table>
        <tr>
            <th>Date</th>
            <th>Day</th>
            <th>Hours</th>
        </tr>
    `;

    dates.forEach(d=>{
        html += `
        <tr>
            <td>${d.date}</td>
            <td>${d.day}</td>
            <td>${data.hoursPerDay}</td>
        </tr>`;
    });

    html += "</table>";

    document.getElementById("output").innerHTML = html;
}