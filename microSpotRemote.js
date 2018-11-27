input.onButtonPressed(Button.A, function () {
    serial.writeString("p")
    basic.showLeds(`
        . # . . .
        . # # . .
        . # # # .
        . # # . .
        . # . . .
        `)
})
input.onButtonPressed(Button.B, function () {
    serial.writeString(">")
    basic.showLeds(`
        . . # . .
        . . . # .
        # # # # #
        . . . # .
        . . # . .
        `)
})
input.onGesture(Gesture.Shake, function () {
    serial.writeString("s")
    basic.showLeds(`
        # # # # #
        . # . # .
        # . . . #
        . # . # .
        # # # # #
        `)
})
input.onGesture(Gesture.TiltLeft, function () {
    basic.showLeds(`
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        . . . . .
        `)
    serial.writeString("-")
})
input.onGesture(Gesture.TiltRight, function () {
    serial.writeString("+")
    basic.showLeds(`
        . . # . .
        . . # . .
        # # # # #
        . . # . .
        . . # . .
        `)
})
input.onButtonPressed(Button.AB, function () {
    serial.writeString("!")
    basic.showIcon(IconNames.Happy)
})
basic.showIcon(IconNames.Heart)
basic.showString("MICROSPOT", 75)
