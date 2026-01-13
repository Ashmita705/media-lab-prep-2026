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
