

const newBtn = document.getElementById('button2');
genNew();


// generateand return a random list of cards to insert
// boolean redFirst dictates which colour gets an extra card
function randomList(redFirst){
    fullList = [];
    reds = 8;
    blues = 8;
    black = 1;
    brown = 7;

    // first team gets an extra card to guess
    if (redFirst){
        reds++;
    } else {
        blues++;
    }

    // add cards to array by class names
    while(reds >0){
        fullList.push('red card');
        reds--;
    }
    while(blues >0){
        fullList.push('blue card');
        blues--;
    }
    while(brown >0){
        fullList.push('brown card');
        brown--;
    }
    fullList.push('black card');

    // (Fisher-Yates) shuffle the list
    end = fullList.length;
    while(end>0){
        i = Math.floor(Math.random()*end--);
        temp = fullList[end];
        fullList[end]=fullList[i];
        fullList[i] = temp;
    }

    return fullList;
} //randomList



// removes all card divs from row divs to prepare for new grid
function clearGrid(){

    for (num=1; num <=5; num++){
        aRow = document.getElementById('row' + num);
        while (aRow.firstElementChild){
            aRow.removeChild(aRow.firstElementChild);
        }
    }
} //clearGrid


function updateHeading(redFirst){
    toPrint = "";
    if (redFirst){
        toPrint += "Red ";
    } else {
        toPrint += "Blue ";
    }
    toPrint += "Goes First!";

    document.getElementById('cardHeading').innerHTML = toPrint;

}//updateHeading


function genNew(){

    redFirst = Math.random() < 0.5;
    newList = randomList(redFirst);
    clearGrid()
    
    // add cards to rows
    for (i=0; i<5; i++){
        currRow = "row" + (i+1);
        for (j=0; j<5; j++){
            addCard(currRow, newList[(i*5 + j)]);
        }
    }
    updateHeading(redFirst);

}

//add given cardType (class string) to given row (ID)
function addCard(row, cardType){
    var newCard = document.createElement('div');
    newCard.className = cardType;
    document.getElementById(row).appendChild(newCard);

}


newBtn.addEventListener('click', genNew);

