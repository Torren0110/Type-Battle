const opponents = document.getElementById("opponents");
const battleText = document.getElementById("battleText");
const battleAttack = document.getElementById("inputText");
const battleTimer = document.getElementById("battleTimer");
const battleProgress = document.getElementById("progress1");
const battleResult = document.getElementById("battleResult");
const battleRanking = document.getElementById("battleRanking");
const battleLength = battleText.innerText.length;
const getUrl = '/multi-mode/getInfo/';
const postUrl = '/multi-mode/postInfo/';

var remainingText = battleText.innerText;
var currentWord = "";
var currentWordColor = "";
var doneText = "";
var currentInd = 0;
var timePassed = [0, 0];
var timer;
var wordsDone = 0;
var err = 0;
var opponentsInfo = [];

const countDownTimer = setInterval(() => {
    if(countDownTime === 0)
    {
        if(opponentsInfo.length === 0)
            clearInterval(getCycle);
        timer = setInterval(() => {
            timePassed[1] += 1;
            
            if(timePassed[1] >= 60)
            {
                timePassed[1] = 0;
                timePassed[0] += 1;
            }
            setTimer();
        }, 1000);
        
        battleAttack.disabled = false;
        battleAttack.focus();
        battleTimer.innerText = "Battle Start";
        clearInterval(countDownTimer);
    }
    else
    {
        battleTimer.innerText = "Time to Battle : " + countDownTime;
        countDownTime -= 1;
    }
}, 1000);

function setTimer() {
    var time = "";

    if(timePassed[0] < 10)
        time += "0" + timePassed[0];
    else
        time += timePassed;

    time += " : ";

    if(timePassed[1] < 10)
        time += "0" + timePassed[1];
    else
        time += timePassed[1];

    battleTimer.innerText = time;

}

function getNextWord() {
    var ind = 0;

    doneText += currentWord + " ";
    currentWord = "";

    for (; ind < remainingText.length && remainingText[ind] != ' '; ind++)
        currentWord += remainingText[ind];

    var temp = "";

    for (ind = ind + 1; ind < remainingText.length; ind++)
        temp += remainingText[ind];

    remainingText = temp;
}

function updateBattleText() {
    battleText.innerHTML = "<span style='color: green';>" + doneText + `</span><span class="${currentWordColor}">` + currentWord + " </span><span style='color: grey';>" + remainingText + "</span>";
}

function createOpponentHTML(userName, progress, WPM) {
    return `<div class="opponent">
    <h4> ${userName} </h4>
    Progress: ${progress} <br/>
    WPM: ${WPM}
    </div>`;
}

function updateOpponents() {
    HTMLContent = "";

    var isDone = true;
    for(var i = 0; i < 4; i++)
    {
        if(i < opponentsInfo.length)
        {
            userName = opponentsInfo[i].userName;
            progress = opponentsInfo[i].progress;
            WPM = opponentsInfo[i].WPM;

            if(progress != "100 %")
                isDone = false;

            HTMLContent += createOpponentHTML(userName, progress, WPM)
        }
        else
            HTMLContent += createOpponentHTML('No User Present', "--", "--")

        }
    if(isDone && opponentsInfo.length != 0)
        clearInterval(getCycle);
        
    opponents.innerHTML = HTMLContent;
    createRankingHTML();
}

function isGreater(p1, p2) {
    p1 = p1.slice(0, -2);
    p2 = p2.slice(0, -2);

    return p1 > p2;
}

function sort(l) {
    for(var i = 1; i < l.length; i++) {
        for(var j = i - 1; j >= 0; j--)
        {
            if(isGreater(l[j].progress, l[j + 1].progress) || (l[j].progress === l[j + 1].progress && l[j].wpm >= l[j + 1].wpm))
            {
                break;
            }
            else {
                var temp = l[j];
                l[j] = l[j + 1];
                l[j + 1] = temp;
            }
        }
    }

    return l;
}

function createRankingHTML() {
    var l = [];

    opponentsInfo.forEach((data) => {
        l.push(data);
    })

    var wpm = Math.floor(wordsDone / (timePassed[0] + timePassed[1] / 60)) || 0;
    var progress = Math.floor((doneText.length / battleLength) * 100);

    l.push({
        userName: uname,
        progress: `${progress} %`,
        WPM: wpm
    });

    l = sort(l);

    console.log(l);

    outputHTML = "";

    l.forEach((u) => {
        outputHTML += `<li>${u.userName}</li>`;
    });

    battleRanking.innerHTML = outputHTML;

}

function endBattle() {
    updateBattleText();
    battleAttack.value = "";
    battleAttack.disabled = true;

    var wpm = Math.floor(wordsDone / (timePassed[0] + timePassed[1] / 60)) || 0;
    var accuracy = Math.floor((1 - err / battleLength) * 100);
    var progress = Math.floor((doneText.length / battleLength) * 100);

    updateDatabase(progress, wpm, accuracy)

    battleProgress.innerText = `Progress : ${progress}%`; 
    battleResult.innerText = "Accuracy: " + accuracy + " WPM : " + wpm;
    clearInterval(timer);
    clearInterval(countDownTimer);
}

updateOpponents();
getNextWord();
doneText = doneText.trimStart();
updateBattleText();
createOpponentHTML();

battleAttack.addEventListener('input', (event) => {
    var len = battleAttack.value.length;
    battleAttack.style.color = "black";
    currentWordColor = '';

    if (len - 1 < currentInd) {
        currentInd = len;
    }
    else if (len - 1 === currentInd && currentInd === currentWord.length && (event.data === " " || remainingText === "")) {
        currentInd = 0;
        getNextWord();
        battleAttack.value = "";
        wordsDone += 1;

        var progress = Math.round((doneText.length / battleLength) * 100);
        var wpm = Math.floor(wordsDone / (timePassed[0] + timePassed[1] / 60)) || 0;
        var accuracy = Math.floor((1 - err / battleLength) * 100) || 0;

        updateDatabase(progress, wpm, accuracy);

        battleProgress.innerText = `Progress : ${progress}%`;
    }
    else if (len - 1 === currentInd && event.data === currentWord[currentInd]) {
        currentInd += 1;
        if (remainingText === "" && len === currentWord.length) {
            wordsDone += 1;
            getNextWord();
            doneText = doneText.trimEnd();
            endBattle();
        }
    }
    else {
        battleAttack.style.color = "crimson";
        err += 1;
        currentWordColor = 'text-danger';
    }
    updateBattleText();
});

function updateDatabase(progress, wpm, accuracy) {
    data = {
        userID: uid,
        progress: progress,
        WPM: wpm,
        accuracy: accuracy
    }

    $.ajax({
        type: "post",
        url: postUrl,
        data: data,
        success: (response) => {
            console.log(response);
        }
    });
}

//Gets data of the opponents
const getCycle = setInterval((e) => {
    data = {
        userID: uid
    }
    
    $.ajax({
        type: "get",
        url: getUrl,
        data: data,
        success: (response) => {
            opponentsInfo = response.data;
            updateOpponents();
        }

    });
}, 500)