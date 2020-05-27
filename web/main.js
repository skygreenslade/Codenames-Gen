

const newBtn = document.getElementById('button2');
s = [0, 0, 0]; //seed values for RNG
rngInit();
genNew();


// generate and return a random list of cards to insert
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
        i = Math.floor(rng()*end--);
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


// updates heading to sidplay to the user which team goes first
function updateHeading(redFirst){
    toPrint = "";
    if (redFirst){
        toPrint += "Red ";
        document.getElementById('headingUL').className = 'underline redGrad';
    } else {
        toPrint += "Blue ";
        document.getElementById('headingUL').className = 'underline blueGrad';
    }
    toPrint += "Goes First!";

    document.getElementById('cardHeading').innerHTML = toPrint;

}//updateHeading


// main function which clears grid, generates new grid, and updates displays
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


// run once on page load to initialize randomize function 
// and whenever a seed is given
function rngInit(seed){

    // if no seed is given, generate random seed values
    if (seed == null) {
        s[0] = Math.random()*29999 +1;
        s[1] = Math.random()*29999 +1;
        s[2] = Math.random()*29999 +1;
    } else {
        //create seeds using given string "seed"
        for (i=0; i<3; i++){
            num = seed.charCodeAt(i%(seed.length))*10;
            num = num + seed.charCodeAt((i+3)%(seed.length));
            console.log(num);
            s[i] = num;
        }
        if (s[0]&&s[1]&&s[2] == 0){
            //no zero values please!
            rngInit();
            alert('Sorry, "' + seed +'" will not work as a seed!');
        }
    }
}



// (pseudo) random number generator
function rng(){

    //Wichmann-Hill RNG:
    s[0] = (171*s[0])% 30269;
    s[1] = (172*s[1])% 30307;
    s[2] = (170*s[2])% 30323;
    return (((s[0]/30269) + (s[1]/30307) + (s[2]/30323))%1);
}



//add given cardType (class string) to given row (ID)
function addCard(row, cardType){
    var newCard = document.createElement('div');
    newCard.className = cardType;
    document.getElementById(row).appendChild(newCard);

}


newBtn.addEventListener('click', genNew);
