import QtQuick
import QtQuick.Layouts

Rectangle {

    Layout.fillWidth: true
    Layout.fillHeight: true

    radius: 20

    color: "#10151C"

    border.color: "#222B35"
    border.width: 1

    ColumnLayout {

        anchors.fill: parent
        anchors.margins: 18

        spacing: 10

        Text {

            text: "VISION SYSTEM"

            color: "white"

            font.family: "Orbitron"
            font.pixelSize: 20
            font.bold: true
        }

        Text {

            text: "CAMERA ACTIVE"

            color: "#00FF66"

            font.family: "Orbitron"
            font.pixelSize: 14
        }

        Rectangle {

            Layout.fillWidth: true
            Layout.preferredHeight: 170

            radius: 15

            color: "#050505"

            border.color: "#FF2020"
            border.width: 1

            Text {

                anchors.centerIn: parent

                text: "LIVE CAMERA"

                color: "white"

                font.family: "Orbitron"
                font.pixelSize: 16
                font.bold: true
            }
        }

        Text {

            text: "OBJECTS DETECTED : 0"

            color: "#DDDDDD"

            font.family: "Orbitron"
            font.pixelSize: 13
        }

        Item {
            Layout.fillHeight: true
        }
    }
}