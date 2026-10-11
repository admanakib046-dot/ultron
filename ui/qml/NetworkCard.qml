import QtQuick

Rectangle {

    radius: 20

    color: "#10151C"

    border.color: "#222B35"
    border.width: 1

    Column {

        anchors.fill: parent
        anchors.margins: 18

        spacing: 10

        // Title
        Text {

            text: "NETWORK STATUS"

            color: "white"

            font.family: "Orbitron"
            font.pixelSize: 20
            font.bold: true

        }

        // Connection Status
        Text {

            text: "CONNECTED"

            color: "#00FF66"

            font.family: "Orbitron"
            font.pixelSize: 14
            font.bold: true

        }

        // Download
        Text {

            text: "DOWNLOAD : 0 Mbps"

            color: "#DDDDDD"

            font.family: "Orbitron"
            font.pixelSize: 13

        }

        // Upload
        Text {

            text: "UPLOAD : 0 Mbps"

            color: "#DDDDDD"

            font.family: "Orbitron"
            font.pixelSize: 13

        }

    }

}