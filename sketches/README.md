p5.js sketches: emotion detection, interactive agents (Months 1-2)
# Day 1 p5.js Sketches
**Coding Train 1.1-1.4 Complete**

[Screenshot](day-1.png)
[Live Sketch](https://editor.p5js.org/ashmitachakraborty07/full/KLvKiluH7)

# Day 2: Circle Moves with Mouse Pointer
**Date**: Jan 4, 2026  
**p5.js URL**: https://editor.p5js.org/ashmitachakraborty07/full/wGZTQargI
**Description**: Circle moves with mouse pointer using `mouseX`/`mouseY`

## Code
```javascript
function draw() {
  background(220);
  ellipse(mouseX, mouseY, 60, 60);
}

# Day 2: Circle Moves on Its Own
**Date**: Jan 4, 2026  
**p5.js URL**: [your auto-circle sketch URL]
**Description**: Circle moves automatically across screen using variables

## Code
```javascript
let x = 0;
let speed = 2;

function draw() {
  background(220);
  ellipse(x, height/2, 60, 60);
  x = x + speed;
  if (x > width) x = 0;
}

# Day 4 - p5.js Sketches

**7 Interactive Animations** exploring conditionals, collision detection, and mouse interaction.

**Controls:** Mouse movement, clicks (check each sketch)

**Screenshots:**  
`day-4-[1-7]-code.png` & `day-4-[1-7]-output.png`

**Concepts Covered:**
- Bouncing rectangle (4-wall collision)
- Mouse tracking  
- Color mapping
- if/else if/else logic
- AND (&&) / OR (||) operators

# p5.js Classes + Arrays (Sat Jan 17, 2026)

**Status**: ✅ Sat 2:06AM COMPLETE

## **Today's Massive Catchup**
✅ 6.2: Classes in JavaScript (ES6)
✅ 6.3: Constructor Arguments
✅ 6.4: Adding JavaScript files
✅ 7.1: What is an Array
✅ 7.2: Arrays + Loops
✅ Practice: Multiple sketches + screenshots

## **Key Concepts Mastered**
📌 OOP: Classes w/ constructor(x,y,r)
📌 Arrays of objects: let bubbles = []
📌 Array methods: push(), for loops

## **Live Sketches**
![Day11-Classes](/sketches/Day11-Classes.png)
![Day12-Arrays](/sketches/Day12-Arrays.png)

**Progress**: Month 1 p5.js Days 1-14 (47%) → Media Lab portfolio ready
## Jan 29, 2026 - p5.js Lectures 3-4 ✅

**Arrays & Loops Practice**
- **Arrays**: 1 bubble moving across screen
- **for...of loop**: 3 bubbles moving diagonally across screen

**Progress**: Clean array iteration + bubble motion working
# Mouse-Controlled Bubble

**What it does**: Single bubble moves across screen with basic mouse interaction

**Features**:
- Array fundamentals practiced
- MouseX/MouseY position tracking
- Smooth bubble motion

**Tech Stack**: p5.js
**Status**: Lecture 3 complete ✅
# p5.js Lecture Sketches
**Techolution Coding Round Foundation**

## Completed Sketches
- `mouseBubble/` - Single bubble + mouse interaction
- `diagonalBubbles/` - 3 bubbles array with for...of loop
- `[others]/` - Full OOP classes practiced

**Status**: Lectures 1-7 complete, 7.8 (images) → Feb 2 AM
**Portfolio Ready**: Clean, documented, Git-committed
# Day 9 - Image Loading & Display ✅

**What it does**: Loads and displays external images in p5.js canvas

**Key Features**:
- `preload()` for image loading
- `loadImage()` syntax mastered
- `image(img, x, y, w, h)` positioning
- Image scaling + canvas integration

**Tech Stack**: p5.js imageMode()
**Status**: Lecture 7.8 complete
**Techolution Skill**: Asset management + async loading

**Demo**: [Insert screenshot/video]
 #day-10
# Portfolio Project #1 - Interactive Day/Night House 🌞🌙

**What it does**: Mouse-controlled man triggers full environment state change

**Core Features**:
- **3 OOP Classes**: House, Man, Environment (stars/clouds)
- **State Management**: Man position → day/night boolean
- **Visual Effects**: Sky lerpColor(), twinkling stars array, drifting clouds
- **Interactivity**: MouseX controls man → environment responds

**Day/Night Logic**:




