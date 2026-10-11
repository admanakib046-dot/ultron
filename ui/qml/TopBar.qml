import QtQuick
import QtQuick.Controls

Rectangle {

    color: "transparent"

    Rectangle {

        anchors.fill: parent
        anchors.margins: 15

        radius: 20

        color: "#0E131A"
        border.color: "#202733"
        border.width: 1

        // ---------------- Left ----------------

        Column {

            anchors.left: parent.left
            anchors.leftMargin: 30
            anchors.verticalCenter: parent.verticalCenter

            spacing: 10

            Text {

                text: "GOOD EVENING, JAGUER"

                color: "white"

                font.family: "Orbitron"
                font.pixelSize: 42
                font.bold: true
            }

            Text {

                text: "ULTRON IS NOW ONLINE."

                color: "#DDDDDD"

                font.family: "Orbitron"
                font.pixelSize: 18
            }

            Rectangle {

                width: 320
                height: 3

                radius: 2

                color: "#FF2020"
            }
        }

        // ---------------- Right ----------------

        Column {

            anchors.right: parent.right
            anchors.rightMargin: 35
            anchors.verticalCenter: parent.verticalCenter

            spacing: 4

            Text {

                text: Qt.formatTime(new Date(), "hh:mm AP")

                color: "white"

                font.family: "Orbitron"
                font.pixelSize: 38
                font.bold: true
            }

            Text {

                text: Qt.formatDate(new Date(), "dddd")

                color: "#CCCCCC"

                font.family: "Orbitron"
                font.pixelSize: 20
            }

            Text {

                text: Qt.formatDate(new Date(), "dd MMMM yyyy")

                color: "#AAAAAA"

                font.family: "Orbitron"
                font.pixelSize: 18
            }
        }
    }
}