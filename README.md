# Birds Surprise

This repository documents the steps I took to generate a list of birds I could use to encode a secret message, as part of a Christmas surprise in 2024.




## Instructions

First, clone this repo:

```bash
git clone git@github.com/theteacat/birds-surprise
cd birds-surprise
```

Next, extract all of the bird names from [Wikipedia's Spanish Birds page](https://en.wikipedia.org/wiki/List_of_birds_of_Spain#Ducks,_geese,_and_waterfowl) running the following javascript snippet in the developer tools of your browser:

```javascript
let tmpInput = document.createElement("textarea")
tmpInput.value = (
    Array.from(
        document.getElementsByClassName("div-col")
    ).map(
        divcol => divcol.children[0]
    ).map(
        ul => Array.from(
            ul.children
        ).map(
            li => li.children[0].innerText
        ).join("\n")
    ).join("\n")
)
tmpInput.select()
setTimeout(()=>{
    navigator.clipboard.writeText(tmpInput.value)
    console.log(`Copied to the clipboard: ${tmpInput.value}`)
}, 3000)
```

You then need to focus on the webpage within 3 seconds so the `navigator.clipboard.writeText` call doesn't fail.

This will put a list of all the birds in your clipboard, which can then be pasted into the [`birds.csv`](./birds.csv) file.

Now you have a dataset of bird names, you can run my terrible python code:

```bash
python3 main.py
```

This will ask you for a target message. If you don't have one in mind yet, there is a default.



## Example Output

```
Target Message (I'm enjoying looking at all the bird pictures, but i will post it soon): 
Target Sequence: IMENJOYINGLOOKINGATALLTHEBIRDPICTURESBUTIWILLPOSTITSOON
IMEN---------------------------------------------------: EURASIAN MOORHEN
----JO-------------------------------------------------: STEJNEGER'S SCOTER
------YING---------------------------------------------: EGYPTIAN GOOSE
----------LOOK-----------------------------------------: LESSER SHORT-TOED LARK
--------------INGATA-----------------------------------: MOURNING WHEATEAR
--------------------LLTHE------------------------------: ATLAS FLYCATCHER
-------------------------BIRDPI------------------------: BAIRD'S SANDPIPER
-------------------------------CTURE-------------------: CINEREOUS VULTURE
------------------------------------SBUTI--------------: HOUSE BUNTING
-----------------------------------------WILLP---------: WILSON'S PHALAROPE
----------------------------------------------OSTITS---: RUFOUS-TAILED ROCK-THRUSH
----------------------------------------------------OON: SOOTY TERN
Total birds required: 12
Average letters per bird: 4.583333333333333
```