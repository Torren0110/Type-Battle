const battleText = document.getElementById("battleText");
const battleAttack = document.getElementById("inputText");
const battleTimer = document.getElementById("battleTimer");
const battleProgress = document.getElementById("progress1");
const battleResult = document.getElementById("battleResult");
const battleLength = battleText.innerText.length;

var remainingText = battleText.innerText;
var currentWord = "";
var currentWordColor = "";
var doneText = "";
var currentInd = 0;
var countDown = 3;
var timePassed = [0, 0];
var timer;
var wordsDone = 0;
var err = 0;

const countDownTimer = setInterval(() => {
    if(countDown === 0)
    {
        
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
        battleTimer.innerText = "Time to Battle : " + countDown;
        countDown -= 1;
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

function endBattle() {
    battleAttack.value = "";
    battleAttack.disabled = true;
    updateBattleText();

    var wpm = Math.floor(wordsDone / (timePassed[0] + timePassed[1] / 60));

    var accuracy = Math.floor((1 - err / battleLength) * 100);
    var progress = Math.floor((doneText.length / battleLength) * 100);

    battleProgress.innerText = `Progress : ${progress}%`; 
    battleResult.innerText = "Accuracy: " + accuracy + " WPM : " + wpm;
    clearInterval(timer);
}

getNextWord();
doneText = doneText.trimStart();
updateBattleText();


battleAttack.addEventListener('input', (event) => {
    var len = battleAttack.value.length;
    battleAttack.style.color = "black";
    currentWordColor = '';

    console.log(len, currentInd, currentWord, event.data);

    if (len - 1 < currentInd) {
        currentInd = len;
    }
    else if (len - 1 === currentInd && currentInd === currentWord.length && (event.data === " " || remainingText === "")) {
        currentInd = 0;
        getNextWord();
        battleAttack.value = "";
        wordsDone += 1;

        progress = Math.round((doneText.length / battleLength) * 100);
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




