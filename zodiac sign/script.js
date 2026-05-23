function findZodiac() {
    const dob = document.getElementById("dob").value;
    const result = document.getElementById("result");

    if (!dob) {
        result.innerHTML = "<p>Please select your date of birth.</p>";
        return;
    }

    const date = new Date(dob);
    const day = date.getDate();
    const month = date.getMonth() + 1;

    let sign = "";
    let image = "";

    if ((month === 3 && day >= 21) || (month === 4 && day <= 19)) {
        sign = "Aries";
        image = "Aries.jpg";
    } else if ((month === 4 && day >= 20) || (month === 5 && day <= 20)) {
        sign = "Taurus";
        image = "Taurus.png";
    } else if ((month === 5 && day >= 21) || (month === 6 && day <= 20)) {
        sign = "Gemini";
        image = "gemini.jpg";
    } else if ((month === 6 && day >= 21) || (month === 7 && day <= 22)) {
        sign = "Cancer";
        image = "cancer.jpg";
    } else if ((month === 7 && day >= 23) || (month === 8 && day <= 22)) {
        sign = "Leo";
        image = "leo.jpg";
    } else if ((month === 8 && day >= 23) || (month === 9 && day <= 22)) {
        sign = "Virgo";
        image = "virgo.png";
    } else if ((month === 9 && day >= 23) || (month === 10 && day <= 22)) {
        sign = "Libra";
        image = "libra.png";
    } else if ((month === 10 && day >= 23) || (month === 11 && day <= 21)) {
        sign = "Scorpio";
        image = "scorpia.jpg";
    } else if ((month === 11 && day >= 22) || (month === 12 && day <= 21)) {
        sign = "Sagittarius";
        image = "sag.png";
    } else if ((month === 12 && day >= 22) || (month === 1 && day <= 19)) {
        sign = "Capricorn";
        image = "capiricon.png";
    } else if ((month === 1 && day >= 20) || (month === 2 && day <= 18)) {
        sign = "Aquarius";
        image = "aqua.png";
    } else {
        sign = "Pisces";
        image = "pisces.png";
    }

    result.innerHTML = `
        <div class="sign-name">✨ ${sign}</div>
        <img src="${image}" alt="${sign}">
    `;
}80