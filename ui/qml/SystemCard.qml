import QtQuick

Rectangle {

    radius: 20

    color: "#10151C"

    border.color: "#222B35"
    border.width: 1

    Column {

        anchors.fill: parent
        anchors.margins: 18

        spacing: 12

        // Title
        Text {
            text: "SYSTEM OVERVIEW"

            color: "white"

            font.family: "Orbitron"
            font.pixelSize: 22
            font.bold: true
        }

        Repeater {

            model: [
                ["CPU", 23],
                ["RAM", 45],
                ["DISK", 38],
                ["GPU", 28]
            ]

            delegate: Column {

                spacing: 4

                // Label
                Text {
                    text: modelData[0]

                    color: "#CCCCCC"

                    font.family: "Orbitron"
                    font.pixelSize: 14
                }

                // Progress Bar
                Rectangle {

                    width: 250
                    height: 6

                    radius: 3

                    color: "#1D2530"

                    Rectangle {

                        width: parent.width * modelData[1] / 100
                        height: parent.height

                        radius: 3

                        color: "#FF2020"
                    }
                }

                // Percentage
                Text {
                    text: modelData[1] + "%"

                    color: "white"

                    font.family: "Orbitron"
                    font.pixelSize: 13
                    font.bold: true
                }

            }

        }

    }

}