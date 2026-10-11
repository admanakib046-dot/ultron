import QtQuick
import QtQuick.Layouts

Rectangle {

    radius: 20
    color: "#10151C"

    border.color: "#222B35"
    border.width: 1

    ColumnLayout {

        anchors.fill: parent
        anchors.margins: 18
        spacing: 14

        // Title
        Text {
            text: "MEMORY CORE"
            color: "white"

            font.family: "Orbitron"
            font.pixelSize: 20
            font.bold: true
        }

        // Status
        Text {
            text: "STORED MEMORIES : 0"
            color: "#CCCCCC"

            font.family: "Orbitron"
            font.pixelSize: 13
        }

        // Circular Memory Indicator
        Item {

            Layout.fillWidth: true
            Layout.preferredHeight: 170

            Rectangle {

                width: 110
                height: 110

                radius: 55

                anchors.centerIn: parent

                color: "transparent"

                border.width: 8
                border.color: "#FF2A2A"

                Text {

                    anchors.centerIn: parent

                    text: "0%"

                    color: "white"

                    font.family: "Orbitron"
                    font.pixelSize: 24
                    font.bold: true
                }
            }
        }

        Rectangle {

            Layout.fillWidth: true
            height: 2

            color: "#222B35"
        }

        Text {

            text: "MEMORY STATUS"

            color: "#FF4040"

            font.family: "Orbitron"
            font.pixelSize: 14
            font.bold: true
        }

        Text {

            text: "READY"

            color: "#00FF66"

            font.family: "Orbitron"
            font.pixelSize: 13
        }

        Rectangle {

            Layout.fillWidth: true
            height: 10

            radius: 5

            color: "#202833"

            Rectangle {

                width: parent.width * 0.05
                height: parent.height

                radius: 5

                color: "#FF2A2A"
            }
        }

        Text {

            text: "CAPACITY : 5%"

            color: "#BBBBBB"

            font.family: "Orbitron"
            font.pixelSize: 12
        }

        Item {
            Layout.fillHeight: true
        }
    }
}