import QtQuick
import QtQuick.Layouts

Item {
    Layout.fillWidth: true
    Layout.fillHeight: true

    Rectangle {
        anchors.fill: parent
        anchors.margins: 20
        radius: 30
        color: "transparent"
        clip: true

        // ===========================
        // 3D ULTRON CORE
        // ===========================

        Core3D {
            id: reactor

            anchors.centerIn: parent

            width: 700
            height: 700
        }

        // ===========================
        // Bottom Status
        // ===========================

        Column {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 40

            spacing: 8

            Text {
                text: "ULTRON AI ENGINE"

                color: "#FF4040"

                font.family: "Orbitron"
                font.pixelSize: 22
                font.bold: true
            }

            Text {
                text: "ALL SYSTEMS OPERATIONAL"

                color: "#00FF66"

                font.family: "Orbitron"
                font.pixelSize: 15
            }
        }

        // ===========================
        // Top Label
        // ===========================

        Text {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.top: parent.top
            anchors.topMargin: 25

            text: "AI REACTOR"

            color: "#88FFFFFF"

            font.family: "Orbitron"
            font.pixelSize: 18
            font.bold: true
        }
    }
}