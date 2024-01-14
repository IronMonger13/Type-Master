import time
import fontstyle
from random import randint


# Functions
def sleep():
    time.sleep(0.8)

def textSmooth(str, arg = True, timer = 0.01):
    if arg == True:
        for char in range(len(str)):
            print(textFormatting(str[char]), end="")
            time.sleep(timer)
    else:
        for char in range(len(str)):
            print(str[char], end="")
            time.sleep(timer)    

def textFormatting(str):
    return fontstyle.apply(str, "BOLD/BLACK/WHITE_BG")

def wordCounter(str):
    count = 1
    for i in range (0, len(str)):
        if str[i] == " ":
            count += 1
    return count

def mistakeCounter(strGen, strEntered, arg):
    mistakes = 0
    for check in range(0, arg):
        if strGen[check] != strEntered[check]:
            mistakes += 1
    return mistakes


# Driver Code
paragraphs = (
    "In the serene embrace of nature, a babbling brook winds its way through a lush, emerald-green meadow. The sun, a radiant orb in the cobalt sky, casts a warm glow upon the landscape, creating a dance of shadows and light. Tall grasses sway gently in the breeze, and a kaleidoscope of wildflowers adds a burst of color to the scene.",
    "In the heart of a bustling metropolis, skyscrapers stretch towards the heavens, their reflective surfaces capturing the vibrant energy of urban life. Streets pulse with the rhythm of footsteps, and a symphony of car horns weaves through the air. Neon signs flicker, painting the cityscape in hues of electric pink and vivid blue. Sidewalks are adorned with a diverse array of characters, each with their own story etched in the lines on their faces.",
    "Beneath the starry canvas of the night sky, a secluded beach invites contemplation. The rhythmic ebb and flow of the tide serenades the shore, while moonlight casts a silvery glow upon the sands. Seashells, treasures of the sea, rest scattered like delicate jewels.",
    "Within the hushed confines of a forgotten library, dusty shelves cradle volumes of untold stories. The air carries the comforting scent of aging parchment and ink. Sunlight filters through stained glass windows, casting a mosaic of colors on creaking wooden tables.",
    "Amidst the rolling hills of a sun-kissed vineyard, rows of grapevines stand in orderly formation like soldiers in a vast, green army. The aroma of ripening fruit mingles with the earthy scent of the soil, creating an olfactory symphony. The sun, a benevolent overseer, bathes the landscape in a golden glow, casting long shadows as it begins its descent.",
    "Amidst the towering canopies of an ancient forest, sunlight filters through the emerald foliage, creating a dappled mosaic on the forest floor. Moss-covered rocks and fallen logs bear witness to the passage of time, while the air is filled with the soft hum of unseen insects and the occasional call of distant birds.",
    "Beneath a canvas of swirling watercolor skies, a vast desert landscape stretches to the horizon. Golden dunes rise like rippling waves frozen in time, their crests catching the warm hues of the setting sun. A solitary cactus stands sentinel, its silhouette etched against the twilight sky.",
    "In the heart of a bustling market, vibrant stalls create a kaleidoscope of colors and aromas. Piles of exotic spices form mountains of reds, yellows, and greens, while the rhythmic chopping of fresh produce adds a percussive beat to the lively atmosphere.",
    "Within the hushed confines of an art studio, the scent of paint lingers in the air, a fragrant symphony of creativity. Canvases, bearing the imprints of countless brushstrokes, lean against easels like portals into the artist's imagination. Jars of vibrant pigments stand in orderly rows, ready to breathe life into the next masterpiece.",
    "Beneath the canopy of a sprawling botanical garden, a tapestry of nature unfolds in a riot of colors and textures. Exotic blooms, like living jewels, nod gracefully in the breeze, while verdant foliage forms a lush carpet underfoot. Butterflies, the ethereal dancers of this enchanting realm, flit from flower to flower, their delicate wings a kaleidoscope of hues."
)

flag = True
while flag == True:
    if flag == True:
        textDecider = randint(0, len(paragraphs) - 1)
        textSmooth("Enter player name:")
        name = input(" ")
        sleep()
        textSmooth("Generating your Type Master Text!")
        print("\n\n")
        sleep()

        text = paragraphs[textDecider]

        textSmooth(text, False)
        print("\n")
        sleep()
        textSmooth("Start typing as soon as the timer hits 0! ", True, 0.1)
        print("\n")
        for i in range (3, 0, -1):
            print(str(i) + "\n")
            sleep()
        
        textSmooth("START!")
        print("\n")

        startSeconds = time.time()

        answer  = input()
        endSeconds = time.time()

        # Calculating Time Taken
        timeTaken = round(endSeconds - startSeconds, 0)
        minutes = timeTaken//60
        seconds = timeTaken - (minutes * 60)

        # Getting Generated Text's Stats
        genChars = len(text)
        genWords = wordCounter(text)

        # Getting User Stats
        wordsTyped = wordCounter(answer)
        charsTyped = len(answer)

        # Counting Mistakes
        if charsTyped <= genChars:
            mistakes = mistakeCounter(text, answer, charsTyped)
            mistakes += genChars - charsTyped
        else:
            mistakes = mistakeCounter(text, answer, genChars)
            mistakes += charsTyped - genChars

        # Calculating Words per Minute
        wpm = round((wordsTyped/round(timeTaken, 0)) * 60, 2)
                
        # Calculating Accuracy
        accuracy = (charsTyped - mistakes)/genChars
        if (accuracy <=  0):
            accuracy = 0
        else:
            accuracy = round(accuracy * 100, 2)

        # Displaying Results
        print("\n")
        textSmooth("Calculating Stats", True, 0.01)
        print("\n")
        
        for i in range(3, 0, -1):
            print(".")
            sleep()

        print("\n")
        textSmooth("Total Words Typed:")
        print(f" {wordsTyped}")
        sleep()
        textSmooth("Total Characters Typed:")
        print(f" {charsTyped}")
        sleep()
        textSmooth("Accuracy:")
        print(f" {accuracy}%")
        sleep()
        textSmooth("Time Taken:")
        print(f" {minutes} minutes,  {seconds} seconds")
        sleep()
        textSmooth("Words per Minute:")
        print(f" {wpm}")

        # Try Again Prompt
        innerFlag = True
        while innerFlag == True:
            print("\n")
            textSmooth("Press")
            textSmooth("\n1 to Play Again\n2 to Exit\n", False)
            tryAgain = input("\n")
            if(tryAgain == "1"):
                print("\n")
                flag = True
                innerFlag = False
            elif(tryAgain == "2"):
                print("\n")
                textSmooth(f"Thanks for playing, {name}!")
                flag = False
                innerFlag = False
            else:
                textSmooth("PLEASE ENTER A VALID CHOICE!")
                innerFlag = True
